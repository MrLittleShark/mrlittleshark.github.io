-- Applied via Supabase migration expand_foamlab_personal_shortcuts.
begin;
alter table public.foamlab_profiles drop constraint foamlab_profiles_shortcuts_check;
alter table public.foamlab_profiles add constraint foamlab_profiles_shortcuts_check
check (shortcuts <@ array['courses','topics','start','commands','dictionaries','algorithms',
 'linux','cpp','programming','tools','resources','recommendations','sharing','authors',
 'community','assignments','announcements']::text[] and cardinality(shortcuts) <= 18);
commit;
