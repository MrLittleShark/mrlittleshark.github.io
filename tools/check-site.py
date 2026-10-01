from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,zipfile,hashlib
root=Path(__file__).resolve().parents[1]/'public-openfoam'
errors=[];linkcount=0
class Page(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.h1=0;self.html=0
    def handle_starttag(self,tag,attrs):
        if tag=='h1':self.h1+=1
        if tag=='html':self.html+=1
        attrs=dict(attrs)
        for key in ['href','src']:
            if key in attrs:self.links.append(attrs[key])
pages=list(root.rglob('*.html'))
for f in pages:
    p=Page();text=f.read_text(encoding='utf-8');p.feed(text)
    if p.h1!=1:errors.append(f'{f.relative_to(root)}: h1 count {p.h1}')
    if p.html!=1:errors.append(f'{f.relative_to(root)}: html count {p.html}')
    if '{% raw %}' in text or '{% endraw %}' in text:errors.append(f'{f}: raw tag leaked')
    for url in p.links:
        parsed=urlsplit(url)
        if parsed.scheme or parsed.netloc or not parsed.path:continue
        target=(root/unquote(parsed.path).lstrip('/')) if parsed.path.startswith('/') else f.parent/unquote(parsed.path)
        if parsed.path.endswith('/'):target=target/'index.html'
        linkcount+=1
        if not target.exists():errors.append(f'{f.relative_to(root)}: broken {url}')
assert len(list((root/'lessons').glob('*/index.html')))==28
assert len(list((root/'reference').glob('*/index.html')))==37
for n in range(1,29):
    for name in [f'lesson-{n:02d}.docx',f'lesson-{n:02d}-cases.zip']:
        with zipfile.ZipFile(root/'downloads'/name) as z:
            if z.testzip():errors.append('Invalid archive '+name)
old=['hello-world','入学燕园','french1','Steve Jobs']
for p in pages:
    if any(t in str(p) for t in old):errors.append('Legacy blog page remains '+str(p))
report={'html_pages':len(pages),'local_links_checked':linkcount,'lessons':28,'reference_chapters':37,'commands':len(json.loads((root/'assets/commands.json').read_text(encoding='utf-8'))),'dictionaries':len(json.loads((root/'assets/dictionaries.json').read_text(encoding='utf-8'))),'total_bytes':sum(p.stat().st_size for p in root.rglob('*') if p.is_file()),'errors':errors}
(root.parent/'.openfoam-work'/'site-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2));raise SystemExit(bool(errors))
