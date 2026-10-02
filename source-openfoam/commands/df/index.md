---
title: "df · 检查文件系统可用空间"
layout: reference
description: "检查文件系统可用空间。"
cms_slug: "command-df"
---

<p>检查文件系统可用空间。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：查看存储</h2>
<pre><code class="language-bash">df -h
</code></pre>
<p>列出容量、已用、可用及挂载点。</p>
<h2>示例 2：检查算例所在磁盘</h2>
<pre><code class="language-bash">df -h caseA
</code></pre>
<p>只显示包含算例的文件系统。</p>
<h2>示例 3：检查文件节点余量</h2>
<pre><code class="language-bash">df -i caseA
</code></pre>
<p>检查 inode，适用于大量小文件导致无法写入的情况。</p>
<h2>示例 4：以字节记录</h2>
<pre><code class="language-bash">df -B1 caseA
</code></pre>
<p>统一以字节显示，便于脚本比较。</p>
<h2>示例 5：比较主目录和临时目录</h2>
<pre><code class="language-bash">df -hT "$HOME" /tmp
</code></pre>
<p>-T 显示文件系统类型，可判断两个目录的存储来源。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/coreutils/manual/">源码与说明</a></p>
