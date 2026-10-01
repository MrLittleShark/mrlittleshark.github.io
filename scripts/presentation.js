'use strict';
const fs=require('node:fs');const path=require('node:path');const presentation=require('../lib/presentation.cjs');
const target=path.join(hexo.base_dir,'themes/foam-lab/source/assets/vendor/katex');fs.mkdirSync(target,{recursive:true});
fs.copyFileSync(path.join(hexo.base_dir,'node_modules/katex/dist/katex.min.css'),path.join(target,'katex.min.css'));
fs.cpSync(path.join(hexo.base_dir,'node_modules/katex/dist/fonts'),path.join(target,'fonts'),{recursive:true});
fs.copyFileSync(path.join(hexo.base_dir,'node_modules/katex/LICENSE'),path.join(target,'LICENSE.txt'));
fs.copyFileSync(path.join(hexo.base_dir,'node_modules/highlight.js/LICENSE'),path.join(target,'highlight-LICENSE.txt'));
hexo.extend.filter.register('before_post_render',data=>{data.content=presentation.protectMath(data.content);return data;},5);
hexo.extend.filter.register('after_post_render',data=>{try{data.content=presentation.render(data.content);}catch(e){throw new Error('Formula/code rendering failed in '+data.source+': '+e.message);}return data;},20);
// Dynamic command cards reuse the same highlighter at build time.
hexo.extend.generator.register('formatted-commands',function(){const data=JSON.parse(fs.readFileSync(path.join(this.source_dir,'assets/commands.json'),'utf8'));return {path:'assets/commands-display.json',data:JSON.stringify(data.map(c=>({...c,display:presentation.codeHTML(c.example,'bash')})))};});
