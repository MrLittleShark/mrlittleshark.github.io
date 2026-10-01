const fs=require('node:fs'),path=require('node:path'),katex=require('katex'),cheerio=require('cheerio'),{marked}=require('marked');
const {protectMath,render}=require('../../lib/presentation.cjs');
let formulas=0,blocks=0,errors=[];
for(const file of ['programming-content.json','programming-resources-content.json','core-content.json']){
 for(const item of JSON.parse(fs.readFileSync(path.join(__dirname,file),'utf8'))){
  const protectedBody=protectMath(item.body),$=cheerio.load(protectedBody,{},false);
  $('.tex-source').each((_,el)=>{formulas++;try{katex.renderToString($(el).attr('data-tex'),{throwOnError:true,strict:'error',trust:false})}catch(e){errors.push({slug:item.slug,tex:$(el).attr('data-tex'),error:e.message})}});
  try{const html=render(marked.parse(protectedBody));blocks+=(html.match(/class="code-panel"/g)||[]).length;}catch(e){errors.push({slug:item.slug,error:e.message})}
 }
}
console.log(JSON.stringify({formulas,blocks,errors},null,2));process.exitCode=errors.length?1:0;
