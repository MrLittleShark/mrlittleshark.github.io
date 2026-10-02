---
title: "foamSolverSweeps · 启动后交互输入日志名，如 log.simpleFoam"
layout: reference
description: "启动后交互输入日志名，如 log.simpleFoam。脚本按预设的旧式日志行格式提取统计量。"
cms_slug: "command-foamsolversweeps"
---

<p>启动后交互输入日志名，如 log.simpleFoam。脚本按预设的旧式日志行格式提取统计量。</p><h2>开始前</h2>
<p>这是读取日志的交互脚本，启动后从标准输入读一个文件名；统计固定格式的压力 p 和 U 求解行。日志中的 No Iterations 数值需位于第 15 个空白分隔字段；脚本使用固定 /tmp/FOAM_iters.* 临时文件，多个统计顺序执行。</p>
<h2>示例 1：统计一次方腔求解</h2>
<pre><code class="language-bash">printf '%s\n' caseA/log.icoFoam | foamSolverSweeps
</code></pre>
<p>打印执行时间范围、时间步数量、p 和 U 的累计迭代次数。</p>
<h2>示例 2：比较两组网格</h2>
<pre><code class="language-bash">for c in coarse fine; do printf '%s\n' "$c/log.icoFoam" | foamSolverSweeps; done
</code></pre>
<p>先准备两组对应日志，按顺序统计离散规模对求解迭代的影响。</p>
<h2>示例 3：比较压力求解设置</h2>
<pre><code class="language-bash">printf '%s\n' log.pressure-PCG | foamSolverSweeps
printf '%s\n' log.pressure-GAMG | foamSolverSweeps
</code></pre>
<p>两个日志应来自相同物理条件下的不同压力线性求解设置；对比累计 sweep 数。</p>
<h2>示例 4：保留统计结果</h2>
<pre><code class="language-bash">printf '%s\n' caseA/log.icoFoam | foamSolverSweeps &gt; sweeps.txt
</code></pre>
<p>生成简短汇总，可与网格规模和运行时间一起记录。</p>
<h2>示例 5：统计连续重启日志</h2>
<pre><code class="language-bash">cat log.part1 log.part2 &gt; log.combined
printf '%s\n' log.combined | foamSolverSweeps
</code></pre>
<p>按时间顺序合并两段互不重复的日志，得到全过程累计统计。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamSolverSweeps">源码与说明</a> · <a href="/assets/command-help/foamsolversweeps.txt">帮助文本</a></p>
