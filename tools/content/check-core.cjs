const fs=require('node:fs'),path=require('node:path');
const {protectMath,render}=require('../../lib/presentation.cjs');
const cheerio=require('cheerio');
(async()=>{
 const {marked}=await import('marked');
 const items=JSON.parse(fs.readFileSync(path.join(__dirname,'core-content.json'),'utf8'));
 const root=path.resolve(__dirname,'../..');
 const errors=[],slugs=new Set();let math=0,codes=0,figures=0;
 const rendered=[];
 for(const item of items){
  if(slugs.has(item.slug))errors.push({slug:item.slug,error:'duplicate slug'});slugs.add(item.slug);
  if(!/^[a-z0-9-]+$/.test(item.slug))errors.push({slug:item.slug,error:'invalid slug'});
  if(item.body.length<600)errors.push({slug:item.slug,error:'body too short'});
  try{
   const html=render(marked.parse(protectMath(item.body)));
   const $=cheerio.load(html);
   math+=$('.math-formula').length;codes+=$('.code-panel').length;figures+=$('img').length;
   $('img').each((_,el)=>{const src=$(el).attr('src');if(src.startsWith('/')&&!fs.existsSync(path.join(root,'source-openfoam',src)))errors.push({slug:item.slug,error:'missing figure',src});});
   if(!$('img').length)errors.push({slug:item.slug,error:'no figure'});
   if(!fs.existsSync(path.join(root,'source-openfoam',item.cover_url)))errors.push({slug:item.slug,error:'missing cover'});
   rendered.push(`<article id="${item.slug}"><div class="eyebrow">${item.track} / ${item.metadata.duration}</div><h1>${item.title}</h1><p class="summary">${item.summary}</p>${html}</article>`);
  }catch(e){errors.push({slug:item.slug,error:String(e)});}
 }
 const dir=path.join(root,'.openfoam-work/replan');fs.mkdirSync(dir,{recursive:true});
 const report={items:items.length,math,codes,figures,slugs:[...slugs],errors};
 fs.writeFileSync(path.join(dir,'core-content-check.json'),JSON.stringify(report,null,2));
 const katexCss=fs.readFileSync(path.join(root,'node_modules/katex/dist/katex.min.css'),'utf8').replaceAll('url(fonts/', 'url(file:///'+path.join(root,'node_modules/katex/dist/fonts').replaceAll('\\','/')+'/');
 const local=rendered.join('\n').replaceAll('src="/assets/', 'src="file:///'+path.join(root,'source-openfoam/assets').replaceAll('\\','/')+'/');
 fs.writeFileSync(path.join(dir,'core-preview.html'),`<!doctype html><meta charset="utf-8"><title>FoamLab core content QA</title><style>${katexCss}*{box-sizing:border-box}body{margin:0;background:#edf3f8;color:#16334d;font:17px/1.95 "Microsoft YaHei",sans-serif}article{max-width:1000px;margin:36px auto;padding:56px 70px;background:white;border:1px solid #dbe7f0;border-radius:18px}h1{font-size:32px;line-height:1.5}h3{font-size:24px;margin-top:40px}.eyebrow{color:#247cb7;letter-spacing:.04em}.summary{color:#61758a;font-size:19px}img{display:block;width:100%;height:auto;margin:28px 0}pre{overflow:auto;background:#102c44;color:#e6f2fb;padding:22px;margin:0;font:14px/1.75 Consolas,monospace}code{font-family:Consolas,monospace}p code,li code{background:#eef5fb;padding:2px 5px}.code-panel{margin:24px 0;border-radius:10px;overflow:hidden}.code-toolbar{background:#e4edf6;padding:7px 14px;font-size:13px;display:flex;gap:18px}.code-toolbar button{display:none}.math-display{display:block;overflow:auto;margin:22px 0}.katex-display{margin:0}table{border-collapse:collapse;width:100%;font-size:15px}th,td{border:1px solid #d6e3ed;padding:10px;text-align:left}a{color:#1268a7}blockquote{border-left:3px solid #2686bf;padding-left:18px}</style>${local}`);
 console.log(JSON.stringify({items:items.length,math,codes,figures,errors},null,2));
 process.exitCode=errors.length?1:0;
})();
