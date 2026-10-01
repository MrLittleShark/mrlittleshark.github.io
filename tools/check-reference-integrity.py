"""Validate pinned reference coverage, source hashes, links and CMS identities."""
import hashlib
import json
import pathlib
import re
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'source-openfoam'

def load(path):
    return json.loads(path.read_text(encoding='utf-8'))

commands = load(SOURCE/'assets/commands.json')
dictionaries = load(SOURCE/'assets/dictionaries.json')
cms = load(ROOT/'tools/content/reference-content.json')
legacy_file = ROOT/'tools/content/legacy-reference-content.json'
legacy = load(legacy_file) if legacy_file.exists() else []
cms += legacy
examples = load(SOURCE/'assets/reference-example-manifest.json')
audit = load(SOURCE/'assets/reference-audit.json')
errors = []
if len({x['name'] for x in commands}) != len(commands):
    errors.append('Duplicate command names')
if len({x['slug'] for x in cms}) != len(cms):
    errors.append('Duplicate CMS slugs')
core = [x for x in commands if x['scope'] in ('core-solver','core-utility')]
if len(core) != 278:
    errors.append('Expected 278 pinned solvers/utilities, found '+str(len(core)))
for item in commands+dictionaries:
    page = SOURCE/item['url'].strip('/')/'index.md'
    if not page.exists():
        errors.append('Missing reference page '+item['url'])
for item in examples:
    path = SOURCE/item['download'].lstrip('/')
    if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
        errors.append('Example differs from pinned source: '+item['path'])
for item in cms:
    for url in re.findall(r'(?:href|src)="([^"]+)"',item['body']):
        if not url.startswith('/'):
            continue
        path = urllib.parse.unquote(urllib.parse.urlsplit(url).path).lstrip('/')
        target = SOURCE/path
        if not target.exists() and not (target/'index.md').exists() and not (ROOT/'themes/foam-lab/source'/path).exists():
            errors.append('Missing internal target '+url+' in '+item['slug'])
    for key in ('kind','title','summary','body','track','series','status','sort_order','metadata'):
        if key not in item:
            errors.append('Missing CMS field '+key+' in '+item['slug'])
result = dict(commands=len(commands),core=len(core),configurations=len(dictionaries),complete_example_hashes_verified=len(examples),legacy_chapters=len(legacy),cms_records=len(cms),errors=errors)
dest=ROOT/'.openfoam-work/replan/reference-integrity.json'
dest.parent.mkdir(parents=True,exist_ok=True)
dest.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
