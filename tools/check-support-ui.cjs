/* All authentication, database and storage traffic is fulfilled in this fixture.
 * The one-pixel image is test data, not a payment code. No external writes occur. */
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const {chromium}=require('C:/Users/shark/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const ORIGIN=process.env.FOAM_CHECK_ORIGIN||'http://localhost:4173',ROOT=path.resolve(__dirname,'..'),OUT=path.join(ROOT,'.openfoam-work/replan');
const ADMIN='11111111-1111-4111-8111-111111111111',MEMBER='22222222-2222-4222-8222-222222222222',checks=[];
const PNG=Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+aZ1sAAAAASUVORK5CYII=','base64');
const defaultSupport={enabled:false,message:'用于资料整理、计算示例核验与网站维护。',wechat_url:'',alipay_url:''};
const tick=()=>new Promise(resolve=>setTimeout(resolve,25));
async function until(predicate){for(let i=0;i<200;i++){if(predicate())return;await tick();}throw Error('Fixture condition timed out');}
async function fixture(browser,role='anon',options={}){
 const context=await browser.newContext({viewport:options.mobile?{width:390,height:844}:{width:1440,height:1000}});
 const user=role==='anon'?null:{id:role==='admin'?ADMIN:MEMBER,email:'fixture@example.invalid',aud:'authenticated',role:'authenticated',app_metadata:{provider:'github',providers:['github']},user_metadata:{user_name:'fixture-user'},created_at:'2026-10-02T01:00:00Z',identities:[]};
 const state={support:options.missing?undefined:{...defaultSupport,...options.support},failRead:false,failSave:false,failUpload:false,holdUploads:false,held:[],writes:[],reads:[],errors:[]};
 const token=user?['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9',Buffer.from(JSON.stringify({sub:user.id,exp:Math.floor(Date.now()/1000)+3600,role:'authenticated'})).toString('base64url'),'fixture-signature'].join('.'):null;
 await context.addInitScript(({user,token})=>{localStorage.clear();sessionStorage.clear();if(user)localStorage.setItem('foamlab-auth',JSON.stringify({access_token:token,refresh_token:'fixture-refresh',expires_at:Math.floor(Date.now()/1000)+3600,expires_in:3600,token_type:'bearer',user}));},{user,token});
 await context.route('**/*',async route=>{
  const req=route.request(),url=new URL(req.url()),method=req.method();
  const headers={'access-control-allow-origin':'*','access-control-expose-headers':'content-range'};
  const reply=(data,status=200,extra={})=>route.fulfill({status,headers:{...headers,...extra},contentType:'application/json',body:JSON.stringify(data)});
  if(url.origin===ORIGIN){
   if(url.pathname==='/assets/auth-config.json')return reply({supabaseUrl:'https://support-fixture.supabase.co',publishableKey:'sb_publishable_fixture'});
   if(['/assets/support.js','/assets/lab.js','/assets/cms.js'].includes(url.pathname))return route.fulfill({contentType:'text/javascript',body:fs.readFileSync(path.join(ROOT,'themes/foam-lab/source',url.pathname),'utf8')});
   return route.continue();
  }
  if(url.hostname==='fixture-images.invalid')return url.pathname==='/broken.png'?route.fulfill({status:404,body:''}):route.fulfill({contentType:'image/png',body:PNG});
  if(url.hostname!=='support-fixture.supabase.co')return route.abort();
  if(method==='OPTIONS')return route.fulfill({status:204,headers:{...headers,'access-control-allow-methods':'GET,POST,PATCH,PUT,DELETE,HEAD','access-control-allow-headers':'*'}});
  if(url.pathname==='/auth/v1/settings')return reply({external:{github:true}});
  if(url.pathname==='/auth/v1/user')return reply(user||{},user?200:401);
  if(url.pathname.startsWith('/auth/'))return reply({});
  if(url.pathname.startsWith('/storage/v1/object/public/'))return route.fulfill({contentType:'image/png',headers,body:PNG});
  if(url.pathname.startsWith('/storage/')){
   assert.equal(method,'POST');state.writes.push({table:'storage',path:url.pathname});
   if(state.holdUploads)await new Promise(resolve=>state.held.push({path:url.pathname,release:resolve}));
   return state.failUpload?reply({message:'模拟上传失败',error:'fixture upload rejected'},400):reply({Key:url.pathname.split('/object/')[1]});
  }
  const table=url.pathname.split('/').pop();
  if(method==='POST'){
   assert.equal(table,'foamlab_settings','Unexpected fixture write');assert.equal(role,'admin');
   const body=req.postDataJSON();state.writes.push({table,body});
   if(state.failSave)return reply({message:'模拟保存失败'},503);
   assert.equal(body.key,'support');state.support=structuredClone(body.value);return route.fulfill({status:204,headers});
  }
  assert(['GET','HEAD'].includes(method),'Unexpected mutation '+method);state.reads.push({table,key:url.searchParams.get('key')});
  let rows=[];
  if(table==='foamlab_settings'){
   if(state.failRead&&url.searchParams.get('key')==='eq.support')return reply({message:'模拟读取失败'},503);
   rows=[{key:'site',value:{name:'FoamLab',discussion_open:true}},...(state.support?[{key:'support',value:state.support}]:[])];
  }else if(table==='foamlab_roles')rows=role!=='anon'&&role!=='member'?[{user_id:user.id,role}]:[];
  else if(table==='foamlab_profiles')rows=user?[{user_id:user.id,display_name:'隔离测试用户'}]:[];
  else assert(['foamlab_public_profiles','foamlab_learning_progress','foamlab_content','foamlab_threads','foamlab_messages','foamlab_revisions'].includes(table),'Unknown table '+table);
  rows=rows.filter(row=>[...url.searchParams].every(([key,value])=>!value.startsWith('eq.')||String(row[key])===value.slice(3)));
  if(method==='HEAD')return route.fulfill({status:200,headers:{...headers,'content-range':'0-0/'+rows.length}});
  if((req.headers().accept||'').includes('vnd.pgrst.object'))return rows.length===1?reply(rows[0]):reply({code:'PGRST116',message:'No rows',details:'The result contains 0 rows'},406);
  return reply(rows,200,{'content-range':'0-'+Math.max(0,rows.length-1)+'/'+rows.length});
 });
 const page=await context.newPage();page.on('pageerror',e=>state.errors.push(e.message));
 return {page,state,async close(){assert.deepEqual(state.errors,[],'Unhandled browser errors');await context.close();}};
}
async function adminSettings(f){await f.page.goto(ORIGIN+'/admin/');await f.page.locator('[data-cms-tab=settings]').click();await f.page.locator('#cms-support-form').waitFor();}
async function status(page,text){await page.waitForFunction(t=>document.querySelector('#cms-support-form .form-status')?.textContent.includes(t),text);}
async function submit(page){await page.locator('#cms-support-form [type=submit]').click();}
const imageFile=(name='fixture.png')=>({name,mimeType:'image/png',buffer:PNG});
(async()=>{
 fs.mkdirSync(OUT,{recursive:true});const browser=await chromium.launch({channel:'msedge',headless:true});
 try{
  for(const missing of [false,true]){
   const f=await fixture(browser,'anon',{missing,mobile:true});await f.page.goto(ORIGIN+'/support/');await f.page.locator('.support-inactive').waitFor();
   assert.match(await f.page.locator('#support-content').textContent(),/暂未启用/);assert.equal(await f.page.locator('#support-content img').count(),0);assert.equal(f.state.writes.length,0);
   assert(await f.page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2));if(!missing)await f.page.screenshot({path:path.join(OUT,'support-disabled-mobile.png'),fullPage:true,animations:'disabled'});await f.close();
  }checks.push('anonymous default and missing configuration stay disabled; mobile layout; no writes');

  const publicView=await fixture(browser,'anon',{support:{enabled:true,message:'<img src=x onerror=alert(1)> 资料核验',wechat_url:'https://fixture-images.invalid/wechat.png',alipay_url:'http://unsafe.invalid/qr.png'}});
  await publicView.page.goto(ORIGIN+'/support/');await publicView.page.locator('.support-option img').waitFor();assert.equal(await publicView.page.locator('.support-option').count(),1);assert.equal(await publicView.page.locator('.support-note img').count(),0);assert.match(await publicView.page.locator('.support-note').textContent(),/<img/);assert.match(await publicView.page.locator('.support-option a').getAttribute('rel'),/noopener/);assert.equal(publicView.state.writes.length,0);
  publicView.state.support.alipay_url='https://fixture-images.invalid/alipay.png';await publicView.page.reload();await publicView.page.waitForFunction(()=>document.querySelectorAll('.support-option').length===2);await publicView.page.screenshot({path:path.join(OUT,'support-enabled-mock.png'),fullPage:true,animations:'disabled'});await publicView.page.setViewportSize({width:390,height:844});assert(await publicView.page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2));await publicView.page.screenshot({path:path.join(OUT,'support-enabled-mobile-mock.png'),fullPage:true,animations:'disabled'});
  publicView.state.support.wechat_url='https://fixture-images.invalid/broken.png';await publicView.page.reload();await publicView.page.locator('#support-content .lab-evidence').waitFor();assert.match(await publicView.page.locator('#support-content .lab-evidence').textContent(),/无法载入/);await publicView.close();checks.push('public enabled image rendering; escaped message; unsafe URL filtered; broken image fallback; desktop/mobile');

  const failed=await fixture(browser);failed.state.failRead=true;await failed.page.goto(ORIGIN+'/support/');await failed.page.locator('#support-content [role=alert]').waitFor();assert.match(await failed.page.locator('#support-content').textContent(),/模拟读取失败/);assert.equal(failed.state.writes.length,0);await failed.close();checks.push('public read failure reports service error rather than inventing payment details');

  const admin=await fixture(browser,'admin');const p=admin.page;await adminSettings(admin);assert.equal(await p.locator('#cms-support-form').count(),1);await p.locator('#cms-support-form [name=enabled]').check();await submit(p);await status(p,'至少配置一种');assert.equal(admin.state.writes.length,0);
  await p.locator('#cms-support-form [name=wechat_url]').fill('https://fixture-images.invalid/wechat.png');
  for(const invalid of ['javascript:alert(1)','http://unsafe.invalid/qr.png','not-an-image-address','https://user:secret@fixture-images.invalid/qr.png']){
   await p.locator('#cms-support-form [name=alipay_url]').fill(invalid);await submit(p);await status(p,'支付宝图片地址无效');assert.equal(admin.state.writes.length,0);assert.equal(await p.locator('#cms-support-form [name=alipay_url]').inputValue(),invalid);
  }
  await p.locator('#cms-support-form [name=alipay_url]').fill('');checks.push('admin enable requires a code; nonempty unsafe or malformed address rejected without silently clearing it');

  for(const file of [{name:'bad.svg',mimeType:'image/svg+xml',buffer:Buffer.from('<svg/>')},{name:'large.png',mimeType:'image/png',buffer:Buffer.alloc(5*1024*1024+1)},{name:'empty.png',mimeType:'image/png',buffer:Buffer.alloc(0)}]){
   await p.setInputFiles('[data-support-upload=wechat]',file);await status(p,'请选择不超过 5 MB');assert.equal(admin.state.writes.length,0);
  }checks.push('upload rejects unsupported type, oversized file and empty file');

  admin.state.holdUploads=true;await p.setInputFiles('[data-support-upload=wechat]',imageFile());await until(()=>admin.state.held.length===1);await p.setInputFiles('[data-support-upload=alipay]',imageFile('second.png'));await until(()=>admin.state.held.length===2);
  assert(await p.locator('#cms-support-form [type=submit]').isDisabled());admin.state.held[0].release();await p.waitForFunction(()=>!document.querySelector('[data-support-upload=wechat]').disabled);assert(await p.locator('#cms-support-form [type=submit]').isDisabled());
  await p.locator('#cms-support-form').dispatchEvent('submit');await status(p,'等待所有图片');assert.equal(admin.state.writes.filter(w=>w.table==='foamlab_settings').length,0);admin.state.held[1].release();await p.waitForFunction(()=>!document.querySelector('#cms-support-form [type=submit]').disabled);admin.state.holdUploads=false;
  assert.match(await p.locator('#cms-support-form [name=wechat_url]').inputValue(),/\/library\/support-wechat-.*\.png$/);assert.match(await p.locator('#cms-support-form [name=alipay_url]').inputValue(),/\/library\/support-alipay-.*\.png$/);assert.equal(await p.locator('.support-admin-preview:not([hidden])').count(),2);assert.equal(admin.state.support.enabled,false);checks.push('concurrent uploads keep save disabled until both finish; direct submit blocked; upload does not auto-publish');

  admin.state.failUpload=true;const old=await p.locator('#cms-support-form [name=wechat_url]').inputValue();await p.setInputFiles('[data-support-upload=wechat]',imageFile('fail.png'));await status(p,'模拟上传失败');assert.equal(await p.locator('#cms-support-form [name=wechat_url]').inputValue(),old);assert.equal(await p.locator('#cms-support-form [type=submit]').isDisabled(),false);admin.state.failUpload=false;checks.push('upload failure preserves prior image and restores controls');

  await p.locator('#cms-support-form [name=message]').fill('支持可复核算例与资料维护');admin.state.failSave=true;await submit(p);await status(p,'模拟保存失败');assert.equal(admin.state.support.enabled,false);assert.equal(await p.locator('#cms-support-form [name=message]').inputValue(),'支持可复核算例与资料维护');admin.state.failSave=false;await submit(p);await status(p,'支持设置已保存');assert.equal(admin.state.support.enabled,true);assert.equal(admin.state.support.message,'支持可复核算例与资料维护');
  await p.evaluate(()=>{document.activeElement?.blur();scrollTo(0,0);});await p.screenshot({path:path.join(OUT,'support-admin-mock.png'),fullPage:true,animations:'disabled'});await p.setViewportSize({width:390,height:844});assert(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2));await p.evaluate(()=>scrollTo(0,0));await p.screenshot({path:path.join(OUT,'support-admin-mobile-mock.png'),fullPage:true,animations:'disabled'});
  await p.goto(ORIGIN+'/support/');await p.waitForFunction(()=>document.querySelectorAll('.support-option').length===2);assert.equal(await p.locator('.support-note').textContent(),'支持可复核算例与资料维护');await adminSettings(admin);assert(await p.locator('#cms-support-form [name=enabled]').isChecked());assert.equal(await p.locator('#cms-support-form').count(),1);await p.locator('#cms-support-form [name=enabled]').uncheck();await submit(p);await status(p,'支持设置已保存');await p.goto(ORIGIN+'/support/');await p.locator('.support-inactive').waitFor();await admin.close();checks.push('save failure retry; settings persist across admin/public navigation; disable hides codes; mobile admin');

  for(const role of ['anon','member','editor','moderator']){
   const f=await fixture(browser,role);await f.page.goto(ORIGIN+(role==='member'?'/studio/':'/admin/'));await f.page.waitForFunction(()=>window.FoamLab?.role!==null||!!document.querySelector('#cms-root [data-lab-login]'));await f.page.locator('#cms-root .lab-loading').waitFor({state:'detached'});assert.equal(await f.page.locator('[data-cms-tab=settings]').count(),0);assert.equal(await f.page.locator('#cms-support-form').count(),0);
   // Even an injected settings form cannot activate the admin-only extension.
   await f.page.evaluate(()=>{const form=document.createElement('form');form.id='cms-settings-form';document.querySelector('#cms-root').append(form);});await f.page.waitForTimeout(120);assert.equal(await f.page.locator('#cms-support-form').count(),0);assert.equal(f.state.reads.filter(r=>r.key==='eq.support').length,0);assert.equal(f.state.writes.length,0);await f.close();
  }checks.push('anonymous, member, editor and moderator cannot see or trigger support settings');
  const report={passed:checks.length,checks,externalWrites:0,note:'All authentication/database/storage responses and images are isolated fixtures; no real QR or payment flow tested.'};fs.writeFileSync(path.join(OUT,'support-ui-check.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
