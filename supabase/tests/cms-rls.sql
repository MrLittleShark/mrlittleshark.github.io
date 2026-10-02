begin;
-- Test identities and content exist only inside this rolled-back transaction.
insert into auth.users(id,role,aud,email) values('10000000-0000-4000-8000-000000000001','authenticated','authenticated','foamlab-test-one@example.invalid'),('10000000-0000-4000-8000-000000000002','authenticated','authenticated','foamlab-test-two@example.invalid');
insert into auth.identities(user_id,provider_id,provider,identity_data) values
('10000000-0000-4000-8000-000000000001','foamlab-rls-one','github','{"sub":"foamlab-rls-one"}'),
('10000000-0000-4000-8000-000000000002','foamlab-rls-two','github','{"sub":"foamlab-rls-two"}');
insert into public.foamlab_content(id,slug,kind,title,body,status,author_id) values
('20000000-0000-4000-8000-000000000001','test-public-rls','lesson','RLS published test','Test body','published','10000000-0000-4000-8000-000000000002'),
('20000000-0000-4000-8000-000000000002','test-draft-rls','lesson','RLS draft test','Private draft','draft','10000000-0000-4000-8000-000000000002');
set local role anon;
do $$ begin
 if (select count(*) from public.foamlab_content where slug like 'test-%-rls')<>1 then raise exception 'Anonymous draft isolation failed'; end if;
 begin insert into public.foamlab_threads(title,body) values('Anon should fail','Anonymous insert test');raise exception 'Anonymous write succeeded';exception when insufficient_privilege then null;end;
end $$;
reset role;
select set_config('request.jwt.claim.sub','10000000-0000-4000-8000-000000000001',true);
set local role authenticated;
do $$ begin
 if (select count(*) from public.foamlab_content where slug='test-draft-rls')<>0 then raise exception 'Other user draft leaked';end if;
 begin insert into public.foamlab_roles(user_id,role) values(auth.uid(),'admin');raise exception 'Self promotion succeeded';exception when insufficient_privilege then null;end;
 insert into public.foamlab_content(slug,kind,title,status) values('test-member-publish','article','Member publication','published');
 begin insert into public.foamlab_content(slug,kind,title,status) values('test-illegal-publish','lesson','Illegal course publish','published');raise exception 'Member course publish succeeded';exception when insufficient_privilege then null;end;
 insert into public.foamlab_content(slug,kind,title,status) values('test-member-draft','article','Member draft','draft');
 insert into public.foamlab_threads(id,title,body) values('30000000-0000-4000-8000-000000000001','Test question title','Reproducible question body');
 begin update public.foamlab_threads set pinned=true where id='30000000-0000-4000-8000-000000000001';raise exception 'Member pin succeeded';exception when raise_exception then if sqlerrm='Member pin succeeded' then raise;end if;end;
 insert into public.foamlab_messages(thread_id,body) values('30000000-0000-4000-8000-000000000001','A public answer');
 insert into public.foamlab_messages(content_id,body) values('20000000-0000-4000-8000-000000000001','A course comment');
 begin insert into public.foamlab_messages(content_id,body) values('20000000-0000-4000-8000-000000000002','Comment on private draft');raise exception 'Private draft comment succeeded';exception when insufficient_privilege then null;end;
end $$;
reset role;
update public.foamlab_content set comments_enabled=false where id='20000000-0000-4000-8000-000000000001';
insert into public.foamlab_roles(user_id,role) values('10000000-0000-4000-8000-000000000002','moderator');
select set_config('request.jwt.claim.sub','10000000-0000-4000-8000-000000000002',true);
set local role authenticated;
update public.foamlab_threads set status='closed',pinned=true where id='30000000-0000-4000-8000-000000000001';
reset role;
select set_config('request.jwt.claim.sub','10000000-0000-4000-8000-000000000001',true);
set local role authenticated;
do $$ begin
 begin insert into public.foamlab_messages(content_id,body) values('20000000-0000-4000-8000-000000000001','Closed comments test');raise exception 'Disabled comments accepted';exception when insufficient_privilege then null;end;
 begin insert into public.foamlab_messages(thread_id,body) values('30000000-0000-4000-8000-000000000001','Closed thread test');raise exception 'Closed topic accepted reply';exception when insufficient_privilege then null;end;
 if (select count(*) from public.foamlab_revisions)>0 then raise exception 'Revision history leaked';end if;
 begin insert into storage.objects(bucket_id,name) values('foamlab-resources','test-member-file');raise exception 'Member upload succeeded';exception when insufficient_privilege then null;end;
end $$;
reset role;
rollback;
select 'RLS assertions passed; all fixture changes rolled back' as result;
