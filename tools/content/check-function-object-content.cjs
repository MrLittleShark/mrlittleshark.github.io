const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),katex=require('katex'),cheerio=require('cheerio'),{marked}=require('marked');
const {protectMath,render}=require('../../lib/presentation.cjs');
const rows=JSON.parse(fs.readFileSync(path.join(__dirname,'function-objects-content.json'),'utf8'));
let formulas=0,codeBlocks=0,tables=0,links=0;
for(const row of rows){
 assert(!/\{\{|&quot;|&#x20;|源码注释|核验范围/.test(row.body),row.slug);
 const $=cheerio.load(protectMath(row.body),{},false);
 $('.tex-source').each((_,el)=>{katex.renderToString($(el).attr('data-tex'),{throwOnError:true,strict:'error',trust:false});formulas++;});
 const out=render(marked.parse(protectMath(row.body))),dom=cheerio.load(out);
 codeBlocks+=dom('.code-panel').length;tables+=dom('table').length;
 dom('[href],[src]').each((_,el)=>{
  const href=dom(el).attr('href')||dom(el).attr('src');if(!href?.startsWith('/'))return;links++;
  const u=new URL(href,'http://localhost');
  if(u.pathname==='/read/')assert(rows.some(x=>x.slug===u.searchParams.get('slug')),href);
  else assert(fs.existsSync(path.join(__dirname,'../../source-openfoam',u.pathname)),href);
 });
 for(const d of row.metadata.downloads||[])assert(d.size_bytes===fs.statSync(path.join(__dirname,'../../source-openfoam',d.url)).size,d.url);
 assert(dom('h2').length>=2,row.slug);assert(dom('img').length>=1,row.slug);
 assert(!dom('.code-panel .code-panel').length,'Nested code panels');
}
console.log(JSON.stringify({pages:rows.length,formulas,codeBlocks,tables,localLinks:links},null,2));
