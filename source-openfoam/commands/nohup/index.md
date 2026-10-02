---
title: "nohup · 使程序忽略挂断信号并重定向日志"
layout: reference
description: "使程序忽略挂断信号并重定向日志。"
cms_slug: "command-nohup"
---

<p>使程序忽略挂断信号并重定向日志。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：后台启动</h2>
<pre><code class="language-bash">nohup icoFoam -case caseA &gt; caseA/log.icoFoam 2&gt;&amp;1 &amp;
solverPid=$!
</code></pre>
<p>忽略挂断信号，&amp; 返回终端；$! 保存后台 PID。</p>
<h2>示例 2：运行批处理</h2>
<pre><code class="language-bash">nohup bash caseA/Allrun &gt; caseA/log.Allrun 2&gt;&amp;1 &amp;
</code></pre>
<p>Allrun 应在内部进入自身目录；文件保存全过程输出。</p>
<h2>示例 3：明确标准输入</h2>
<pre><code class="language-bash">nohup icoFoam -case caseA &lt;/dev/null &gt; caseA/log.detached 2&gt;&amp;1 &amp;
</code></pre>
<p>无需人工输入的计算可将标准输入连接到 /dev/null。</p>
<h2>示例 4：追加诊断记录</h2>
<pre><code class="language-bash">nohup checkMesh -case caseA &gt;&gt; mesh-history.log 2&gt;&amp;1 &amp;
</code></pre>
<blockquote>
<blockquote>
<p>将新检查附加到已有日志，保留历史内容。</p>
</blockquote>
</blockquote>
<h2>示例 5：持久保存进程号</h2>
<pre><code class="language-bash">nohup icoFoam -case caseA &gt; caseA/log.job 2&gt;&amp;1 &amp;
printf '%s\n' "$!" &gt; caseA/solver.pid
ps -p "$(cat caseA/solver.pid)" -o pid,etime,args
</code></pre>
<p>PID 文件供稍后检查。进程退出后 ps 不会列出它。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/coreutils/manual/">源码与说明</a></p>
