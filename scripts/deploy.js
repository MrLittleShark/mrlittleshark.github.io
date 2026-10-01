'use strict';
// A Hexo deployer that preserves repository history and refuses non-fast-forward pushes.
const fs=require('node:fs');
const path=require('node:path');
const {execFileSync}=require('node:child_process');
hexo.extend.deployer.register('git-safe',async function(args){
  const root=path.resolve(this.base_dir), deploy=path.resolve(root,'.deploy_foamlab');
  if(args.source_branch==='foamlab-source'){
    const python=process.platform==='win32'&&fs.existsSync('D:/anaconda3/python.exe')?'D:/anaconda3/python.exe':process.platform==='win32'?'python':'python3';
    const sync=mode=>execFileSync(python,['-X','utf8',path.join(root,'tools/source-sync.py'),mode],{cwd:root,stdio:'inherit'});
    sync('pull');
    await this.call('generate');
    sync('push');
    this.log.info('Hexo source published; GitHub Actions will validate, build and deploy the website.');
    return;
  }
  if(path.dirname(deploy)!==root||path.basename(deploy)!=='.deploy_foamlab')throw new Error('Unexpected deployment directory');
  const repo=args.repo,branch=args.branch||'main';
  if(repo!=='https://github.com/MrLittleShark/MrLittleShark.github.io.git'||branch!=='main')throw new Error('Review deploy.js for a new repository or branch');
  const run=(...gitArgs)=>execFileSync('git',gitArgs,{cwd:deploy,stdio:'inherit',env:{...process.env,GIT_TERMINAL_PROMPT:'0',GCM_INTERACTIVE:'Never'}});
  if(!fs.existsSync(path.join(deploy,'.git'))){
    if(fs.existsSync(deploy)&&fs.readdirSync(deploy).length)throw new Error('Deployment folder is not an empty Git checkout');
    execFileSync('git',['clone','--branch',branch,repo,deploy],{cwd:root,stdio:'inherit',env:{...process.env,GIT_TERMINAL_PROMPT:'0',GCM_INTERACTIVE:'Never'}});
  }
  const dirty=execFileSync('git',['status','--porcelain'],{cwd:deploy,encoding:'utf8'}).trim();
  if(dirty)throw new Error('Deployment checkout has local changes; inspect .deploy_foamlab before retrying');
  run('fetch','origin',branch);
  run('merge','--ff-only','origin/'+branch);
  const publicDir=path.resolve(this.public_dir);
  if(!publicDir.startsWith(root+path.sep)||!fs.existsSync(path.join(publicDir,'index.html')))throw new Error('Generate the website before deploying');
  // Only this verified, dedicated generated-site checkout is cleared.
  for(const entry of fs.readdirSync(deploy)){if(entry!=='.git'){const target=path.resolve(deploy,entry);if(path.dirname(target)!==deploy)throw new Error('Unsafe target');fs.rmSync(target,{recursive:true,force:true});}}
  fs.cpSync(publicDir,deploy,{recursive:true});
  const forms=path.join(root,'.github','ISSUE_TEMPLATE');
  if(fs.existsSync(forms))fs.cpSync(forms,path.join(deploy,'.github','ISSUE_TEMPLATE'),{recursive:true});
  const workflows=path.join(root,'.github','workflows');
  if(fs.existsSync(workflows))fs.cpSync(workflows,path.join(deploy,'.github','workflows'),{recursive:true});
  fs.writeFileSync(path.join(deploy,'.nojekyll'),'');
  fs.writeFileSync(path.join(deploy,'README.md'),'# FoamLab\n\nOpenFOAM v2512 learning website.\n\nhttps://mrlittleshark.github.io/\n\nBuilt and deployed with Hexo. Course interactions use public GitHub Issues.\n');
  run('add','--all');
  const changes=execFileSync('git',['diff','--cached','--name-only'],{cwd:deploy,encoding:'utf8'}).trim();
  if(changes)run('commit','-m',args.message||'Publish FoamLab OpenFOAM v2512 learning site');
  // A concurrent upstream change rejects this push instead of being overwritten.
  run('push','origin','HEAD:'+branch);
  this.log.info('Published with Hexo; Git history preserved.');
});
