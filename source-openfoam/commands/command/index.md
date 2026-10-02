---
title: "command · 查询外部程序的实际位置"
layout: reference
description: "查询外部程序的实际位置。"
cms_slug: "command-command"
---

<p>查询外部程序的实际位置。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：定位程序</h2>
<pre><code class="language-bash">command -v blockMesh
</code></pre>
<p>返回 PATH 中选中的程序；未找到则退出非零。</p>
<h2>示例 2：检查可选依赖</h2>
<pre><code class="language-bash">if command -v gnuplot &gt;/dev/null; then echo "gnuplot available"; fi
</code></pre>
<p>成功时进入分支，适用于绘图前的依赖检查。</p>
<h2>示例 3：绕过同名函数</h2>
<pre><code class="language-bash">command cp caseA/system/controlDict controlDict.copy
</code></pre>
<p>跳过名为 cp 的 shell 函数；已展开的 alias 另行处理。</p>
<h2>示例 4：区分命令类别</h2>
<pre><code class="language-bash">command -V source
command -V blockMesh
</code></pre>
<p>-V 给出描述，区分内建命令和外部文件。</p>
<h2>示例 5：保存程序路径</h2>
<pre><code class="language-bash">meshProgram=$(command -v blockMesh) || exit 1
"$meshProgram" -case caseA
</code></pre>
<p>用于脚本，查找失败立即退出；成功后按绝对路径生成网格。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/bash/manual/">源码与说明</a></p>
