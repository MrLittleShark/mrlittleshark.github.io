/* Test the published UI shape against the complete local content corpus. */
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {chromium}=require('C:/Users/shark/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const {fixture,ready,content}=require('./check-cms-ui.cjs');
const ROOT=path.resolve(__dirname,'..'),OUT=path.join(ROOT,'.openfoam-work/editorial');
const rows=fs.readdirSync(path.join(ROOT,'tools/content')).filter(x=>x.endsWith('content.json')).flatMap(x=>JSON.parse(fs.readFileSync(path.join(ROOT,'tools/content',x),'utf8')));
const checks=[];
function populate(f){f.db.foamlab_content=rows.map((r,i)=>content('dddddddd-dddd-4ddd-8ddd-'+String(i).padStart(12,'0'),r.slug,r));f.db.foamlab_settings.push({key:'support',value:{enabled:true,wechat_url:'/assets/support/wechat.jpg',alipay_url:'/assets/support/alipay.jpg'}});}
async function inspect(p){assert.equal(await p.locator('.math-error').count(),0);assert.equal(await p.locator('.page-outline').count(),await p.locator('.fl-home').count()?0:1);const size=await p.evaluate(()=>({w:innerWidth,scroll:document.documentElement.scrollWidth}));assert(size.scroll<=size.w+2,'page horizontal overflow '+JSON.stringify(size));}
(async()=>{const browser=await chromium.launch({channel:'msedge',headless:true});try{
 const f=await fixture(browser);populate(f);const p=f.page;
 await ready(p,'/','.science-hero');await inspect(p);assert.equal(await p.locator('.fl-hero .fl-flow').count(),1);assert.equal(await p.locator('.footer a[href="/maintenance/"]').count(),0);assert.equal(await p.locator('.footer a[href="/design/"]').count(),0);await p.screenshot({path:path.join(OUT,'preview-home.png')});checks.push('home flow illustration and public footer');
 for(const [url,n] of [['/cpp/',10],['/linux/',8],['/programming/',20]]){await ready(p,url,'.lab-card');assert.equal(await p.locator('.lab-card').count(),n);await inspect(p);}checks.push('Linux C++ and programming catalogs');
 for(const slug of ['cfd-and-openfoam','development-solver','development-boundary','development-utility','programming-10','start-openfoam-v2512','simple-piso-pimple','programming-12','programming-14','cpp-10','linux-03','algorithm-theory-01','openfoam-org-com-comparison']){
  const row=rows.find(r=>r.slug===slug);if(!row)continue;
  await ready(p,'/read/?slug='+slug,'#live-article .prose');await p.waitForFunction(()=>document.querySelectorAll('.page-outline nav a').length>2);await inspect(p);assert((await p.locator('#live-article .code-panel').count())>0,slug+' code panels');if(row.kind==='lesson'){await p.waitForSelector('.lesson-navigation');assert.equal(await p.locator('#chapter-list [aria-current="page"]').count(),1);assert.equal(await p.locator('.chapter-controls > *').count(),4);}
  assert((await p.locator('#page-back-link').textContent()).includes('返回'));
 }
 checks.push('article code TeX chapter navigation and directory return');
 await ready(p,'/dictionaries/system-decomposepardict/','.prose');await p.waitForTimeout(400);
 const widths=await p.locator('.prose table').evaluateAll(tables=>tables.filter(t=>t.getClientRects().length).map(t=>({table:t.getBoundingClientRect().width,row:t.rows[0]?.getBoundingClientRect().width,wrapper:t.parentElement.getBoundingClientRect().width})));
 assert(widths.length>0);widths.forEach(w=>{assert(Math.abs(w.table-w.row)<2);assert(w.table>=w.wrapper-3);});await p.screenshot({path:path.join(OUT,'preview-dictionary.png')});checks.push('full width table rows and header');
 await p.locator('.page-outline summary').click();const jump=p.locator('.page-outline nav a').nth(2);const hash=await jump.getAttribute('href');await jump.click();await p.waitForTimeout(100);assert.equal(new URL(p.url()).hash,hash);assert.equal(await p.locator('.page-outline').getAttribute('open'),null);checks.push('upper right outline jump');
 await p.locator('[data-support-open]').scrollIntoViewIfNeeded();await p.locator('[data-support-open]').hover();await p.waitForSelector('#support-popover:not([hidden]) .support-mini-code img');await p.locator('#support-popover img').evaluateAll(imgs=>Promise.all(imgs.map(i=>i.decode())));assert.equal(await p.locator('#support-popover img').count(),2);await p.screenshot({path:path.join(OUT,'preview-support.png')});await p.mouse.move(10,10);assert(await p.locator('#support-popover').isHidden());checks.push('two small QR codes show on hover and hide on exit');
 await p.goto('http://localhost:4173/');await p.evaluate(()=>document.documentElement.dataset.theme='dark');await p.screenshot({path:path.join(OUT,'preview-home-dark.png')});
 assert.deepEqual(f.errors,[]);await f.close();
 const m=await fixture(browser,'anon',{mobile:true});populate(m);await ready(m.page,'/read/?slug=programming-14','#live-article .prose');await inspect(m.page);await m.page.screenshot({path:path.join(OUT,'preview-mobile.png')});assert.deepEqual(m.errors,[]);await m.close();checks.push('mobile reader and dark appearance');
 fs.writeFileSync(path.join(OUT,'browser-check.json'),JSON.stringify({checks,passed:checks.length,externalWrites:0},null,2));console.log(JSON.stringify({checks,passed:checks.length}));
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exitCode=1;});
