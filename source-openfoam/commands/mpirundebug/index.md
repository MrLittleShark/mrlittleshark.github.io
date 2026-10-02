---
title: "mpirunDebug · 计算前完成分区"
layout: reference
description: "计算前完成分区。图形调试模式需配置 xterm 及对应调试器。"
cms_slug: "command-mpirundebug"
---

<p>计算前完成分区。图形调试模式需配置 xterm 及对应调试器。</p><h2>用法</h2><pre><code class="language-bash">mpirunDebug -log -np 4 simpleFoam -parallel</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-method=MODE</td><td>The run mode</td></tr><tr><td>-spawn=TYPE</td><td>Spawn type: (1) local (2) remote</td></tr><tr><td>-yes</td><td>Start without additional prompting</td></tr><tr><td>-local</td><td>Same as -spawn=1</td></tr><tr><td>-remote</td><td>Same as -spawn=2</td></tr><tr><td>-clean</td><td>Remove log and startup files</td></tr><tr><td>-no-core</td><td>Restrict core dump to 0 size</td></tr><tr><td>-quick</td><td>Valgrind with &#x27;summary&#x27; (not &#x27;full&#x27;) and use -no-core</td></tr><tr><td>-decompose-dict=&lt;file&gt;</td><td>Specific decomposeParDict name</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-decomposeParDict &lt;file&gt;</td><td>使用指定的并行分解字典。</td></tr><tr><td>-normal</td><td>= -method=0</td></tr><tr><td>-log</td><td>= -method=3</td></tr><tr><td>-xlog</td><td>= -method=4  (log + xterm)</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: mpirunDebug [OPTION] -np &lt;N&gt; &lt;executable&gt; &lt;args&gt;

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
  -xvalgrind    = -method=5  (valgrind + xterm)</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/mpirunDebug">源码与说明</a> · <a href="/assets/command-help/mpirundebug.txt">帮助文本</a></p>
