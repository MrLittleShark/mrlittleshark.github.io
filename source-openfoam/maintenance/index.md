---
title: 网站维护手册
layout: page
section: maintenance
---

## 管理入口

打开 [网站管理平台](/admin/)，使用仓库所有者 **MrLittleShark** 的 GitHub 账号授权。首次管理授权需要允许访问公开仓库。普通学习账号的资料和学习进度功能保持独立。

管理服务在服务端核验 GitHub 账号、与当前登录会话关联的身份及仓库写入权限。修改个人资料中的姓名或用户名不能获得管理权限。若提示授权失效，重新点击管理授权按钮。

## 发布作业和公告

1. 选择“发布作业 / 公告”，填写类型、标题和正文。作业可以使用 28 讲练习模板。
2. 补充截止日期、时区、提交内容和评价要求，点击“检查发布内容”。
3. 核对后确认发布。记录保存在公开 GitHub Issues 中；课堂页面刷新后可见。
4. 在“已发布记录”中修改内容或将状态设为“已结束”。关闭作业后不再显示该作业的快捷提交按钮，GitHub 本身不会自动禁止逾期提交。

学生在作业中心点击“提交此作业”，到 GitHub 确认提交并添加附件。教师在对应提交下评论反馈。答疑使用同一方式公开讨论。不要提交密码、访问令牌或个人敏感信息。

## 修改课程正文

在“课程内容维护”选择页面并载入当前版本，修改后点击“保存并发布更新”。源文件保存到仓库的 `foamlab-source` 分支。GitHub Actions 检查 TeX 并调用 Hexo 构建，成功后更新网站。源文件已保存与网站已发布是两个状态，请在“发布状态与维护”确认结果。构建失败时原网站继续提供服务。

保留文件开头的 `---` 页面信息，以及原有的 Hexo raw 标记。网页编辑使用版本校验；若提示文件已变化，重新载入并合并修改。源文件的历史版本可在 GitHub 提交记录中查看。

### 公式

正文使用 TeX。行内示例：\(\mathrm{Re}=UL/\nu\)。独立公式示例：

\[
\Delta p=\frac{2\sigma}{R}
\]

对应源文件写法如下，推荐显式定界符：

```tex
行内：\(\mathrm{Re}=UL/\nu\)
独立公式：
\[
\Delta p=\frac{2\sigma}{R}
\]
```

支持 `$...$` 和 `$$...$$`，但 Shell 环境变量应放在代码块中。TeX 在构建时渲染，不依赖外部公式服务。公式语法错误会中止发布。

### 代码与配置

使用 Markdown 围栏代码块，注明 `bash`、`openfoam`、`cpp` 或 `python`。网站显示语言、行数、语法高亮、复制和换行按钮。复制结果不含工具栏文字。已有课程的 HTML `pre` / `code` 块也会得到相同显示效果。代码中的美元符号、变量和运算符保留原样。

```openfoam
application     interFoam;
startFrom       startTime;
deltaT          1e-5;
adjustTimeStep  yes;
maxCo           0.5;
```

作业与公告正文在 GitHub 使用 Markdown 和 TeX；课堂列表显示文字摘要，完整内容在记录链接中查看。

## 本地维护与发布

本地工程目录为 `E:\Hexo`。双击“启动学习网站.cmd”预览，双击“发布学习网站.cmd”发布。本地发布先同步远程源文件，执行 Hexo 构建，再推送源文件并触发自动发布。若同一文件在网页和本地均有修改，同步程序会停止并列出冲突文件；先合并内容，不能直接覆盖。

| 内容 | 本地位置 |
| --- | --- |
| 28 讲课程 | `source-openfoam/lessons` |
| 参考章节与 Dict 页面 | `source-openfoam/reference`、`source-openfoam/dictionaries` |
| 命令、配置索引数据 | `source-openfoam/assets/commands.json`、`dictionaries.json` |
| 课程目录与模板 | `source-openfoam/_data/learning.json`、`source-openfoam/assets/assignment-templates.json` |
| 页面结构与样式 | `themes/foam-lab` |
| 原始文档与算例包 | `source-openfoam/downloads` |
| 管理服务 | `supabase/functions/foamlab-admin/index.ts` |

普通内容修改不需要重新运行 Word 导入。`tools/build-content.py` 会覆盖导入生成的课程、参考页面和索引；需要重新导入时，应先备份并合并已经在线修改的内容。全文搜索索引随 Hexo 构建自动更新。

## 备份与故障检查

- 内容和主题：备份 `foamlab-source` 分支及本地工程。Git 历史保存正文修改记录。
- 个人资料与进度：由 Supabase 数据库保存，数据库备份与 Git 仓库备份相互独立。
- 发布失败：查看 [GitHub Actions](https://github.com/MrLittleShark/mrlittleshark.github.io/actions)，修正对应文件后重新发布。
- 登录失败：检查 Supabase GitHub 提供商和回调配置，见本地 `supabase/SETUP.md`。
- 课堂列表加载失败：使用页面上的 GitHub 入口查看记录；公开 API 存在频率限制。

界面右上角按钮依次切换亮色、暗色、跟随系统；显示偏好保存在当前浏览器。首页图片来自 [OpenFOAM 官方网站](https://www.openfoam.com/)，图注保留来源。本站是学习资料整理网站。
