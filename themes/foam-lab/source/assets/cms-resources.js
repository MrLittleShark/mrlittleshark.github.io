'use strict';
window.FoamCMSResources=async C=>{
 const {L,run,notice,all,UI}=C,esc=L.esc,p=L.$('#cms-panel'),bucket=L.client.storage.from('foamlab-resources');
 let files=[],content=[],page=1,query='',source='',uploading=false;
 const canonical=url=>{try{return new URL(url,location.origin).href;}catch{return '';}};
 const decoded=url=>{try{return decodeURI(url);}catch{return url;}};
 const references=file=>{const absolute=canonical(file.url);if(!absolute)return [];const local=new URL(absolute).origin===location.origin?new URL(absolute).pathname:null,candidates=[file.url,absolute,local].filter(Boolean).flatMap(url=>[url,decoded(url)]);return content.filter(row=>{const text=JSON.stringify([row.metadata,row.cover_url,row.body]).replaceAll('&amp;','&'),plain=decoded(text);return candidates.some(url=>text.includes(url)||plain.includes(url));});};
 const label=file=>file.label||file.name.replace(/^[a-f0-9-]{36}-/,'');
 async function load(){
  content=await all('foamlab_content','id,title,slug,kind,status,revision,metadata,body,cover_url,track,series');
  const uploaded=[];for(let offset=0;;offset+=100){const batch=L.check(await bucket.list('library',{limit:100,offset,sortBy:{column:'name',order:'asc'}}));uploaded.push(...batch.filter(f=>f.id||f.metadata));if(batch.length<100)break;}
  let staticFiles=[];const response=await fetch('/assets/download-inventory.json');if(!response.ok)throw Error('站点文件目录暂时无法读取，请刷新。');staticFiles=await response.json();
  files=uploaded.map(f=>({name:f.name,url:bucket.getPublicUrl('library/'+f.name).data.publicUrl,size:f.metadata?.size||0,source:'upload',date:f.created_at}));
  files.push(...staticFiles.map(f=>({...f,source:'site'})));
  const known=new Set(files.map(f=>canonical(f.url)));
  for(const row of content){const downloads=[...(Array.isArray(row.metadata?.downloads)?row.metadata.downloads:[]),...(row.metadata?.download_url?[{url:row.metadata.download_url,label:row.title}]:[])];for(const d of downloads){if(!L.safeURL(d.url)||known.has(canonical(d.url)))continue;known.add(canonical(d.url));files.push({name:d.url.split('/').pop(),label:d.label,url:d.url,size:d.size_bytes||0,source:'link'});}}
 }
 p.innerHTML='<div class="cms-toolbar"><div><h2>下载资源</h2><p>查看文件、下载条目及引用它们的文章。</p></div><label class="button">上传文件<input id="cms-upload" type="file" multiple hidden></label></div><div class="cms-subtabs"><button class="selected" data-resource-tab="files">文件与附件</button><button data-resource-tab="entries">下载条目</button></div><progress id="cms-upload-progress" value="0" max="100" hidden></progress><div class="cms-filters"><input id="cms-file-search" type="search" placeholder="搜索文件名或引用文章" aria-label="搜索资源"><select id="cms-file-source" aria-label="文件来源"><option value="">全部来源</option><option value="upload">后台上传</option><option value="site">随网站发布</option><option value="link">外部链接</option></select></div><div id="cms-files" class="cms-table"></div><div id="cms-file-pager"></div>';
 let mode='files';
 function render(){
  L.$('#cms-file-source').hidden=mode==='entries';
  const target=mode==='entries'?content.filter(x=>x.kind==='resource'):files;
  const shown=target.filter(f=>mode==='entries'?[f.title,f.track,f.series].join(' ').toLowerCase().includes(query):(!source||f.source===source)&&[label(f),...references(f).map(r=>r.title)].join(' ').toLowerCase().includes(query));
  page=Math.max(1,Math.min(page,Math.ceil(shown.length/25)||1));
  L.$('#cms-files').innerHTML=shown.slice((page-1)*25,page*25).map(f=>{
   if(mode==='entries')return '<div class="cms-file-row"><div><strong>'+esc(f.title)+'</strong><small>'+esc(UI.locationLabel(f))+'</small></div><span class="pill">'+esc(({draft:'草稿',published:'已发布',archived:'已下架',trash:'回收站'})[f.status])+'</span><div class="cms-row-actions"><button class="text-button" data-resource-edit="'+f.id+'">编辑下载条目</button></div></div>';
   const used=references(f),index=files.indexOf(f);
   return '<div class="cms-file-row"><div><a href="'+esc(L.safeURL(f.url))+'" target="_blank" rel="noopener">'+esc(label(f))+' ↗</a><small>'+esc(({upload:'后台上传',site:'随网站发布',link:'外部链接'})[f.source])+' · '+(f.size?L.fileSize(f.size):'大小未记录')+'</small></div><div class="cms-muted">'+(used.length?'<details><summary>'+used.length+' 篇内容引用</summary>'+used.map(r=>'<div><button class="text-button" data-resource-edit="'+r.id+'">'+esc(r.title)+'</button></div>').join('')+'</details>':'暂无文章引用')+'</div><div class="cms-row-actions"><button class="text-button" data-copy-file="'+index+'">复制地址</button><button class="text-button" data-create-resource="'+esc(f.url)+'" data-file-index="'+index+'">建立下载条目</button>'+(f.source==='upload'?'<button class="text-button danger" data-delete-file="'+index+'">删除</button>':'')+'</div></div>';
  }).join('')||'<div class="cms-empty">没有符合条件的资源。</div>';
  L.$('#cms-file-pager').innerHTML=UI.pager(page,shown.length);
 }
 await load();render();
 p.querySelectorAll('[data-resource-tab]').forEach(b=>b.onclick=()=>{mode=b.dataset.resourceTab;page=1;p.querySelectorAll('[data-resource-tab]').forEach(x=>x.classList.toggle('selected',x===b));render();});
 L.$('#cms-file-search').oninput=e=>{query=e.target.value.toLowerCase();page=1;render();};L.$('#cms-file-source').onchange=e=>{source=e.target.value;page=1;render();};
 L.$('#cms-file-pager').onclick=e=>{const b=e.target.closest('[data-page]');if(b){page=Number(b.dataset.page);render();}};
 L.$('#cms-upload').onchange=e=>{const selection=[...e.target.files];if(!selection.length||uploading)return;run(async()=>{
  for(const file of selection)if(!file.size||file.size>52428800)throw Error(file.name+'：请选择 50 MB 以内的非空文件。');
  uploading=true;const progress=L.$('#cms-upload-progress');progress.hidden=false;let count=0;
  try{for(const file of selection){const name=crypto.randomUUID()+'-'+file.name.replace(/[^\p{L}\p{N}._-]/gu,'_');L.check(await bucket.upload('library/'+name,file,{contentType:file.type||'application/octet-stream',upsert:false}));count++;progress.value=count/selection.length*100;}}
  finally{uploading=false;await load();mode='files';source='upload';L.$('#cms-file-source').value=source;page=1;render();notice('已上传 '+count+' / '+selection.length+' 个文件。');progress.hidden=true;}
 });};
 L.$('#cms-files').onclick=e=>{const b=e.target.closest('[data-copy-file],[data-delete-file],[data-create-resource],[data-resource-edit]');if(!b)return;run(async()=>{
  if(b.dataset.resourceEdit){await C.openItem(b.dataset.resourceEdit);return;}
  if(b.dataset.copyFile!==undefined){await navigator.clipboard.writeText(files[Number(b.dataset.copyFile)].url);notice('文件地址已复制。');return;}
  if(b.dataset.createResource){const file=files[Number(b.dataset.fileIndex)];await C.openItem(null,{kind:'resource',slug:'resource-'+crypto.randomUUID().slice(0,12),title:label(file),body:'',metadata:{downloads:[{label:label(file),url:file.url,size_bytes:file.size,description:''}]}});notice('补充资料说明后保存或发布。');L.$('#cms-attachments').open=true;return;}
  const file=files[Number(b.dataset.deleteFile)];content=await all('foamlab_content','id,title,slug,kind,status,metadata,body,cover_url,track,series');const used=references(file);
  if(used.length){await UI.confirmAction({title:'文件仍被文章引用',message:label(file),details:used.map(x=>x.title),action:'返回管理引用',html:'<p>先在引用文章中替换或移除下载地址，再删除文件。</p>'});render();return;}
  if(!await UI.confirmAction({title:'永久删除文件？',message:label(file),details:['后台已检查：当前没有文章引用此文件。','文件会从存储中删除，原下载地址将失效。'],action:'确认删除',danger:true}))return;
  L.check(await bucket.remove(['library/'+file.name]));await load();render();notice('文件已删除。');
 });};
};
