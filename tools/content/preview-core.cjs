const {chromium}=require('C:/Users/shark/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('node:fs'),path=require('node:path');
(async()=>{
 const root=path.resolve(__dirname,'../..');
 const out=path.join(root,'.openfoam-work/replan');
 const browser=await chromium.launch({channel:'msedge',headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:1100},deviceScaleFactor:1});
 await page.goto('file:///'+path.join(out,'core-preview.html').replaceAll('\\','/'));
 await page.locator('#finite-volume-conservation').scrollIntoViewIfNeeded();
 await page.screenshot({path:path.join(out,'core-course-preview.png')});
 const imgs=fs.readdirSync(path.join(root,'source-openfoam/assets/diagrams')).filter(n=>n.startsWith('core-')&&n.endsWith('.svg'));
 let doc='<!doctype html><meta charset="utf-8"><style>body{margin:16px;display:grid;grid-template-columns:1fr 1fr;gap:12px;background:#dae6ef}img{width:100%;display:block}</style>';
 for(const img of imgs)doc+=`<img src="file:///${path.join(root,'source-openfoam/assets/diagrams',img).replaceAll('\\','/')}">`;
 fs.writeFileSync(path.join(out,'core-figures.html'),doc);
 await page.goto('file:///'+path.join(out,'core-figures.html').replaceAll('\\','/'));
 await page.screenshot({path:path.join(out,'core-figures-contact.png'),fullPage:true});
 console.log(JSON.stringify({figures:imgs.length,broken:await page.locator('img').evaluateAll(nodes=>nodes.filter(n=>!n.complete||!n.naturalWidth).map(n=>n.src))}));
 await browser.close();
})();
