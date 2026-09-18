#!/usr/bin/env python3
"""Validate the public Skazka Hub release page and transition metadata."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local_links(root: Path, readme: str) -> set[str]:
    refs = re.findall(r'(?:src|href)="([^"]+)"', readme)
    refs += re.findall(r'\]\(([^)]+)\)', readme)
    images = set()
    for ref in refs:
        url = urlsplit(ref)
        if url.scheme or ref.startswith('#'):
            continue
        path = unquote(url.path)
        target = (root / path).resolve()
        assert target.is_relative_to(root.resolve()), 'Link escapes repository'
        assert target.is_file(), f'Broken local link: {path}'
        if path.endswith('.png'):
            images.add(path)
    return images


def check_transition(root: Path, review: dict, readme: str, notes: str) -> None:
    legacy = json.loads((root / 'update.json').read_text())
    android9 = json.loads((root / 'update-android9.json').read_text())
    canonical = json.loads((root / 'update-canonical.json').read_text())
    migration = json.loads((root / 'package-migration.json').read_text())

    assert review['version'] == legacy['versionName'] == '0.6.23-preview'
    assert review['canonical_version'] == canonical['versionName'] == '0.7.0-preview'
    assert legacy['packageName'] == 'me.zaza.reader'
    assert canonical['packageName'] == 'com.kroxaboom.skazkahub'
    assert migration['packageName'] == canonical['packageName']
    assert migration['versionCode'] == canonical['versionCode']
    assert migration['versionName'] == canonical['versionName']
    assert migration['sha256'] == canonical['sha256']
    assert migration['size'] == canonical['size']
    assert migration['apkUrl'] == canonical['apkUrl']
    assert android9 == legacy, 'Legacy compatibility feed drifted from update.json'

    for manifest in (legacy, canonical):
        apk = root / Path(manifest['apkUrl']).name
        assert apk.is_file(), f'Missing APK: {apk.name}'
        assert apk.stat().st_size == manifest['size'], f'{apk.name}: size mismatch'
        assert digest(apk) == manifest['sha256'], f'{apk.name}: SHA-256 mismatch'
        assert manifest['minSdk'] == 33

    assert '0.6.23-preview → 0.7.0-preview' in readme
    assert 'me.zaza.reader' in readme and 'com.kroxaboom.skazkahub' in readme
    assert 'update-canonical.json' in readme and 'package-migration.json' in readme
    assert '0.6.23-preview' in notes and '0.7.0-preview' in notes
    assert 'RU' in notes and 'EN' in notes
    assert not local_links(root, readme), 'Transition page should not claim stale release screenshots'


def check(root: Path) -> None:
    review = json.loads((root / 'release-page.json').read_text())
    readme = (root / 'README.md').read_text()
    notes = (root / 'RELEASE_NOTES.md').read_text()

    gate_commit = review.get('device_gate_commit', '')
    assert re.fullmatch(r'[0-9a-f]{40}', gate_commit), 'HOSTKEY device-gate commit is missing'

    for name in ['README.md', 'RELEASE_NOTES.md']:
        assert review['files'][name] == digest(root / name), f'{name} changed since page review'

    assert 'img.shields.io/github/v/release/kroxaboom-sudo/skazka-hub-releases' in readme
    assert 'https://github.com/kroxaboom-sudo/skazka-hub-releases/releases/latest' in readme
    local_links(root, readme)

    mode = review.get('mode', 'standard')
    if mode == 'package-migration':
        check_transition(root, review, readme, notes)
    else:
        raise AssertionError(f'Unsupported release page mode: {mode}')

    print('PASS release page: transition metadata, APK hashes, RU/EN notes and links')


if __name__ == '__main__':
    import sys
    check(Path(sys.argv[1] if len(sys.argv) > 1 else '.'))
