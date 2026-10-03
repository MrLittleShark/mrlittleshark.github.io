"""Apply reviewed purpose-first descriptions without rewriting examples."""
from pathlib import Path
import html,json,re

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'source-openfoam'
overrides=json.loads((Path(__file__).parent/'command-summary-overrides.json').read_text(encoding='utf-8'))
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,data):p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
records=load(SRC/'assets/commands.json')
unknown=set(overrides)-{r['name'] for r in records}
assert not unknown,unknown
changes=[]
by_slug={}
for r in records:
    name=r['name']
    if name not in overrides:continue
    summary=overrides[name]
    if r['description']==summary:continue
    old=r['description'];title=name+' · '+summary.rstrip('。')
    changes.append({'slug':'command-'+r['url'].strip('/').split('/')[-1],'old_summary':old,'summary':summary,'old_title':r['title'],'title':title})
    r['description']=summary;r['title']=title
    by_slug[changes[-1]['slug']]=changes[-1]
    page=SRC/r['url'].strip('/')/'index.md';text=page.read_text(encoding='utf-8')
    text=re.sub(r'(?m)^title:.*$',lambda _: 'title: '+json.dumps(title,ensure_ascii=False),text,count=1)
    text=re.sub(r'(?m)^description:.*$',lambda _: 'description: '+json.dumps(summary,ensure_ascii=False),text,count=1)
    text=text.replace('<p>'+html.escape(old)+'</p>','<p>'+html.escape(summary)+'</p>',1)
    page.write_text(text,encoding='utf-8')
save(SRC/'assets/commands.json',records)
learning=load(SRC/'_data/learning.json')
for r in learning['commands']:
    if r['name'] in overrides:
        r['description']=overrides[r['name']];r['title']=r['name']+' · '+r['description'].rstrip('。')
save(SRC/'_data/learning.json',learning)
content=load(ROOT/'tools/content/reference-content.json')
for row in content:
    c=by_slug.get(row['slug'])
    if not c:continue
    row['summary']=c['summary'];row['title']=c['title']
    row['body']=row['body'].replace('<p>'+html.escape(c['old_summary'])+'</p>','<p>'+html.escape(c['summary'])+'</p>',1)
save(ROOT/'tools/content/reference-content.json',content)
report={'reviewed':len(records),'changed':len(changes),'changes':changes}
out=ROOT/'.openfoam-work/command-summary-review';out.mkdir(exist_ok=True)
if changes:
    save(out/'changes.json',report)
print('Reviewed:',len(records),'Changed:',len(changes))
