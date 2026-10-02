---
title: "du · 检查算例或结果目录的存储占用"
layout: reference
description: "检查算例或结果目录的存储占用。"
cms_slug: "command-du"
---

<p>检查算例或结果目录的存储占用。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：汇总算例占用</h2>
<pre><code class="language-bash">du -sh caseA
</code></pre>
<p>-s 汇总磁盘实际占用，-h 使用易读单位。</p>
<h2>示例 2：展开一级目录</h2>
<pre><code class="language-bash">du -h --max-depth=1 caseA
</code></pre>
<p>分别列出时间目录、constant 等的磁盘占用。</p>
<h2>示例 3：比较两套算例</h2>
<pre><code class="language-bash">du -sh caseA caseB
</code></pre>
<p>每个输入输出一行。</p>
<h2>示例 4：按占用排序</h2>
<pre><code class="language-bash">du -h --max-depth=1 caseA | sort -h
</code></pre>
<p>最大值在末尾，总目录的汇总项也参与排序。</p>
<h2>示例 5：获取逻辑字节数</h2>
<pre><code class="language-bash">du -sb caseA
</code></pre>
<p>-b 统计 apparent size；稀疏文件逻辑尺寸可大于磁盘实际占用。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/coreutils/manual/">源码与说明</a></p>
