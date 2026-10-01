const fs = require('node:fs');
const path = require('node:path');
const {chromium} = require('C:/Users/shark/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const output = path.resolve(__dirname, '../.openfoam-work/typography');
fs.mkdirSync(output, {recursive: true});
const spacing = '*{line-height:1.5!important;letter-spacing:.12em!important;word-spacing:.16em!important}p{margin-bottom:2em!important}';

async function inspect(page) {
  return page.evaluate(() => {
    const rgb = colour => [...colour.matchAll(/[\d.]+/g)].map(item => Number(item[0]));
    function composite(front, back) {const a=front.length>3?front[3]:1;return [0,1,2].map(i=>front[i]*a+back[i]*(1-a));}
    function background(el) {if(!el)return [255,255,255];const c=rgb(getComputedStyle(el).backgroundColor);return composite(c,background(el.parentElement));}
    function luminance(c) {return c.map(v=>{v/=255;return v<=.04045?v/12.92:Math.pow((v+.055)/1.055,2.4)}).reduce((s,v,i)=>s+v*[.2126,.7152,.0722][i],0);}
    function label(el) {return `${el.tagName.toLowerCase()}${el.id?'#'+el.id:''}${typeof el.className==='string'&&el.className?'.'+el.className.trim().split(/\s+/).join('.'):''}`;}
    const lows=[], clips=[];
    for(const el of document.querySelectorAll('body *')) {
      if(el.namespaceURI!=='http://www.w3.org/1999/xhtml'||el.closest('pre,.katex,.science-cover,[hidden],.sr-only,.foam-ripple-layer'))continue;
      const r=el.getBoundingClientRect(),s=getComputedStyle(el);
      if(!r.width||!r.height||s.visibility==='hidden'||r.right<=0||r.left>=innerWidth)continue;
      const text=[...el.childNodes].filter(n=>n.nodeType===3).map(n=>n.textContent.trim()).join(' ').trim();
      if(!text)continue;
      const bg=background(el),fg=composite(rgb(s.color),bg),a=luminance(bg),b=luminance(fg),ratio=(Math.max(a,b)+.05)/(Math.min(a,b)+.05);
      const large=parseFloat(s.fontSize)>=24||(parseFloat(s.fontSize)>=18.66&&Number(s.fontWeight)>=700);
      if(ratio<(large?3:4.5)&&!el.closest(':disabled,[aria-disabled="true"]'))lows.push({element:label(el),text:text.slice(0,55),ratio:+ratio.toFixed(2),size:s.fontSize,colour:s.color});
      const x=el.scrollWidth>el.clientWidth+2,y=el.scrollHeight>el.clientHeight+2;
      if((x&&['hidden','clip'].includes(s.overflowX)||y&&['hidden','clip'].includes(s.overflowY))&&!el.closest('.sidebar'))clips.push({element:label(el),text:text.slice(0,55),x,y,overflow:s.overflow});
    }
    const outside=[...document.querySelectorAll('main a,main button,main input,main select')].filter(el=>{const r=el.getBoundingClientRect();return r.width&&r.height&&(r.left<-.5||r.right>innerWidth+.5)}).map(el=>({element:label(el),text:el.textContent.trim().slice(0,45)}));
    const para=document.querySelector('.prose p')||document.querySelector('.science-intro>p');
    const cs=getComputedStyle(para);
    return {viewport:innerWidth,pageWidth:document.documentElement.scrollWidth,overflow:document.documentElement.scrollWidth>innerWidth+1,fonts:[...document.fonts].map(f=>({family:f.family,status:f.status,weight:f.weight})),bodyType:{family:cs.fontFamily,size:cs.fontSize,line:cs.lineHeight},lowContrast:lows,clipping:clips,outside};
  });
}
(async()=>{
  const browser=await chromium.launch({channel:'msedge',headless:true});
  const results=[];
  for(const theme of ['light','dark'])for(const device of ['desktop','mobile','zoom200'])for(const kind of ['home','reader']) {
    const width=device==='desktop'?1440:device==='mobile'?390:720;
    const context=await browser.newContext({viewport:{width,height:device==='mobile'?844:1000},deviceScaleFactor:device==='zoom200'?2:1,reducedMotion:'reduce'});
    await context.addInitScript(theme=>localStorage.setItem('foamlab.theme',theme),theme);
    const page=await context.newPage();
    const errors=[];page.on('pageerror',e=>errors.push(e.message));
    await page.goto('http://localhost:4173/'+(kind==='reader'?'read/?slug=programming-10':''),{waitUntil:'networkidle'});
    if(kind==='reader')await page.waitForSelector('.prose h2');
    await page.evaluate(()=>document.fonts.ready);
    const cdp=await context.newCDPSession(page);
    await cdp.send('DOM.enable');await cdp.send('CSS.enable');
    const {root:dom}=await cdp.send('DOM.getDocument');
    const {nodeId}=await cdp.send('DOM.querySelector',{nodeId:dom.nodeId,selector:kind==='reader'?'.prose p':'.science-intro>p'});
    const platformFonts=await cdp.send('CSS.getPlatformFontsForNode',{nodeId});
    const name=`${device}-${theme}-${kind}`;
    const normal=await inspect(page);
    await page.screenshot({path:path.join(output,name+'.png'),fullPage:kind==='home'});
    if(kind==='reader'){
      await page.locator('.prose h2').nth(1).scrollIntoViewIfNeeded();
      await page.screenshot({path:path.join(output,name+'-body.png')});
      await page.evaluate(()=>scrollTo(0,0));
    }
    await page.addStyleTag({content:spacing});
    const spaced=await inspect(page);
    await page.screenshot({path:path.join(output,name+'-spacing.png'),fullPage:kind==='home'});
    const controls=await page.locator('main a,main button').count();
    results.push({name,zoomNote:device==='zoom200'?'Equivalent 200% desktop layout: 1440px physical viewport represented by 720 CSS pixels; not a browser zoom API.':undefined,platformFonts,normal,spaced,controls,errors});
    console.log(name,JSON.stringify({overflow:[normal.overflow,spaced.overflow],lowContrast:[normal.lowContrast.length,spaced.lowContrast.length],clips:[normal.clipping.length,spaced.clipping.length],outside:[normal.outside.length,spaced.outside.length],errors}));
    await context.close();
  }
  fs.writeFileSync(path.join(output,'report.json'),JSON.stringify({note:'Focused rendering checks only. Computed colour checks approximate composite backgrounds and exclude raster images, figures and TeX; they do not establish full WCAG compliance.',results},null,2));
  await browser.close();
})().catch(error=>{console.error(error);process.exit(1)});
