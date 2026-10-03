/* Local-only Auth member RPCs for browser interaction tests. */
const {ADMIN,MEMBER}=require('./check-cms-ui.cjs');
async function memberRPC(f,count=3){
 const registered=Array.from({length:count},(_,n)=>({user_id:n===0?ADMIN:n===1?MEMBER:`aaaaaaaa-aaaa-4aaa-8aaa-${String(n).padStart(12,'0')}`,display_name:n===0?'测试管理员':n===1?'测试会员':'新注册成员 '+n,username:'user-'+String(n).padStart(2,'0'),email:`user-${n}@example.invalid`,registered_at:new Date(Date.UTC(2026,0,n+1)).toISOString(),last_sign_in_at:n%3?null:new Date(Date.UTC(2026,2,n+1)).toISOString(),level:n+1,xp:n*(n+1)*25,institution:n===1?'测试大学':'',research:n===1?'湍流':'',learning_stage:n===1?'research':'',bio:''}));
 const requests=[];let failure=false,conflict=false,delayed='';
 await f.context.route('**/rest/v1/rpc/foamlab_admin_*',async route=>{
  const req=route.request(),cors={'access-control-allow-origin':'*','access-control-allow-headers':'*','access-control-allow-methods':'POST,OPTIONS'};
  if(req.method()==='OPTIONS')return route.fulfill({status:204,headers:cors});
  const name=new URL(req.url()).pathname.split('/').pop(),args=req.postDataJSON();requests.push({name,args});
  const reply=(value,status=200)=>route.fulfill({status,contentType:'application/json',headers:cors,body:JSON.stringify(value)});
  if(name==='foamlab_admin_members'){
   if(failure)return reply({message:'测试：成员服务暂时不可用'},503);
   let items=registered.map(r=>({...r,role:f.db.foamlab_roles.find(x=>x.user_id===r.user_id)?.role||'member'}));
   if(args.p_query)items=items.filter(r=>[r.display_name,r.username,r.email,r.user_id,r.institution,r.research].join(' ').toLowerCase().includes(args.p_query.toLowerCase()));
   if(args.p_role)items=items.filter(r=>r.role===args.p_role);
   items.sort((a,b)=>{const x=a[args.p_sort],y=b[args.p_sort];if(x==null)return y==null?0:1;if(y==null)return -1;const compare=typeof x==='number'?x-y:x.localeCompare(y);return args.p_direction==='desc'?-compare:compare;});
   const total=items.length,page=Math.min(args.p_page,Math.max(1,Math.ceil(total/args.p_size)));items=items.slice((page-1)*args.p_size,page*args.p_size);
   if(delayed===args.p_query)await new Promise(r=>setTimeout(r,800));
   return reply({items,total,page,page_size:args.p_size});
  }
  if(conflict)return reply({message:'该用户权限已被修改，请刷新成员列表后重试。',code:'40001'},409);
  f.writes.push({table:name,method:'POST',body:args});const old=f.db.foamlab_roles.find(r=>r.user_id===args.p_user_id);
  if(args.p_role==='member')f.db.foamlab_roles=f.db.foamlab_roles.filter(r=>r.user_id!==args.p_user_id);
  else if(old)old.role=args.p_role;else f.db.foamlab_roles.push({user_id:args.p_user_id,role:args.p_role});
  return reply({user_id:args.p_user_id,role:args.p_role,changed:true});
 });
 return {registered,requests,fail:v=>failure=v,conflict:v=>conflict=v,delay:v=>delayed=v};
}
module.exports={memberRPC};
