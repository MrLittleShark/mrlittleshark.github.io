---
title: "cloneParallelCase · 复制已分区的算例及选定时间数据"
layout: reference
description: "复制已分区的算例及选定时间数据。"
cms_slug: "command-cloneparallelcase"
---

<p>复制已分区的算例及选定时间数据。</p><h2>开始前</h2>
<p>先在单独一行执行 source "$WM_PROJECT_DIR/bin/tools/RunFunctions"。示例在个人算例工作区操作，caseA、caseB 均为可修改的副本。 源为未合并存储的并行算例，含 processor0 等目录及各自 constant；目标须不存在。指定时间按目录名字精确匹配。</p>
<h2>示例 1：复制所有分区数据</h2>
<pre><code class="language-bash">cloneParallelCase caseA parallel-copy
</code></pre>
<p>复制顶层 constant/system 和所有 processor* 目录。</p>
<h2>示例 2：只取初始时刻</h2>
<pre><code class="language-bash">cloneParallelCase caseA parallel-zero 0
</code></pre>
<p>每个子域复制 constant 和存在的 0 时间目录。</p>
<h2>示例 3：取某个重启时刻</h2>
<pre><code class="language-bash">cloneParallelCase caseA restart-05 0.5
</code></pre>
<p>要求子域内实际存在 0.5；复制后将 controlDict 的起始设置对应到该时刻。</p>
<h2>示例 4：保留两个时刻</h2>
<pre><code class="language-bash">cloneParallelCase caseA compare-times 0.5 1
</code></pre>
<p>各分区只收录指定时刻和 constant，便于比较或分享。</p>
<h2>示例 5：组织重启试验</h2>
<pre><code class="language-bash">mkdir -p restart-study
cloneParallelCase caseA restart-study/base 1
cloneParallelCase caseA restart-study/variant 1
</code></pre>
<p>从同一已写出时刻生成两份分区算例，用于修改后续运行设置。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
