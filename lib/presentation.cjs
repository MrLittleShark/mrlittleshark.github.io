'use strict';
const katex=require('katex');const cheerio=require('cheerio');const hljs=require('highlight.js/lib/core').newInstance();
for(const lang of ['bash','cpp','python','json','yaml','makefile','ini','plaintext','powershell','latex'])hljs.registerLanguage(lang,require('highlight.js/lib/languages/'+lang));
hljs.registerLanguage('openfoam',h=>({name:'OpenFOAM dictionary',aliases:['foam','dict'],keywords:{keyword:'FoamFile dimensions internalField boundaryField type value uniform nonuniform application solver libs functions include includeIfPresent includeEtc includeFunc code codeInclude codeOptions codeLibs name object class version format location',literal:'true false yes no on off',built_in:'fixedValue zeroGradient noSlip empty wedge symmetryPlane cyclic inletOutlet fixedFluxPressure laminar RAS LES Gauss Euler backward CrankNicolson upwind linear linearUpwind limitedLinear PIMPLE SIMPLE PISO PCG PBiCGStab GAMG smoothSolver'},contains:[h.C_LINE_COMMENT_MODE,h.C_BLOCK_COMMENT_MODE,h.QUOTE_STRING_MODE,h.C_NUMBER_MODE,{className:'meta',begin:/#[A-Za-z{][^\n]*/},{className:'variable',begin:/\$[A-Za-z_{][\w{}./]*/}]}));
const escape=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
function guess(code){
 if(/\b(?:fvm::|fvc::|const scalar|const vector|forAll\(|#include\s*["<])/.test(code))return 'cpp';
 if(/\b(?:FoamFile|boundaryField|internalField|ddtSchemes|fvSolution|castellatedMesh|PIMPLE|nCorrectors)\b/.test(code)||/\b(?:type|value|solver|application|dimensions)\s+[^\n]+;/.test(code))return 'openfoam';
 if(/\b(?:EXE_INC|EXE_LIBS|LIB_LIBS|FOAM_USER_APPBIN)\b/.test(code)&&!/^(?:\$|cd |source )/m.test(code))return 'makefile';
 if(/^(?:from \w+ import |import \w+|def \w+\(|print\()/m.test(code))return 'python';
 if(/(?:^|\n)(?:\$ |#!.*(?:bash|sh)|#SBATCH|source |cd |cp |rm |mkdir |echo |export |blockMesh|checkMesh|\w+Foam|foam\w+|mpirun|wmake|grep |git |npm |node |python )/.test(code))return 'bash';
 if(/[{};]/.test(code))return 'openfoam';return 'plaintext';
}
const labels={bash:'Bash / 终端',cpp:'C++',openfoam:'OpenFOAM 字典',python:'Python',makefile:'Makefile',plaintext:'文本 / 日志',json:'JSON',yaml:'YAML',powershell:'PowerShell',ini:'配置文件',tex:'TeX / LaTeX',latex:'TeX / LaTeX'};
function codeHTML(source,language){const lang=hljs.getLanguage(language)?language:guess(source);return {language:lang,label:labels[lang]||lang,html:hljs.highlight(source,{language:lang,ignoreIllegals:true}).value};}
const MATH=/\\\[([\s\S]*?)\\\]|\\\(([\s\S]*?)\\\)|\$\$([\s\S]*?)\$\$|(?<![\\\w])\$(?![\s{(])([^$\n<>]+?)(?<!\s)\$(?!\w)/g;
function protectMath(markdown){
 // Process fenced/inline code first, preserving shell dollars literally.
 return markdown.replace(/(`{3,}|~{3,})[^\n]*\n[\s\S]*?\1|`+[^`]*`+|<pre\b[^>]*>[\s\S]*?<\/pre>|<code\b[^>]*>[\s\S]*?<\/code>|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|\$\$[\s\S]*?\$\$|(?<![\\\w])\$(?![\s{(])[^$\n<>]+?(?<!\s)\$(?!\w)/g,part=>{
   if(/^(?:`|~|<pre|<code)/.test(part))return part;
   const display=part.startsWith('\\[')||part.startsWith('$$');const n=part.startsWith('$')&&!display?1:2;const tex=part.slice(n,-n).replace(/&(?:amp|lt|gt|quot|#x27|#39);/g,e=>({'&amp;':'&','&lt;':'<','&gt;':'>','&quot;':'"','&#x27;':"'",'&#39;':"'"}[e]));
   return '<span class="tex-source" data-display="'+display+'" data-tex="'+escape(tex)+'"></span>';
 });
}
function render(content){const $=cheerio.load(content,{},false);
 $('.tex-source').each((_,node)=>{const el=$(node),tex=el.attr('data-tex')||'',display=el.attr('data-display')==='true';const result=katex.renderToString(tex,{displayMode:display,throwOnError:true,trust:false,strict:'error',output:'htmlAndMathml',maxExpand:1000});el.replaceWith('<span class="math-formula'+(display?' math-display':'')+'" data-tex="'+escape(tex)+'">'+result+'</span>');});
 $('pre > code').each((_,node)=>{const code=$(node),pre=code.parent();if(pre.parent().hasClass('code-panel'))return;const source=code.text();const result=codeHTML(source,(code.attr('class')||'').match(/language-([\w-]+)/)?.[1]);code.attr('class','hljs language-'+result.language).html(result.html);pre.attr('tabindex','0').attr('aria-label',result.label+'代码');pre.wrap('<div class="code-panel" data-language="'+result.language+'"></div>');pre.before('<div class="code-toolbar"><span class="code-language">'+result.label+'</span><span class="code-lines">'+source.replace(/\n$/,'').split('\n').length+' 行</span><button type="button" class="code-wrap" aria-pressed="false">自动换行</button><button type="button" class="copy-code" aria-label="复制代码">复制</button></div>');});
 return $.html();}
module.exports={protectMath,render,codeHTML,guess};
