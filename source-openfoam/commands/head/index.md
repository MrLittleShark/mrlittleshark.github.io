---
title: "head · 查看文件开头"
layout: reference
description: "查看文件开头。"
cms_slug: "command-head"
---

<p>查看文件开头。</p><h2>开始前</h2>
<p>在 Bash 中创建独立练习目录：mkdir -p "$HOME/foam-command-lab"，再 cd "$HOME/foam-command-lab"。caseA 表示复制到其中的完整算例，caseB 为另一份副本；日志例子需先完成对应计算。</p>
<h2>示例 1：查看日志横幅</h2>
<pre><code class="language-bash">head caseA/log.icoFoam
</code></pre>
<p>默认显示前 10 行。</p>
<h2>示例 2：查看启动阶段</h2>
<pre><code class="language-bash">head -n 60 caseA/log.icoFoam
</code></pre>
<p>前 60 行通常包含所读文件、模型与初始检查。</p>
<h2>示例 3：检查测点坐标</h2>
<pre><code class="language-bash">head -n 8 caseA/postProcessing/probes/0/U
</code></pre>
<p>先生成 probes 输出；前几行记录测点及数据列。</p>
<h2>示例 4：对比启动日志</h2>
<pre><code class="language-bash">head -n 30 caseA/log.icoFoam caseB/log.icoFoam
</code></pre>
<p>每个输入附文件名标题，便于区分两次运行。</p>
<h2>示例 5：制作小型数据集</h2>
<pre><code class="language-bash">head -n 100 measurements.csv &gt; measurements-small.csv
</code></pre>
<p>取原文件前 100 行，保留首行标题。</p>
<h2>参考</h2><p><a href="https://www.gnu.org/software/coreutils/manual/">源码与说明</a></p>
