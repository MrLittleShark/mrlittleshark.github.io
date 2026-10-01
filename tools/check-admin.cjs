const assert=require('node:assert/strict'),fs=require('node:fs');
(async()=>{
 const source=fs.readFileSync('supabase/functions/foamlab-admin/index.ts','utf8');
 const {createHandler}=await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));
 const owner=112299157;let calls=[],mode='owner';
 const response=(data,status=200,headers={})=>new Response(JSON.stringify(data),{status,headers:{'Content-Type':'application/json',...headers}});
 const handler=createHandler({url:'https://auth.example',key:'public'},async(url,options)=>{
  calls.push({url,options});
  if(url.endsWith('/auth/v1/user'))return response({id:'verified-user',user_metadata:{role:'admin'},identities:[{provider:'github',id:mode==='mismatch'?'42':String(owner)}]});
  if(url==='https://api.github.com/user')return response({id:mode==='student'?42:owner,login:'MrLittleShark'},200,{'x-oauth-scopes':mode==='readonly'?'read:user':'public_repo'});
  if(url.endsWith('/issues/5')&&options.method!=='PATCH')return response({user:{id:42},title:'[作业发布] Student'});
  if(url.includes('/contents/')&&options.method==='PUT')return response({message:'conflict'},409);
  if(url.endsWith('/issues')&&options.method==='POST')return response({number:16,html_url:'https://github.com/example/issues/16',title:JSON.parse(options.body).title});
  return response({permissions:{push:true}});
 });
 async function call(input,authorization='Bearer mock.jwt.token'){calls=[];return handler(new Request('https://service.example',{method:'POST',headers:{Authorization:authorization,Origin:'https://mrlittleshark.github.io'},body:JSON.stringify({githubToken:'test-only',...input})}));}
 assert.equal((await call({action:'status'},'')).status,401);assert.equal(calls.length,0);
 mode='student';assert.equal((await call({action:'publish',kind:'assignment',title:'Test',body:'Body'})).status,403);assert.equal(calls.length,2);
 mode='mismatch';assert.equal((await call({action:'status'})).status,403);
 mode='owner';assert.equal((await call({action:'status'})).status,200);
 assert.equal((await call({action:'content-save',path:'source-openfoam/../_config.yml'})).status,403);
 assert.equal((await call({action:'record-update',number:5,kind:'assignment',title:'Test',body:'Body',state:'closed'})).status,403);assert(!calls.some(x=>x.options.method==='PATCH'));
 mode='readonly';assert.equal((await call({action:'publish',kind:'assignment',title:'Test',body:'Body'})).status,403);
 mode='owner';const publish=await call({action:'publish',kind:'assignment',title:'Test',body:'Body'});assert.equal(publish.status,200);assert.equal((await publish.json()).title,'[作业发布] Test');
 assert.equal((await call({action:'content-save',path:'source-openfoam/lessons/01/index.md',content:'---\ntitle: Test\n---\nBody',sha:'a'.repeat(40)})).status,409);
 console.log('Admin authorization, identity binding, path restriction, scope checks, publication and conflict handling: passed (isolated HTTP fixtures).');
})().catch(e=>{console.error(e);process.exitCode=1;});
