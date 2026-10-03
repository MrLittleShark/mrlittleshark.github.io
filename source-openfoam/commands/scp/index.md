---
title: "scp · 通过 SSH 在本机与远程计算机之间复制文件"
layout: reference
description: "通过 SSH 在本机与远程计算机之间复制文件。"
cms_slug: "command-scp"
---

<p>通过 SSH 在本机与远程计算机之间复制文件。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：上传字典</h2>
<pre><code class="language-bash">scp caseA/system/controlDict student@compute.example.org:~/cases/caseA/system/
</code></pre>
<p>远端目标目录需预先建立。</p>
<h2>示例 2：下载日志</h2>
<pre><code class="language-bash">scp student@compute.example.org:~/cases/caseA/log.icoFoam ./remote-icoFoam.log
</code></pre>
<p>将日志下载并改名，保留远端文件。</p>
<h2>示例 3：上传目录</h2>
<pre><code class="language-bash">scp -r caseA student@compute.example.org:~/cases/
</code></pre>
<p>-r 递归复制完整算例。</p>
<h2>示例 4：指定服务端口</h2>
<pre><code class="language-bash">scp -P 2222 caseA/system/fvSchemes student@compute.example.org:~/cases/caseA/system/
</code></pre>
<p>scp 用大写 -P 指定端口。</p>
<h2>示例 5：下载两份报告</h2>
<pre><code class="language-bash">scp student@compute.example.org:~/cases/caseA/log.blockMesh student@compute.example.org:~/cases/caseA/log.checkMesh ./
</code></pre>
<p>多个源文件后跟一个目标目录，复制两份独立日志。</p>
<h2>参考</h2><p><a href="https://www.openssh.com/manual.html">源码与说明</a></p>
