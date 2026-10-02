---
title: "pwd · 显示当前工作目录"
layout: reference
description: "显示当前工作目录。"
cms_slug: "command-pwd"
---

<p>显示当前工作目录。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：查看当前位置</h2>
<pre><code class="language-bash">cd caseA
pwd
</code></pre>
<p>输出算例的绝对路径，后续相对路径从这里起算。</p>
<h2>示例 2：传递绝对路径</h2>
<pre><code class="language-bash">caseDir=$(pwd)
checkMesh -case "$caseDir"
</code></pre>
<p>在算例目录执行。命令替换保存路径，双引号允许路径含空格。</p>
<h2>示例 3：识别目录链接</h2>
<pre><code class="language-bash">ln -s caseA case-link
cd case-link
pwd -L
pwd -P
</code></pre>
<p>-L 显示逻辑路径，-P 显示解析符号链接后的真实路径。</p>
<h2>示例 4：逐个定位算例</h2>
<pre><code class="language-bash">for c in caseA caseB; do (cd "$c" &amp;&amp; pwd); done
</code></pre>
<p>每个子 shell 打印算例路径，循环结束后父目录不变。</p>
<h2>示例 5：记录检查位置</h2>
<pre><code class="language-bash">{ pwd; date; checkMesh -case caseA; } &gt; mesh-report.txt 2&gt;&amp;1
</code></pre>
<p>报告先记录执行目录和日期，再保存网格检查输出。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/bash/manual/">源码与说明</a></p>
