/* Full-corpus formatting checks for readable tutorial content. */
const fs=require('node:fs'),path=require('node:path'),{marked}=require('marked'),cheerio=require('cheerio'),P=require('../lib/presentation.cjs');
const root=path.resolve(__dirname,'..'),dir=path.join(root,'tools/content');
const rows=fs.readdirSync(dir).filter(f=>f.endsWith('content.json')).flatMap(f=>JSON.parse(fs.readFileSync(path.join(dir,f),'utf8')));
const errors=[];let codeBlocks=0,tables=0,formulas=0,figures=0;
const forbidden=['核验范围：','不能仅凭相同键名推断为同一个参数','教程保留的参数注释','内容已与在线资料库同步','完成标志：'];
for(const row of rows){
 try{
  if(/[\x00-\x08\x0b\x0c\x0e-\x1f]/.test(row.body))errors.push(row.slug+': control character');
  if((row.body.match(/^```/gm)||[]).length%2)errors.push(row.slug+': unclosed fenced code');
  const $=cheerio.load(P.render(marked.parse(P.protectMath(row.body))));
  codeBlocks+=$('pre code').length;tables+=$('table').length;formulas+=$('.math-formula').length;figures+=$('img').length;
  $('pre,code,.katex').remove();
  const text=$.text();for(const phrase of forbidden)if(text.includes(phrase))errors.push(row.slug+': boilerplate '+phrase);
  for(const cell of $('td').toArray())if(/^[\s*/\\_-]{12,}$/.test($(cell).text()))errors.push(row.slug+': decorative separator imported as table data');
  for(const heading of $('h2,h3').toArray()){if(!$(heading).next().length)errors.push(row.slug+': empty final section '+$(heading).text());}
 }catch(e){errors.push(row.slug+': '+e.message);}
}
const commands=JSON.parse(fs.readFileSync(path.join(root,'source-openfoam/assets/commands.json'),'utf8'));
for(const c of commands){if(!c.examples?.length)errors.push('command '+c.name+': no code example');if(/核验|源码说明：|已记录的选项：/.test(c.details||''))errors.push('command '+c.name+': prose dump in card');}
const report={pages:rows.length,courses:rows.filter(r=>r.kind==='lesson').length,codeBlocks,tables,formulas,figures,commands:commands.length,commandExamples:commands.reduce((n,c)=>n+(c.examples?.length||0),0),errors};
fs.mkdirSync(path.join(root,'.openfoam-work/editorial'),{recursive:true});fs.writeFileSync(path.join(root,'.openfoam-work/editorial/format-check.json'),JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));process.exitCode=errors.length?1:0;
