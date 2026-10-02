begin;
insert into auth.users(id,role,aud,email) values
 ('11000000-0000-4000-8000-000000000001','authenticated','authenticated','author-test@example.invalid'),
 ('11000000-0000-4000-8000-000000000002','authenticated','authenticated','manager-test@example.invalid');
insert into auth.identities(user_id,provider_id,provider,identity_data) values
 ('11000000-0000-4000-8000-000000000001','foamlab-author-check','github','{"sub":"foamlab-author-check"}'),
 ('11000000-0000-4000-8000-000000000002','foamlab-manager-check','github','{"sub":"foamlab-manager-check"}');
insert into public.foamlab_content(id,slug,kind,title,status,author_id) values
 ('21000000-0000-4000-8000-000000000002','permission-other-article','article','Other author','published','11000000-0000-4000-8000-000000000002');
select set_config('request.jwt.claim.sub','11000000-0000-4000-8000-000000000001',true);
set local role authenticated;
insert into public.foamlab_content(id,slug,kind,title,status,published_at) values
 ('21000000-0000-4000-8000-000000000001','permission-own-article','article','Author publication','published','2000-01-01');
do $$ begin
 if (select published_at from public.foamlab_content where slug='permission-own-article')<>now() then raise exception 'Publication timestamp is not server-controlled'; end if;
 update public.foamlab_content set title='Author revision',published_at='2000-01-01' where slug='permission-own-article';
 if (select title from public.foamlab_content where slug='permission-own-article')<>'Author revision' then raise exception 'Own publication cannot be edited';end if;
 if (select published_at from public.foamlab_content where slug='permission-own-article')<>now() then raise exception 'Publication timestamp was overwritten';end if;
 update public.foamlab_content set title='Unauthorized' where slug='permission-other-article';
 if found then raise exception 'Other author publication was edited';end if;
 begin insert into public.foamlab_content(slug,kind,title,status) values('permission-illegal-course','lesson','Invalid course','published');raise exception 'Member created a lesson';exception when insufficient_privilege then null;end;
 begin update public.foamlab_content set metadata='{"admin_only":true}' where slug='permission-own-article';raise exception 'Member created private admin content';exception when insufficient_privilege then null;end;
 begin update public.foamlab_content set metadata='{"canonical_path":"/commands/"}' where slug='permission-own-article';raise exception 'Member assigned a canonical route';exception when insufficient_privilege then null;end;
 begin update public.foamlab_content set author_id='11000000-0000-4000-8000-000000000002' where slug='permission-own-article';raise exception 'Member impersonated an author';exception when insufficient_privilege then null;end;
 begin update public.foamlab_author_levels set level=99 where user_id=auth.uid();raise exception 'Member changed public level';exception when insufficient_privilege then null;end;
 delete from public.foamlab_content where slug='permission-own-article';if found then raise exception 'Member permanently deleted content';end if;
end $$;
reset role;
update public.foamlab_pets set xp=600 where user_id='11000000-0000-4000-8000-000000000001';
set local role anon;
do $$ begin
 if (select level from public.foamlab_author_levels where user_id='11000000-0000-4000-8000-000000000001')<>5 then raise exception 'Public author level not synchronized';end if;
 begin perform xp from public.foamlab_pets;raise exception 'Private experience is public';exception when insufficient_privilege then null;end;
 begin insert into public.foamlab_content(slug,kind,title,status) values('permission-anon','article','Anon article','published');raise exception 'Anonymous publication succeeded';exception when insufficient_privilege then null;end;
end $$;
reset role;
insert into public.foamlab_roles(user_id,role) values('11000000-0000-4000-8000-000000000001','blocked'),('11000000-0000-4000-8000-000000000002','admin');
set local role authenticated;
do $$ begin
 begin insert into public.foamlab_content(slug,kind,title,status) values('permission-blocked','article','Blocked article','published');raise exception 'Blocked member published';exception when insufficient_privilege then null;end;
 update public.foamlab_content set title='Blocked edit' where slug='permission-own-article';if found then raise exception 'Blocked author edited content';end if;
end $$;
reset role;
select set_config('request.jwt.claim.sub','11000000-0000-4000-8000-000000000002',true);
set local role authenticated;
update public.foamlab_content set status='trash' where slug='permission-own-article';
do $$ begin
 delete from public.foamlab_content where slug='permission-own-article';if not found then raise exception 'Admin could not delete trashed article';end if;
end $$;
reset role;
rollback;
select 'PASS: author publish/edit, ownership, blocked users, admin deletion, public level and timestamps; fixtures rolled back' as result;
