---
title: "find · 在目录树中按文件名、类型和时间等条件查找文件"
layout: reference
description: "在目录树中按文件名、类型和时间等条件查找文件。"
cms_slug: "command-find"
---

<p>在目录树中按文件名、类型和时间等条件查找文件。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：寻找控制字典</h2>
<pre><code class="language-bash">find . -type f -name controlDict
</code></pre>
<p>递归搜索普通文件，打印相对路径。</p>
<h2>示例 2：只看直接子目录</h2>
<pre><code class="language-bash">find caseA -maxdepth 1 -type d
</code></pre>
<p>深度 1 避免进入各时间目录内部。</p>
<h2>示例 3：寻找大文件</h2>
<pre><code class="language-bash">find caseA -type f -size +100M
</code></pre>
<p>筛选超过 100 MiB 的普通文件。</p>
<h2>示例 4：寻找最近修改的设置</h2>
<pre><code class="language-bash">find caseA/system -type f -mtime -1
</code></pre>
<p>-mtime -1 筛选不足 24 小时内修改的文件。</p>
<h2>示例 5：批量读取求解器</h2>
<pre><code class="language-bash">find runs -type f -path '*/system/controlDict' -exec foamDictionary {} -entry application -value \;
</code></pre>
<p>runs 中先准备多个算例；{} 替换为每个找到的文件。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/findutils/manual/">源码与说明</a></p>
