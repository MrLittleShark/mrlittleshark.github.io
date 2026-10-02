---
title: "grep · 按文本模式检索文件"
layout: reference
description: "按文本模式检索文件。"
cms_slug: "command-grep"
---

<p>按文本模式检索文件。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：寻找压力残差</h2>
<pre><code class="language-bash">grep 'Solving for p,' caseA/log.icoFoam
</code></pre>
<p>输出压力求解行；p_rgh 需采用对应名称。</p>
<h2>示例 2：同时看时间与库朗数</h2>
<pre><code class="language-bash">grep -E '^Time =|Courant Number' caseA/log.icoFoam
</code></pre>
<p>-E 启用扩展正则，竖线表示任选一个模式。</p>
<h2>示例 3：错误前后信息</h2>
<pre><code class="language-bash">grep -n -A 12 -B 3 'FOAM FATAL' caseA/log.icoFoam
</code></pre>
<p>-n 标出行号，-A/-B 显示后 12 行和前 3 行。</p>
<h2>示例 4：搜索算例设置</h2>
<pre><code class="language-bash">grep -R -n 'div(phi,U)' caseA/system
</code></pre>
<p>递归查找字典中的对流项，附文件名和行号。</p>
<h2>示例 5：统计求解调用</h2>
<pre><code class="language-bash">grep -c 'Solving for p,' caseA/log.icoFoam
</code></pre>
<p>-c 返回匹配行数；一次时间步可能含多次压力校正。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/grep/manual/">源码与说明</a></p>
