-- Publish after /function-objects/ is deployed.
begin;
update public.foamlab_sections
set name = '配置与字典速查'
where key = 'dictionaries' and name = '配置与字典' and revision = 1;

insert into public.foamlab_sections
  (key, name, parent_id, href, description, nav_group, visible, sort_order)
values
  ('function-objects', 'functionObject 速查', null, '/function-objects/',
   '按名称、用途与参数查找功能对象。', '学习空间', true, 365)
on conflict (key) do nothing;
commit;

select key, name, href, visible, sort_order, revision
from public.foamlab_sections
where key in ('dictionaries', 'function-objects');
