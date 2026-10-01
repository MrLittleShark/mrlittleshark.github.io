begin;
insert into auth.users(id,role,aud,email,raw_user_meta_data) values
('10000000-0000-4000-8000-000000000003','authenticated','authenticated','foamlab-test-email@example.invalid','{"provider":"github","user_name":"MrLittleShark"}');
insert into auth.identities(user_id,provider_id,provider,identity_data) values
('10000000-0000-4000-8000-000000000003','foamlab-email-test','email','{"sub":"foamlab-email-test"}');
select set_config('request.jwt.claim.sub','10000000-0000-4000-8000-000000000003',true);
set local role authenticated;
do $$ begin
 if foamlab_private.has_github_identity() then raise exception 'Editable metadata forged a GitHub identity';end if;
 begin insert into public.foamlab_threads(title,body) values('Email-only account','This must be rejected');raise exception 'Email-only discussion succeeded';exception when insufficient_privilege then null;end;
 begin insert into public.foamlab_content(slug,kind,title,status) values('email-only-test-draft','article','Email-only draft','draft');raise exception 'Email-only draft succeeded';exception when insufficient_privilege then null;end;
end $$;
reset role;
rollback;
select 'GitHub identity requirements passed; fixtures rolled back' as result;
