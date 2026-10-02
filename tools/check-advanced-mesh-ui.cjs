/* Isolated checks for nested mesh topics, reading, downloads and CMS locations. */
'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {chromium}=require('C:/Users/shark/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const {fixture,content,ready}=require('./check-cms-ui.cjs');
const ROOT=path.resolve(__dirname,'..'),OUT=path.join(ROOT,'.openfoam-work/advanced-mesh');
const rows=JSON.parse(fs.readFileSync(path.join(ROOT,'tools/content/advanced-mesh-content.json'),'utf8'));
const nodes=JSON.parse(fs.readFileSync(path.join(ROOT,'tools/content/advanced-mesh/sections.json'),'utf8'));
const parent=nodes.find(n=>n.key==='topic-meshes');
const existing=[{id:'1f14bf4e-a678-459c-9bea-413184204c5b',key:'topics',name:'专题学习',parent_id:null,href:'/topics/',visible:true,nav_group:'学习空间',sort_order:120},{id:'4342316d-cb35-4abd-a0be-3af53c95254d',key:'topic-meshing',name:'网格划分',parent_id:parent.id,href:'/topics/meshing/',visible:true,nav_group:'学习空间',sort_order:170},{id:'098acc0d-1381-4ebe-91cd-59ce79a3ab74',key:'topic-dynamic-mesh',name:'动网格',parent_id:parent.id,href:'/topics/dynamic-mesh/',visible:true,nav_group:'学习空间',sort_order:180}];
function populate(f){
 f.db.foamlab_sections=[...existing,...nodes];
 const old=JSON.parse(fs.readFileSync(path.join(ROOT,'tools/content/topics-content.json'),'utf8')).filter(r=>['topic-meshing','topic-dynamic-mesh'].includes(r.slug)).map(r=>({...r,section_ids:[existing.find(n=>n.key===r.slug).id]}));
 f.db.foamlab_content=[...rows,...old].map((r,i)=>content('b0000000-0000-4000-8000-'+String(i+1).padStart(12,'0'),r.slug,r));
}
async function inspect(p){assert.equal(await p.locator('.math-error').count(),0);assert(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2),'page overflow');}
(async()=>{const browser=await chromium.launch({channel:'msedge',headless:true}),checks=[];try{
 const f=await fixture(browser,'anon'),p=f.page;populate(f);
 await ready(p,'/topics/','.topic-collection');assert.equal(await p.locator('#topic-hub .topic-collection').count(),1);assert.equal(await p.locator('#topic-hub .topic-collection h2').innerText(),'各类网格');checks.push('Topic root shows the mesh collection once');
 await ready(p,'/topics/meshes/','#topic-branches');assert.equal(await p.locator('#topic-branches .topic-collection').count(),6);assert.equal(await p.locator('#topic-courses .lab-card').count(),6);assert.match(await p.locator('.topic-introduction').innerText(),/根据计算问题选择网格方法/);await inspect(p);await p.screenshot({path:path.join(OUT,'mesh-hub-desktop.png'),fullPage:true});
 await ready(p,'/topics/dynamic-mesh/','#topic-courses .lab-card');assert.match(await p.locator('.topic-breadcrumbs').innerText(),/专题学习.*各类网格.*动网格/s);assert.equal(await p.locator('.topic-breadcrumbs a').last().getAttribute('href'),'/topics/meshes/');assert.match(await p.locator('.topic-introduction').innerText(),/让边界运动带动周围网格/);checks.push('Nested topics, preserved dynamic-mesh URL, own introduction and parent breadcrumbs');
 for(const row of rows.filter(r=>r.kind==='lesson')){
  await ready(p,'/read/?slug='+row.slug,'#live-article>.prose');await p.locator('.lesson-navigation .chapter-controls').waitFor();await p.waitForFunction(()=>document.querySelectorAll('.page-outline nav a').length>=6);await inspect(p);
  assert.equal(await p.locator('#chapter-list a').count(),6);assert(await p.locator('#live-article .code-panel').count()>=5);
  const section=[...nodes,...existing].find(n=>n.id===row.section_ids[0]);assert.equal(await p.locator('#page-back-link').getAttribute('href'),section.href);
  assert.equal(await p.locator('#live-article .prose').evaluate(e=>/\{\{(?:file|block|entry):/.test(e.textContent)),false);
  const imgs=p.locator('#live-article .prose img');await imgs.evaluateAll(async es=>{for(const e of es){e.loading='eager';await e.decode();}});assert(await imgs.count()>=1);
  for(const url of await p.locator('#live-article a[href$=".zip"]').evaluateAll(es=>[...new Set(es.map(e=>e.href))])){const r=await f.context.request.get(url);assert(r.ok());assert.equal((await r.body()).subarray(0,2).toString(),'PK');}
 }
 checks.push('Six lessons render TeX, highlighted code, figures, downloads, chapter navigation and category returns');
 await ready(p,'/read/?slug=advanced-mesh-03','#live-article>.prose');await p.locator('#live-article .prose img').first().scrollIntoViewIfNeeded();await p.screenshot({path:path.join(OUT,'mesh-lesson-desktop.png')});await p.evaluate(()=>document.documentElement.dataset.theme='dark');await p.screenshot({path:path.join(OUT,'mesh-lesson-dark.png')});await f.close();
 const m=await fixture(browser,'anon',{mobile:true});populate(m);await ready(m.page,'/topics/meshes/','#topic-branches');await inspect(m.page);await m.page.screenshot({path:path.join(OUT,'mesh-hub-mobile.png'),fullPage:true});await ready(m.page,'/read/?slug=advanced-mesh-06','#live-article>.prose');await inspect(m.page);await m.close();checks.push('Desktop, dark theme and narrow mobile layouts');
 const a=await fixture(browser,'admin');populate(a);await ready(a.page,'/admin/','.cms-directory-tree');await a.page.locator('[data-tree-toggle="'+existing[0].id+'"]').click();await a.page.locator('[data-tree-toggle="'+parent.id+'"]').click();const child=nodes.find(n=>n.key==='topic-rotating-frames');await a.page.locator('[data-select-directory="'+child.id+'"]').click();assert.equal(await a.page.locator('#cms-table .cms-table-row').count(),3);assert.match(await a.page.locator('#cms-table .cms-location').first().innerText(),/专题学习.*各类网格.*旋转参考系/);await a.page.screenshot({path:path.join(OUT,'mesh-admin.png'),fullPage:true});await a.close();checks.push('Admin filters articles by full module/submodule location');
 fs.writeFileSync(path.join(OUT,'ui-check.json'),JSON.stringify({passed:checks.length,checks},null,2));console.log(JSON.stringify({passed:checks.length,checks},null,2));
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exitCode=1;});
