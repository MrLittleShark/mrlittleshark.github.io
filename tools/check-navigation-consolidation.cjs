'use strict';
const assert=require('node:assert/strict'),path=require('node:path'),fs=require('node:fs');
const {chromium}=require('C:/Users/shark/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const {fixture,ready,content,ORIGIN}=require('./check-cms-ui.cjs');
const out=path.resolve(__dirname,'../.openfoam-work/navigation');fs.mkdirSync(out,{recursive:true});
const checks=[];
const rows=[
 ['core','lesson','起步与算例'],['core-numerics','lesson','数值方法'],
 ['algorithm','lesson','数值方法与理论'],['linux','lesson','Linux 入门'],
 ['cpp','lesson','C++ 入门'],['programming','lesson','OpenFOAM 编程'],
 ['notes','resource','文档'],['case','resource','算例'],
 ['web','recommendation','文档'],['video','recommendation','视频'],
 ['article','article','技术文章'],['diary','log','作者日志']
].map(([slug,kind,track],i)=>content(`00000000-0000-4000-8000-${String(i+1).padStart(12,'0')}`,slug,{kind,track,title:slug,series:kind==='lesson'?'课程 '+track:''}));
const cardSlugs=p=>p.locator('.lab-card-main').evaluateAll(nodes=>nodes.map(a=>new URL(a.href).searchParams.get('slug')).sort());
async function catalog(p,url){await ready(p,url,'.lab-card');}
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 try{
  const f=await fixture(browser,'anon',{persistSession:true}),p=f.page;f.db.foamlab_content=structuredClone(rows);
  await catalog(p,'/programming/');
  assert.deepEqual(await cardSlugs(p),['programming']);
  assert.equal(await p.locator('.programming-foundations a[href="/linux/"]').count(),1);
  assert.equal(await p.locator('.programming-foundations a[href="/cpp/"]').count(),1);
  assert.equal(await p.locator('.course-entry-links').count(),0);
  assert.equal(await p.locator('#sidebar a[href="/authors/"],#sidebar a[href="/recommendations/"],#sidebar a[href="/account/"]').count(),0);
  assert.equal(await p.locator('#sidebar a[href="/sharing/"]').count(),1);
  assert.equal(await p.locator('[data-nav-section="algorithms"]').count(),0);
  assert.equal(await p.locator('[data-nav-section="topics"] a[href="/algorithms/"]').count(),1);
  await catalog(p,'/algorithms/');assert.deepEqual(await cardSlugs(p),['algorithm','core-numerics']);
  assert.equal(await p.locator('.course-entry-links,.lab-catalog-page a[href="/linux/"],.lab-catalog-page a[href="/cpp/"]').count(),0);
  assert.equal(await p.locator('#breadcrumb-parent').getAttribute('href'),'/topics/');
  assert(await p.locator('[data-nav-section="topics"] a[href="/algorithms/"]').evaluate(e=>e.classList.contains('active')));
  await p.screenshot({path:path.join(out,'algorithms-desktop.png'),animations:'disabled'});
  await catalog(p,'/courses/');assert.deepEqual(await cardSlugs(p),['core','core-numerics']);
  await ready(p,'/topics/','.topic-collection[data-topic="algorithms"]');
  assert.equal(await p.locator('.topic-collection[data-topic="algorithms"]').getAttribute('href'),'/algorithms/');
  checks.push('programming and system courses have separate catalogs; numerical methods nested in topics with correct parent');

  await catalog(p,'/resources/');assert.deepEqual(await cardSlugs(p),['case','notes','video','web']);
  await p.locator('[data-catalog-kind="recommendation"]').click();assert.deepEqual(await cardSlugs(p),['video','web']);
  await p.locator('[data-track="文档"]').click();assert.deepEqual(await cardSlugs(p),['web']);
  await p.locator('#catalog-query').fill('web');
  await p.reload();await p.waitForSelector('.lab-card');assert.deepEqual(await cardSlugs(p),['web']);
  assert.equal(await p.locator('#catalog-query').inputValue(),'web');
  assert(await p.locator('[data-nav-section="resources"] a[href="/resources/?kind=recommendation"]').evaluate(e=>e.classList.contains('active')));
  await p.locator('.lab-card-main').click();await p.waitForSelector('#lab-comments');
  const back=await p.locator('#page-back-link').getAttribute('href');assert(back.startsWith('/resources/'));assert(back.includes('kind=recommendation'));assert(back.includes('q=web'));
  assert.match(await p.locator('#breadcrumb-parent').textContent(),/资料中心/);
  await p.locator('#page-back-link').click();await p.waitForSelector('.lab-card');
  await p.locator('#catalog-query').fill('');await p.locator('[data-catalog-kind="resource"]').click();
  assert.deepEqual(await cardSlugs(p),['case','notes']);assert.equal(new URL(p.url()).searchParams.has('track'),false);
  await p.goBack();await p.waitForFunction(()=>document.querySelector('[data-catalog-kind="recommendation"]')?.getAttribute('aria-pressed')==='true');
  assert.deepEqual(await cardSlugs(p),['web']);
  checks.push('merged resource types, theme and search filters, reload, browser back and article return preserve state');

  await p.goto(ORIGIN+'/recommendations/?q=web&track='+encodeURIComponent('文档')+'#catalog-query');
  await p.waitForURL('**/resources/**');await p.waitForSelector('.lab-card');
  assert.equal(new URL(p.url()).searchParams.get('kind'),'recommendation');assert.equal(new URL(p.url()).hash,'#catalog-query');assert.deepEqual(await cardSlugs(p),['web']);
  await p.goto(ORIGIN+'/authors/?q=diary');await p.waitForURL('**/sharing/**');await p.waitForSelector('.lab-card');assert.deepEqual(await cardSlugs(p),['diary']);
  await p.locator('#catalog-query').fill('');assert.deepEqual(await cardSlugs(p),['article','diary']);
  await p.locator('.lab-card-main[href="/read/?slug=diary"]').click();await p.waitForSelector('#lab-comments');
  assert.equal(await p.locator('#breadcrumb-parent').textContent(),'实践与分享');
  assert(await p.locator('#sidebar a[href="/sharing/"]').evaluate(e=>e.classList.contains('active')));
  await ready(p,'/read/?slug=algorithm','#lab-comments');assert(await p.locator('[data-nav-section="topics"] a[href="/algorithms/"]').evaluate(e=>e.classList.contains('active')));
  await ready(p,'/read/?slug=core-numerics','#lab-comments');assert.equal(await p.locator('#breadcrumb-parent').getAttribute('href'),'/courses/');
  checks.push('old catalogs redirect with filters; articles, logs and numerical lessons highlight their own parent');

  await catalog(p,'/resources/?kind=recommendation');await p.setViewportSize({width:390,height:844});
  await p.locator('.mobile-menu').click();
  const toggle=p.locator('[data-nav-section="resources"] .nav-expand');
  await toggle.click();assert.equal(await toggle.getAttribute('aria-expanded'),'false');
  await toggle.click();assert.equal(await toggle.getAttribute('aria-expanded'),'true');
  await p.evaluate(()=>document.documentElement.dataset.theme='dark');
  assert(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
  await p.screenshot({path:path.join(out,'resources-mobile-dark.png'),animations:'disabled'});
  checks.push('mobile sidebar expands and collapses without horizontal overflow');await f.close();

  const m=await fixture(browser,'member',{persistSession:true});
  m.db.foamlab_profiles[0].shortcuts=['authors','sharing','recommendations','resources'];
  await ready(m.page,'/account/','#account-name');await m.page.evaluate(()=>window.foamAuth.profileReady);
  assert.deepEqual(await m.page.locator('#account-shortcuts a').evaluateAll(a=>a.map(x=>x.getAttribute('href'))),['/sharing/','/resources/']);
  assert.equal(await m.page.locator('[name=shortcuts]:checked').count(),2);
  await m.page.locator('#profile-form button[type=submit]').click();await m.page.getByText('个人资料已保存到账号。',{exact:true}).waitFor();
  assert.deepEqual(m.db.foamlab_profiles[0].shortcuts.sort(),['resources','sharing']);
  await m.page.locator('#account-nav-label').click();await m.page.locator('#account-panel').waitFor();
  assert.equal(await m.page.locator('#account-panel-name').textContent(),'测试读者');
  checks.push('legacy personal shortcuts merge without duplication; header account panel remains accessible');await m.close();
  const report={passed:checks.length,checks,externalWrites:0};fs.writeFileSync(path.join(out,'checks.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
