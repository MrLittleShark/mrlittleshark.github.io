begin;
do $guard$
begin
 if not exists (select 1 from public.foamlab_sections where key='start' and id='23d52459-166d-45e2-add5-02a1a162bbc3' and parent_id is null) then raise exception 'Quick-start directory changed'; end if;
 if not exists (select 1 from public.foamlab_sections where key='resource' and id='2afc879c-9111-4a48-9df2-04f773463f5b' and revision=1) then raise exception 'Resource directory changed'; end if;
 if not exists (select 1 from public.foamlab_content where slug='site-start' and revision=3 and section_ids=array['e6678588-d338-4310-9724-b2f97acf1d5b'::uuid]) then raise exception 'Quick-start content changed'; end if;
end $guard$;
update public.foamlab_content
set section_ids=array['23d52459-166d-45e2-add5-02a1a162bbc3'::uuid],track='入门指南',series='快速开始',
    summary='用方腔算例练习环境加载、网格生成、求解与结果查看。'
where slug='site-start';
update public.foamlab_sections set name='算例与源码' where id='2afc879c-9111-4a48-9df2-04f773463f5b';
commit;
select c.slug,c.section_ids,s.name,s.parent_id from public.foamlab_content c join public.foamlab_sections s on s.id=any(c.section_ids) where c.slug='site-start';
select key,name,revision from public.foamlab_sections where key='resource';
