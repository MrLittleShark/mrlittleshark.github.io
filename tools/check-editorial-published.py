"""Read back public content and deployed assets; performs no external writes."""
from pathlib import Path
import concurrent.futures, hashlib, json, urllib.request, urllib.parse

ROOT=Path(__file__).resolve().parents[1]
ORIGIN='https://foamlabshark.github.io'
config=json.loads((ROOT/'source-openfoam/assets/auth-config.json').read_text(encoding='utf-8'))
headers={'apikey':config['publishableKey'],'User-Agent':'FoamLab-public-verification'}

def rest(path, data=None):
    h=dict(headers)
    if data is not None:h['Content-Type']='application/json'
    req=urllib.request.Request(config['supabaseUrl']+'/rest/v1/'+path,headers=h,data=None if data is None else json.dumps(data).encode())
    with urllib.request.urlopen(req,timeout=45) as response:return json.load(response)

rows=[r for p in (ROOT/'tools/content').glob('*content.json') for r in json.loads(p.read_text(encoding='utf-8'))]
expected={r['slug']:r for r in rows if r.get('status','published')=='published' and not r.get('metadata',{}).get('admin_only')}
fields=['slug','title','summary','body','track','series','sort_order','metadata','cover_url','status','comments_enabled']
online={r['slug']:r for r in rest('foamlab_content?select='+','.join(fields)+'&order=slug&limit=1000')}
assert set(online)==set(expected),('Public content set differs',set(online)^set(expected))
defaults={'summary':'','body':'','track':'','series':'','sort_order':0,'metadata':{},'cover_url':'','status':'published','comments_enabled':True}
errors=[]
baseline_path=ROOT/'.openfoam-work/editorial/database-before.json'
baseline={r['slug']:r for r in json.loads(baseline_path.read_text(encoding='utf-8'))} if baseline_path.exists() else {}
for slug,row in expected.items():
    for key in fields:
        wanted=row.get(key,defaults.get(key))
        actual=online[slug].get(key)
        if key=='metadata' and 'seed_version' not in wanted and 'seed_version' in actual:
            # The original import records a server-side provenance tag. An
            # unchanged metadata field deliberately retains this existing tag.
            previous=baseline.get(slug,{}).get('metadata',{}).get('seed_version')
            assert actual['seed_version']==previous,(slug,'Unexpected provenance tag')
            actual={k:v for k,v in actual.items() if k!='seed_version'}
        if wanted!=actual:errors.append(slug+': '+key)
assert not errors,errors
assert rest('foamlab_content?select=slug&slug=in.(site-maintenance,site-design)')==[]
for query in ['维护','设计']:
    assert not any(r['slug'] in ('site-maintenance','site-design') for r in rest('rpc/foamlab_search_content',{'query':query}))
support=rest('foamlab_settings?select=value&key=eq.support')[0]['value']
assert support['enabled'] and support['wechat_url']=='/assets/support/wechat.jpg' and support['alipay_url']=='/assets/support/alipay.jpg'

paths={d['url'] for r in rows if r['kind']=='lesson' for d in r.get('metadata',{}).get('downloads',[]) if d['url'].startswith('/')}
paths.update(['/assets/covers/foamlab-aircraft-background-v1.png','/assets/science/development-solver-decay.png','/assets/science/development-boundary-results.png','/assets/science/development-utility-volume-average.png','/assets/support/wechat.jpg','/assets/support/alipay.jpg'])
paths.update('/assets/'+name for name in ['page-outline.js','page-outline.css','lab.js','site.js','support.js','navigation.css','reader.css','admin-doc.js'])

def asset(path):
    req=urllib.request.Request(ORIGIN+path,headers={'User-Agent':'FoamLab-public-verification','Cache-Control':'no-cache'})
    with urllib.request.urlopen(req,timeout=45) as response:remote=response.read()
    local=(ROOT/'public-openfoam'/path.lstrip('/')).read_bytes()
    if Path(path).suffix in ('.js','.css','.json','.svg'):
        remote=remote.replace(b'\r\n',b'\n');local=local.replace(b'\r\n',b'\n')
    assert remote==local,'Deployed asset differs: '+path
    return {'path':path,'bytes':len(remote),'sha256':hashlib.sha256(remote).hexdigest()}

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:assets=list(pool.map(asset,sorted(paths)))
report={'origin':ORIGIN,'published_records':len(online),'fields_compared':fields,'private_documents_hidden':True,'support_enabled':True,'assets':assets,'external_writes':0}
out=ROOT/'.openfoam-work/editorial/published-content-check.json';out.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'published_records':len(online),'assets_verified':len(assets),'private_documents_hidden':True,'errors':errors},ensure_ascii=False))
