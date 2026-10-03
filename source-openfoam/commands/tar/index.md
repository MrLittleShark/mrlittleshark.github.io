---
title: "tar · 将多个文件和目录归档，也可提取已有归档中的文件"
layout: reference
description: "将多个文件和目录归档，也可提取已有归档中的文件。"
cms_slug: "command-tar"
---

<p>将多个文件和目录归档，也可提取已有归档中的文件。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：打包算例</h2>
<pre><code class="language-bash">tar -czf caseA.tar.gz caseA
</code></pre>
<p>-c 创建，-z gzip 压缩，-f 指定包名；原算例保留。</p>
<h2>示例 2：检查包内文件</h2>
<pre><code class="language-bash">tar -tzf caseA.tar.gz
</code></pre>
<p>-t 仅列出归档路径。</p>
<h2>示例 3：独立解压</h2>
<pre><code class="language-bash">mkdir -p unpacked
tar -xzf caseA.tar.gz -C unpacked
</code></pre>
<p>-x 解包，-C 选择输出目录，得到 unpacked/caseA。</p>
<h2>示例 4：只分享输入</h2>
<pre><code class="language-bash">tar -czf caseA-input.tar.gz -C caseA 0 constant system
</code></pre>
<p>收录三组输入；constant 下已有网格也包含在内。</p>
<h2>示例 5：排除日志和分区</h2>
<pre><code class="language-bash">tar -czf caseA-share.tar.gz --exclude='caseA/log*' --exclude='caseA/processor*' caseA
</code></pre>
<p>模式由 tar 处理，其他时间结果仍会被收录。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/tar/manual/">源码与说明</a></p>
