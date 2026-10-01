---
title: "foamCleanTutorials  递归清理教程结果"
layout: reference
description: "按规则删除结果并执行相关 Allclean；存在 0.orig 时，默认清理过程可移除 0 目录。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>按规则删除结果并执行相关 Allclean；存在 0.orig 时，默认清理过程可移除 0 目录。</p><h2>v2512 源码中的用途</h2><p>Recursively clean an OpenFOAM case directory, using Allclean, Allwclean (when present) or regular cleanCase.</p><h2>使用入口</h2><pre><code class="language-bash">foamCleanTutorials -case ./caseCopy</code></pre><h2>使用条件与核对</h2><p>按规则删除结果并执行相关 Allclean；存在 0.orig 时，默认清理过程可移除 0 目录。 用法：foamCleanTutorials [选项] [目录] 示例：foamCleanTutorials -case ./caseCopy
Recursively clean an OpenFOAM case directory, using Allclean, Allwclean (when present) or regular cleanCase.
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-auto -case -help -no-auto -self</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamcleantutorials.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamCleanTutorials
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCleanTutorials

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamCleanTutorials [OPTION]
       foamCleanTutorials [OPTION] directory
options:
  -0            Perform cleanCase, remove 0/ unconditionally
  -auto         Perform cleanCase, remove 0/ if 0.orig/ exists [default]
  -no-auto      Perform cleanCase only
  -case=DIR     Specify starting directory, default is cwd
  -self         Avoid Allclean script (prevent infinite recursion)
  -help         Print the usage

Recursively clean an OpenFOAM case directory, using Allclean or Allwclean
when present.

In the default &#x27;auto&#x27; mode, it will use cleanCase and will automatically
remove the 0/ directory if a corresponding 0.orig directory exists.

Equivalent options:
  | -case=DIR  | -case DIR |</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCleanTutorials">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
