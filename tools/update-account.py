from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=R/'themes/foam-lab/source/assets/account.js'
s=p.read_text(encoding='utf-8')
s=s.replace("const count=state.progress.length;", "const count=state.progress.length;")
start=s.index("const count=state.progress.length;")
end=s.index("\n const username=",start)
s=s[:start]+"const count=state.progress.length;text('#account-completed',String(count));text('#account-progress-state','已完成 '+count+' 个新版课程单元，记录保存在当前账号。');$('#account-progress-bar').style.width=(state.totalLessons?count/state.totalLessons*100:0)+'%';$('#account-continue').href='/courses/';$('#account-continue').textContent='继续探索学习路径 →';$('#import-progress').hidden=true;"+s[end:]
s=s.replace("state.client.from('foamlab_progress').select('lesson_id,completed')", "state.client.from('foamlab_learning_progress').select('content_id,completed')")
s=s.replace(".map(x=>x.lesson_id)",".map(x=>x.content_id)")
# Completion in the new reader uses UUID content identifiers. Retain old rows server-side without mapping them to unrelated courses.
p.write_text(s,encoding='utf-8')
p=R/'themes/foam-lab/layout/account.ejs';s=p.read_text(encoding='utf-8').replace('/ 28 讲','个课程单元').replace('例如：气液两相流、电化学传质','例如：湍流模拟、传热与数值方法').replace('个人资料仅当前登录账号可读写，不作为教师权限的依据。','学校、研究方向与学习目标仅当前账号可读写；参与讨论时公开显示名称。个人资料不决定管理权限。')
s=s.replace('</aside></div></div>','<div class="profile-links"><h3>创作与社区</h3><a href="/studio/">作者工作台 →</a><a href="/community/">讨论中心 →</a><a href="/authors/">作者专栏 →</a><a href="/admin/" id="profile-admin-link" hidden>网站管理平台 →</a></div></aside></div></div>');p.write_text(s,encoding='utf-8')
p=R/'themes/foam-lab/source/assets/site.js';s=p.read_text(encoding='utf-8');start=s.index(' let completed=safeRead(');end=s.index(' // Search text',start);s=s[:start]+s[end:]
s=s.replace("index=await r.json();", "index=await r.json();try{await window.FoamLab.ready;const live=await window.FoamLab.client.from('foamlab_content').select('slug,title,summary,body,kind').eq('status','published').limit(1000);if(!live.error)index.push(...live.data.map(x=>({title:x.title,url:'/read/?slug='+encodeURIComponent(x.slug),kind:({lesson:'课程',tool:'工具',log:'日志',article:'分享',resource:'资料'})[x.kind]||'参考',text:x.summary+' '+x.body})));}catch{}")
s=s.replace("h.textContent=c.name;", "if(c.url){const a=document.createElement('a');a.href=c.url;a.textContent=c.name;h.append(a);}else h.textContent=c.name;")
s=s.replace("card.append(top,p,pre,details);", "card.append(top,p,pre,details);if(c.verificationText){const note=document.createElement('small');note.className='command-evidence';note.textContent=c.verificationText;card.append(note);}if(c.url){const a=document.createElement('a');a.className='text-link';a.href=c.url;a.textContent='完整帮助与源码 →';card.append(a);}")
p.write_text(s,encoding='utf-8')
print('Account and search adapted to stable content IDs.')
