/* Content checks include Markdown, TeX, code, figures and local downloads. */
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const {marked}=require('marked'),cheerio=require('cheerio');const P=require('../lib/presentation.cjs');
const root=path.resolve(__dirname,'..'),base=path.join(root,'source-openfoam'),dir=path.join(root,'tools/content');
const rows=fs.readdirSync(dir).filter(f=>f.endsWith('content.json')).flatMap(f=>JSON.parse(fs.readFileSync(path.join(dir,f),'utf8'))),slugs=new Set(rows.map(r=>r.slug));const errors=[];let math=0,codes=0,images=0,links=0;
if(slugs.size!==rows.length)errors.push('duplicate slug');
for(const r of rows){try{const rendered=P.render(marked.parse(P.protectMath(r.body||'')));const $=cheerio.load(rendered);math+=$('.math-formula').length;codes+=$('pre code').length;images+=$('img').length;
 for(const n of $('[href],[src]').toArray())for(const attr of ['href','src']){const raw=$(n).attr(attr);if(!raw||!raw.startsWith('/')||raw.startsWith('//'))continue;links++;const u=new URL(raw,'https://foamlab.invalid');if(u.pathname==='/read/'){if(!slugs.has(u.searchParams.get('slug')))errors.push(r.slug+': unknown article '+raw);continue;}const p=path.join(base,decodeURIComponent(u.pathname));if(u.pathname.endsWith('/')){if(!fs.existsSync(path.join(p,'index.md')))errors.push(r.slug+': missing page '+raw);}else if(!fs.existsSync(p)&&!u.pathname.startsWith('/assets/vendor/'))errors.push(r.slug+': missing asset '+raw);}
 if(r.kind==='lesson'&&!$('img').length)errors.push(r.slug+': course lacks an explanatory figure');
}catch(e){errors.push(r.slug+': '+e.message);}}
const report={records:rows.length,courses:rows.filter(r=>r.kind==='lesson').length,math,codes,images,links,errors};fs.mkdirSync(path.join(root,'.openfoam-work/replan'),{recursive:true});fs.writeFileSync(path.join(root,'.openfoam-work/replan/content-integrity.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));process.exitCode=errors.length?1:0;
