"""Remove import boilerplate and meaningless comment rows from old handbooks."""
from pathlib import Path
import json,re
from bs4 import BeautifulSoup

HERE=Path(__file__).parent
path=HERE/'legacy-reference-content.json'
rows=json.loads(path.read_text(encoding='utf-8'))
changed=0;removed=0
for row in rows:
    old=row['body'];soup=BeautifulSoup(old,'html.parser')
    for node in soup.select('.source-note'):
        if any(x in node.get_text() for x in ['适用版本','核验','兼容性','固定版本']):node.decompose();removed+=1
    for tr in soup.select('tr'):
        cells=tr.find_all(['td','th'])
        if cells and any(re.fullmatch(r'[\s*/\\—_-]{12,}',c.get_text()) for c in cells):tr.decompose();removed+=1
    for node in soup.select('p'):
        txt=node.get_text(' ',strip=True)
        if txt.startswith(('核验范围：','本页核验记录：','资料核验：','所有示例均需','本页基于固定版本')):node.decompose();removed+=1
    for h in soup.select('h2,h3'):
        if h.get_text(strip=True)=='教程保留的参数注释':
            nxt=h.find_next_sibling()
            while nxt and nxt.name not in ['h2','h3']:
                after=nxt.find_next_sibling();nxt.decompose();nxt=after
            h.decompose();removed+=1
    for h in soup.select('h2,h3'):
        if h.find_next_sibling() is None: h.decompose();removed+=1
    body=str(soup).replace('OpenCFD OpenFOAM v2512','OpenFOAM v2512')
    row['summary']=re.sub(r'^(第\s*\d+\s*章\s*|\d+\s*)','',row['title']).strip()+'：用法与配置实例。'
    row['body']=body
    if old!=body:changed+=1
path.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'legacy_pages':len(rows),'changed':changed,'removed_boilerplate':removed}))
