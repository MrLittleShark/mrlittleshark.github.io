const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {chromium}=require('C:/Users/shark/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root=path.resolve(__dirname,'../..'),out=path.join(root,'.openfoam-work/function-objects');
const node={...JSON.parse(fs.readFileSync(path.join(__dirname,'function-objects/section.json'))),visible:true};
const rows=JSON.parse(fs.readFileSync(path.join(__dirname,'function-objects-content.json'))).map((r,i)=>({...r,id:`f0f00000-0000-4000-8000-${String(i+1).padStart(12,'0')}`,author_id:null,created_at:'2026-10-03T12:00:00Z',updated_at:'2026-10-03T12:00:00Z',published_at:'2026-10-03T12:00:00Z'}));
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 const context=await browser.newContext({viewport:{width:1440,height:1000}});let failures=[];
 await context.route('**/rest/v1/foamlab_sections?*',async route=>{
  const response=await route.fetch(),original=await response.json();assert(Array.isArray(original));
  await route.fulfill({response,json:[...original.filter(n=>n.id!==node.id),node]});
 });
 await context.route('**/rest/v1/foamlab_content?*',async route=>{
  const u=new URL(route.request().url()),q=u.searchParams,slug=q.get('slug')?.replace(/^eq\./,''),id=q.get('id')?.replace(/^eq\./,'');
  let data;
  if(slug?.startsWith('function-objects-'))data=rows.find(r=>r.slug===slug);
  else if(id&&rows.some(r=>r.id===id))data=rows.find(r=>r.id===id);
  else if(q.get('series')==='eq.functionObject 后处理')data=rows.filter(r=>r.kind==='lesson');
  else if(q.get('section_ids')?.includes(node.id))data=rows;
  if(data){if(route.request().headers().accept?.includes('application/vnd.pgrst.object+json'))data=Array.isArray(data)?data[0]:data;else if(!Array.isArray(data))data=[data];return route.fulfill({json:data});}
  return route.continue();
 });
 const page=await context.newPage();page.on('pageerror',e=>failures.push(e.message));
 await page.goto('http://localhost:4176/topics/function-objects/');await page.locator('#topic-courses .lab-card').first().waitFor();
 assert.equal(await page.locator('#topic-courses .lab-card').count(),12);
 await page.screenshot({path:path.join(out,'topic-desktop.png'),fullPage:false});
 const pagination=page.locator('.pagination');
 const names=await page.locator('button,a').allTextContents();assert(names.some(x=>x.includes('最后一页'))||names.some(x=>x.trim()==='末页'));
 const last=page.getByRole('button',{name:'最后一页',exact:true});
 if(await last.count()){await last.click();assert.equal(await page.locator('#topic-courses .lab-card').count(),5);}
 const results=[];
 for(const row of rows.filter(r=>r.kind==='lesson')){
  await page.goto('http://localhost:4176/read/?slug='+row.slug);
  await page.locator('#live-article .prose h2').first().waitFor();
  await page.locator('.lesson-navigation [data-chapter=last]').waitFor();
  await page.locator('#live-article img').evaluateAll(imgs=>imgs.forEach(i=>i.loading='eager'));
  await page.waitForFunction(()=>[...document.querySelectorAll('#live-article img')].every(i=>i.complete));
  const result=await page.evaluate(()=>({heading:document.querySelector('#live-article h1')?.textContent,mathErrors:document.querySelectorAll('.katex-error').length,nested:document.querySelectorAll('.code-panel .code-panel').length,brokenImages:[...document.querySelectorAll('#live-article img')].filter(i=>!i.naturalWidth).map(i=>i.src),overflow:document.documentElement.scrollWidth>innerWidth+2,back:document.querySelector('#page-back-link')?.getAttribute('href'),chapters:document.querySelectorAll('#chapter-list a').length,toc:document.querySelectorAll('#toc-list a,.article-toc a').length}));
  assert.equal(result.mathErrors,0,row.slug);assert.equal(result.nested,0,row.slug);assert.equal(result.brokenImages.length,0,row.slug);assert(!result.overflow,row.slug);assert.equal(result.chapters,17,row.slug);assert.equal(result.back,'/topics/function-objects/',row.slug);assert(result.toc>5,row.slug);results.push({slug:row.slug,...result});
  if(row.slug==='function-objects-11')await page.screenshot({path:path.join(out,'lesson-desktop.png'),fullPage:false});
 }
 await page.emulateMedia({colorScheme:'dark'});await page.evaluate(()=>{localStorage.setItem('theme','dark');document.documentElement.dataset.theme='dark';});
 await page.screenshot({path:path.join(out,'lesson-dark.png'),fullPage:false});
 await page.setViewportSize({width:390,height:844});await page.goto('http://localhost:4176/read/?slug=function-objects-11');await page.locator('#live-article .prose h2').first().waitFor();await page.locator('.lesson-navigation [data-chapter=last]').waitFor();
 assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+2));await page.screenshot({path:path.join(out,'lesson-mobile.png'),fullPage:false});
 assert.equal(failures.length,0,failures.join('\n'));fs.writeFileSync(path.join(out,'browser-check.json'),JSON.stringify({pages:results,errors:failures},null,2));
 console.log(JSON.stringify({pages:results.length,desktop:'passed',mobile:'passed',pageErrors:failures},null,2));await context.unrouteAll({behavior:'ignoreErrors'});await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
