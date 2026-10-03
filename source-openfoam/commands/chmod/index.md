---
title: "chmod · 修改文件或目录的读、写和执行权限"
layout: reference
description: "修改文件或目录的读、写和执行权限。"
cms_slug: "command-chmod"
---

<p>修改文件或目录的读、写和执行权限。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：运行自编脚本</h2>
<pre><code class="language-bash">chmod u+x caseA/Allrun
./caseA/Allrun
</code></pre>
<p>u+x 给所有者增加执行位；脚本首行需指定正确解释器。</p>
<h2>示例 2：设置两个脚本</h2>
<pre><code class="language-bash">chmod u+x caseA/Allrun caseA/Allclean
</code></pre>
<p>保留读写权限，同时增加执行权限。</p>
<h2>示例 3：保护个人设置</h2>
<pre><code class="language-bash">chmod 600 project.env
</code></pre>
<p>只有所有者可读写。</p>
<h2>示例 4：分享只读笔记</h2>
<pre><code class="language-bash">chmod 644 notes.txt
</code></pre>
<p>所有者可写，组和其他用户可读；父目录还需允许进入。</p>
<h2>示例 5：设置共享目录</h2>
<pre><code class="language-bash">mkdir -p shared-results
chmod 755 shared-results
</code></pre>
<p>所有者可写，其他用户可列出和进入；各文件权限单独管理。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/coreutils/manual/">源码与说明</a></p>
