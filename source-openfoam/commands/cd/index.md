---
title: "cd · 切换工作目录；含空格的路径使用引号"
layout: reference
description: "切换工作目录；含空格的路径使用引号。"
cms_slug: "command-cd"
---

<p>切换工作目录；含空格的路径使用引号。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：进入算例</h2>
<pre><code class="language-bash">cd caseA
pwd
</code></pre>
<p>相对路径从当前目录出发，pwd 检查结果。</p>
<h2>示例 2：返回上层</h2>
<pre><code class="language-bash">cd system
cd ..
</code></pre>
<p>从算例根目录执行；先进入 system，再回到算例。</p>
<h2>示例 3：返回上一位置</h2>
<pre><code class="language-bash">cd "$WM_PROJECT_DIR/src"
cd -
</code></pre>
<p>cd - 返回之前的位置，并打印路径。</p>
<h2>示例 4：处理路径中的空格</h2>
<pre><code class="language-bash">mkdir -p "mesh tests"
cd "mesh tests"
</code></pre>
<p>双引号将整个目录名作为一个参数。</p>
<h2>示例 5：在子目录完成一个任务</h2>
<pre><code class="language-bash">(cd caseA &amp;&amp; blockMesh)
pwd
</code></pre>
<p>&amp;&amp; 使切换失败时不运行网格程序；子 shell 结束后仍在原目录。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/bash/manual/">源码与说明</a></p>
