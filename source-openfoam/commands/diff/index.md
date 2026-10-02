---
title: "diff · 对比两份字典或日志"
layout: reference
description: "对比两份字典或日志。"
cms_slug: "command-diff"
---

<p>对比两份字典或日志。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：比较修改前后</h2>
<pre><code class="language-bash">diff controlDict.before caseA/system/controlDict
</code></pre>
<p>相同返回 0，有差异返回 1，并显示差异行。</p>
<h2>示例 2：带上下文比较</h2>
<pre><code class="language-bash">diff -u controlDict.before caseA/system/controlDict
</code></pre>
<p>统一格式包含相邻行，+ 是新行，- 是旧行。</p>
<h2>示例 3：比较设置目录</h2>
<pre><code class="language-bash">diff -ru caseA/system caseB/system
</code></pre>
<p>-r 递归进入子目录，比较两组数值设置。</p>
<h2>示例 4：忽略空格差异</h2>
<pre><code class="language-bash">diff -w caseA/system/fvSchemes caseB/system/fvSchemes
</code></pre>
<p>-w 忽略空白变化，便于检查实际条目。</p>
<h2>示例 5：仅列出不同文件</h2>
<pre><code class="language-bash">diff -rq caseA/constant caseB/constant
</code></pre>
<p>-q 不展开差异内容，先定位物性和网格变化。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/diffutils/manual/">源码与说明</a></p>
