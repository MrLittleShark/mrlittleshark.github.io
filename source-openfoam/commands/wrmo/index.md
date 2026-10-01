---
title: "wrmo · OpenFOAM 官方脚本"
layout: reference
description: "Remove all .o files from the object directory tree corresponding to the current source derectory or remove only the .o file corresponding to the optionally specified [file]. With the -a/-all/all option the .o files are removed for all platf"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>Remove all .o files from the object directory tree corresponding to the current source derectory or remove only the .o file corresponding to the optionally specified [file]. With the -a/-all/all option the .o files are removed for all platforms rather than just the current platform.</p><h2>v2512 源码中的用途</h2><p>Remove all .o files from the object directory tree corresponding to the current source derectory or remove only the .o file corresponding to the optionally specified [file]. With the -a/-all/all option the .o files are removed for all platforms rather than just the current platform.</p><h2>使用入口</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;&#36;WM_PROJECT_DIR/wmake/wrmo&quot;</code></pre><h2>使用条件与核对</h2><p>
Remove all .o files from the object directory tree corresponding to the current source derectory or remove only the .o file corresponding to the optionally specified [file]. With the -a/-all/all option the .o files are removed for all platforms rather than just the current platform.
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-a -h</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/wrmo.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: wrmo
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wrmo

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: wrmo [OPTION] [file1 [... fileN]]

options:
  -a | -all | all   All platforms (current: &#36;WM_OPTIONS)
  -h | -help        Print the usage

Remove all .o files or remove .o file corresponding to &lt;file&gt;</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wrmo">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
