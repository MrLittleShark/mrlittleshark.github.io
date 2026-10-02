---
title: "mpirunDebug · 计算前完成分区"
layout: reference
description: "计算前完成分区。图形调试模式需配置 xterm 及对应调试器。"
cms_slug: "command-mpirundebug"
---

<p>计算前完成分区。图形调试模式需配置 xterm 及对应调试器。</p><h2>开始前</h2>
<p>加载 v2512 环境，使用个人算例副本 caseA。并行示例先配置 decomposeParDict 并完成 decomposePar，程序和字典须匹配。 示例使用已分成两个子域的算例；调试模式按需安装 gdb、xterm、valgrind 或 gperftools。</p>
<h2>示例 1：普通 MPI 启动</h2>
<pre><code class="language-bash">cd caseA
mpirunDebug -normal -np 2 icoFoam -parallel
</code></pre>
<p>normal 选择常规运行方式并使用本地启动。</p>
<h2>示例 2：分别保存各进程日志</h2>
<pre><code class="language-bash">cd caseA
mpirunDebug -log -np 2 icoFoam -parallel
</code></pre>
<p>log 模式输出每个进程的日志，便于寻找首先出错的子域。</p>
<h2>示例 3：使用 GDB 调试</h2>
<pre><code class="language-bash">cd caseA
mpirunDebug -method=2 -local -yes -np 2 icoFoam -parallel
</code></pre>
<p>method=2 使用 gdb；-yes 跳过启动前确认，适合已准备好调试环境时。</p>
<h2>示例 4：做内存检查</h2>
<pre><code class="language-bash">cd caseA
mpirunDebug -valgrind -np 2 icoFoam -parallel
</code></pre>
<p>以 Valgrind 包装每个进程并保存报告，执行速度通常较慢。</p>
<h2>示例 5：缩短内存诊断输出</h2>
<pre><code class="language-bash">cd caseA
mpirunDebug -valgrind -quick -np 2 icoFoam -parallel
</code></pre>
<p>-quick 使用摘要级内存检查并限制 core 文件，适用于先定位明显内存问题。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-method=MODE</code></td><td>The run mode</td></tr><tr><td><code>-spawn=TYPE</code></td><td>Spawn type: (1) local (2) remote</td></tr><tr><td><code>-yes</code></td><td>Start without additional prompting</td></tr><tr><td><code>-local</code></td><td>Same as -spawn=1</td></tr><tr><td><code>-remote</code></td><td>Same as -spawn=2</td></tr><tr><td><code>-clean</code></td><td>Remove log and startup files</td></tr><tr><td><code>-no-core</code></td><td>Restrict core dump to 0 size</td></tr><tr><td><code>-quick</code></td><td>Valgrind with &#x27;summary&#x27; (not &#x27;full&#x27;) and use -no-core</td></tr><tr><td><code>-decompose-dict=&lt;file&gt;</code></td><td>Specific decomposeParDict name</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的并行分解字典。</td></tr><tr><td><code>-normal</code></td><td>= -method=0</td></tr><tr><td><code>-log</code></td><td>= -method=3</td></tr><tr><td><code>-xlog</code></td><td>= -method=4  (log + xterm)</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: mpirunDebug [OPTION] -np &lt;N&gt; &lt;executable&gt; &lt;args&gt;

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
