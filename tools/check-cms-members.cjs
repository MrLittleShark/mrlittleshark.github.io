const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const {chromium}=require('C:/Users/shark/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const {fixture,ready,OUT,ADMIN,MEMBER}=require('./check-cms-ui.cjs');
const {memberRPC}=require('./member-fixture.cjs');
const checks=[];
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 try{
  const f=await fixture(browser,'admin'),p=f.page,rpc=await memberRPC(f,61);
  const done=()=>p.waitForFunction(()=>document.querySelector('.cms-member-status')?.textContent.startsWith('共 '));
  const change=async(key,value)=>{const e=p.locator(`[data-member-filter="${key}"]`);key==='q'?await e.fill(value):await e.selectOption(value);await done();};
  await ready(p,'/admin/?tab=members','.cms-member-table');await done();
  assert.equal(await p.locator('[data-member-id]').count(),25);assert.equal(await p.locator('.cms-nav>[data-cms-tab=roles]').textContent(),'成员管理');
  assert((await p.locator('.cms-member-status').textContent()).includes('61 位成员'));checks.push('full registration list includes 59 users without public/private profiles');
  await p.getByRole('button',{name:'最后一页',exact:true}).click();await done();assert.equal(await p.locator('[data-member-id]').count(),11);
  assert(await p.getByRole('button',{name:'最后一页',exact:true}).isDisabled());assert(await p.locator(`[data-member-id="${ADMIN}"] [data-member-role]`).isDisabled());
  await p.getByRole('button',{name:'第一页',exact:true}).click();await done();assert(await p.getByRole('button',{name:'第一页',exact:true}).isDisabled());
  await p.getByRole('button',{name:'下一页',exact:true}).click();await done();assert((await p.locator('.cms-member-pager').textContent()).includes('第 2 / 3 页'));
  await p.getByRole('button',{name:'上一页',exact:true}).click();await done();
  await change('size','50');assert.equal(await p.locator('[data-member-id]').count(),50);checks.push('first, previous, numbered, next, last pages; 25/50 rows');
  await change('sort','level');assert((await p.locator('[data-member-id] td:nth-child(2)').first().textContent()).startsWith('Lv.61'));
  await change('direction','asc');assert((await p.locator('[data-member-id] td:nth-child(2)').first().textContent()).startsWith('Lv.1'));
  await change('sort','username');assert((await p.locator('[data-member-id]').first().textContent()).includes('@user-00'));
  await change('sort','last_sign_in_at');assert((await p.locator('[data-member-id]').first().textContent()).includes('@user-00'));
  await change('role','admin');assert.equal(await p.locator('[data-member-id]').count(),1);
  await change('role','member');assert((await p.locator('.cms-member-status').textContent()).includes('60 位成员'));
  await change('q','user-01');assert.equal(await p.locator('[data-member-id]').count(),1);checks.push('numeric grade, username, registration/login order, combined search and role filter');
  await p.locator('[data-member-info]').last().click();await p.locator('.cms-member-profile[open]').waitFor();assert.match(await p.locator('.cms-member-profile').textContent(),/测试大学[\s\S]*湍流[\s\S]*研究应用/);await p.keyboard.press('Escape');
  const row=p.locator(`[data-member-id="${MEMBER}"]`);
  await row.locator('[data-member-role]').selectOption('admin');assert(await row.locator('[data-member-save]').isEnabled());await row.locator('[data-member-cancel]').click();assert.equal(await row.locator('[data-member-role]').inputValue(),'member');
  await row.locator('[data-member-role]').selectOption('admin');await row.locator('[data-member-save]').click();await p.locator('.cms-dialog[open]').waitFor();await p.locator('.cms-dialog button[value=cancel]').click();assert.equal(f.writes.filter(w=>w.table==='foamlab_admin_set_member_role').length,0);
  await row.locator('[data-member-save]').click();await p.locator('.cms-dialog button[value=confirm]').click();await p.waitForFunction(()=>document.querySelector('#cms-notice').textContent.includes('已保存为管理员'));
  assert.deepEqual(f.writes.at(-1).body,{p_user_id:MEMBER,p_role:'admin',p_expected_role:'member'});assert.equal(await p.locator('[data-member-id]').count(),0);checks.push('profile detail, row cancel, confirmation cancel, confirmed admin grant updates active member filter');
  await change('role','admin');await row.locator('[data-member-role]').selectOption('member');rpc.conflict(true);await row.locator('[data-member-save]').click();await p.locator('.cms-dialog button[value=confirm]').click();await p.waitForFunction(()=>document.querySelector('#cms-notice').textContent.includes('已被修改'));assert.equal(await row.locator('[data-member-role]').inputValue(),'member');rpc.conflict(false);
  await row.locator('[data-member-save]').click();await p.locator('.cms-dialog button[value=confirm]').click();await p.waitForFunction(()=>document.querySelector('#cms-notice').textContent.includes('已保存为普通会员'));assert.equal(await p.locator('[data-member-id]').count(),0);checks.push('optimistic permission conflict keeps pending selection; restore ordinary membership');
  await p.click('[data-members-reset]');await done();rpc.delay('user-01');await p.locator('[data-member-filter=q]').fill('user-01');await p.waitForRequest(r=>r.url().includes('foamlab_admin_members')&&r.postDataJSON()?.p_query==='user-01');await p.locator('[data-member-filter=q]').fill('user-02');await done();await p.waitForTimeout(900);assert((await p.locator('.cms-member-table').textContent()).includes('@user-02'));assert(!(await p.locator('.cms-member-table').textContent()).includes('@user-01'));rpc.delay('');checks.push('late network responses cannot overwrite current search');
  await change('q','user-03');await p.click('[data-cms-tab=content]');await p.locator('#cms-new').waitFor();await p.click('[data-cms-tab=roles]');await done();assert.equal(await p.locator('[data-member-filter=q]').inputValue(),'user-03');checks.push('filter and sorting survive tab changes');
  rpc.fail(true);await p.click('[data-members-refresh]');await p.waitForFunction(()=>document.querySelector('.cms-member-status').textContent.includes('暂时不可用'));assert.equal(await p.locator('[data-member-id]').count(),0);rpc.fail(false);await p.locator('.cms-empty [data-members-refresh]').click();await done();checks.push('network error and successful retry without a misleading empty list');
  rpc.registered[3].display_name='<img src=x onerror="window.memberXSS=true">';await p.click('[data-members-refresh]');await done();assert.equal(await p.locator('.cms-member-results img').count(),0);assert.equal(await p.evaluate(()=>window.memberXSS),undefined);rpc.registered[3].display_name='新注册成员 3';
  await p.click('[data-members-reset]');await done();await p.screenshot({path:path.join(OUT,'cms-members-desktop.png'),fullPage:true});
  await p.evaluate(()=>document.documentElement.setAttribute('data-theme','dark'));await p.screenshot({path:path.join(OUT,'cms-members-dark.png'),fullPage:true});
  await p.setViewportSize({width:390,height:844});await p.evaluate(()=>document.documentElement.setAttribute('data-theme','light'));await p.waitForTimeout(450);assert(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2));await p.screenshot({path:path.join(OUT,'cms-members-mobile.png'),fullPage:false,animations:'disabled'});await p.locator('[data-member-id]').first().scrollIntoViewIfNeeded();await p.screenshot({path:path.join(OUT,'cms-members-mobile-row.png'),animations:'disabled'});checks.push('escaped member text; desktop, dark and mobile layouts');await f.close();
  for(const role of ['anon','member','editor','moderator','blocked']){
   const x=await fixture(browser,role);await ready(x.page,'/admin/?tab=members','#cms-root');await x.page.waitForFunction(()=>!document.querySelector('#cms-root .lab-loading'));assert.equal(await x.page.locator('[data-cms-tab=roles]').count(),0);assert.equal(await x.page.locator('.cms-members').count(),0);await x.close();
  }checks.push('admin-only tab and route gate for guests, members, editors, moderators and blocked users');
  fs.writeFileSync(path.join(OUT,'cms-members-check.json'),JSON.stringify({passed:checks.length,checks,realUserWrites:0},null,2));console.log(JSON.stringify({passed:checks.length,checks,realUserWrites:0},null,2));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
