---
title: "foamJob  启动后台计算并记录日志"
layout: reference
description: "默认日志名为 log。-parallel 启用 MPI，-screen 同时输出至终端，-wait 等待计算结束。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>默认日志名为 log。-parallel 启用 MPI，-screen 同时输出至终端，-wait 等待计算结束。</p><h2>v2512 源码中的用途</h2><p>Run an OpenFOAM job in background. Redirects the output to &#x27;log&#x27; in the case directory.</p><h2>使用入口</h2><pre><code class="language-bash">foamJob -log-app simpleFoam</code></pre><h2>使用条件与核对</h2><p>默认日志名为 log。-parallel 启用 MPI，-screen 同时输出至终端，-wait 等待计算结束。 用法：foamJob [选项] 应用 [应用参数] 示例：foamJob -log-app simpleFoam
Run an OpenFOAM job in background. Redirects the output to &#x27;log&#x27; in the case directory.
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-append -case -help -log -log-app -no-check -no-log -parallel -screen -wait</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamjob.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamJob
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamJob

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamJob [OPTION] &lt;application&gt; ...
options:
  -case &lt;dir&gt;       specify alternative case directory, default is the cwd
  -parallel         run in parallel (with mpirun)
  -screen           also send output to screen
  -append           append to existing log file instead of overwriting it
  -log=FILE         specify the log file
  -log-app          Use log.{appName} for the log file
  -no-check         run without fewer checks (eg, processor dirs etc)
  -no-log           run without log file
  -wait             wait for execution to complete (when not using -screen)
  -help             print the usage

Run an OpenFOAM job in background, redirecting output to a &#x27;log&#x27; file
in the case directory</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamJob">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
