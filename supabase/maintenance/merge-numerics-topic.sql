begin;
do $guard$
begin
 if not exists (select 1 from public.foamlab_sections where id='d8198ea8-e06c-4071-a76e-38e0db38fd23' and key='algorithms' and revision=2) then raise exception 'Numerics section changed'; end if;
 if not exists (select 1 from public.foamlab_sections where id='2d803b45-4d2f-44d0-b07e-568d11c4abc7' and key='topic-finite-volume') then raise exception 'Finite volume section missing'; end if;
 if exists (select 1 from public.foamlab_sections where parent_id='d8198ea8-e06c-4071-a76e-38e0db38fd23') then raise exception 'Numerics has new child sections'; end if;
 if (select count(*) from public.foamlab_content where 'd8198ea8-e06c-4071-a76e-38e0db38fd23'::uuid=any(section_ids))<>12 then raise exception 'Numerics contents changed'; end if;
 if exists (select 1 from jsonb_to_recordset($expected$[{"id":"331dede2-03ea-4678-8657-e331331c52dc","revision":5},{"id":"931a89cf-5f75-4463-b6aa-97a8dda7f97d","revision":2},{"id":"62e39923-d8d4-4d7f-941b-70d9d023166e","revision":2},{"id":"9031703e-9a1f-4602-8d00-d7fea16ba3c1","revision":2},{"id":"f0ae6c98-ff8b-4f09-b104-ff0691413439","revision":2},{"id":"93af7e0e-8c9f-4a51-8ece-d0d193d50081","revision":2},{"id":"50f37a1a-f9ff-4633-9038-89968a5cfff0","revision":6},{"id":"e17d17d6-61d8-46d4-831e-cf2184eb76b2","revision":5},{"id":"7295d720-6652-4f88-99b2-18955264f961","revision":6},{"id":"4c5da7c9-234e-4d76-8341-5f70466c37a4","revision":5},{"id":"d93a798b-233c-4b35-ac1f-9a9ec5971817","revision":5},{"id":"4b0be4e2-752e-47a8-ae89-d3035861cf0b","revision":5}]$expected$::jsonb) as e(id uuid,revision integer) left join public.foamlab_content c on c.id=e.id and c.revision=e.revision where c.id is null) then raise exception 'Content revision changed'; end if;
 if exists (select 1 from public.foamlab_content where 'd8198ea8-e06c-4071-a76e-38e0db38fd23'::uuid=any(section_ids) and kind='lesson' and not ('2d803b45-4d2f-44d0-b07e-568d11c4abc7'::uuid=any(section_ids))) then raise exception 'Lesson missing from finite volume'; end if;
end $guard$;
-- All eleven lessons already belong to finite volume; remove only the duplicate location.
update public.foamlab_content
set section_ids=array_remove(section_ids,'d8198ea8-e06c-4071-a76e-38e0db38fd23'::uuid),
    status=case when slug='topic-algorithms' then 'archived' else status end
where 'd8198ea8-e06c-4071-a76e-38e0db38fd23'::uuid=any(section_ids);
delete from public.foamlab_sections where id='d8198ea8-e06c-4071-a76e-38e0db38fd23';
update public.foamlab_content set body=replace(body,'](/algorithms/)','](/topics/finite-volume/)')
where slug='release-2026-10-rebuild' and body like '%](/algorithms/)%';
commit;
select
 (select count(*) from public.foamlab_sections where key='algorithms') as duplicate_sections,
 (select count(*) from public.foamlab_content where 'd8198ea8-e06c-4071-a76e-38e0db38fd23'::uuid=any(section_ids)) as dangling_locations,
 (select count(*) from public.foamlab_content where kind='lesson' and status='published' and '2d803b45-4d2f-44d0-b07e-568d11c4abc7'::uuid=any(section_ids)) as finite_volume_lessons,
 (select status from public.foamlab_content where slug='topic-algorithms') as old_introduction;
