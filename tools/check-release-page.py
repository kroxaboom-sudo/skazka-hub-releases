#!/usr/bin/env python3
"""Fail publication when release documentation or screenshot evidence is stale."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


def check(root: Path) -> None:
    manifest = json.loads((root / 'update.json').read_text())
    review = json.loads((root / 'release-page.json').read_text())
    version = manifest['versionName']
    readme = (root / 'README.md').read_text()
    notes = (root / 'RELEASE_NOTES.md').read_text()

    assert review['version'] == version, 'Review release-page.json for this release'
    gate_commit = review.get('device_gate_commit', '')
    assert re.fullmatch(r'[0-9a-f]{40}', gate_commit), 'HOSTKEY device-gate commit is missing'
    for name in ['README.md', 'RELEASE_NOTES.md']:
        digest = hashlib.sha256((root / name).read_bytes()).hexdigest()
        assert review['files'][name] == digest, f'{name} changed since page review'

    assert notes.startswith('# Skazka Hub ' + version + '\n'), 'Stale release notes'
    assert manifest['notes'].strip() in notes, 'Updater and release notes disagree'
    assert 'img.shields.io/github/v/release/kroxaboom-sudo/skazka-hub-releases' in readme
    assert 'https://github.com/kroxaboom-sudo/skazka-hub-releases/releases/latest' in readme
    refs = re.findall(r'(?:src|href)="([^"]+)"', readme)
    refs += re.findall(r'\]\(([^)]+)\)', readme)
    local_images = set()
    for ref in refs:
        url = urlsplit(ref)
        if url.scheme or ref.startswith('#'):
            continue
        path = unquote(url.path)
        target = (root / path).resolve()
        assert target.is_relative_to(root.resolve()), 'Link escapes repository'
        assert target.is_file(), f'Broken local link: {path}'
        if path.endswith('.png'):
            local_images.add(path)

    screenshots = review['screenshots']
    assert len(screenshots) >= 2, 'At least two verified screenshots required'
    assert {item['path'] for item in screenshots} == local_images
    for item in screenshots:
        assert item['version'] == version, 'Capture screenshots for the release version'
        evidence = item.get('capture_evidence') or item.get('capture_run') or ''
        assert evidence, 'Capture evidence missing'
        if item.get('capture_run'):
            assert item['capture_run'].startswith('https://github.com/'), 'Invalid GitHub capture evidence'
        else:
            assert 'HOSTKEY' in evidence and 'Android 13' in evidence, 'HOSTKEY capture evidence is incomplete'
        data = (root / item['path']).read_bytes()
        assert data.startswith(b'\x89PNG\r\n\x1a\n'), 'Invalid PNG'
        assert hashlib.sha256(data).hexdigest() == item['sha256'], 'Screenshot changed'

    assert f'**{version}**' in readme, 'Screenshot version caption is stale'
    print('PASS release page: version, HOSTKEY evidence, notes, links and screenshots')


if __name__ == '__main__':
    import sys
    check(Path(sys.argv[1] if len(sys.argv) > 1 else '.'))
