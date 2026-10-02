'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const {chromium}=require('C:/Users/shark/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const {fixture,ORIGIN,MEMBER}=require('./check-cms-ui.cjs');
const out=path.resolve(__dirname,'../.openfoam-work/account-menu');fs.mkdirSync(out,{recursive:true});
const checks=[];
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 try{
  const f=await fixture(browser,'member',{persistSession:true});let xp=600;
  await f.context.route('**/rest/v1/rpc/foamlab_pet',r=>{
   const data=r.request().postDataJSON();if(data.operation==='checkin')xp+=10;
   return r.fulfill({contentType:'application/json',headers:{'access-control-allow-origin':'*'},body:JSON.stringify({pet:{user_id:MEMBER,name:'泡泡',form:'cub',outfit:'scarf',decoration:'no-decor',action:'wave',motion:true,visible:true,xp},level:5,level_start:500,next_level_xp:750,checked_in:xp>600,items:[],events:[]})});
  });
  const p=f.page;
  await p.goto(ORIGIN+'/');await p.waitForFunction(()=>window.foamAuth?.profile?.display_name&&window.foamAuth.pet?.level===5);
  assert.equal(await p.locator('#home-panda-account').textContent(),'查看我的熊猫与学习记录 →');
  await p.locator('#account-nav-label').click();await p.locator('#account-panel').waitFor();
  assert.equal(await p.locator('#account-nav-label').getAttribute('aria-expanded'),'true');
  assert.equal(await p.locator('#account-panel-name').textContent(),'测试读者');assert.equal(await p.locator('#account-panel-level').textContent(),'Lv.5');
  assert.match(await p.locator('#account-panel-xp').textContent(),/600 经验/);assert(await p.locator('#account-panel-badge').isVisible());
  assert(await p.locator('#account-panel [data-management-link]').isHidden());
  for(const theme of ['light','dark']){await p.evaluate(t=>document.documentElement.dataset.theme=t,theme);await p.screenshot({path:path.join(out,'desktop-'+theme+'.png'),animations:'disabled'});}
  await p.keyboard.press('Escape');assert(await p.locator('#account-panel').isHidden());assert(await p.locator('#account-nav-label').evaluate(el=>el===document.activeElement));
  await p.locator('#account-nav-label').click();await p.locator('h1').click();assert(await p.locator('#account-panel').isHidden());
  checks.push('homepage login prompt, shared identity, nickname, level, XP, keyboard and outside dismissal');
  const other=await f.context.newPage();await other.goto(ORIGIN+'/courses/');await other.waitForFunction(()=>window.foamAuth?.pet?.xp===600);await other.locator('#account-nav-label').click();
  await p.goto(ORIGIN+'/account/#my-panda');await p.locator('#panda-checkin').click();await p.waitForFunction(()=>window.foamAuth.pet?.xp===610);
  await other.waitForFunction(()=>document.querySelector('#account-panel-xp')?.textContent.includes('610 经验'));
  await p.locator('#account-nav-label').click();assert.match(await p.locator('#account-panel-xp').textContent(),/610 经验/);
  await p.locator('#account-panel a[href="/account/#profile-form"]').click();await p.waitForURL('**/account/#profile-form');await p.evaluate(()=>window.foamAuth.profileReady);
  await p.locator('[name=display_name]').fill('小鲨鱼');await p.getByRole('button',{name:'保存个人资料',exact:true}).click();await p.getByText('个人资料已保存到账号。',{exact:true}).waitFor();
  await p.locator('#account-nav-label').click();assert.equal(await p.locator('#account-panel-name').textContent(),'小鲨鱼');
  await other.waitForFunction(()=>document.querySelector('#account-panel-name')?.textContent==='小鲨鱼');await other.close();
  for(const url of ['/courses/','/community/','/commands/','/']){
   await p.goto(ORIGIN+url);await p.evaluate(()=>window.foamAuth.ready);await p.locator('#account-nav-label').click();
   assert.equal(await p.locator('#account-panel-name').textContent(),'小鲨鱼');assert.equal(await p.locator('#account-panel-level').textContent(),'Lv.5');assert.match(await p.locator('#account-panel-xp').textContent(),/610 经验/);
  }
  checks.push('check-in and profile edits update the panel and survive navigation');
  for(const width of [320,390]){
   await p.setViewportSize({width,height:844});const r=await p.locator('#account-panel').boundingBox();assert(r.x>=0&&r.x+r.width<=width);assert(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
  }
  for(const theme of ['light','dark']){await p.evaluate(t=>document.documentElement.dataset.theme=t,theme);await p.screenshot({path:path.join(out,'mobile-'+theme+'.png'),animations:'disabled'});}
  checks.push('account panel fits mobile screens in both themes');
  await p.locator('#account-panel [data-account-sign-out]').click();await p.waitForFunction(()=>window.foamAuth&&!window.foamAuth.loading&&!window.foamAuth.user);
  await p.locator('#account-nav-label').click();await p.locator('#account-panel-sign-in').waitFor();
  assert(await p.locator('#account-panel-member').isHidden());assert.equal(await p.locator('#account-panel-status').textContent(),'尚未登录');assert.match(await p.locator('#home-panda-account').textContent(),/^登录后/);
  checks.push('panel logout removes member data and shows GitHub sign-in');await f.close();

  const slow=await fixture(browser,'member',{persistSession:true});let release;const held=new Promise(resolve=>release=resolve);
  await slow.context.route('https://cms-fixture.supabase.co/auth/v1/user',async r=>{await held;await r.fulfill({contentType:'application/json',body:JSON.stringify({id:MEMBER,user_metadata:{user_name:'fixture-user'}})});});
  await slow.page.goto(ORIGIN+'/');await slow.page.waitForFunction(()=>window.foamAuth?.user&&!window.foamAuth.loading);
  // If ready still awaited user/profile calls, this would time out until release.
  await slow.page.evaluate(()=>Promise.race([window.foamAuth.ready,new Promise((_,reject)=>setTimeout(()=>reject(Error('auth ready blocked by profile service')),1000))]));
  await slow.page.locator('#account-nav-label').click();assert.equal(await slow.page.locator('#account-panel-status').textContent(),'GitHub 账号已登录');assert.equal(await slow.page.locator('#home-panda-account').textContent(),'查看我的熊猫与学习记录 →');
  release();await slow.page.evaluate(()=>window.foamAuth.profileReady);checks.push('slow profile verification does not block shared login or the account panel');await slow.close();
  const result={status:'passed',checks,externalWrites:0};fs.writeFileSync(path.join(out,'results.json'),JSON.stringify(result,null,2));console.log(JSON.stringify(result,null,2));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
