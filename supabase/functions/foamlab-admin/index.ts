// Administrative requests require BOTH a verified Supabase session and the
// authorized individual's GitHub token. The organization owns the repository;
// profile metadata never grants a role.
const REPO='foamlabshark/foamlabshark.github.io';
const OWNER_ID=112299157;
const SOURCE_BRANCH='foamlab-source';
const ALLOWED_ORIGINS=new Set(['https://foamlabshark.github.io','http://localhost:4173','http://127.0.0.1:4173']);
const CONTENT_PATH=/^source-openfoam\/(?:lessons\/(?:0[1-9]|1[0-9]|2[0-8])|reference\/(?:manual|guide)-\d{2}|dictionaries\/[a-z0-9-]+|start|bubble|maintenance)\/index\.md$/;
export function createHandler(env,request=fetch){return async function handler(req){
 const origin=req.headers.get('Origin')||'';const cors={'Access-Control-Allow-Origin':ALLOWED_ORIGINS.has(origin)?origin:'https://foamlabshark.github.io','Access-Control-Allow-Headers':'authorization,apikey,content-type,x-client-info','Access-Control-Allow-Methods':'POST,OPTIONS','Vary':'Origin','Cache-Control':'no-store'};
 const respond=(data,status=200)=>new Response(JSON.stringify(data),{status,headers:{...cors,'Content-Type':'application/json; charset=utf-8'}});
 if(origin&&!ALLOWED_ORIGINS.has(origin))return respond({error:'不允许的请求来源。'},403);
 if(req.method==='OPTIONS')return new Response('ok',{headers:cors});
 if(req.method!=='POST')return respond({error:'仅接受 POST 请求。'},405);
 try{
  const authorization=req.headers.get('Authorization')||'';if(!/^Bearer [\w.-]+$/.test(authorization))return respond({error:'请先登录管理员账号。'},401);
  const raw=await req.text();if(raw.length>450000)return respond({error:'内容超出单次编辑长度。'},413);
  let input;try{input=JSON.parse(raw);}catch{return respond({error:'请求格式错误。'},400);}
  const auth=await request(env.url+'/auth/v1/user',{headers:{Authorization:authorization,apikey:env.key}});if(!auth.ok)return respond({error:'登录状态已失效，请重新登录。'},401);const user=await auth.json();if(!user.id)return respond({error:'未验证的登录会话。'},401);
  const token=input.githubToken;if(typeof token!=='string'||!token||token.length>2000)return respond({error:'请重新进行管理员 GitHub 授权。',code:'github_authorization_required'},403);
  const ghHeaders={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'FoamLab-Admin'};
  const identityResponse=await request('https://api.github.com/user',{headers:ghHeaders});if(!identityResponse.ok)return respond({error:'GitHub 授权已失效，请重新授权。',code:'github_authorization_required'},403);
  const github=await identityResponse.json();
  // GitHub's /user response, not client supplied usernames or editable metadata.
  if(github.id!==OWNER_ID)return respond({error:'当前账号没有本站管理权限。'},403);
  const linked=(user.identities||[]).some(i=>i.provider==='github'&&[i.id,i.provider_id,i.identity_data?.sub,i.identity_data?.provider_id].some(id=>String(id)===String(github.id)));
  if(!linked)return respond({error:'GitHub 授权与当前登录账号不一致，请重新登录。'},403);
  const scopes=(identityResponse.headers.get('x-oauth-scopes')||'').split(',').map(s=>s.trim());const writeAccess=scopes.includes('repo')||scopes.includes('public_repo');
  async function gh(endpoint,options={}){const response=await request('https://api.github.com/repos/'+REPO+endpoint,{...options,headers:{...ghHeaders,'Content-Type':'application/json'},body:options.body?JSON.stringify(options.body):undefined});const data=await response.json();if(!response.ok){const error=new Error(response.status===409?'内容已被其他操作更新，请重新载入后合并修改。':response.status===403?'GitHub 拒绝写入，请重新授予管理权限。':'GitHub 操作未完成（HTTP '+response.status+'）。');error.status=response.status;throw error;}return data;}
  if(input.action==='status'){const repo=await gh('');return respond({admin:true,login:github.login,writeAccess:writeAccess&&!!repo.permissions?.push,sourceBranch:SOURCE_BRANCH});}
  if(input.action==='records'){const items=await gh('/issues?state=all&per_page=100');return respond({items:items.filter(i=>!i.pull_request&&i.user?.id===OWNER_ID&&/^\[(作业发布|公告)\]/.test(i.title)).map(i=>({number:i.number,title:i.title,body:i.body,state:i.state,url:i.html_url}))});}
  if(input.action==='deployment'){const d=await gh('/actions/workflows/foamlab-pages.yml/runs?per_page=5');return respond({runs:(d.workflow_runs||[]).map(r=>({id:r.id,status:r.status,conclusion:r.conclusion,url:r.html_url,branch:r.head_branch,sha:r.head_sha,created:r.created_at}))});}
  if(input.action==='content-list'){const tree=await gh('/git/trees/'+SOURCE_BRANCH+'?recursive=1');return respond({files:tree.tree.filter(f=>f.type==='blob'&&CONTENT_PATH.test(f.path)).map(f=>({path:f.path,sha:f.sha}))});}
  if(['content-read','content-save'].includes(input.action)){
   if(typeof input.path!=='string'||!CONTENT_PATH.test(input.path))return respond({error:'此路径不能通过管理平台编辑。'},403);
   const endpoint='/contents/'+input.path.split('/').map(encodeURIComponent).join('/');
   if(input.action==='content-read'){const f=await gh(endpoint+'?ref='+SOURCE_BRANCH);return respond({path:f.path,sha:f.sha,content:f.content,encoding:'base64'});}
   if(!writeAccess)return respond({error:'请重新授权公开仓库写入权限。',code:'github_authorization_required'},403);
   if(typeof input.content!=='string'||input.content.length>300000||!input.content.startsWith('---\n')||typeof input.sha!=='string'||!/^[a-f0-9]{40}$/.test(input.sha))return respond({error:'正文或版本信息不完整。'},400);
   const bytes=new TextEncoder().encode(input.content);let binary='';for(const b of bytes)binary+=String.fromCharCode(b);
   const saved=await gh(endpoint,{method:'PUT',body:{message:'Update learning content: '+input.path,content:btoa(binary),sha:input.sha,branch:SOURCE_BRANCH}});return respond({saved:true,sha:saved.content.sha,commit:saved.commit.sha,url:saved.commit.html_url});
  }
  if(input.action==='publish'||input.action==='record-update'){
   if(!writeAccess)return respond({error:'请重新授权公开仓库写入权限。',code:'github_authorization_required'},403);
   if(!['assignment','announcement'].includes(input.kind)||typeof input.title!=='string'||!input.title.trim()||input.title.length>100||typeof input.body!=='string'||!input.body.trim()||input.body.length>20000)return respond({error:'请检查标题、类型与正文。'},400);
   const title=(input.kind==='assignment'?'[作业发布] ':'[公告] ')+input.title.trim();let item;
   if(input.action==='record-update'){
    if(!Number.isInteger(input.number)||input.number<1)return respond({error:'记录编号无效。'},400);
    const existing=await gh('/issues/'+input.number);if(existing.user?.id!==OWNER_ID||!/^\[(作业发布|公告)\]/.test(existing.title))return respond({error:'只能编辑管理员发布的作业或公告。'},403);
    if(!['open','closed'].includes(input.state))return respond({error:'记录状态无效。'},400);
    item=await gh('/issues/'+input.number,{method:'PATCH',body:{title,body:input.body,state:input.state}});
   }else item=await gh('/issues',{method:'POST',body:{title,body:input.body}});
   return respond({number:item.number,url:item.html_url,title:item.title});
  }
  return respond({error:'未知管理操作。'},400);
 }catch(error){return respond({error:error.status?error.message:'管理服务暂时不可用，请稍后重试。'},error.status||502);}
};}
if(typeof Deno!=='undefined'){
 const keys=JSON.parse(Deno.env.get('SUPABASE_PUBLISHABLE_KEYS')||'{}');
 Deno.serve(createHandler({url:Deno.env.get('SUPABASE_URL'),key:keys.default||Deno.env.get('SUPABASE_ANON_KEY')}));
}
