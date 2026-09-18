#!/usr/bin/env python3
"""Validate the canonical Skazka Hub release page and legacy migration bridge."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_links(root: Path, readme: str) -> None:
    refs = re.findall(r'(?:src|href)="([^"]+)"', readme)
    refs += re.findall(r'\]\(([^)]+)\)', readme)
    for ref in refs:
        url = urlsplit(ref)
        if url.scheme or ref.startswith('#'):
            continue
        path = unquote(url.path)
        target = (root / path).resolve()
        assert target.is_relative_to(root.resolve()), 'Link escapes repository'
        assert target.is_file(), f'Broken local link: {path}'


def check(root: Path) -> None:
    review = json.loads((root / 'release-page.json').read_text())
    legacy = json.loads((root / 'update.json').read_text())
    android9 = json.loads((root / 'update-android9.json').read_text())
    canonical = json.loads((root / 'update-canonical.json').read_text())
    migration = json.loads((root / 'package-migration.json').read_text())
    readme = (root / 'README.md').read_text()
    notes = (root / 'RELEASE_NOTES.md').read_text()

    assert review['mode'] == 'canonical-with-legacy-bridge'
    assert review['canonical_version'] == '0.7.1-preview'
    assert review['legacy_bridge_version'] == '0.6.23-preview'
    gate_commit = review.get('device_gate_commit', '')
    assert re.fullmatch(r'[0-9a-f]{40}', gate_commit), 'HOSTKEY/source gate commit missing'

    for name in ['README.md', 'RELEASE_NOTES.md', 'tools/check-release-page.py']:
        assert review['files'][name] == digest(root / name), f'{name} changed since release-page review'

    assert legacy == android9, 'Legacy compatibility feeds diverged'
    assert (legacy['packageName'], legacy['versionName'], legacy['versionCode']) == (
        'me.zaza.reader', '0.6.23-preview', 29)
    assert legacy['minSdk'] == 33
    assert legacy['sha256'] == '23e091bdd6f5c35567dd5c962d15172e5188cb101e6e456cb22298c4bf1bafec'
    assert '/releases/download/v0.6.23-preview/SkazkaHub-0.6.23-preview.apk' in legacy['apkUrl']
    legacy_apk = root / 'SkazkaHub-0.6.23-preview.apk'
    assert legacy_apk.is_file()
    assert legacy_apk.stat().st_size == legacy['size']
    assert digest(legacy_apk) == legacy['sha256']

    assert (canonical['packageName'], canonical['versionName'], canonical['versionCode']) == (
        'com.kroxaboom.skazkahub', '0.7.1-preview', 30)
    assert canonical['minSdk'] == 33
    canonical_apk = root / 'SkazkaHub-0.7.1-preview.apk'
    assert canonical_apk.is_file()
    assert canonical_apk.stat().st_size == canonical['size']
    assert digest(canonical_apk) == canonical['sha256']
    assert '/releases/download/v0.7.1-preview/SkazkaHub-0.7.1-preview.apk' in canonical['apkUrl']

    expected_migration = {k: v for k, v in canonical.items() if k != 'notes'}
    assert migration == expected_migration, 'Migration feed differs from canonical feed'

    assert notes.startswith('# Skazka Hub 0.7.1-preview\n')
    assert '## RU' in notes and '## EN' in notes
    assert 'com.kroxaboom.skazkahub' in readme and 'me.zaza.reader' in readme
    assert 'update-canonical.json' in readme and 'package-migration.json' in readme
    assert 'https://github.com/kroxaboom-sudo/skazka-hub-releases/releases/latest' in readme
    check_links(root, readme)

    print('PASS release page: canonical 0.7.1, immutable legacy bridge, RU/EN, APK hashes and links')


if __name__ == '__main__':
    import sys
    check(Path(sys.argv[1] if len(sys.argv) > 1 else '.'))
