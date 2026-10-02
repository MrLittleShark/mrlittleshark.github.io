# FoamLab · OpenFOAM v2512 学习社区

网站：<https://foamlabshark.github.io/>。本地工程：`E:\Hexo`。

本站使用 **OpenFOAM v2512**，由 Hexo 8.1.2 和 `themes/foam-lab` 主题生成，部署到 GitHub Pages。Supabase 提供 GitHub 登录、内容管理、讨论、评论、附件和跨设备学习记录。

## 内容范围

仓库已转移至 [foamlabshark/foamlabshark.github.io](https://github.com/foamlabshark/foamlabshark.github.io)。本地发布仓库与源码同步工具均使用该地址，源码分支仍为 foamlab-source。日常发布继续使用“发布学习网站.cmd”。

已有 Supabase 项目的域名配置见 [域名迁移说明](supabase/SETUP.md)。在线内容库中的 3 篇作业和维护手册已通过 [内容链接更新 SQL](supabase/maintenance/repository-domain-transfer.sql) 同步新地址。数据库内容、登录返回地址及历史 Edge Function 的部署分别管理，不会随 Hexo 配置自动更新。

以下数量为本次重构的初始内容清单；后台增删后，线上目录以实际已发布记录为准。

| 内容 | 初始规模与范围 |
| --- | --- |
| 课程单元 | 72 个：30 个 OpenFOAM 基础与应用、20 个 OpenFOAM 编程、10 个 C++ 入门、8 个 Linux 入门、4 个数值理论单元 |
| 命令目录 | 443 条，区分核心求解器、核心工具、官方脚本、shell 函数、构建辅助与 Linux 配套命令 |
| 配置参考 | 111 项配置字典、场文件、函数对象与编译配置，附 288 份完整的 v2512 官方教程文件 |
| 主题参考 | 37 个重新审校的参考章节，保留通用内容并修正版本差异 |
| 扩展工具 | ParaView、Gmsh、SALOME、PyVista、PyFoam、FreeCAD 等 6 篇使用说明 |
| 分类推荐 | 15 项，分官方文档、教程与课程、源码与开发、几何网格、可视化与数据、学术社区 |
| 实践与分享 | 公开作业、资料包、作者日志、文章投稿、站内讨论与评论 |

443 条目录不等于 443 个已安装的 OpenFOAM 可执行程序。固定版本源码的核心范围为 `applications/solvers` 中的 108 个求解器和 `applications/utilities` 中的 170 个工具，共 278 个目标。其中 273 个在本机 v2512 环境显示了 `-help-full`，另 5 个未安装。`applications/tools` 下另列的 `foamCalc`、`foamExprParserInfo` 也未安装。脚本与 shell 入口单独标注依据，不把源码存在、帮助可执行和物理算例验证混为一谈。

课程参考 Wolf 培训资料，命令与字典示例固定到官方 `OpenFOAM-v2512` 标签。具体检查与实际运行记录见 [VERIFICATION.md](VERIFICATION.md)。

## 日常内容管理

打开 [管理平台](https://foamlabshark.github.io/admin/)，使用已分配角色的 GitHub 账号登录。日常管理无需额外提供 GitHub 仓库访问令牌，也无需重新部署 Hexo。

| 角色 | 主要权限 |
| --- | --- |
| 管理员 | 全站内容、文件、成员角色、站点设置、社区管理与永久删除 |
| 内容编辑 | 建立、编辑、发布、归档与恢复内容，维护附件及编辑历史 |
| 社区版主 | 主题和评论的隐藏、恢复、置顶、关闭与处理 |
| 普通会员 | 提问、回答、评论、个人学习记录，以及自己的文章和日志草稿 |
| 禁止发言账号 | 公开阅读；停止社区写入与投稿 |

权限由数据库角色和行级访问控制执行，认证写入要求真实 GitHub 身份关联，修改个人资料或伪造身份元数据不能改变角色。站内管理的内容类型包括课程单元、课程集合、分享文章、作者日志、下载资料、资源推荐、扩展工具、专题模块、公告、作业、命令与配置。普通会员在 [作者工作台](https://foamlabshark.github.io/studio/)保存文章或日志草稿，编辑审核后发布。

内容正文地址为 `/read/?slug=地址标识`。`track` 决定分类，`series` 组织连续课程或专栏，`sort_order` 数值越小越靠前。课程的首章、上一章、下一章和末章导航，只读取同一 `series` 中已发布的课程单元；同权重时按 `slug` 排序。更改标题或排序无需手工修改翻页链接。

内容保存支持修订历史与并发冲突检查；回收站恢复为草稿，永久删除需要管理员权限。文件上传到公开 `foamlab-resources` 存储桶，常规文件上限 50 MB。内容归档与删除附件是两个动作，删除文件前应检查其引用。

完整操作说明见 [维护手册主稿](tools/content/authored-pages/site-maintenance.md)及[管理员维护入口](https://foamlabshark.github.io/admin/maintenance/)。

## 讨论、评论与作业

[讨论中心](https://foamlabshark.github.io/community/)允许匿名阅读；提问、回答和评论需要 GitHub 登录。新版站内讨论存储在 Supabase。GitHub Issues 保留为公开作业提交入口，提交链接可以粘贴到作业评论区。两处内容不会自动互相同步。

管理员或版主可置顶、关闭、隐藏和恢复主题及回复。文章评论可逐篇开关，站点设置可暂停新建讨论。普通用户每小时最多新建 5 个主题、发布 40 条回答或评论。关闭站内主题后停止新增回复；作业中写出的截止日期不会自动限制外部 GitHub Issues 的提交。

GitHub OAuth 由 Supabase Auth 处理。个人资料与新版课程进度使用数据库权限隔离并跨设备同步；旧版 28 讲完成记录保留在原表，不自动转换成新课程进度。公开社区显示名称与私有学习资料分别处理。

## 分类推荐与支持入口

[资源推荐](https://foamlabshark.github.io/recommendations/)使用 `recommendation` 类型。编辑可维护标题、分类、正文、外部入口和版本核对信息；分类来自 `track`，统一系列可填“资源推荐”。第三方工具的版本兼容性与社区经验应分别注明，不能把推荐条目写成未经验证的运行承诺。

[支持入口](https://foamlabshark.github.io/support/)的启用状态、用途说明、微信与支付宝图片由管理员在“站点与导航”中维护。页脚以小型“支持作者”入口展示两张收款码，鼠标移出即关闭；手机点击展开。 可上传不超过 5 MB 的 PNG、JPEG 或 WebP 图片，核对预览与收款对象后保存并启用。关闭入口不会删除已上传的公开图片。

## 本地预览与 Hexo 发布

已安装 Node.js 20.19 或更新版本时，在工程目录运行：

```powershell
npm ci
npm run build
npm run preview
```

打开 <http://localhost:4173>。Windows 也可双击 `启动学习网站.cmd`。预览读取所配置的内容服务；本地预览不等于一套独立的测试数据库，使用真实账号保存内容会影响所连接的服务。

修改外观、脚本、静态下载或参考源页面后，双击 `发布学习网站.cmd`，或执行：

```powershell
npm run deploy
```

`git-safe` 发布器将源码同步到 `foamlab-source` 分支；`.github/workflows/foamlab-pages.yml` 在 GitHub Actions 中安装锁定依赖、校验 TeX、构建 Hexo 并发布 Pages。Pages 设置使用 **GitHub Actions**。工作流兼容历史 `main` 静态分支；日常维护主稿为 `foamlab-source`，构建目录为 `public-openfoam`。

发布前会检查远端源码变更。同步工作副本为 `.source_foamlab`，基线为 `.openfoam-work/source-sync.json`。发生冲突时比较并合并文件，再使用以下命令标记对应文件已处理；不要删除基线或强制推送以绕过冲突。

```powershell
python tools/source-sync.py resolve source-openfoam/maintenance/index.md
```

此命令只适用于已经人工合并的实际冲突路径。发布结果以 [GitHub Actions](https://github.com/foamlabshark/foamlabshark.github.io/actions)及线上页面复核为准；每次发布的实际结果记录在 `VERIFICATION.md`。

## 内容主稿与目录

| 位置 | 用途 |
| --- | --- |
| Supabase `foamlab_content` | 已发布课程、文章、资料、推荐及参考覆盖正文的日常主稿 |
| `tools/content/*content.json` | 本轮审校后的本地内容主稿；后台后续修改需先导出合并 |
| `tools/content/authored-lessons`、`authored-pages` | 逐课与逐页审校后的 Markdown 主稿 |
| `tools/content/apply-editorial.py` | 应用正文、编程实训和标题修订，刷新静态参考页 |
| `tools/content/programming10-walkthrough.json`、`programming14-correction.json`、`programming-workflow-*.json` | 编程课逐步讲解与案例修订 |
| `tools/content/development-*-content.json` | 求解器、边界条件和工具开发实训 |
| `tools/content/rewrite-reference.py` | 命令、配置及 288 份示例的案例说明 |
| `tools/revise-legacy-reference.py` | 37 个主题参考章节的审校生成器 |
| `tools/content/build-recommendations.py` | 15 个资源推荐条目生成器 |
| `source-openfoam/assets/commands.json`、`dictionaries.json` | 命令与配置搜索目录 |
| `source-openfoam/commands`、`dictionaries`、`reference` | 可直接访问的静态参考初始版本 |
| `source-openfoam/assets/examples/v2512` | 完整教程配置及来源校验清单所对应文件 |
| `source-openfoam/downloads` | 静态资料、编程包与运行证据 |
| `source-openfoam/admin/maintenance`、`admin/design` | 仅管理员与编辑可读的文档入口 |
| `themes/foam-lab/layout`、`themes/foam-lab/source/assets` | 模板、样式、浏览器交互及本地依赖 |
| `supabase/migrations`、`supabase/tests` | 数据库结构、权限变更与隔离测试 |

静态参考页面会读取其关联 CMS 正文；后台归档后页面显示归档状态，但历史 HTML 或缓存不一定立即消失。需要彻底移除时，另行删除对应静态源文件并重新发布。

生成器会重写本地生成文件，运行前应保存人工修改。旧 `tools/build-content.py` 对应最初的 Word 与 28 讲导入流程，**不应作为新版内容重建入口**。内容 JSON、源文件和数据库是不同存储层，改动不会自动双向同步。

`tools/prepare-cms-seed.py` 仅生成导入 SQL，默认跳过已经存在的 `slug`。它不直接连接或修改数据库。维护时优先使用管理平台；需要批量迁移时先导出备份、审查 SQL，并在受控环境执行。Hexo 发布不部署数据库迁移、认证设置、存储策略或历史 Edge Function。

## 数学、代码与界面

课程目录卡片和正文开头均提供配套案例下载。后台编辑课程时，在“专题与配套案例”中上传 ZIP、填写使用说明和核验范围，并关联湍流、多相流、网格划分、动网格专题。五个专题（有限体积法、湍流、多相流、网格划分、动网格）入口为 `/topics/`，专题介绍使用 `module` 内容记录，元数据 `topic_key` 保持稳定。

基础课程案例包位于 `source-openfoam/downloads/courses/`，编程课程使用现有逐课 ZIP。包中保留输入文件、来源与许可；实际运行过的新增案例另附日志和解析比较数据。下载元数据记录文件大小与 SHA-256，替换包后需同步更新元数据。

Wolf 图源索引为 `tools/content/wolf-figures.json`，图片位于 `source-openfoam/assets/wolf/`。`wolf_media.py` 统一生成署名与出处，`integrate-wolf-figures.py` 将插图放入相应课程。点击正文插图可放大并保留图注。

编辑主稿位于 `tools/content/authored-lessons/` 和 `authored-pages/`。Linux、C++、数值理论与版本比较文章保存在各自 `*content.json` 中；命令和字典讲解使用 `command-guides.json`、`dictionary-guides.json`、`field-guides.json`、`reference-example-notes.json`。参考页运行 `rewrite-reference.py`，再运行 `apply-editorial.py`、`build-finite-volume-topic.py` 和 `tools/build-lesson-snippets.py`。旧生成器仅用于追溯原始材料。发布前导出数据库，通过修订号保护的更新批次同步正文；Hexo 发布负责页面、脚本和附件。

正文公式使用 TeX，推荐 `\(...\)` 与 `\[...\]`。静态页面在构建时渲染，CMS 正文在浏览器中处理；编辑时先预览，排除语法错误。代码块标明 `bash`、`openfoam`、`cpp`、`python`、`makefile` 等语言，保留可复制的原文。图片应区分教学示意、资料原图、生成式封面与真实计算图。

界面采用“纸张底色 + 墨绿”主题（`themes/foam-lab/source/assets/foamlab-theme.css`，最后加载），支持亮色、暗色、跟随系统。中文正文、标题和代码使用不同字体层级；Noto 字体子集及许可证随站点托管，新增罕见字由系统字体回退。具体字号、行距、对比度和响应式规则见 [字体与界面设计规范](tools/content/authored-pages/site-design.md)，管理员线上入口为 `/admin/design/`。首页插图是矢量熊猫与按圆柱绕流势流公式画的流线，均为示意，不表示计算结果。

## 检查与备份

本轮使用的主要检查入口如下；浏览器脚本依赖 Playwright 和本地预览，部分路径为当前 Windows 环境配置。

```powershell
node tools/check-tex.cjs
node tools/check-rebuild.cjs
python tools/check-reference-integrity.py
npm run build
python tools/check-generated.py
node tools/check-cms-ui.cjs
node tools/check-refinements.cjs
```

`check-cms-ui.cjs` 使用隔离请求数据，不向公开社区发布测试内容。历史 `check-admin.cjs` 等脚本针对早期管理流程，不能代替新版 CMS 与数据库权限验证。最终联机检查、部署提交与运行结果记录在 [VERIFICATION.md](VERIFICATION.md)。

管理平台“导出与维护”可导出当前可访问的内容和站点设置；导出包含附件地址，**不包含附件本体、认证用户、私有资料或完整数据库备份**。同时保存附件、源码 Git 历史和数据库迁移记录；完整数据库与身份备份在 Supabase 侧管理。公开配置只允许使用 publishable key，OAuth Secret 和服务端密钥不得写入前端、仓库或资料附件。


## 本轮界面与内容编辑

维护手册和设计规范在管理平台内提供，数据库标记 `admin_only` 并保存为草稿；RLS 和公开搜索都排除内部文档。普通会员的学习入口包含课程、资料、讨论与个人记录，Linux/C++ 归入 OpenFOAM 编程。

每页右上角提供跳转目录；标题上方的返回按钮保留进入详情前的关键词与筛选。表格铺满正文宽度，窄屏按表格局部横向滚动。页脚支持作者使用悬停二维码，移动设备点击打开，点击空白关闭；收款码由管理员站点设置维护。

页面背景为浅色网格纹理（纯 CSS），不再使用照片背景。`source-openfoam/assets/covers/` 下的飞机、竹林背景图目前未被页面引用，仅作存档。

正文示意图由 `tools/content/draw-diagrams.py` 统一绘制：24 张 `core-*` 概念图逐张手绘，`cpp-*`、`programming-*`、`reference-*` 流程图的文字来自 `tools/content/diagram-flows.json`。`build-core.py` 等旧生成器仍会写出旧版图，重跑它们之后要再运行一次 `python tools/content/draw-diagrams.py`。

追加内容与界面检查：`node tools/check-editorial.cjs`、`node tools/check-editorial-ui.cjs`。示例源码保持原文件；补充说明由 `reference-example-notes.json` 管理。
