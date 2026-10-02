"""Read-only deployment checks; GitHub credentials stay in process memory."""
import json,os,subprocess,urllib.request,urllib.error
from pathlib import Path
env=dict(os.environ,GIT_TERMINAL_PROMPT='0',GCM_INTERACTIVE='Never')
p=subprocess.run(['git','credential','fill'],input='protocol=https\nhost=github.com\n\n',text=True,capture_output=True,env=env,timeout=20)
credential=dict(line.split('=',1) for line in p.stdout.splitlines() if '=' in line)
headers={'Accept':'application/vnd.github+json','User-Agent':'FoamLab-check'}
if credential.get('password'):headers['Authorization']='Bearer '+credential['password']
report={}
for key,endpoint in [('pages','pages'),('build','pages/builds/latest')]:
    req=urllib.request.Request('https://api.github.com/repos/foamlabshark/foamlabshark.github.io/'+endpoint,headers=headers)
    try:
        with urllib.request.urlopen(req,timeout=20) as r:d=json.load(r)
        report[key]={k:d.get(k) for k in ['status','commit','html_url','source','error','build_type'] if k in d}
    except urllib.error.HTTPError as e:report[key]={'http_status':e.code}
report['routes']=[]
for route in ['/','/commands/','/dictionaries/','/account/','/lessons/28/','/assignments/','/announcements/','/community/','/admin/','/maintenance/','/2024/10/17/hello-world/','/2024/10/17/french1/']:
    try:
        with urllib.request.urlopen('https://foamlabshark.github.io'+route,timeout=25) as r:
            body=r.read().decode('utf-8');report['routes'].append({'path':route,'status':r.status,'foamlab':'FoamLab' in body})
    except urllib.error.HTTPError as e:report['routes'].append({'path':route,'status':e.code})
print(json.dumps(report,ensure_ascii=False,indent=2))
(Path(__file__).resolve().parents[1]/'.openfoam-work/live-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
