"""Prepare deterministic SQL import batches; existing CMS edits are never overwritten by default."""
from pathlib import Path
import json,sys,hashlib
R=Path(__file__).resolve().parents[1]
out=R/'.openfoam-work/cms-seed';out.mkdir(parents=True,exist_ok=True)
files=[R/'tools/content'/name for name in sys.argv[1:] if name.endswith('.json')]
if not files: files=sorted((R/'tools/content').glob('*content.json'))
rows=[]
for path in files:
 for row in json.loads(path.read_text(encoding='utf-8')):
  v={k:row.get(k) for k in ['slug','kind','title','summary','body','track','series','sort_order','metadata']}
  for k in ['summary','body','track','series']:v[k]=v[k] or ''
  v['sort_order']=v['sort_order'] or 0;v['metadata']=v['metadata'] or {};v['metadata']['seed_version']='2026-10-02'
  v['author_name']=row.get('author_name','FoamLab');v['status']=row.get('status','published');v['cover_url']=row.get('cover_url','');v['comments_enabled']=row.get('comments_enabled',True)
  rows.append(v)
assert len(set(x['slug'] for x in rows))==len(rows),'Duplicate content slug'
sql_head="""with owner as (select user_id from auth.identities where provider='github' and provider_id='112299157'), inserted as (
insert into public.foamlab_content(slug,kind,title,summary,body,track,series,sort_order,metadata,author_name,status,cover_url,comments_enabled,author_id)
select x.slug,x.kind,x.title,x.summary,x.body,x.track,x.series,x.sort_order,x.metadata,x.author_name,x.status,x.cover_url,x.comments_enabled,(select user_id from owner)
from jsonb_to_recordset($foamlab_seed$"""
sql_tail="""$foamlab_seed$::jsonb) as x(slug text,kind text,title text,summary text,body text,track text,series text,sort_order integer,metadata jsonb,author_name text,status text,cover_url text,comments_enabled boolean)
on conflict(slug) do nothing returning id) select count(*) as imported from inserted;"""
if '--refresh-seed' in sys.argv:
 sql_tail=sql_tail.replace('on conflict(slug) do nothing', "on conflict(slug) do update set "+','.join(k+'=excluded.'+k for k in ['title','summary','body','track','series','sort_order','metadata','cover_url'])+" where public.foamlab_content.revision=1 and public.foamlab_content.metadata->>'seed_version'='2026-10-02'")
batches=[];batch=[];size=0
for row in rows:
 text=json.dumps(row,ensure_ascii=False,separators=(',',':'));assert '$foamlab_seed$' not in text
 if batch and size+len(text)>55000:batches.append(batch);batch=[];size=0
 batch.append(row);size+=len(text)
if batch:batches.append(batch)
manifest=[]
for i,batch in enumerate(batches):
 p=out/f'batch-{i:03}.sql';p.write_text(sql_head+json.dumps(batch,ensure_ascii=False,separators=(',',':'))+sql_tail,encoding='utf-8');manifest.append(str(p))
(out/'manifest.json').write_text(json.dumps(manifest),encoding='utf-8')
print(json.dumps({'records':len(rows),'batches':len(batches),'files':[p.name for p in files]},ensure_ascii=False))
