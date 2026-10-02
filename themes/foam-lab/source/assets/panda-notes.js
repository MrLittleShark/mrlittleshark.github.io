'use strict';
(() => {
 const mark='<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="11" cy="11" r="9" fill="#283738"/><circle cx="37" cy="11" r="9" fill="#283738"/><ellipse cx="24" cy="26" rx="22" ry="20" fill="#fffcf4" stroke="#d3decd"/><ellipse cx="15" cy="24" rx="6" ry="8" fill="#283738" transform="rotate(25 15 24)"/><ellipse cx="33" cy="24" rx="6" ry="8" fill="#283738" transform="rotate(-25 33 24)"/><circle cx="16" cy="23" r="2" fill="white"/><circle cx="32" cy="23" r="2" fill="white"/><path d="M21 32q3-3 6 0l-3 4Z" fill="#283738"/></svg>';
 function enhance(){
  // Restyle a few existing operational explanations without adding duplicate prose.
  const starts=['第一行适用于安装到该路径的 Ubuntu 软件包。','本例是二维方腔。','cp -r 复制整个目录','计算会频繁读写文件，Linux 本地目录','终端显示乱码时，检查文件编码','在另一个终端进入同一算例，执行 tail -f','修改一处打印文本，重新编译并运行。'];
  document.querySelectorAll('.prose > p').forEach(p=>{if(starts.some(s=>p.textContent.trim().startsWith(s))&&!p.closest('.panda-note')){const note=document.createElement('aside');note.className='note';p.before(note);note.append(p);}});
  // Only explicit short learning tips, never source quotations or warnings.
  document.querySelectorAll('.prose blockquote,.prose .tip,.prose .callout-tip,.prose .note').forEach(el=>{
   if(el.dataset.pandaNote||el.querySelector('pre,figure,table')||el.textContent.length>450)return;
   const first=el.firstElementChild,lead=first?.querySelector(':scope > strong:first-child');
   const explicit=el.matches('.tip,.callout-tip,.note');
   if(!explicit&&!(lead&&/^(提示|小提示|小技巧|操作提示|学习提示)[：:]?$/.test(lead.textContent.trim())))return;
   el.dataset.pandaNote='true';el.classList.add('panda-note');if(lead)lead.remove();
   const label=document.createElement('div');label.className='panda-note-label';label.innerHTML=mark+'<span>熊猫说</span>';el.prepend(label);
  });
 }
 enhance();window.addEventListener('foamlab:content-ready',enhance);
 const main=document.querySelector('main');if(main){let queued=false;new MutationObserver(()=>{if(queued)return;queued=true;requestAnimationFrame(()=>{queued=false;enhance();});}).observe(main,{childList:true,subtree:true});}
})();
