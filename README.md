# FoamLab · OpenFOAM v2512 学习社区

网站：<https://mrlittleshark.github.io/>。本地工程：`E:\Hexo`。

本站以 **OpenCFD OpenFOAM v2512** 为软件基准，使用 Hexo 8.1.2 和 `themes/foam-lab` 主题生成网站，部署到 GitHub Pages。Supabase 提供 GitHub 登录、内容管理、讨论、评论、附件和跨设备学习记录。课程、参考资料、实践分享与讨论分别组织，电极气泡专题暂不纳入当前内容。

## 内容范围

以下数量为本次重构的初始内容清单；后台增删后，线上目录以实际已发布记录为准。

| 内容 | 初始规模与范围 |
| --- | --- |
| 课程单元 | 46 个：29 个基础、网格、数值方法、模型与后处理单元，17 个 BasicOFProgramming 编程单元 |
| 命令目录 | 443 条，区分核心求解器、核心工具、官方脚本、shell 函数、构建辅助与 Linux 配套命令 |
| 配置参考 | 111 项配置字典、场文件、函数对象与编译配置，附 281 份完整的 v2512 官方教程文件 |
| 主题参考 | 37 个重新审校的参考章节，保留通用内容并修正版本差异 |
| 扩展工具 | ParaView、Gmsh、SALOME、PyVista、PyFoam、FreeCAD 等 6 篇使用说明 |
| 分类推荐 | 15 项，分官方文档、教程与课程、源码与开发、几何网格、可视化与数据、学术社区 |
| 实践与分享 | 公开作业、资料包、作者日志、文章投稿、站内讨论与评论 |

443 条目录不等于 443 个已安装的 OpenFOAM 可执行程序。固定版本源码的核心范围为 `applications/solvers` 中的 108 个求解器和 `applications/utilities` 中的 170 个工具，共 278 个目标。其中 273 个在本机 v2512 环境显示了 `-help-full`，另 5 个未安装。`applications/tools` 下另列的 `foamCalc`、`foamExprParserInfo` 也未安装。脚本与 shell 入口单独标注依据，不把源码存在、帮助可执行和物理算例验证混为一谈。

课程参考 Wolf 培训资料并重新组织。Wolf 原培训基于 OpenFOAM Foundation 9；本站运行和配置依据为 OpenCFD v2512，两者不是可直接互换的版本。命令与字典示例固定到官方 `OpenFOAM-v2512` 标签。核验范围见 [VERIFICATION.md](VERIFICATION.md)。

## 日常内容管理

打开 [管理平台](https://mrlittleshark.github.io/admin/)，使用已分配角色的 GitHub 账号登录。日常管理无需额外提供 GitHub 仓库访问令牌，也无需重新部署 Hexo。

| 角色 | 主要权限 |
| --- | --- |
| 管理员 | 全站内容、文件、成员角色、站点设置、社区管理与永久删除 |
| 内容编辑 | 建立、编辑、发布、归档与恢复内容，维护附件及编辑历史 |
| 社区版主 | 主题和评论的隐藏、恢复、置顶、关闭与处理 |
| 普通会员 | 提问、回答、评论、个人学习记录，以及自己的文章和日志草稿 |
| 禁止发言账号 | 公开阅读；停止社区写入与投稿 |

权限由数据库角色和行级访问控制执行，认证写入要求真实 GitHub 身份关联，修改个人资料或伪造身份元数据不能改变角色。站内管理的内容类型包括课程单元、课程集合、分享文章、作者日志、下载资料、资源推荐、扩展工具、专题模块、公告、作业、命令与配置。普通会员在 [作者工作台](https://mrlittleshark.github.io/studio/)保存文章或日志草稿，编辑审核后发布。

内容正文地址为 `/read/?slug=地址标识`。`track` 决定分类，`series` 组织连续课程或专栏，`sort_order` 数值越小越靠前。课程的首章、上一章、下一章和末章导航，只读取同一 `series` 中已发布的课程单元；同权重时按 `slug` 排序。更改标题或排序无需手工修改翻页链接。

内容保存支持修订历史与并发冲突检查；回收站恢复为草稿，永久删除需要管理员权限。文件上传到公开 `foamlab-resources` 存储桶，常规文件上限 50 MB。内容归档与删除附件是两个动作，删除文件前应检查其引用。

完整操作说明见 [维护手册](source-openfoam/maintenance/index.md)及[线上维护入口](https://mrlittleshark.github.io/maintenance/)。

## 讨论、评论与作业

[讨论中心](https://mrlittleshark.github.io/community/)允许匿名阅读；提问、回答和评论需要 GitHub 登录。新版站内讨论存储在 Supabase。GitHub Issues 保留为公开作业提交入口，提交链接可以粘贴到作业评论区。两处内容不会自动互相同步。

管理员或版主可置顶、关闭、隐藏和恢复主题及回复。文章评论可逐篇开关，站点设置可暂停新建讨论。普通用户每小时最多新建 5 个主题、发布 40 条回答或评论。关闭站内主题后停止新增回复；作业中写出的截止日期不会自动限制外部 GitHub Issues 的提交。

GitHub OAuth 由 Supabase Auth 处理。个人资料与新版课程进度使用数据库权限隔离并跨设备同步；旧版 28 讲完成记录保留在原表，不自动转换成新课程进度。公开社区显示名称与私有学习资料分别处理。

## 分类推荐与支持入口

[资源推荐](https://mrlittleshark.github.io/recommendations/)使用 `recommendation` 类型。编辑可维护标题、分类、正文、外部入口和版本核对信息；分类来自 `track`，统一系列可填“资源推荐”。第三方工具的版本兼容性与社区经验应分别注明，不能把推荐条目写成未经验证的运行承诺。

[支持入口](https://mrlittleshark.github.io/support/)的启用状态、用途说明、微信与支付宝图片由管理员在“站点与导航”中维护。**本次未上传真实收款码，入口保持停用。** 可上传不超过 5 MB 的 PNG、JPEG 或 WebP 图片，核对预览与收款对象后保存并启用。关闭入口不会删除已上传的公开图片。

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

此命令只适用于已经人工合并的实际冲突路径。发布结果以 [GitHub Actions](https://github.com/MrLittleShark/mrlittleshark.github.io/actions)及线上页面复核为准；本轮最终部署检查尚待补记。

## 内容主稿与目录

| 位置 | 用途 |
| --- | --- |
| Supabase `foamlab_content` | 已发布课程、文章、资料、推荐及参考覆盖正文的日常主稿 |
| `tools/content/*content.json` | 可审查的初始内容数据；不自动读取后台后续修改 |
| `tools/content/build-core.py` | 基础课程、数值方法及工具说明生成器 |
| `tools/content/build-programming-content.py` | 17 个编程单元生成器 |
| `tools/build-reference-library.py` | 命令、配置页及官方示例清单生成器 |
| `tools/revise-legacy-reference.py` | 37 个主题参考章节的审校生成器 |
| `tools/content/build-recommendations.py` | 15 个资源推荐条目生成器 |
| `source-openfoam/assets/commands.json`、`dictionaries.json` | 命令与配置搜索目录 |
| `source-openfoam/commands`、`dictionaries`、`reference` | 可直接访问的静态参考初始版本 |
| `source-openfoam/assets/examples/v2512` | 完整教程配置及来源校验清单所对应文件 |
| `source-openfoam/downloads` | 静态资料、编程包与运行证据 |
| `source-openfoam/maintenance`、`design` | 维护手册及字体界面规范 |
| `themes/foam-lab/layout`、`themes/foam-lab/source/assets` | 模板、样式、浏览器交互及本地依赖 |
| `supabase/migrations`、`supabase/tests` | 数据库结构、权限变更与隔离测试 |

静态参考页面会读取其关联 CMS 正文；后台归档后页面显示归档状态，但历史 HTML 或缓存不一定立即消失。需要彻底移除时，另行删除对应静态源文件并重新发布。

生成器会重写本地生成文件，运行前应保存人工修改。旧 `tools/build-content.py` 对应最初的 Word 与 28 讲导入流程，**不应作为新版内容重建入口**。内容 JSON、源文件和数据库是不同存储层，改动不会自动双向同步。

`tools/prepare-cms-seed.py` 仅生成导入 SQL，默认跳过已经存在的 `slug`。它不直接连接或修改数据库。维护时优先使用管理平台；需要批量迁移时先导出备份、审查 SQL，并在受控环境执行。Hexo 发布不部署数据库迁移、认证设置、存储策略或历史 Edge Function。

## 数学、代码与界面

正文公式使用 TeX，推荐 `\(...\)` 与 `\[...\]`。静态页面在构建时渲染，CMS 正文在浏览器中处理；编辑时先预览，排除语法错误。代码块标明 `bash`、`openfoam`、`cpp`、`python`、`makefile` 等语言，保留可复制的原文。图片应区分教学示意、资料原图、生成式封面与真实计算图。

界面使用蓝色体系并支持亮色、暗色、跟随系统。中文正文、标题和代码使用不同字体层级；Noto 字体子集及许可证随站点托管，新增罕见字由系统字体回退。具体字号、行距、对比度和响应式规则见 [字体与界面设计规范](source-openfoam/design/index.md)，线上入口为 `/design/`。封面为 CFD 主题生成式插图，不表示真实计算结果。

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
