---
title: "wmakeCollect · 调度并行编译任务"
layout: reference
description: "调度并行编译任务。"
cms_slug: "command-wmakecollect"
---

<p>调度并行编译任务。</p><h2>开始前</h2>
<p>这是队列构建内部调度器，通常由 wmake -queue 调用。直接演示需要 g++、make，前四例依次在独立练习目录执行；每个编译命令须以“源文件 -o 目标文件”结尾。</p>
<h2>示例 1：初始化独立编译队列</h2>
<pre><code class="language-bash">export WM_COLLECT_DIR="$(mktemp -d "$HOME/wmake-queue.XXXXXX")"
export WM_NCOMPPROCS=2
wmakeCollect -clean
printf 'int valueA() { return 1; }\n' &gt; queueA.C
printf 'int valueB() { return 2; }\n' &gt; queueB.C
</code></pre>
<p>-clean 移除本例队列控制文件；两份简单源码用于演示实际编译命令。</p>
<h2>示例 2：提交第一个编译任务</h2>
<pre><code class="language-bash">wmakeCollect g++ -c queueA.C -o queueA.o
</code></pre>
<p>最后三个参数须对应源文件、-o 和目标文件；此时只记录编译规则。</p>
<h2>示例 3：提交第二个编译任务</h2>
<pre><code class="language-bash">wmakeCollect g++ -c queueB.C -o queueB.o
</code></pre>
<p>为第二个源码记录独立目标，稍后与第一项一起执行。</p>
<h2>示例 4：执行已收集任务</h2>
<pre><code class="language-bash">wmakeCollect
</code></pre>
<p>无命令参数时汇总 Makefile，按 WM_NCOMPPROCS=2 运行 make，生成 queueA.o 和 queueB.o。</p>
<h2>示例 5：在真实项目中启用队列</h2>
<pre><code class="language-bash">cd user-project
wmakeLnIncludeAll
wmake -queue
</code></pre>
<p>预先建立头文件链接，再由 wmake 自己生成正确依赖与编译命令，适用于多编译单元项目。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-clean</code></td><td>编译前清理旧 Makefile。</td></tr><tr><td><code>-kill</code></td><td>程序终止后清理生成的 Makefile。</td></tr><tr><td><code>-h | -help</code></td><td>显示用法。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wmakeCollect">源码与说明</a> · <a href="/assets/command-help/wmakecollect.txt">帮助文本</a></p>
