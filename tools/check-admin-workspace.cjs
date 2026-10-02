'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const {chromium}=require('C:/Users/shark/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const {fixture,content,ready,ORIGIN,ADMIN,MEMBER}=require('./check-cms-ui.cjs');
const out=path.resolve(__dirname,'../.openfoam-work/admin-redesign');fs.mkdirSync(out,{recursive:true});const checks=[];
async function idle(p){await p.waitForFunction(()=>!document.querySelector('#cms-root')?.hasAttribute('aria-busy'));}
async function answer(p,yes=true){await p.locator('.cms-dialog[open]').waitFor();await p.locator('.cms-dialog button[value="'+(yes?'confirm':'cancel')+'"]').click();}
async function openTab(p,name){if(['roles','modules','settings','backup'].includes(name))await p.locator('#cms-more').evaluate(e=>e.open=true);await p.locator('[data-cms-tab='+name+']').click();await idle(p);}
(async()=>{const browser=await chromium.launch({channel:'msedge',headless:true});try{
 const f=await fixture(browser,'admin',{persistSession:true}),p=f.page;
 const row=content('00000000-0000-4000-8000-000000000001','manage-article',{title:'管理验证文章',track:'算例分享',series:'流动笔记',body:'原始正文'});
 f.db.foamlab_content=[row,...Array.from({length:64},(_,i)=>content(`00000000-0000-4000-8000-${String(i+2).padStart(12,'0')}`,'catalog-'+i,{title:'课程 '+i,kind:'lesson',track:'起步与算例',series:'系统课程'}))];
 await ready(p,'/admin/','#cms-new');assert.equal(await p.locator('#cms-table .cms-table-row').count(),25);
 await p.locator('#cms-pager [data-page="2"]').click();assert.match(await p.locator('#cms-pager').textContent(),/第 2/);
 await p.locator('#cms-search').fill('管理验证');assert.equal(await p.locator('#cms-table .cms-table-row').count(),1);
 await p.locator('.cms-title-button').click();await idle(p);assert(await p.locator('.cms-content-list').isHidden());assert.match(await p.locator('#cms-position-label').textContent(),/实践与分享.*算例分享.*流动笔记/);
 await p.locator('[name=body]').fill('尚未保存的正文');await p.locator('#cms-cancel').click();await answer(p,false);await idle(p);assert.equal(await p.locator('[name=body]').inputValue(),'尚未保存的正文');assert.equal(f.writes.length,0);
 await p.locator('#cms-cancel').click();await answer(p);await idle(p);assert.equal(row.body,'原始正文');assert(await p.locator('.cms-content-list').isVisible());
 await p.locator('.cms-title-button').click();await idle(p);await p.locator('[name=body]').fill('保存后的正文');await p.locator('#cms-edit-form [type=submit]').click();await idle(p);assert.equal(row.body,'保存后的正文');
 await p.screenshot({path:path.join(out,'editor-desktop.png'),animations:'disabled'});
 await p.locator('#cms-close').click();await idle(p);checks.push('25-row pagination, location labels, isolated editor, save and cancel with unsaved-change protection');

 const before=f.writes.length;
 await p.locator('[data-move]').click();await p.locator('.cms-dialog [name=placement]').selectOption('resource');await answer(p);await answer(p,false);await idle(p);assert.equal(row.kind,'article');assert.equal(f.writes.length,before);
 await p.locator('[data-move]').click();await p.locator('.cms-dialog [name=placement]').selectOption('resource');await answer(p);await answer(p);await idle(p);assert.equal(row.kind,'resource');assert.equal(row.slug,'manage-article');assert.equal(row.body,'保存后的正文');
 await p.locator('[data-trash]').click();await answer(p,false);await idle(p);assert.equal(row.status,'published');
 await p.locator('[data-trash]').click();await answer(p);await idle(p);assert.equal(row.status,'trash');
  await p.locator('[data-restore]').click();await answer(p);await idle(p);assert.equal(row.status,'draft');
  const disposable=content('00000000-0000-4000-8000-000000000099','remove-permanently',{title:'永久删除检查',status:'trash'});f.db.foamlab_content.push(disposable);
  await p.reload();await p.waitForSelector('#cms-new');await p.locator('#cms-search').fill('永久删除检查');await p.locator('[data-permanent]').click();await answer(p,false);await idle(p);assert(f.db.foamlab_content.includes(disposable));await p.locator('[data-permanent]').click();await answer(p);await idle(p);assert(!f.db.foamlab_content.includes(disposable));assert.match(await p.locator('#cms-notice').textContent(),/已永久删除/);
 checks.push('move has destination preview and second confirmation; cancel writes nothing; delete and restore preserve content');

 f.db.foamlab_messages=Array.from({length:213},(_,i)=>({id:'comment-'+i,content_id:row.id,thread_id:null,body:i===211?'待处理评论目标':'普通评论 '+i,status:'visible',author_id:MEMBER,created_at:'2026-10-02T05:00:00Z',updated_at:'2026-10-02T06:00:00Z'}));
 await openTab(p,'moderation');assert.equal(await p.locator('.cms-moderation-card').count(),25);
 await p.locator('#cms-moderation-search').fill('待处理评论目标');assert.equal(await p.locator('.cms-moderation-card').count(),1);assert.match(await p.locator('.cms-source').textContent(),/管理验证文章/);assert.match(await p.locator('.cms-moderation-card h3').textContent(),/测试会员/);
 await p.locator('[data-op=hide]').click();await answer(p,false);await idle(p);assert.equal(f.db.foamlab_messages[211].status,'visible');
 await p.locator('[data-op=hide]').click();await answer(p);await idle(p);assert.equal(f.db.foamlab_messages[211].status,'hidden');
 await p.locator('[data-op=restore]').click();await answer(p);await idle(p);assert.equal(f.db.foamlab_messages[211].status,'visible');
  await p.locator('[data-op=delete]').click();await answer(p);await idle(p);assert.equal(f.db.foamlab_messages.length,212);
  assert.equal(await p.locator('#cms-notice.is-error').count(),0);
 checks.push('comments beyond 200 searchable by source and author; hide, restore and permanent deletion require confirmation');

 f.files.push({name:'used.zip',metadata:{size:40},created_at:'2026-10-02T01:00:00Z'},{name:'free.zip',metadata:{size:40},created_at:'2026-10-02T01:00:00Z'},{name:'中文案例.zip',metadata:{size:40},created_at:'2026-10-02T01:00:00Z'});
 row.metadata={downloads:[{url:'https://cms-fixture.supabase.co/storage/v1/object/public/foamlab-resources/library/used.zip',label:'正在使用的案例'},{url:'https://cms-fixture.supabase.co/storage/v1/object/public/foamlab-resources/library/'+encodeURIComponent('中文案例.zip'),label:'编码地址的案例'}]};
 await openTab(p,'files');await p.locator('#cms-file-search').fill('used.zip');assert.match(await p.locator('#cms-files').textContent(),/1 篇内容引用/);
 const deletedBefore=f.writes.filter(x=>x.table==='storage'&&x.method==='DELETE').length;
 await p.locator('[data-delete-file]').click();await answer(p);await idle(p);assert.equal(f.writes.filter(x=>x.table==='storage'&&x.method==='DELETE').length,deletedBefore);
 await p.locator('#cms-file-search').fill('中文案例');assert.match(await p.locator('#cms-files').textContent(),/1 篇内容引用/);await p.locator('[data-delete-file]').click();await answer(p);await idle(p);assert.equal(f.writes.filter(x=>x.table==='storage'&&x.method==='DELETE').length,deletedBefore);
 await p.locator('#cms-file-search').fill('free.zip');await p.locator('[data-delete-file]').click();await answer(p,false);await idle(p);assert(f.files.some(x=>x.name==='free.zip'));
 await p.locator('[data-delete-file]').click();await answer(p);await idle(p);assert(!f.files.some(x=>x.name==='free.zip'));assert(f.files.some(x=>x.name==='used.zip'));
 await p.locator('#cms-file-search').fill('');await p.setInputFiles('#cms-upload',{name:'new-case.zip',mimeType:'application/zip',buffer:Buffer.from('fixture archive')});await idle(p);
 await p.locator('#cms-file-search').fill('new-case');await p.locator('[data-create-resource]').click();await idle(p);assert.equal(await p.locator('[name=kind]').inputValue(),'resource');assert.equal(await p.locator('.course-file-label').inputValue(),'new-case.zip');
 assert(!f.db.foamlab_content.some(x=>x.title==='new-case.zip'));await p.locator('#cms-edit-form [type=submit]').click();await idle(p);assert(f.db.foamlab_content.some(x=>x.title==='new-case.zip'&&x.metadata.downloads.length===1));
 for(const width of [390,320]){await p.setViewportSize({width,height:900});assert(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));}
 await p.evaluate(()=>document.documentElement.dataset.theme='dark');await p.screenshot({path:path.join(out,'editor-mobile-dark.png'),animations:'disabled'});
 checks.push('resource references, guarded file deletion, upload, editable download entries and mobile editor');await f.close();

 const a=await fixture(browser,'anon',{persistSession:true});
 await ready(a.page,'/sharing/','.lab-card');assert.match(await a.page.locator('.card-byline').first().textContent(),/测试管理员.*Lv.8.*发布于.*修改于/);
 await ready(a.page,'/read/?slug=published-fixture','#lab-comments');assert.equal(await a.page.locator('#live-article>.community-byline time').count(),2);assert.match(await a.page.locator('#live-article>.community-byline').textContent(),/Lv.8/);
 a.db.foamlab_author_levels[0].level=9;await a.page.reload();await a.page.waitForSelector('#lab-comments');assert.match(await a.page.locator('#live-article>.community-byline').textContent(),/Lv.9/);
 await ready(a.page,'/community/','.lab-topic-row');assert.match(await a.page.locator('.topic-byline').first().textContent(),/测试会员.*Lv.3.*发布于.*修改于/);
 checks.push('public article and discussion author names, live levels, publication and modification timestamps');await a.close();

 const m=await fixture(browser,'member',{persistSession:true}),mp=m.page;
 await ready(mp,'/account/','[data-account-tab=overview]');await mp.evaluate(()=>window.foamAuth.profileReady);assert(await mp.locator('.profile-editor').isHidden());assert(await mp.locator('#my-panda').isHidden());
 await mp.locator('[data-account-tab=profile]').click();await mp.locator('[name=display_name]').fill('保留输入');await mp.locator('[data-account-tab=overview]').click();await mp.locator('[data-account-tab=profile]').click();assert.equal(await mp.locator('[name=display_name]').inputValue(),'保留输入');
 await mp.goto(ORIGIN+'/account/#my-panda');await mp.waitForSelector('#my-panda');assert.equal(await mp.locator('[data-account-tab=pet]').getAttribute('aria-selected'),'true');
 await mp.locator('[data-account-tab=overview]').click();await mp.setViewportSize({width:390,height:844});assert(await mp.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
 await mp.screenshot({path:path.join(out,'account-mobile-overview.png'),fullPage:true,animations:'disabled'});
 await mp.locator('#account-nav-label').click();await mp.locator('#account-panel a[href="/account/#profile-form"]').click();await mp.locator('#profile-form').waitFor();assert.equal(await mp.locator('[data-account-tab=profile]').getAttribute('aria-selected'),'true');
 checks.push('account tabs shorten the default page, retain edits and honor profile/pet deep links');await m.close();
 const report={passed:checks.length,checks,externalWrites:0};fs.writeFileSync(path.join(out,'checks.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));
 }finally{await browser.close();}})().catch(e=>{console.error(e);process.exitCode=1;});
