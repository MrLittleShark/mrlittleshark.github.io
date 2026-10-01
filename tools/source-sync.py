"""Synchronize the explicit website source set without overwriting concurrent edits."""
from pathlib import Path
import subprocess,os,json,hashlib,shutil,sys

ROOT=Path(__file__).resolve().parents[1]
CHECKOUT=ROOT/'.source_foamlab'
STATE=ROOT/'.openfoam-work/source-sync.json'
REPO='https://github.com/MrLittleShark/MrLittleShark.github.io.git'
BRANCH='foamlab-source'
DIRECTORIES=('source-openfoam','themes/foam-lab','scripts','lib','tools','supabase','.github')
FILES=('_config.yml','package.json','package-lock.json','.gitignore','README.md','VERIFICATION.md','发布学习网站.cmd','启动学习网站.cmd')
ENV=dict(os.environ,GIT_TERMINAL_PROMPT='0',GCM_INTERACTIVE='Never')

def allowed(name):
    p=Path(name)
    return not p.is_absolute() and '..' not in p.parts and '__pycache__' not in p.parts and p.suffix not in ('.pyc','.log') and (name in FILES or any(name.startswith(d+'/') for d in DIRECTORIES))

def safe(base,name):
    p=(base/name).resolve()
    if not p.is_relative_to(base.resolve()) or not allowed(name):raise RuntimeError('Unexpected source path: '+name)
    return p

def git(*args,cwd=CHECKOUT):
    p=subprocess.run(['git','-c','core.quotepath=false',*args],cwd=cwd,env=ENV,capture_output=True,text=True,encoding='utf-8')
    if p.returncode:raise RuntimeError('git '+args[0]+' failed: '+p.stderr.strip())
    return p.stdout.strip()

def digest(file):
    if not file.is_file():return None
    data=file.read_bytes()
    # Git on Windows may convert text checkout line endings; they are not content edits.
    if file.suffix.lower() in ('.md','.js','.cjs','.mjs','.ts','.py','.yml','.yaml','.json','.css','.ejs','.txt','.ps1','.cmd','.html','.svg','.sql','.toml','.jsonc') or file.name=='.gitignore':data=data.replace(b'\r\n',b'\n')
    return hashlib.sha256(data).hexdigest()

def inventory():
    files={}
    for name in FILES:
        p=safe(ROOT,name)
        if p.is_file():files[name]=digest(p)
    for directory in DIRECTORIES:
        for p in (ROOT/directory).rglob('*'):
            name=p.relative_to(ROOT).as_posix()
            if p.is_file() and allowed(name):files[name]=digest(p)
    return files

def remote_files():return {n:digest(safe(CHECKOUT,n)) for n in git('ls-files').splitlines() if allowed(n)}

def save_state(data):
    STATE.parent.mkdir(parents=True,exist_ok=True)
    STATE.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')

def setup():
    if CHECKOUT.resolve().parent!=ROOT.resolve():raise RuntimeError('Unexpected checkout')
    if not (CHECKOUT/'.git').exists():
        if CHECKOUT.exists() and any(CHECKOUT.iterdir()):raise RuntimeError('Source checkout is not empty')
        CHECKOUT.mkdir(exist_ok=True)
        git('init','-b',BRANCH)
        git('remote','add','origin',REPO)
    if git('remote','get-url','origin')!=REPO or git('branch','--show-current')!=BRANCH:raise RuntimeError('Unexpected source checkout origin or branch')
    if git('status','--porcelain'):raise RuntimeError('Source checkout contains uncommitted changes; inspect .source_foamlab')
    exists=bool(git('ls-remote','--heads','origin',BRANCH))
    if exists:
        git('fetch','origin',BRANCH)
        git('merge','--ff-only','origin/'+BRANCH)
    return exists

def pull():
    if not setup():return False
    remote=remote_files();base=json.loads(STATE.read_text(encoding='utf-8')) if STATE.exists() else {}
    changes=[];conflicts=[]
    for name in sorted(set(base)|set(remote)):
        previous=base.get(name);new=remote.get(name);local=digest(safe(ROOT,name))
        # Upgrade the initial byte-level baseline without treating CRLF as an edit.
        for candidate in (safe(ROOT,name),safe(CHECKOUT,name)):
            if candidate.is_file() and previous==hashlib.sha256(candidate.read_bytes()).hexdigest():
                previous=digest(candidate);break
        if new==previous:continue
        if local not in (previous,new):conflicts.append(name)
        else:changes.append((name,new))
    if conflicts:raise RuntimeError('Local and online changes overlap. Merge these files before publishing:\n'+'\n'.join(conflicts))
    for name,new in changes:
        target=safe(ROOT,name)
        if new is None:
            if target.is_file():target.unlink()
        else:
            target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(safe(CHECKOUT,name),target)
    save_state(remote)
    print('Source synchronized; '+str(len(changes))+' remote file changes applied.')
    return True

def push():
    pull() # A concurrent edit after the build must never silently overwrite a file.
    local=inventory();previous=remote_files()
    for name in sorted(set(previous)-set(local)):
        target=safe(CHECKOUT,name)
        if target.is_file():target.unlink()
    for name,value in local.items():
        if previous.get(name)!=value:
            target=safe(CHECKOUT,name);target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(safe(ROOT,name),target)
    git('add','--all')
    if git('diff','--cached','--name-only'):
        git('commit','-m','Update FoamLab learning website sources')
    git('push','-u','origin','HEAD:'+BRANCH)
    save_state(local)
    print('Source published: '+git('rev-parse','HEAD'))

if __name__=='__main__':
    try:
        if len(sys.argv)==3 and sys.argv[1]=='resolve':
            name=sys.argv[2].replace('\\','/');safe(ROOT,name)
            setup();remote=remote_files();base=json.loads(STATE.read_text(encoding='utf-8')) if STATE.exists() else {}
            if name not in remote:raise RuntimeError('File is not present in the remote source branch')
            base[name]=remote[name];save_state(base);print('Recorded manually merged file: '+name+'. Local content was retained.')
        elif len(sys.argv)==2 and sys.argv[1] in ('pull','push'):pull() if sys.argv[1]=='pull' else push()
        else:raise RuntimeError('Usage: python tools/source-sync.py pull|push|resolve relative-file-path')
    except Exception as e:print(str(e),file=sys.stderr);sys.exit(1)
