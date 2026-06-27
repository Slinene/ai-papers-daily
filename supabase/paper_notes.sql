-- ============================================================
-- paper_notes: 论文沉淀「人工备注 / 评论」存储
-- 读：所有人可读；写：仅管理员邮箱（你自己）可 insert/update/delete
-- 在 Supabase Dashboard → SQL Editor 里整段执行一次即可
-- ============================================================

create table if not exists public.paper_notes (
  slug       text primary key,          -- = Astro paper.slug，形如 "gen-rec/tokenminds-..."（全站唯一）
  topic      text,
  title      text,
  body       text not null default '',
  updated_at timestamptz not null default now()
);

alter table public.paper_notes enable row level security;

-- 公开读
drop policy if exists "public read" on public.paper_notes;
create policy "public read" on public.paper_notes
  for select using (true);

-- 仅管理员写（把邮箱换成你的；anon key 公开无妨，写操作必须带你登录后的 JWT 才放行）
drop policy if exists "admin insert" on public.paper_notes;
create policy "admin insert" on public.paper_notes
  for insert with check ((auth.jwt() ->> 'email') = 'harleycxying@gmail.com');

drop policy if exists "admin update" on public.paper_notes;
create policy "admin update" on public.paper_notes
  for update using ((auth.jwt() ->> 'email') = 'harleycxying@gmail.com')
            with check ((auth.jwt() ->> 'email') = 'harleycxying@gmail.com');

drop policy if exists "admin delete" on public.paper_notes;
create policy "admin delete" on public.paper_notes
  for delete using ((auth.jwt() ->> 'email') = 'harleycxying@gmail.com');

-- 开启 Realtime（多端实时同步）
alter publication supabase_realtime add table public.paper_notes;

-- 自动维护 updated_at
create or replace function public.touch_paper_notes() returns trigger as $$
begin new.updated_at = now(); return new; end;
$$ language plpgsql;

drop trigger if exists trg_touch_paper_notes on public.paper_notes;
create trigger trg_touch_paper_notes before update on public.paper_notes
  for each row execute function public.touch_paper_notes();
