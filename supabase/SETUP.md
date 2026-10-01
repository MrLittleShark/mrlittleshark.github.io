# GitHub 登录与个人资料同步

网站继续由 Hexo 生成并发布至 GitHub Pages。Supabase 负责身份验证与个人数据存储，GitHub Issues 负责公开作业和答疑。

当前项目：`foamlab-openfoam-learning`，项目引用 `nmkforbzmbstasnjxlid`，组织 `MrLittleShark's Org`，区域 Singapore。数据库结构、RLS 策略及公开前端密钥已配置。当前创建工具返回项目费用为 0 / 月；后续套餐调整以 Supabase 后台为准。

当前项目的 GitHub Callback URL：`https://nmkforbzmbstasnjxlid.supabase.co/auth/v1/callback`。设置入口：[GitHub OAuth App](https://github.com/settings/applications/new)、[Supabase Providers](https://supabase.com/dashboard/project/nmkforbzmbstasnjxlid/auth/providers)、[URL Configuration](https://supabase.com/dashboard/project/nmkforbzmbstasnjxlid/auth/url-configuration)。

1. 在自己的 Supabase 组织中创建项目，确认该组织的套餐与费用。
2. 在 SQL Editor 执行 `schema.sql`。两张表均启用 RLS，只允许已认证用户读取、写入自己的记录。
3. 在 GitHub 的 Settings → Developer settings → OAuth Apps 创建应用。Homepage URL 为 `https://mrlittleshark.github.io`，Authorization callback URL 使用 Supabase GitHub provider 页面提供的 `https://项目引用.supabase.co/auth/v1/callback`。
4. 在 Supabase Authentication → Sign In / Providers → GitHub 启用提供商，填写该 OAuth App 的 Client ID 与 Client Secret。Secret 只保存到 Supabase 后台，不写入网站文件或聊天。
5. 在 Authentication → URL Configuration 设置 Site URL 为 `https://mrlittleshark.github.io`，Redirect URLs 添加 `https://mrlittleshark.github.io/account/`。本机调试时可再添加 `http://localhost:4173/account/`；生产环境无需保留调试地址。
6. 将项目 URL 与 **publishable key** 写入 `source-openfoam/assets/auth-config.json`。只使用可公开的 publishable / anon key，不能使用 secret 或 service_role key。
7. 执行 Hexo generate 和 deploy。用 GitHub 登录，编辑资料并保存；在另一浏览器登录同一账号核对资料与进度。再用第二个账号确认不能读取第一个账号的记录。

访客记录保存在 `foamlab.completed`。登录后不会自动将共享电脑上的访客记录写入个人账号，需要在个人中心明确点击“导入本机学习记录”。

个人资料不会赋予教师权限。教师发布记录的识别由课堂配置的可信 GitHub 用户名单决定，仓库管理权限由 GitHub 控制。

官方文档：[GitHub OAuth](https://supabase.com/docs/guides/auth/social-login/auth-github)、[Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security)。
