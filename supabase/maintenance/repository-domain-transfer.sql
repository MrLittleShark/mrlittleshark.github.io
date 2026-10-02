-- Prepared for the transfer to foamlabshark/foamlabshark.github.io.
-- Local synchronization does not execute this file.
-- Review in Supabase SQL Editor, then run when updating online content.
-- Only existing site/repository URLs in four known records are replaced.
-- Existing revision triggers preserve the previous record; reruns are safe.

begin;

with candidates as (
  select id, revision, slug,
    jsonb_build_object('body', body, 'metadata', metadata, 'cover_url', cover_url)::text as original
  from public.foamlab_content
  where slug in ('practice-cavity', 'practice-mesh', 'practice-programming', 'site-maintenance')
), prepared as (
  select id, revision, slug,
    regexp_replace(
      regexp_replace(original, 'mrlittleshark(/|%2F)mrlittleshark\.github\.io',
        'foamlabshark\1foamlabshark.github.io', 'gi'),
      'mrlittleshark\.github\.io', 'foamlabshark.github.io', 'gi'
    )::jsonb as updated
  from candidates
  where original ~* 'mrlittleshark\.github\.io'
)
update public.foamlab_content c
set body = p.updated->>'body',
    metadata = p.updated->'metadata',
    cover_url = p.updated->>'cover_url'
from prepared p
where c.id = p.id and c.revision = p.revision
returning c.slug, c.revision;

commit;
