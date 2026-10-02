'use strict';
const fs=require('node:fs'),path=require('node:path');
hexo.extend.generator.register('download-inventory',()=>{
 const root=path.join(hexo.source_dir,'downloads'),files=[];
 const walk=dir=>{if(!fs.existsSync(dir))return;for(const entry of fs.readdirSync(dir,{withFileTypes:true})){const full=path.join(dir,entry.name);if(entry.isDirectory())walk(full);else if(entry.isFile()){const relative=path.relative(hexo.source_dir,full).split(path.sep).join('/');files.push({name:entry.name,url:'/'+relative.split('/').map(encodeURIComponent).join('/'),size:fs.statSync(full).size});}}};walk(root);
 return {path:'assets/download-inventory.json',data:JSON.stringify(files)};
});
