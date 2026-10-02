-- Run against the project with execute_sql. Every fixture is rolled back.
begin;
insert into auth.users(id,role,aud,email) values
 ('20000000-0000-4000-8000-000000000001','authenticated','authenticated','panda-a@example.invalid'),
 ('20000000-0000-4000-8000-000000000002','authenticated','authenticated','panda-b@example.invalid');
insert into auth.identities(user_id,provider_id,provider,identity_data) values
 ('20000000-0000-4000-8000-000000000001','panda-test-a','github','{"sub":"panda-test-a"}'),
 ('20000000-0000-4000-8000-000000000002','panda-test-b','github','{"sub":"panda-test-b"}');
insert into public.foamlab_content(id,slug,kind,title,status,author_id) values
 ('20000000-0000-4000-8000-000000000011','panda-test-lesson','lesson','宠物测试课程','published','20000000-0000-4000-8000-000000000002'),
 ('20000000-0000-4000-8000-000000000012','panda-test-article','article','宠物测试文章','published','20000000-0000-4000-8000-000000000002'),
 ('20000000-0000-4000-8000-000000000013','panda-test-draft','article','宠物投稿测试','draft','20000000-0000-4000-8000-000000000001');
insert into public.foamlab_threads(id,author_id,title,body) values
 ('20000000-0000-4000-8000-000000000021','20000000-0000-4000-8000-000000000002','一个有效的测试讨论','讨论网格设置与求解方法的详细内容。');
select set_config('request.jwt.claim.sub','20000000-0000-4000-8000-000000000001',true);
set local role authenticated;
do $$
declare s jsonb; rejected boolean; i integer;
begin
 s:=public.foamlab_pet(); assert (s->'pet'->>'xp')::integer=0,'Initial XP';
 assert s->'pet'->>'decoration'='no-decor','Default scene';
 assert jsonb_array_length(s->'items')=42,'Catalog';
 s:=public.foamlab_pet('equip','{"id":"crawl"}');assert s->'pet'->>'action'='crawl','Crawl at level one';
 s:=public.foamlab_pet('equip','{"id":"sing"}');assert s->'pet'->>'action'='sing','Singing at level one';
 rejected:=false;begin perform public.foamlab_pet('equip','{"id":"spin"}');exception when raise_exception then rejected:=true;end;assert rejected,'Locked dance';
 rejected:=false;begin perform public.foamlab_pet('equip','{"id":"pond"}');exception when raise_exception then rejected:=true;end;assert rejected,'Locked decoration';
 rejected:=false;begin perform public.foamlab_pet('equip','{"id":"astronaut"}');exception when raise_exception then rejected:=true;end;assert rejected,'Locked evolution';
 s:=public.foamlab_pet('checkin'); assert (s->>'awarded')::integer=10,'First check-in';
 s:=public.foamlab_pet('checkin'); assert (s->>'awarded')::integer=0 and (s->'pet'->>'xp')::integer=10,'Duplicate check-in';
 rejected:=false;begin update public.foamlab_pets set xp=999999 where user_id=auth.uid();exception when insufficient_privilege then rejected:=true;end;assert rejected,'Client forged XP';
 rejected:=false;begin perform foamlab_private.pet_award(auth.uid(),'topic','forged',999,0);exception when insufficient_privilege then rejected:=true;end;assert rejected,'Client called internal award';
 rejected:=false;begin perform public.foamlab_pet('equip','{"id":"cap"}');exception when raise_exception then rejected:=true;end;assert rejected,'Locked outfit';
 assert (select count(*) from public.foamlab_pets where user_id<>'20000000-0000-4000-8000-000000000001')=0,'Cross-account pet read';
 assert (select count(*) from public.foamlab_pet_events where user_id<>'20000000-0000-4000-8000-000000000001')=0,'Cross-account ledger read';
 insert into public.foamlab_learning_progress(user_id,content_id) values(auth.uid(),'20000000-0000-4000-8000-000000000011');
 update public.foamlab_learning_progress set completed=false where user_id=auth.uid();
 update public.foamlab_learning_progress set completed=true where user_id=auth.uid();
 s:=public.foamlab_pet();assert (s->'pet'->>'xp')::integer=35,'Course completion idempotency';
 delete from public.foamlab_learning_progress where user_id=auth.uid();
 insert into public.foamlab_learning_progress(user_id,content_id) values(auth.uid(),'20000000-0000-4000-8000-000000000011');
 s:=public.foamlab_pet();assert (s->'pet'->>'xp')::integer=35,'Course delete/recreate';
 for i in 1..4 loop
  insert into public.foamlab_threads(author_id,title,body) values(auth.uid(),'测试讨论主题编号'||i,'这是有关网格和边界条件的测试问题编号'||i);
 end loop;
 s:=public.foamlab_pet();assert (s->'pet'->>'xp')::integer=80,'Topic daily cap';
 for i in 1..7 loop
  insert into public.foamlab_messages(thread_id,author_id,body) values('20000000-0000-4000-8000-000000000021',auth.uid(),'这是包含足够文字的有效技术回答编号'||i);
 end loop;
 s:=public.foamlab_pet();assert (s->'pet'->>'xp')::integer=110,'Reply daily cap';
 insert into public.foamlab_messages(content_id,author_id,body) values('20000000-0000-4000-8000-000000000012',auth.uid(),'一条用于测试重复内容的完整文章评论。');
 insert into public.foamlab_messages(content_id,author_id,body) values('20000000-0000-4000-8000-000000000012',auth.uid(),'一条用于测试重复内容的完整文章评论。');
 s:=public.foamlab_pet();assert (s->'pet'->>'xp')::integer=113,'Duplicate content';
 for i in 1..5 loop
  insert into public.foamlab_messages(content_id,author_id,body) values('20000000-0000-4000-8000-000000000012',auth.uid(),'这也是足够长度的文章评论编号'||i);
 end loop;
 s:=public.foamlab_pet();assert (s->'pet'->>'xp')::integer=125,'Comment daily cap';
 s:=public.foamlab_pet('equip','{"id":"scarf"}');assert s->'pet'->>'outfit'='scarf','Unlocked outfit';
 s:=public.foamlab_pet('settings','{"name":"泡泡测试","motion":false,"visible":false,"xp":9999,"user_id":"20000000-0000-4000-8000-000000000002"}');
 assert s->'pet'->>'name'='泡泡测试' and (s->'pet'->>'xp')::integer=125,'Settings cannot set XP or owner';
 assert not (s->'pet'->>'visible')::boolean,'Visibility';
end $$;
reset role;
update public.foamlab_content set status='published' where slug='panda-test-draft';
set local role authenticated;
do $$declare s jsonb;begin s:=public.foamlab_pet();assert (s->'pet'->>'xp')::integer=155 and (s->>'level')::integer=3,'Approved article award and level';end $$;
reset role;
insert into public.foamlab_roles(user_id,role) values('20000000-0000-4000-8000-000000000002','moderator');
select set_config('request.jwt.claim.sub','20000000-0000-4000-8000-000000000002',true);
update public.foamlab_threads set status='hidden' where id='20000000-0000-4000-8000-000000000021';
select set_config('request.jwt.claim.sub','20000000-0000-4000-8000-000000000001',true);
set local role authenticated;
do $$declare s jsonb;begin s:=public.foamlab_pet();assert (s->'pet'->>'xp')::integer=125,'Moderation retracts replies';end $$;
reset role;
-- Test every cosmetic through the same authenticated RPC, then return to level 2.
update public.foamlab_pets set xp=7650 where user_id='20000000-0000-4000-8000-000000000001';
set local role authenticated;
do $$declare s jsonb; entry jsonb; rejected boolean:=false;begin
 s:=public.foamlab_pet();assert (s->>'level')::integer=18,'Level 18 threshold';
 for entry in select jsonb_array_elements(s->'items') loop
  s:=public.foamlab_pet('equip',jsonb_build_object('id',entry->>'id'));
  assert s->'pet'->>(entry->>'category')=entry->>'id','Equipment category saved';
 end loop;
 begin update public.foamlab_pets set decoration='pond' where user_id=auth.uid();exception when insufficient_privilege then rejected:=true;end;assert rejected,'Direct decoration write';
end $$;
reset role;
update public.foamlab_pets set xp=125,form='astronaut',outfit='spacesuit',action='experiment',decoration='observatory' where user_id='20000000-0000-4000-8000-000000000001';
set local role authenticated;
do $$declare s jsonb;begin s:=public.foamlab_pet();assert s->'pet'->>'form'='cub' and s->'pet'->>'outfit'='none' and s->'pet'->>'action'='wave' and s->'pet'->>'decoration'='no-decor','Equipment follows reduced level';end $$;
reset role;
insert into public.foamlab_roles(user_id,role) values('20000000-0000-4000-8000-000000000001','blocked');
set local role authenticated;
do $$declare rejected boolean:=false;begin begin perform public.foamlab_pet();exception when insufficient_privilege then rejected:=true;end;assert rejected,'Blocked user';end $$;
reset role;
set local role anon;
do $$declare rejected boolean:=false;begin begin perform public.foamlab_pet();exception when insufficient_privilege then rejected:=true;end;assert rejected,'Anonymous RPC';end $$;
reset role;
rollback;
select 'Panda XP, caps, idempotency, equip, settings, moderation, RLS and auth tests passed; fixtures rolled back.' as result;
