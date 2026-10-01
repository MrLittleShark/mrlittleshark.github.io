---
title: "foamRunTutorials  递归执行算例脚本"
layout: reference
description: "执行目标目录中的 Allrun 或 Alltest。-dry-run 列出待执行脚本。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>执行目标目录中的 Allrun 或 Alltest。-dry-run 列出待执行脚本。</p><h2>v2512 源码中的用途</h2><p>Recursively run Allrun/Alltest or blockMesh and application, starting with the current directory or the specified -case directory. For tutorials that are known to run poorly, an Allrun-optional placeholder can be used instead of the usual Allrun script. When this is detected, the case will be skipped.</p><h2>使用入口</h2><pre><code class="language-bash">foamRunTutorials -dry-run -case ./cases</code></pre><h2>使用条件与核对</h2><p>执行目标目录中的 Allrun 或 Alltest。-dry-run 列出待执行脚本。 用法：foamRunTutorials [选项] [-case 目录] 示例：foamRunTutorials -dry-run -case ./cases
Recursively run Allrun/Alltest or blockMesh and application, starting with the current directory or the specified -case directory. For tutorials that are known to run poorly, an Allrun-optional placeholder can be used instead of the usual Allrun script. When this is detected, the case will be skipped.
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-case -dry-run -help -parallel -self -serial -test</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamruntutorials.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamRunTutorials
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamRunTutorials

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamRunTutorials [OPTION]
options:
  -case=DIR     Specify starting directory, default is cwd
  -serial       Prefer Allrun-serial if available
  -parallel     Prefer Allrun-parallel if available
  -test         Prefer Alltest script, pass -test argument to scripts
  -dry-run      Only report which script to run
  -self         Avoid initial Allrun / Alltest scripts
                (prevent infinite recursion)
  -help         Print the usage

Recursively run Alltest / Allrun / Allrun-parallel / Allrun-serial
(or simply blockMesh + application)
starting from the current directory or the specified -case directory.

Equivalent options:
  | -case=DIR  | -case DIR |</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamRunTutorials">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
