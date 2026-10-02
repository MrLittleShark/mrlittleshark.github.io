begin;
insert into auth.users(id,role,aud,email) values
 ('31000000-0000-4000-8000-000000000001','authenticated','authenticated','tree-manager@example.invalid'),
 ('31000000-0000-4000-8000-000000000002','authenticated','authenticated','tree-author@example.invalid');
insert into auth.identities(user_id,provider_id,provider,identity_data) values
 ('31000000-0000-4000-8000-000000000001','tree-manager','github','{"sub":"tree-manager"}'),
 ('31000000-0000-4000-8000-000000000002','tree-author','github','{"sub":"tree-author"}');
insert into public.foamlab_roles(user_id,role) values('31000000-0000-4000-8000-000000000001','admin');
select set_config('request.jwt.claim.sub','31000000-0000-4000-8000-000000000001',true);
set local role authenticated;
insert into public.foamlab_sections(id,key,name) values('41000000-0000-4000-8000-000000000001','tree-test-root','测试模块');
insert into public.foamlab_sections(id,key,name,parent_id) values('41000000-0000-4000-8000-000000000002','tree-test-child','测试子模块','41000000-0000-4000-8000-000000000001');
insert into public.foamlab_content(id,slug,kind,title,status,body,metadata,section_ids) values
 ('51000000-0000-4000-8000-000000000001','tree-test-article','article','多位置文章','published','原始正文','{"downloads":[{"url":"/downloads/test.zip"}]}',array['41000000-0000-4000-8000-000000000002'::uuid,(select id from public.foamlab_sections where key='sharing')]);
do $$ begin
 begin
  update public.foamlab_sections set parent_id='41000000-0000-4000-8000-000000000002' where id='41000000-0000-4000-8000-000000000001';
  raise exception 'FAIL: cycle allowed';
 exception when raise_exception then if sqlerrm like 'FAIL:%' then raise; end if; end;
 begin
  update public.foamlab_content set section_ids=array['99999999-9999-4999-8999-999999999999'::uuid] where slug='tree-test-article';
  raise exception 'FAIL: nonexistent location allowed';
 exception when raise_exception then if sqlerrm like 'FAIL:%' then raise; end if; end;
 begin
  delete from public.foamlab_sections where key='tree-test-child';
  raise exception 'FAIL: raw deletion left dangling locations';
 exception when raise_exception then if sqlerrm like 'FAIL:%' then raise; end if; end;
 begin
  perform public.foamlab_delete_section('41000000-0000-4000-8000-000000000001',99);
  raise exception 'FAIL: stale revision deleted directory';
 exception when raise_exception then if sqlerrm like 'FAIL:%' then raise; end if; end;
end $$;
select public.foamlab_delete_section('41000000-0000-4000-8000-000000000001',1);
do $$ begin
 if exists(select 1 from public.foamlab_sections where key like 'tree-test-%') then raise exception 'Subtree not deleted'; end if;
 if not exists(select 1 from public.foamlab_content where slug='tree-test-article' and cardinality(section_ids)=1 and body='原始正文' and metadata->'downloads' is not null and status='published') then raise exception 'Article, attachment or alternate placement lost'; end if;
end $$;
reset role;
select set_config('request.jwt.claim.sub','31000000-0000-4000-8000-000000000002',true);
set local role authenticated;
insert into public.foamlab_content(slug,kind,title,status) values('tree-member-article','article','会员文章','published');
do $$ begin
 if not exists(select 1 from public.foamlab_content c join public.foamlab_sections s on s.id=any(c.section_ids) where c.slug='tree-member-article' and s.key='sharing') then raise exception 'Member default placement missing'; end if;
 begin insert into public.foamlab_sections(name) values('未授权目录');raise exception 'FAIL: member created directory';exception when insufficient_privilege then null;end;
 begin update public.foamlab_content set section_ids='{}' where slug='tree-member-article';raise exception 'FAIL: member moved article';exception when raise_exception then if sqlerrm like 'FAIL:%' then raise;end if;end;
 begin perform public.foamlab_delete_section((select id from public.foamlab_sections where key='courses'),1);raise exception 'FAIL: member removed directory';exception when raise_exception then if sqlerrm like 'FAIL:%' then raise;end if;end;
 update public.foamlab_content set title='会员可修改正文' where slug='tree-member-article';
end $$;
reset role;
set local role anon;
do $$ begin
 if not exists(select 1 from public.foamlab_sections where key='courses') then raise exception 'Public navigation unreadable';end if;
 if not exists(select 1 from public.foamlab_content where slug='tree-member-article') then raise exception 'Published member article unreadable';end if;
 begin insert into public.foamlab_sections(name) values('匿名写入');raise exception 'FAIL: anonymous mutation';exception when insufficient_privilege then null;end;
end $$;
reset role;
rollback;
select 'PASS: nested CRUD, cycles, atomic subtree deletion, alternate locations, article preservation, stale revision and RLS; rolled back' result;
