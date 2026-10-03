-- Isolated fixtures; all inserted accounts, roles and audit rows are rolled back.
begin;
select set_config('foamlab.test_prefix','member-test-'||gen_random_uuid()::text,true);
create temporary table member_test_ids as select n,gen_random_uuid() as id from generate_series(0,54) n;
insert into auth.users(id,aud,role,email,created_at,updated_at,raw_user_meta_data,last_sign_in_at)
 select id,'authenticated','authenticated',current_setting('foamlab.test_prefix')||'-'||lpad(n::text,2,'0')||'@example.invalid',
 '2026-01-01'::timestamptz+n*interval '1 day',now(),
 jsonb_build_object('user_name',current_setting('foamlab.test_prefix')||'-'||lpad(n::text,2,'0'),'full_name','Fixture '||n),
 case when n%2=0 then '2026-03-01'::timestamptz+n*interval '1 day' else null end from member_test_ids;
insert into public.foamlab_roles(user_id,role) select id,case n when 0 then 'admin' when 1 then 'editor' when 2 then 'moderator' else 'blocked' end from member_test_ids where n<4;
insert into public.foamlab_pets(user_id,xp) select id,n*(n+1)*25 from member_test_ids where n>0;
select set_config('foamlab.test_admin',(select id::text from member_test_ids where n=0),true),
 set_config('foamlab.test_target',(select id::text from member_test_ids where n=4),true),
 set_config('foamlab.test_other_roles',(select jsonb_agg(id)::text from member_test_ids where n between 1 and 4),true);
set local role anon;
do $$begin
 begin perform public.foamlab_admin_members();raise exception 'anonymous listing allowed';exception when insufficient_privilege then null;end;
 begin perform public.foamlab_admin_set_member_role(current_setting('foamlab.test_target')::uuid,'admin','member');raise exception 'anonymous role update allowed';exception when insufficient_privilege then null;end;
end $$;
set local role authenticated;
do $$declare uid text; r jsonb; a jsonb; b jsonb; prefix text=current_setting('foamlab.test_prefix'); target uuid=current_setting('foamlab.test_target')::uuid; admin_id uuid=current_setting('foamlab.test_admin')::uuid; begin
 for uid in select jsonb_array_elements_text(current_setting('foamlab.test_other_roles')::jsonb) loop
  perform set_config('request.jwt.claims',jsonb_build_object('sub',uid,'role','authenticated')::text,true);
  begin perform public.foamlab_admin_members();raise exception 'non-admin listing allowed';exception when insufficient_privilege then null;end;
  begin perform public.foamlab_admin_set_member_role(target,'admin','member');raise exception 'non-admin role update allowed';exception when insufficient_privilege then null;end;
 end loop;
 perform set_config('request.jwt.claims',jsonb_build_object('sub',admin_id,'role','authenticated')::text,true);
 r=public.foamlab_admin_members(prefix,'','registered_at','asc',1,25);
 if (r->>'total')::int<>55 or jsonb_array_length(r->'items')<>25 or r->'items'->0->>'user_id'<>admin_id::text then raise exception 'registration listing failed';end if;
 if r->'items'->0->>'display_name'<>'Fixture 0' or (r->'items'->0->>'level')::int<>1 then raise exception 'missing profile fallback failed';end if;
 r=public.foamlab_admin_members(prefix,'','registered_at','asc',999,25);
 if (r->>'page')::int<>3 or jsonb_array_length(r->'items')<>5 then raise exception 'page clamping failed';end if;
 r=public.foamlab_admin_members(prefix,'member','registered_at','desc',1,100);
 if (r->>'total')::int<>51 then raise exception 'member filtering failed';end if;
 r=public.foamlab_admin_members(upper(prefix)||'-04','','username','asc',1,25);
 if (r->>'total')::int<>1 or r->'items'->0->>'user_id'<>target::text then raise exception 'username search failed';end if;
 r=public.foamlab_admin_members(prefix,'','level','desc',1,25);
 if (r->'items'->0->>'level')::int<>55 then raise exception 'numeric level sort failed';end if;
 r=public.foamlab_admin_members(prefix,'','username','desc',1,25);
 if r->'items'->0->>'username'<>prefix||'-54' then raise exception 'username sort failed';end if;
 r=public.foamlab_admin_members(prefix,'','last_sign_in_at','asc',1,100);
 if r->'items'->0->>'user_id'<>admin_id::text or r->'items'->54->>'last_sign_in_at' is not null then raise exception 'last login null ordering failed';end if;
 r=public.foamlab_admin_members(prefix||'-missing','','registered_at','desc',3,25);
 if (r->>'page')::int<>1 or (r->>'total')::int<>0 or r->'items'<>'[]'::jsonb then raise exception 'empty result failed';end if;
 begin perform public.foamlab_admin_members(prefix,'','unexpected','desc',1,25);raise exception 'invalid sort accepted';exception when invalid_parameter_value then null;end;
 begin perform public.foamlab_admin_set_member_role(admin_id,'member','admin');raise exception 'self demotion allowed';exception when insufficient_privilege then null;end;
 begin perform public.foamlab_admin_set_member_role(target,'admin','editor');raise exception 'stale expected role accepted';exception when serialization_failure then null;end;
 begin perform public.foamlab_admin_set_member_role(target,'root','member');raise exception 'invalid role accepted';exception when invalid_parameter_value then null;end;
 begin perform public.foamlab_admin_set_member_role('00000000-0000-0000-0000-000000000000','admin','member');raise exception 'nonexistent user accepted';exception when invalid_parameter_value then null;end;
 begin update public.foamlab_roles set role='member' where user_id=admin_id;raise exception 'direct role mutation allowed';exception when insufficient_privilege then null;end;
 a=public.foamlab_admin_set_member_role(target,'admin','member');
 r=public.foamlab_admin_members(target::text,'admin','registered_at','desc',1,25);
 if (r->>'total')::int<>1 or not (a->>'changed')::boolean then raise exception 'promote to admin failed';end if;
 a=public.foamlab_admin_set_member_role(target,'admin','admin');
 if (a->>'changed')::boolean then raise exception 'no-op role change failed';end if;
 a=public.foamlab_admin_set_member_role(target,'editor','admin');
 a=public.foamlab_admin_set_member_role(target,'moderator','editor');
 a=public.foamlab_admin_set_member_role(target,'blocked','moderator');
 a=public.foamlab_admin_set_member_role(target,'member','blocked');
 r=public.foamlab_admin_members(target::text,'member','registered_at','desc',1,25);
 if (r->>'total')::int<>1 then raise exception 'restore member failed';end if;
end $$;
reset role;
do $$begin
 if (select count(*) from foamlab_private.member_role_history where actor_id=current_setting('foamlab.test_admin')::uuid)<>5 then raise exception 'audit history failed';end if;
end $$;
rollback;
select 'PASS: registered users, all roles, search, sorting, paging, missing profiles, confirmation conflict, self protection, audit; fixtures rolled back' as result;
