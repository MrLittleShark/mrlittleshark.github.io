"""Verify an existing Git credential without printing or storing the credential."""
import subprocess,os,json,urllib.request,urllib.error
env=dict(os.environ,GIT_TERMINAL_PROMPT='0',GCM_INTERACTIVE='Never')
token=os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
if not token:
    p=subprocess.run(['git','credential','fill'],input='protocol=https\nhost=github.com\n\n',text=True,capture_output=True,env=env,timeout=20)
    entries=dict(line.split('=',1) for line in p.stdout.splitlines() if '=' in line)
    token=entries.get('password')
if not token:
    print(json.dumps({'authenticated':False,'reason':'No noninteractive GitHub credential available'}))
    raise SystemExit(0)
for endpoint in ['user','repos/foamlabshark/foamlabshark.github.io','repos/foamlabshark/foamlabshark.github.io/pages']:
    req=urllib.request.Request('https://api.github.com/'+endpoint,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','User-Agent':'FoamLab-setup'})
    try:
        with urllib.request.urlopen(req,timeout=20) as r:d=json.load(r)
        print(json.dumps({'endpoint':endpoint,**{k:d[k] for k in ['login','permissions','source','build_type','html_url','status'] if k in d}},ensure_ascii=False))
    except urllib.error.HTTPError as e:print(json.dumps({'endpoint':endpoint,'status':e.code}))
