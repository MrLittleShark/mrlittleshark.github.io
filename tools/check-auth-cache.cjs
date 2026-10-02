'use strict';
// Deliberately retain the browser HTTP cache. Playwright request routing disables
// that cache, so this regression uses a local HTTP server and a fetch-only API fixture.
const assert=require('node:assert/strict'),http=require('node:http'),fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const {execFileSync}=require('node:child_process');
const {chromium}=require('C:/Users/shark/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root=path.resolve(__dirname,'..'),publicRoot=path.join(root,'public-openfoam'),out=path.join(root,'.openfoam-work/auth-cache');fs.mkdirSync(out,{recursive:true});
const legacy={};for(const name of ['account.js','appearance.js'])legacy['/assets/'+name]=execFileSync('git',['-C',path.join(root,'.source_foamlab'),'show','5703cad:themes/foam-lab/source/assets/'+name],{encoding:'utf8'});
const html=fs.readFileSync(path.join(publicRoot,'index.html'),'utf8');
const noVersion=html.replace(/(\/assets\/[^"']+\.(?:js|css))\?v=[a-f0-9]+/g,'$1');
const seed=noVersion.replace(/<div class="account-actions"[\s\S]*?<\/div>/,'<a class="account-nav" href="/account/" id="account-nav-label">登录 / 个人中心</a>').replace(/<script src="\/assets\/account-menu.js"[^>]*><\/script>/,'');
const hits=new Map(),errors=[];
const server=http.createServer((req,res)=>{
 const url=new URL(req.url,'http://localhost');hits.set(url.pathname+url.search,(hits.get(url.pathname+url.search)||0)+1);
 if(['/seed/','/mixed/','/fixed/'].includes(url.pathname)){res.writeHead(200,{'Content-Type':'text/html; charset=utf-8','Cache-Control':'no-store'});return res.end(url.pathname==='/seed/'?seed:url.pathname==='/mixed/'?noVersion:html);}
 if(url.pathname==='/assets/auth-config.json'){res.writeHead(200,{'Content-Type':'application/json','Cache-Control':'no-store'});return res.end(JSON.stringify({supabaseUrl:'https://cache-fixture.supabase.co',publishableKey:'sb_publishable_fixture'}));}
 const file=path.resolve(publicRoot,'.'+decodeURIComponent(url.pathname));
 if(!file.startsWith(publicRoot+path.sep)||!fs.existsSync(file)||!fs.statSync(file).isFile()){res.writeHead(404);return res.end();}
 const types={'.js':'text/javascript','.css':'text/css','.svg':'image/svg+xml','.json':'application/json','.png':'image/png','.woff2':'font/woff2'};
 res.writeHead(200,{'Content-Type':types[path.extname(file)]||'application/octet-stream','Cache-Control':'public, max-age=3600'});
 res.end(!url.search&&legacy[url.pathname]?legacy[url.pathname]:fs.readFileSync(file));
});
(async()=>{
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));const origin='http://127.0.0.1:'+server.address().port;
 const browser=await chromium.launch({channel:'msedge',headless:true});
 try{
  const context=await browser.newContext({viewport:{width:1440,height:1000}});
  await context.addInitScript(()=>{
   const user={id:'22222222-2222-4222-8222-222222222222',aud:'authenticated',role:'authenticated',app_metadata:{provider:'github'},user_metadata:{user_name:'fixture-user'}};
   if(!localStorage.getItem('foamlab-auth'))localStorage.setItem('foamlab-auth',JSON.stringify({access_token:'eyJhbGciOiJIUzI1NiJ9.'+btoa(JSON.stringify({sub:user.id,exp:Math.floor(Date.now()/1000)+3600}))+'.fixture',refresh_token:'fixture-refresh',expires_at:Math.floor(Date.now()/1000)+3600,expires_in:3600,token_type:'bearer',user}));
   const original=window.fetch;
   window.fetch=async(input,init={})=>{
    const url=new URL(typeof input==='string'?input:input.url||String(input),location.href);
    if(!url.hostname.endsWith('.supabase.co'))return original(input,init);
    let data=[];
    if(url.pathname==='/auth/v1/settings')data={external:{github:true}};
    else if(url.pathname==='/auth/v1/user')data=user;
    else if(url.pathname.endsWith('/foamlab_profiles'))data=[{user_id:user.id,display_name:'测试读者'}];
    else if(url.pathname.endsWith('/rpc/foamlab_pet'))data={pet:{user_id:user.id,name:'泡泡',form:'cub',outfit:'none',action:'wave',visible:true,motion:false,xp:40},level:1,level_start:0,next_level_xp:50,checked_in:false,items:[],events:[]};
    return new Response(JSON.stringify(data),{status:200,headers:{'content-type':'application/json'}});
   };
  });
  const p=await context.newPage();p.on('pageerror',e=>errors.push(e.message));
  await p.goto(origin+'/seed/');await p.evaluate(()=>window.foamAuth.ready);assert(await p.locator('#theme-toggle').isVisible());
  const before=hits.get('/assets/appearance.js');await p.goto(origin+'/mixed/');await p.evaluate(()=>window.foamAuth.ready);
  assert.equal(hits.get('/assets/appearance.js'),before,'old appearance script must actually come from HTTP cache');
  assert.equal(await p.locator('#theme-toggle').count(),0);assert(await p.locator('#nav-sign-out').isHidden());
  assert(errors.some(e=>e.includes('insertBefore')),'reproduce the old-script/new-markup error');
  errors.length=0;
  await p.goto(origin+'/fixed/');await p.evaluate(()=>window.foamAuth.ready);await p.locator('#nav-sign-out').waitFor();
  assert(await p.locator('#theme-toggle').isVisible());assert.equal(await p.locator('#home-panda-account').textContent(),'查看我的熊猫与学习记录 →');
  await p.locator('#account-nav-label').click();await p.locator('#account-panel').waitFor();
  assert.equal(await p.locator('#account-panel-status').textContent(),'GitHub 账号已登录');
  assert.deepEqual(errors,[]);
  const versioned=await p.locator('script[src],link[rel=stylesheet]').evaluateAll(nodes=>nodes.map(n=>n.getAttribute('src')||n.getAttribute('href')).filter(url=>url.startsWith('/assets/')));
  assert(versioned.length>30);for(const url of versioned){const parsed=new URL(url,origin);assert.match(parsed.searchParams.get('v'),/^[a-f0-9]{12}$/);const text=fs.readFileSync(path.join(publicRoot,parsed.pathname),'utf8').replaceAll('\r\n','\n');assert.equal(parsed.searchParams.get('v'),crypto.createHash('sha256').update(text).digest('hex').slice(0,12));}
  await p.screenshot({path:path.join(out,'updated-with-old-cache.png'),animations:'disabled'});
  const result={status:'passed',cacheEnabled:true,legacyBugReproduced:true,versionedAssets:versioned.length,sessionRetained:true,browserErrors:errors};fs.writeFileSync(path.join(out,'results.json'),JSON.stringify(result,null,2));console.log(JSON.stringify(result,null,2));
 }finally{await browser.close();await new Promise(resolve=>server.close(resolve));}
})().catch(e=>{console.error(e);server.close();process.exitCode=1;});
