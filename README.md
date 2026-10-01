# FoamLab OpenFOAM v2512 学习站

网站：<https://mrlittleshark.github.io/>

本地工程使用 Hexo 8.1.2，主题为 `themes/foam-lab`。课程内容面向 OpenCFD / openfoam.com 分支的 v2512。原博客文章已移出内容目录，并在 `.openfoam-backup/2026-10-01/` 保留备份。

## 本地预览

Windows 下双击 `启动学习网站.cmd`，然后打开 <http://localhost:4173>。关闭终端或按 Ctrl+C 停止预览。

已安装 Node.js 20.19 或更高版本时，也可以在工程目录执行：

```powershell
npm ci
npm run build
npm run preview
```

本次环境已更新本地依赖。若终端没有 npm，可用已有的 Node.js 直接执行：

```powershell
node node_modules/hexo/bin/hexo generate
node tools/serve.mjs
```

## 使用 Hexo 发布

双击 `发布学习网站.cmd`，或执行：

```powershell
node node_modules/hexo/bin/hexo generate
node node_modules/hexo/bin/hexo deploy
```

`_config.yml` 配置 `git-safe` 扩展和 `foamlab-source` 源文件分支。发布程序先同步远程网页修改，执行 Hexo 构建，再推送源文件；GitHub Actions 重新校验并部署网站。GitHub Pages 设置使用 **GitHub Actions**。不执行强制推送。

专用源文件工作副本为 `.source_foamlab`，同步基线为 `.openfoam-work/source-sync.json`。网页和本地同时修改同一文件时会停止并列出冲突，不会自动覆盖。合并冲突时可对照本地文件和 `.source_foamlab` 中的远程文件；保存合并结果后先将该文件的原远程内容作为同步基线，再发布。不要删除基线来绕过冲突。仅需采用远程版本时，先备份本地修改，再将工作副本对应文件复制到本地同一路径，重新发布。

发布使用当前用户已有的 Git 凭据，令牌不写入源代码。构建产物为 `public-openfoam`。原 `.deploy_foamlab` 保留静态部署历史，不作为日常内容主稿。

## 管理平台、作业与公告

管理入口：https://mrlittleshark.github.io/admin/ 。公开课堂页面只保留学生使用的查看、提交与答疑功能。

1. 使用 **MrLittleShark** GitHub 账号点击管理授权，首次授权接受公开仓库访问权限。
2. 在“发布作业 / 公告”编辑内容，可选 28 讲练习模板，核对后发布。
3. 在“已发布记录”修改或关闭记录。学生在对应提交的评论区接收反馈。
4. 在“课程内容维护”选择页面、载入当前版本、修改并保存，随后在“发布状态与维护”确认构建成功。

管理服务 `supabase/functions/foamlab-admin/index.ts` 向 Supabase 核验会话，向 GitHub 核验真实账号 ID、关联身份和公开仓库权限。仅仓库所有者账号 ID `112299157` 有管理权限。普通个人资料不能改变权限。修改管理服务后需要另行部署该 Edge Function；Hexo 发布仅更新网站前端与内容。

课堂记录保存在公开 GitHub Issues，标题前缀为 `[作业发布]`、`[作业提交]`、`[公告]`、`[提问]`。作业与公告只展示配置的可信教师记录。关闭作业不等于禁止 GitHub 上的逾期提交；截止日期和评分由教师管理。学生提交、附件上传与答疑需要 GitHub 账号。

完整操作说明见 [网站维护手册](source-openfoam/maintenance/index.md)，线上入口 https://mrlittleshark.github.io/maintenance/ 。

## 个人中心与认证

个人中心使用 Supabase Auth 的 GitHub OAuth，资料与学习进度存储于启用行级访问控制的数据库。认证尚未配置时，页面明确显示服务未启用，不提供模拟登录。配置步骤见 [认证服务配置](supabase/SETUP.md)，数据库结构与策略见 `supabase/schema.sql`。

当前项目 `foamlab-openfoam-learning` 已完成数据库配置，GitHub 提供商已启用。已在实际线上页面验证登录跳转及 PKCE 回调地址，数据库隔离测试通过。首次个人 GitHub 授权由账号本人完成；自动化检查不代替个人授权。个人中心提供资料编辑、常用入口选择、进度同步，以及“我的作业提交”和“我的提问”入口。

## 内容维护

| 位置 | 用途 |
| --- | --- |
| `source-openfoam/lessons/01` 至 `28` | 在线课程正文 |
| `source-openfoam/start` | 初学者快速开始 |
| `source-openfoam/bubble` | 电极气泡专题 |
| `source-openfoam/reference` | 37 个参考手册章节 |
| `source-openfoam/_data/learning.json` | 学习路径与目录数据 |
| `scripts/search-content.js` | 从当前正文自动生成全文搜索索引 |
| `source-openfoam/assets/commands.json` | 242 条命令记录 |
| `source-openfoam/assets/dictionaries.json` | 53 项配置文件、关键字和关联命令 |
| `source-openfoam/dictionaries` | 配置文件独立说明页 |
| `source-openfoam/account` | 个人中心入口 |
| `source-openfoam/downloads` | 原始参考文档、学生讲义和算例包 |
| `themes/foam-lab/source/assets` | 样式、搜索和课堂交互 |
| `.github/ISSUE_TEMPLATE` | GitHub 原生提问、提交与发布表单 |

`tools/build-content.py` 从所提供的四份 Word 资料和本地 28 讲学生版讲义重新导入内容。它会覆盖生成的课程、参考页面和索引；修改课程内容前应明确以 Word 还是网站源文件为维护主稿。脚本中的原始资料路径可按需要调整。

算例包来自已有课程的“代码”目录，排除常规结果时间目录、日志和编译产物，保留原始目录结构。解压后先查看 README 与运行脚本。课程资料中的环境路径需改为学习者自己的路径；本站构建验证不代表算例已在当前环境重新计算。

## 验证

```powershell
python tools/check-site.py
node tools/check-browser.cjs
```

浏览器检查需先启动本地预览，并有 Playwright 与 Edge 可用；`check-browser.cjs` 中的 Playwright 路径对应本次 Windows 环境，可按实际安装位置修改。检查涵盖本地链接、文档与压缩包、全文搜索、命令筛选、学习进度、教师记录过滤、提交跳转、API 故障状态与手机布局。课堂写入通过隔离的浏览器测试数据验证，不向真实仓库发布测试作业或提问。

官方版本资料：<https://www.openfoam.com/news/main-news/openfoam-v2512>。前端采用响应式布局、语义化 HTML、原生对话框和渐进增强，参考 Tailwind 的移动端布局与 Radix 的键盘可访问性设计原则；运行时无需外部字体或前端 CDN。

## TeX、代码与主题

公式使用 TeX 定界符，推荐 `\(...\)` 和 `\[...\]`；也支持 `$...$` 和 `$$...$$`。`lib/presentation.cjs` 在 Hexo 构建时使用本地 KaTeX 渲染。不能解析的公式会中止发布。导入的原始科学公式由 `tools/tex_content.py` 转换；执行代码不参与转换。

围栏代码块标注 `bash`、`openfoam`、`cpp`、`python` 等语言。已有 HTML 代码块自动识别语言，页面提供语法高亮、行数、复制与自动换行。公式、代码及样式资源在本站托管。

顶栏按钮依次切换亮色、暗色、跟随系统；选择保存在当前浏览器，首次加载跟随系统。外观样式在 `themes/foam-lab/source/assets/presentation.css`，逻辑在 `appearance.js`。

首页官方图片原文件与来源说明位于 `source-openfoam/assets/official`。不代表 OpenFOAM 官方认可本站内容。

新增检查：`node tools/check-tex.cjs`、`node tools/check-admin.cjs`、`node tools/check-presentation.cjs`。管理员写入检查使用隔离数据；不向真实课堂发送测试内容。
