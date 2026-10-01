from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,zipfile
R=Path(__file__).resolve().parents[1];root=R/'public-openfoam'
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.h1=0
 def handle_starttag(self,tag,attrs):
  if tag=='h1':self.h1+=1
  for key,value in attrs:
   if key in ('href','src'):self.links.append(value)
errors=[];count=0;pages=list(root.rglob('*.html'))
for file in pages:
 p=Parser();p.feed(file.read_text(encoding='utf-8'));name=file.relative_to(root).as_posix()
 if p.h1!=1 and name!='read/index.html':errors.append(name+': h1 count '+str(p.h1))
 for href in p.links:
  if not href:continue
  u=urlsplit(href)
  if u.scheme or u.netloc or not u.path:continue
  target=root/unquote(u.path).lstrip('/') if u.path.startswith('/') else file.parent/unquote(u.path)
  if u.path.endswith('/'):target=target/'index.html'
  count+=1
  if not target.exists():errors.append(name+': broken '+href)
for p in (root/'downloads').rglob('*.zip'):
 with zipfile.ZipFile(p) as z:
  if z.testzip():errors.append(str(p)+': invalid ZIP')
if (root/'bubble').exists():errors.append('Retired bubble topic still generated')
report={'pages':len(pages),'links':count,'bytes':sum(p.stat().st_size for p in root.rglob('*') if p.is_file()),'errors':errors}
(R/'.openfoam-work/replan/generated-integrity.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2));raise SystemExit(bool(errors))
