"""Read the latest source-branch Pages workflow; credentials stay in memory."""
from pathlib import Path
import json,os,subprocess,urllib.request
root=Path(__file__).resolve().parents[1]
env=dict(os.environ,GIT_TERMINAL_PROMPT='0',GCM_INTERACTIVE='Never')
credential=subprocess.run(['git','credential','fill'],input='protocol=https\nhost=github.com\n\n',capture_output=True,text=True,env=env,timeout=20)
values=dict(line.split('=',1) for line in credential.stdout.splitlines() if '=' in line)
headers={'Accept':'application/vnd.github+json','User-Agent':'FoamLab-deployment-check'}
if values.get('password'):headers['Authorization']='Bearer '+values['password']
url='https://api.github.com/repos/foamlabshark/foamlabshark.github.io/actions/runs?branch=foamlab-source&per_page=3'
with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=25) as response:data=json.load(response)
report=[{k:run.get(k) for k in ['id','head_sha','status','conclusion','html_url','created_at','updated_at']} for run in data.get('workflow_runs',[])]
print(json.dumps(report,ensure_ascii=False,indent=2))
out=root/'.openfoam-work/replan/deployment-status.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
