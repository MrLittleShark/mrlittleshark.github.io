---
title: "top · 交互查看计算资源占用"
layout: reference
description: "交互查看计算资源占用。"
cms_slug: "command-top"
---

<p>交互查看计算资源占用。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：交互观察</h2>
<pre><code class="language-bash">top
</code></pre>
<p>P 按 CPU 排序，M 按内存排序，q 退出。</p>
<h2>示例 2：按用户筛选</h2>
<pre><code class="language-bash">top -u "$USER"
</code></pre>
<p>仅列出自己的进程。</p>
<h2>示例 3：跟踪单个进程</h2>
<pre><code class="language-bash">top -p "$solverPid"
</code></pre>
<p>指定已记录的 PID；MPI 各进程分别有 PID。</p>
<h2>示例 4：保存一次快照</h2>
<pre><code class="language-bash">top -b -n 1 &gt; resources.txt
</code></pre>
<p>-b 非交互输出，-n 1 采样一次后退出。</p>
<h2>示例 5：保存多次采样</h2>
<pre><code class="language-bash">top -b -d 5 -n 12 &gt; resources-minute.txt
</code></pre>
<p>每 5 秒刷新，共 12 次，记录负载变化。</p>
<h2>参考</h2><p><a href="https://gitlab.com/procps-ng/procps">源码与说明</a></p>
