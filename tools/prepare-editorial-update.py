"""Prepare guarded content updates from an exported baseline; never write the DB.

Usage: python tools/prepare-editorial-update.py baseline-directory database-before.json
The exporter checks every original revision again inside each SQL transaction.
"""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]
BASE=Path(sys.argv[1]); SNAPSHOT=Path(sys.argv[2])
OUT=ROOT/'.openfoam-work/editorial/publish';OUT.mkdir(parents=True,exist_ok=True)
def corpus(directory):
    rows=[row for file in sorted(directory.glob('*content.json')) for row in json.loads(file.read_text(encoding='utf-8'))]
    assert len(rows)==len({r['slug'] for r in rows})
    return {r['slug']:r for r in rows}
before=corpus(BASE);after=corpus(ROOT/'tools/content')
snapshot={r['slug']:r for r in json.loads(SNAPSHOT.read_text(encoding='utf-8'))}
fields=['title','summary','body','track','series','sort_order','metadata','cover_url','status','comments_enabled']
defaults={'summary':'','body':'','track':'','series':'','sort_order':0,'metadata':{},'cover_url':'','status':'published','comments_enabled':True}
changes=[]
for slug,row in after.items():
    if slug in before:
        old=before[slug];patch={k:row.get(k,defaults.get(k)) for k in fields if row.get(k,defaults.get(k))!=old.get(k,defaults.get(k))}
        if patch:
            assert slug in snapshot,slug
            changes.append({'slug':slug,'expected_revision':snapshot[slug]['revision'],'patch':patch})
    else:
        assert slug not in snapshot,'New local row already exists: '+slug
        changes.append({'slug':slug,'expected_revision':None,'patch':{**defaults,**row}})
batches=[];batch=[];size=0
for change in changes:
    n=len(json.dumps(change,ensure_ascii=False,separators=(',',':')))
    if batch and size+n>105000:batches.append(batch);batch=[];size=0
    batch.append(change);size+=n
if batch:batches.append(batch)
assignments=[]
for key in fields:
    expr=f"(patch->'{key}')" if key=='metadata' else f"(patch->>'{key}')"
    if key=='sort_order':expr+='::integer'
    if key=='comments_enabled':expr+='::boolean'
    assignments.append(f"{key}=case when patch ? '{key}' then {expr} else c.{key} end")
manifest=[]
for i,batch in enumerate(batches):
    payload=json.dumps(batch,ensure_ascii=False,separators=(',',':'))
    assert '$editorial_data$' not in payload
    query='''do $editorial$
declare item jsonb; patch jsonb; changed integer; owner_id uuid;
begin
 if (select count(*) from auth.identities where provider='github' and provider_id='112299157') <> 1 then
  raise exception 'Expected one authorized content owner';
 end if;
 select user_id into owner_id from auth.identities where provider='github' and provider_id='112299157';
 for item in select value from jsonb_array_elements($editorial_data$'''+payload+'''$editorial_data$::jsonb) loop
  patch:=item->'patch';
  if item->>'expected_revision' is null then
   insert into public.foamlab_content(slug,kind,title,summary,body,track,series,sort_order,metadata,author_name,status,cover_url,comments_enabled,author_id)
   select item->>'slug',patch->>'kind',patch->>'title',patch->>'summary',patch->>'body',patch->>'track',patch->>'series',
     (patch->>'sort_order')::integer,patch->'metadata',coalesce(patch->>'author_name','FoamLab'),patch->>'status',patch->>'cover_url',
     (patch->>'comments_enabled')::boolean,owner_id on conflict(slug) do nothing;
  else
   update public.foamlab_content c set '''+', '.join(assignments)+'''
   where c.slug=item->>'slug' and c.revision=(item->>'expected_revision')::integer;
  end if;
  get diagnostics changed = row_count;
  if changed <> 1 then raise exception 'Concurrent content change: %',item->>'slug'; end if;
 end loop;
end $editorial$;
select '''+str(len(batch))+''' as applied;
'''
    file=OUT/f'batch-{i:03}.sql';file.write_text(query,encoding='utf-8');manifest.append({'file':str(file),'rows':len(batch),'chars':len(query)})
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'changes.json').write_text(json.dumps([{k:v for k,v in r.items() if k!='patch'}|{'fields':list(r['patch'])} for r in changes],ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'rows':len(changes),'new':sum(x['expected_revision'] is None for x in changes),'batches':len(batches)}))
