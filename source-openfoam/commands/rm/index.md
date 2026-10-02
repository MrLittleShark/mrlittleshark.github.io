---
title: "rm · 删除文件；删除前逐项核对路径，删除通常无法撤销"
layout: reference
description: "删除文件；删除前逐项核对路径，删除通常无法撤销。"
cms_slug: "command-rm"
---

<p>删除文件；删除前逐项核对路径，删除通常无法撤销。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：删除单个临时文件</h2>
<pre><code class="language-bash">printf 'temporary\n' &gt; discard.txt
rm -i discard.txt
</code></pre>
<p>删除本例新建的文件，-i 会先询问。</p>
<h2>示例 2：指定多个文件</h2>
<pre><code class="language-bash">touch trial-a.tmp trial-b.tmp trial-c.tmp
rm -i trial-a.tmp trial-b.tmp trial-c.tmp
</code></pre>
<p>逐个确认，明确控制处理范围。</p>
<h2>示例 3：删除特殊名字</h2>
<pre><code class="language-bash">touch -- -temporary
rm -i -- -temporary
</code></pre>
<p>-- 之后按文件名处理，短横线不再表示选项。</p>
<h2>示例 4：删除独立测试目录</h2>
<pre><code class="language-bash">trialDir=$(mktemp -d "$PWD/rm-demo.XXXXXX")
printf 'sample\n' &gt; "$trialDir/output.txt"
rm -rI -- "$trialDir"
</code></pre>
<p>-r 递归处理，-I 在递归删除前询问一次；变量只指向新建目录。</p>
<h2>示例 5：筛选临时输出</h2>
<pre><code class="language-bash">mkdir -p disposable
touch disposable/a.tmp disposable/keep.txt
find disposable -type f -name '*.tmp' -exec rm -i -- {} \;
</code></pre>
<p>只匹配 .tmp 文件，逐个确认；keep.txt 保留。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/coreutils/manual/">源码与说明</a></p>
