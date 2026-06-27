// 论文备注（Supabase）公开配置。
// anon key 与 URL 都是「可公开」的（写权限由数据库 RLS 按邮箱限制，仅你登录后可写），
// 所以直接提交到仓库没有安全问题。
//
// 填好下面三项后，详情页底部的「备注 / 评论」功能即生效；
// 留为 REPLACE_ME 时功能自动休眠（线上不显示、不报错）。

export const SUPABASE_URL = 'REPLACE_ME_SUPABASE_URL';        // 形如 https://xxxx.supabase.co
export const SUPABASE_ANON_KEY = 'REPLACE_ME_SUPABASE_ANON_KEY';
export const ADMIN_EMAIL = 'harleycxying@gmail.com';          // 只有这个邮箱登录后可写

export const NOTES_ENABLED =
  !SUPABASE_URL.startsWith('REPLACE_ME') && !SUPABASE_ANON_KEY.startsWith('REPLACE_ME');
