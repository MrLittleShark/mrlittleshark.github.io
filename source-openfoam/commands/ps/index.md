---
title: "ps · 显示进程及其进程号、运行状态等信息"
layout: reference
description: "显示进程及其进程号、运行状态等信息。"
cms_slug: "command-ps"
---

<p>显示进程及其进程号、运行状态等信息。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：查看自己的进程</h2>
<pre><code class="language-bash">ps -u "$USER"
</code></pre>
<p>按用户筛选，列出 PID 和程序名。</p>
<h2>示例 2：定位求解器</h2>
<pre><code class="language-bash">ps -eo pid,ppid,etime,%cpu,%mem,args | grep '[i]coFoam'
</code></pre>
<p>显示父进程、运行时间与资源比例，正则避免匹配 grep 自身。</p>
<h2>示例 3：检查已记录的 PID</h2>
<pre><code class="language-bash">ps -p "$solverPid" -o pid,stat,etime,args
</code></pre>
<p>solverPid 取启动后台求解器时的 $!；程序结束后不再出现。</p>
<h2>示例 4：查看进程关系</h2>
<pre><code class="language-bash">ps -u "$USER" -f --forest
</code></pre>
<p>树状缩进显示 MPI 启动器及子进程。</p>
<h2>示例 5：找内存占用大户</h2>
<pre><code class="language-bash">ps -u "$USER" -o pid,rss,args --sort=-rss
</code></pre>
<p>rss 以 KiB 表示常驻内存，降序排列。</p>
<h2>参考</h2><p><a href="https://gitlab.com/procps-ng/procps">源码与说明</a></p>
