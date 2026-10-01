---
title: "mpirunDebug  记录 MPI 分进程日志或启动调试"
layout: reference
description: "计算前完成分区。图形调试模式需配置 xterm 及对应调试器。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>计算前完成分区。图形调试模式需配置 xterm 及对应调试器。</p><h2>v2512 源码中的用途</h2><p>Invoke mpirun with separate per-processor log files etc. Requires bash on all processors.</p><h2>使用入口</h2><pre><code class="language-bash">mpirunDebug -log -np 4 simpleFoam -parallel</code></pre><h2>使用条件与核对</h2><p>计算前完成分区。图形调试模式需配置 xterm 及对应调试器。 用法：mpirunDebug [选项] -np N 程序 参数 示例：mpirunDebug -log -np 4 simpleFoam -parallel
Invoke mpirun with separate per-processor log files etc. Requires bash on all processors.
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-clean -decompose-dict -decomposeParDict -help -local -log -method -no-core -normal -quick -remote -spawn -valgrind -xlog -xvalgrind -yes</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/mpirundebug.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: mpirunDebug
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/mpirunDebug

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: mpirunDebug [OPTION] -np &lt;N&gt; &lt;executable&gt; &lt;args&gt;

options:
  -method=MODE  The run mode
        (0)  normal
        (1)  gdb+xterm
        (2)  gdb
        (3)  log
        (4)  log + xterm
        (5)  valgrind + xterm
       (5l)  valgrind + log
        (6)  gperftools(callgrind)
  -spawn=TYPE   Spawn type: (1) local (2) remote
  -yes          Start without additional prompting
  -local        Same as -spawn=1
  -remote       Same as -spawn=2
  -clean        Remove log and startup files
  -no-core      Restrict core dump to 0 size
  -quick        Valgrind with &#x27;summary&#x27; (not &#x27;full&#x27;) and use -no-core
  -decompose-dict=&lt;file&gt;   Specific decomposeParDict name
  -help         Print the usage

Invoke mpirun with separate per-processor log files or with separate XTerms.
Also detects some OpenFOAM options:
  -decomposeParDict &lt;file&gt;   Use specified file for decomposePar dictionary

Common shortcuts. Sets default spawn to -local, add -yes.
  -normal       = -method=0
  -log          = -method=3
  -xlog         = -method=4  (log + xterm)
  -valgrind     = -method=5l (valgrind + log)
  -xvalgrind    = -method=5  (valgrind + xterm)</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/mpirunDebug">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
