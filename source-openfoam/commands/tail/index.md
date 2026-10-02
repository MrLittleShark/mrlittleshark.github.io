---
title: "tail · 查看或持续监视日志末尾"
layout: reference
description: "查看或持续监视日志末尾。"
cms_slug: "command-tail"
---

<p>查看或持续监视日志末尾。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：看当前进度</h2>
<pre><code class="language-bash">tail caseA/log.icoFoam
</code></pre>
<p>默认最后 10 行，显示最新输出。</p>
<h2>示例 2：保留错误上下文</h2>
<pre><code class="language-bash">tail -n 80 caseA/log.icoFoam &gt; solver-last80.txt
</code></pre>
<p>将末尾 80 行写到小文件，便于分享诊断。</p>
<h2>示例 3：实时跟踪</h2>
<pre><code class="language-bash">tail -f caseA/log.icoFoam
</code></pre>
<p>持续显示新增行；Ctrl+C 仅停止 tail。</p>
<h2>示例 4：跟踪重新生成的文件</h2>
<pre><code class="language-bash">tail -F caseA/log.icoFoam
</code></pre>
<p>按名字重试，文件被重建后仍可继续跟踪。</p>
<h2>示例 5：去掉单行表头</h2>
<pre><code class="language-bash">tail -n +2 measurements.csv &gt; measurements-data.csv
</code></pre>
<p>+2 从第 2 行输出到末尾。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/coreutils/manual/">源码与说明</a></p>
