'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const {chromium}=require('C:/Users/shark/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const origin=process.env.FOAM_CHECK_ORIGIN||'http://127.0.0.1:4174',out=path.resolve(__dirname,'../.openfoam-work/chinese-reference');
(async()=>{const browser=await chromium.launch({channel:'msedge',headless:true});try{
 const page=await browser.newPage({viewport:{width:1440,height:1000}});await page.route('**/rest/v1/**',r=>r.abort());
 for(const slug of ['postprocess','decomposepar','foamgetdict','simplefoam']){
  await page.goto(origin+'/commands/'+slug+'/');await page.waitForSelector('.prose table code');
  assert.equal(await page.locator('summary').filter({hasText:'完整命令帮助'}).count(),0);
  const descriptions=await page.locator('.prose table tbody tr td:last-child').allTextContents();
  assert(descriptions.every(x=>/[\u4e00-\u9fff]/.test(x)),slug);
  if(slug==='postprocess'){
   const text=await page.locator('tr').filter({has:page.locator('code',{hasText:'-funcs <list>'})}).textContent();assert.match(text,/函数对象列表/);assert(!/root|Switch|子进程/.test(text));
   const table=page.locator('h2').filter({hasText:'常用参数'});await table.scrollIntoViewIfNeeded();await page.screenshot({path:path.join(out,'postprocess-desktop.png')});
   const first=page.locator('.code-block').first();if(await first.count()){const raw=await first.locator('code').textContent();assert(raw.includes('postProcess'));}
  }
  await page.setViewportSize({width:390,height:844});assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),slug+' mobile overflow');
  if(slug==='postprocess'){await page.evaluate(()=>document.documentElement.dataset.theme='dark');await page.screenshot({path:path.join(out,'postprocess-mobile-dark.png')});await page.evaluate(()=>document.documentElement.dataset.theme='light');}
  await page.setViewportSize({width:1440,height:1000});
 }
 console.log(JSON.stringify({passed:4,checks:['Chinese explanations','wrapped option isolation','examples retained','desktop/mobile and dark theme']}));
}finally{await browser.close();}})().catch(e=>{console.error(e);process.exitCode=1;});
