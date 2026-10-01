---
title: "Allrun"
layout: reference
description: "算例提供的运行脚本，具体执行步骤由该文件定义。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>算例提供的运行脚本，具体执行步骤由该文件定义。</p><h2>v2512 源码中的用途</h2><p>Run tutorial cases and summarize the outcome as &#x27;testLoopReport&#x27;</p><h2>使用入口</h2><pre><code class="language-bash">./Allrun</code></pre><h2>使用条件与核对</h2><p>算例提供的运行脚本，具体执行步骤由该文件定义。 示例中的算例名、路径与主机名须按实际环境替换。
Run tutorial cases and summarize the outcome as &#x27;testLoopReport&#x27;
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-collect -help -no-collect -test</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/allrun.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: Allrun
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/Allrun

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: Allrun [OPTION]
options:
  -collect          Collect logs only. Can be useful for aborted runs.
  -no-collect       Run without collecting logs
  -test             Pass -test argument to scripts, end of option processing
  --                End of option processing
  -help             print the usage

Run tutorial cases and summarize the outcome as &#x27;testLoopReport&#x27;</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/Allrun">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
