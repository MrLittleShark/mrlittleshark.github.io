---
title: "ls · 列出文件与目录"
layout: reference
description: "列出文件与目录。"
cms_slug: "command-ls"
---

<p>列出文件与目录。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：查看目录</h2>
<pre><code class="language-bash">ls caseA
</code></pre>
<p>列出初始场、物性、系统设置与已写出的时间目录。</p>
<h2>示例 2：查看权限和大小</h2>
<pre><code class="language-bash">ls -lh caseA/system
</code></pre>
<p>-l 输出详细信息，-h 以易读单位显示大小。</p>
<h2>示例 3：查看隐藏文件</h2>
<pre><code class="language-bash">ls -a caseA
</code></pre>
<p>-a 包括以点号开头的文件，如 .gitignore。</p>
<h2>示例 4：按更新时间排列日志</h2>
<pre><code class="language-bash">ls -lt caseA/log.*
</code></pre>
<p>-t 把最近修改的日志放在前面，便于找到最新一轮计算。</p>
<h2>示例 5：列出并行子域</h2>
<pre><code class="language-bash">ls -d caseA/processor*/
</code></pre>
<p>-d 仅显示目录名。未合并存储时可看到各 processor 子域。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/coreutils/manual/">源码与说明</a></p>
