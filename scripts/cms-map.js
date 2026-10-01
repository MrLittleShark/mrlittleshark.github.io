'use strict';
const fs=require('node:fs'),path=require('node:path');
const directory=path.join(hexo.base_dir,'tools/content'),routes=new Map();
if(fs.existsSync(directory))for(const name of fs.readdirSync(directory).filter(n=>n.endsWith('content.json'))){for(const item of JSON.parse(fs.readFileSync(path.join(directory,name),'utf8'))){if(item.metadata?.canonical_path)routes.set(item.metadata.canonical_path,item.slug);}}
hexo.extend.filter.register('before_post_render',data=>{const route='/'+String(data.source||'').replace(/index\.md$/,'').replace(/^\//,'');data.cms_slug=routes.get(route)||'';return data;},4);
