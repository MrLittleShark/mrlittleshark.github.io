// Real Supabase browser SDK; isolated HTTP fixtures and synthetic sessions only.
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const {chromium}=require('C:/Users/shark/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const {fixture,ORIGIN}=require('./check-cms-ui.cjs');
const checks=[];
const json=(route,body,status=200)=>route.fulfill({status,contentType:'application/json',headers:{'access-control-allow-origin':'*'},body:JSON.stringify(body)});
async function visit(page,path){await page.goto(ORIGIN+path);await page.evaluate(async()=>{await window.foamAuth.ready;await window.foamAuth.profileReady;});}
async function signed(page){assert.equal(await page.locator('#account-nav-label').textContent(),'个人中心');assert(await page.evaluate(()=>!!window.foamAuth.user));}
const waitSigned=page=>page.waitForFunction(()=>window.foamAuth?.user&&!window.foamAuth.loading&&window.FoamLab?.user);
const waitOut=page=>page.waitForFunction(()=>window.foamAuth&&!window.foamAuth.loading&&!window.foamAuth.user&&!window.FoamLab?.user);
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 try{
  const f=await fixture(browser,'member',{persistSession:true});
  await visit(f.page,'/account/');await signed(f.page);
  await f.context.route('https://cms-fixture.supabase.co/auth/v1/settings',r=>json(r,{message:'temporary outage'},503));
  await visit(f.page,'/courses/');await signed(f.page);
  checks.push('session survives navigation when provider settings are unavailable');
  await f.context.route('https://cms-fixture.supabase.co/auth/v1/user',r=>json(r,{message:'temporary outage'},502));
  await visit(f.page,'/commands/');await signed(f.page);
  checks.push('temporary user-service failure does not become logout');
  await f.context.unroute('https://cms-fixture.supabase.co/auth/v1/user');
  await f.context.route('https://cms-fixture.supabase.co/rest/v1/foamlab_profiles?**',r=>json(r,{message:'temporary data outage'},503));
  await visit(f.page,'/account/');await signed(f.page);
  assert(await f.page.locator('[name=display_name]').isDisabled());assert(await f.page.locator('#sign-in').isHidden());
  checks.push('profile-service failure keeps login and disables unavailable editing');
  await f.context.unroute('https://cms-fixture.supabase.co/rest/v1/foamlab_profiles?**');
  for(const route of ['/community/','/programming/','/account/']){await visit(f.page,route);await signed(f.page);}
  await f.page.reload();await waitSigned(f.page);
  const saved=await f.context.storageState();
  await f.close();
  const restored=await fixture(browser,'member',{persistSession:true,storageState:saved});
  await visit(restored.page,'/account/');await signed(restored.page);
  checks.push('full page navigation, reload, and restored browser storage keep the session');
  const tab=await restored.context.newPage();await visit(tab,'/community/');await waitSigned(tab);
  await restored.page.locator('#nav-sign-out').click();
  await waitOut(restored.page);await waitOut(tab);
  assert.equal(await tab.evaluate(()=>localStorage.getItem('foamlab-auth')),null);
  await visit(tab,'/courses/');await waitOut(tab);
  assert(await tab.locator('#nav-sign-out').isHidden());
  checks.push('explicit logout clears persistent storage and updates all open tabs');
  await restored.close();

  const expired=structuredClone(saved),entry=expired.origins[0].localStorage.find(x=>x.name==='foamlab-auth');
  const oldSession=JSON.parse(entry.value);oldSession.expires_at=Math.floor(Date.now()/1000)-60;entry.value=JSON.stringify(oldSession);
  const renewed={...oldSession,access_token:oldSession.access_token.replace('test-signature','renewed-signature'),expires_at:Math.floor(Date.now()/1000)+7200,expires_in:7200,refresh_token:'rotated-fixture-refresh'};
  let refreshes=0;
  const refresh=await fixture(browser,'member',{persistSession:true,storageState:expired});
  await refresh.context.route('https://cms-fixture.supabase.co/auth/v1/token?grant_type=refresh_token',r=>{refreshes++;assert.equal(r.request().postDataJSON().refresh_token,'fixture-refresh');return json(r,renewed);});
  await visit(refresh.page,'/courses/');await signed(refresh.page);
  assert.equal(refreshes,1);assert.equal(await refresh.page.evaluate(()=>JSON.parse(localStorage.getItem('foamlab-auth')).refresh_token),'rotated-fixture-refresh');
  await visit(refresh.page,'/community/');await signed(refresh.page);assert.equal(refreshes,1);
  checks.push('expired access token is renewed once and reused after navigation');await refresh.close();

  const invalid=await fixture(browser,'member',{persistSession:true,storageState:expired});
  await invalid.context.route('https://cms-fixture.supabase.co/auth/v1/token?grant_type=refresh_token',r=>json(r,{message:'Invalid Refresh Token',code:'refresh_token_not_found'},400));
  await visit(invalid.page,'/account/');await waitOut(invalid.page);
  assert.equal(await invalid.page.evaluate(()=>localStorage.getItem('foamlab-auth')),null);
  checks.push('revoked refresh token returns to signed-out state');await invalid.close();

  const denied=await fixture(browser,'member',{persistSession:true});
  await denied.context.route('https://cms-fixture.supabase.co/auth/v1/user',r=>json(r,{message:'Invalid JWT',code:'bad_jwt'},401));
  await visit(denied.page,'/account/');await waitOut(denied.page);
  assert.equal(await denied.page.evaluate(()=>localStorage.getItem('foamlab-auth')),null);
  checks.push('confirmed invalid identity clears the stored session');await denied.close();

  const oauth=await fixture(browser,'anon',{persistSession:true});let challenge='',exchanges=0;
  await oauth.context.route('https://cms-fixture.supabase.co/auth/v1/authorize?**',async r=>{
   const u=new URL(r.request().url());assert.equal(u.searchParams.get('provider'),'github');assert.equal(u.searchParams.get('redirect_to'),ORIGIN+'/account/');challenge=u.searchParams.get('code_challenge');assert(challenge);
   await r.fulfill({status:302,headers:{location:ORIGIN+'/account/?code=fixture-auth-code'},body:''});
  });
  await oauth.context.route('https://cms-fixture.supabase.co/auth/v1/token?grant_type=pkce',r=>{
   const body=r.request().postDataJSON();assert.equal(body.auth_code,'fixture-auth-code');assert.equal(crypto.createHash('sha256').update(body.code_verifier).digest('base64url'),challenge);exchanges++;return json(r,renewed);
  });
  await oauth.context.route('https://cms-fixture.supabase.co/auth/v1/user',r=>json(r,renewed.user));
  await visit(oauth.page,'/account/');await waitOut(oauth.page);
  const waitingTab=await oauth.context.newPage();await visit(waitingTab,'/community/');await waitOut(waitingTab);
  await oauth.page.locator('#sign-in').click();await waitSigned(oauth.page);await waitSigned(waitingTab);
  assert.equal(exchanges,1);await visit(oauth.page,'/commands/');await signed(oauth.page);
  assert.equal(await oauth.page.evaluate(()=>!!localStorage.getItem('foamlab-auth')),true);
  checks.push('OAuth PKCE callback persists login and signs in an already-open tab');
  await oauth.close();

  const admin=await fixture(browser,'admin',{persistSession:true});
  await visit(admin.page,'/admin/');await admin.page.locator('#cms-new').waitFor();
  const adminTab=await admin.context.newPage();await visit(adminTab,'/account/');await adminTab.waitForFunction(()=>document.querySelector('#profile-admin-link')?.hidden===false);
  await adminTab.locator('#sign-out').click();await waitOut(adminTab);await waitOut(admin.page);
  assert.equal(await admin.page.locator('#cms-new').count(),0);assert(await adminTab.locator('#profile-admin-link').isHidden());
  checks.push('logout removes administrator controls in every open page');await admin.close();

  const slow=await fixture(browser,'member',{persistSession:true});
  let releaseProfile;const pendingProfile=new Promise(resolve=>releaseProfile=resolve);
  await slow.context.route('https://cms-fixture.supabase.co/rest/v1/foamlab_profiles?**',async r=>{await pendingProfile;return json(r,{user_id:renewed.user.id,display_name:'Delayed response'});});
  await slow.page.goto(ORIGIN+'/account/');await slow.page.locator('#nav-sign-out').waitFor();
  await slow.page.locator('#nav-sign-out').click();await slow.page.waitForFunction(()=>window.foamAuth?.user===null);
  releaseProfile();await slow.page.evaluate(()=>window.foamAuth.ready);await waitOut(slow.page);
  assert.equal(await slow.page.locator('#account-name').textContent(),'尚未登录');
  assert.equal(await slow.page.evaluate(()=>window.foamAuth.profile),null);
  checks.push('late profile response cannot restore an explicitly ended session');await slow.close();

  const logoutError=await fixture(browser,'member',{persistSession:true});await visit(logoutError.page,'/account/');
  await logoutError.context.route('https://cms-fixture.supabase.co/auth/v1/logout?**',r=>json(r,{message:'temporary outage'},503));
  await logoutError.page.locator('#nav-sign-out').click();await waitOut(logoutError.page);
  assert.equal(await logoutError.page.evaluate(()=>localStorage.getItem('foamlab-auth')),null);
  checks.push('explicit logout clears this browser even during a service outage');await logoutError.close();

  const mobile=await fixture(browser,'member',{persistSession:true,mobile:true});await visit(mobile.page,'/account/');await waitSigned(mobile.page);
  assert(await mobile.page.locator('#nav-sign-out').isVisible());
  assert(await mobile.page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
  await mobile.page.setViewportSize({width:320,height:750});assert(await mobile.page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));await mobile.page.setViewportSize({width:390,height:844});
  const out=path.resolve(__dirname,'../.openfoam-work/auth-session');fs.mkdirSync(out,{recursive:true});
  for(const theme of ['light','dark']){await mobile.page.evaluate(theme=>document.documentElement.dataset.theme=theme,theme);await mobile.page.screenshot({path:path.join(out,'mobile-'+theme+'.png'),animations:'disabled'});}
  checks.push('mobile header fits in light and dark themes');await mobile.close();
  const result={status:'passed',mode:'real browser SDK with isolated auth service, no real GitHub credentials',checks};fs.writeFileSync(path.resolve(__dirname,'../.openfoam-work/auth-session/results.json'),JSON.stringify(result,null,2));console.log(JSON.stringify(result,null,2));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
