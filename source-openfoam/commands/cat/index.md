---
title: "cat · 查看短文本文件"
layout: reference
description: "查看短文本文件。"
cms_slug: "command-cat"
---

<p>查看短文本文件。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：阅读短字典</h2>
<pre><code class="language-bash">cat caseA/system/controlDict
</code></pre>
<p>将整个文件输出到终端。</p>
<h2>示例 2：显示行号</h2>
<pre><code class="language-bash">cat -n caseA/system/fvSolution
</code></pre>
<p>-n 逐行编号，便于与解析报错对应。</p>
<h2>示例 3：合并两份日志</h2>
<pre><code class="language-bash">cat mesh.log solver.log &gt; combined.log
</code></pre>
<p>按给定顺序连接文件，新生成 combined.log。</p>
<h2>示例 4：编写分解条目</h2>
<pre><code class="language-bash">cat &gt; decomposition-entry.txt &lt;&lt;'EOF'
numberOfSubdomains 4;
method scotch;
EOF
</code></pre>
<p>带引号的 EOF 使正文按字面保存，输出两项字典条目。</p>
<h2>示例 5：显示隐藏字符</h2>
<pre><code class="language-bash">cat -A caseA/Allrun
</code></pre>
<p>-A 显示行末和制表符，Windows 回车会显示为 ^M。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/coreutils/manual/">源码与说明</a></p>
