'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {chromium}=require('C:/Users/shark/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const {fixture,content,ready,ORIGIN}=require('./check-cms-ui.cjs');
const ROOT=path.resolve(__dirname,'..'),OUT=path.join(ROOT,'.openfoam-work/coded-fields');
const rows=JSON.parse(fs.readFileSync(path.join(ROOT,'tools/content/coded-fields-content.json'),'utf8'));
const section=JSON.parse(fs.readFileSync(path.join(ROOT,'tools/content/coded-fields/section.json'),'utf8'));
const parent={id:'70f057e1-459d-426d-8d4a-aad75391f95a',key:'programming',name:'OpenFOAM 编程',parent_id:null,href:'/programming/',nav_group:'学习空间',visible:true,sort_order:370};
function populate(f){f.db.foamlab_sections=[parent,{...section,parent_id:parent.id,visible:true}];f.db.foamlab_content=rows.map((r,i)=>content('a0000000-0000-4000-8000-'+String(i+1).padStart(12,'0'),r.slug,r));}
async function inspect(p){assert.equal(await p.locator('.math-error').count(),0);assert(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2),'page overflows');assert.equal(await p.locator('.page-outline').count(),1);}
(async()=>{const browser=await chromium.launch({channel:'msedge',headless:true}),checks=[];try{
 const f=await fixture(browser,'anon'),p=f.page;populate(f);
 await ready(p,section.href,'.lab-card');assert.equal(await p.locator('.lab-card').count(),6);assert.equal(await p.locator('.lab-card-download').count(),6);await inspect(p);await p.screenshot({path:path.join(OUT,'module-desktop.png'),fullPage:true});checks.push('New submodule lists all six lessons and their downloads');
 for(const [i,row] of rows.entries()){
  await ready(p,'/read/?slug='+row.slug,'#live-article>.prose');await p.locator('.lesson-navigation .chapter-controls').waitFor();await p.waitForFunction(()=>document.querySelectorAll('.page-outline nav a').length>5);await inspect(p);
  assert.equal(await p.locator('#chapter-list a').count(),6);
  assert.equal(await p.locator('.lesson-navigation .chapter-heading a').getAttribute('href'),section.href);
  assert.equal(await p.locator('#page-back-link').getAttribute('href'),section.href);
  assert.equal(await p.locator('.lesson-navigation [data-chapter=first]').isDisabled(),i===0);
  assert.equal(await p.locator('.lesson-navigation [data-chapter=last]').isDisabled(),i===5);
  assert(await p.locator('#live-article .code-panel').count()>=5);
  assert.equal(await p.locator('#live-article .prose').evaluate(e=>/\{\{(?:file|snippet|boundary):/.test(e.textContent)),false);
  const imgs=p.locator('#live-article .prose img');await imgs.evaluateAll(async es=>{for(const e of es){e.loading='eager';await e.decode();}});assert.equal(await imgs.count(),1);
  const downloads=await p.locator('#live-article a[href$=".zip"]').evaluateAll(es=>[...new Set(es.map(e=>e.href))]);for(const url of downloads){const r=await f.context.request.get(url);assert(r.ok());const b=await r.body();assert.equal(b.subarray(0,2).toString(),'PK');}
 }
 checks.push('Six readers: math, highlighted code, figures, chapter controls, module return and valid ZIP files');
 await ready(p,'/read/?slug=coded-fields-06','#live-article>.prose');await p.locator('#live-article .prose img').scrollIntoViewIfNeeded();await p.screenshot({path:path.join(OUT,'lesson-desktop.png')});await p.evaluate(()=>document.documentElement.dataset.theme='dark');await p.screenshot({path:path.join(OUT,'lesson-dark.png')});assert.deepEqual(f.errors,[]);await f.close();
 const m=await fixture(browser,'anon',{mobile:true});populate(m);await ready(m.page,'/read/?slug=coded-fields-01','#live-article>.prose');await inspect(m.page);await m.page.locator('.code-panel').first().scrollIntoViewIfNeeded();await m.page.screenshot({path:path.join(OUT,'lesson-mobile.png')});await m.close();checks.push('Desktop, dark mode and mobile layouts');
 const a=await fixture(browser,'admin');populate(a);await ready(a.page,'/admin/','.cms-directory-tree');await a.page.locator('[data-tree-toggle="'+parent.id+'"]').click();await a.page.locator('[data-select-directory="'+section.id+'"]').click();assert.equal(await a.page.locator('#cms-table .cms-table-row').count(),6);assert.match(await a.page.locator('#cms-table .cms-location').first().textContent(),/OpenFOAM 编程.*用代码设置初始与边界条件/);await a.page.screenshot({path:path.join(OUT,'module-admin.png'),fullPage:true});await a.close();checks.push('Admin directory shows all lessons at the correct module/submodule location');
 fs.writeFileSync(path.join(OUT,'ui-check.json'),JSON.stringify({checks,passed:checks.length},null,2));console.log(JSON.stringify({checks,passed:checks.length},null,2));
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exitCode=1;});
