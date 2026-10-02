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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-method=MODE</code></td><td>指定运行模式。</td></tr><tr><td><code>-spawn=TYPE</code></td><td>指定启动方式：1 为本地，2 为远程。</td></tr><tr><td><code>-yes</code></td><td>直接启动，省略额外提示。</td></tr><tr><td><code>-local</code></td><td>等同于 -spawn=1。</td></tr><tr><td><code>-remote</code></td><td>等同于 -spawn=2。</td></tr><tr><td><code>-clean</code></td><td>删除日志与启动文件。</td></tr><tr><td><code>-no-core</code></td><td>将核心转储文件的大小限制为 0。</td></tr><tr><td><code>-quick</code></td><td>使用 Valgrind 的 summary 检查级别，并启用 -no-core。</td></tr><tr><td><code>-decompose-dict=&lt;file&gt;</code></td><td>指定 decomposeParDict 的文件名。</td></tr><tr><td><code>-help</code></td><td>显示用法。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 文件。</td></tr><tr><td><code>-normal</code></td><td>等同于 -method=0，采用普通运行方式。</td></tr><tr><td><code>-log</code></td><td>等同于 -method=3，将输出写入日志。</td></tr><tr><td><code>-xlog</code></td><td>等同于 -method=4，使用日志和 xterm 窗口。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（2 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-valgrind</code></td><td>等同于 -method=5l，使用 Valgrind 并记录日志。</td></tr><tr><td><code>-xvalgrind</code></td><td>等同于 -method=5，使用 Valgrind 和 xterm 窗口。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/mpirunDebug">源码与说明</a> · <a href="/assets/command-help/mpirundebug.txt">帮助文本</a></p>
