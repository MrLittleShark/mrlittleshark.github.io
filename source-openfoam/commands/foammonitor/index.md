---
title: "foamMonitor · 用绘图工具查看并更新时序数据"
layout: reference
description: "用绘图工具查看并更新时序数据。"
cms_slug: "command-foammonitor"
---

<p>用绘图工具查看并更新时序数据。</p><h2>绘制压力残差</h2>
<pre><code class="language-bash">foamLog log.simpleFoam
foamMonitor -l logs/p_0
</code></pre>
<p>先将求解日志转成列数据，再绘图。该脚本依赖相应绘图程序；文件名称以 <code>foamLog</code> 输出为准。</p>
<h2>绘制多个分量</h2>
<pre><code class="language-bash">foamMonitor -l logs/Ux_0
</code></pre>
<p>该命令一次读取一个文件。另开终端运行 foamMonitor -l logs/Uy_0，可分别观察两个速度分量。多列数据则可放在同一文件中绘图。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-g | -grid</td><td>Draw grid lines</td></tr><tr><td>-i | -idle &lt;time&gt;</td><td>Stop if &lt;file&gt; unchanging for &lt;time&gt; sec (default = 60)</td></tr><tr><td>-l | -logscale</td><td>Plot y-axis data on log scale</td></tr><tr><td>-r | -refresh &lt;time&gt;</td><td>Refresh display every &lt;time&gt; sec (default = 10)</td></tr><tr><td>-x | -xrange &lt;range&gt;</td><td>Set &lt;range&gt; of x-axis data, format &quot;[0:1]&quot;</td></tr><tr><td>-y | -yrange &lt;range&gt;</td><td>Set &lt;range&gt; of y-axis data, format &quot;[0:1]&quot;</td></tr><tr><td>-h | -help</td><td>Display short help and exit</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamMonitor [OPTIONS] &lt;file&gt;
Options:
  -g | -grid            Draw grid lines
  -i | -idle &lt;time&gt;     Stop if &lt;file&gt; unchanging for &lt;time&gt; sec (default = 60)
  -l | -logscale        Plot y-axis data on log scale
  -r | -refresh &lt;time&gt;  Refresh display every &lt;time&gt; sec (default = 10)
  -x | -xrange &lt;range&gt;  Set &lt;range&gt; of x-axis data, format &quot;[0:1]&quot;
  -y | -yrange &lt;range&gt;  Set &lt;range&gt; of y-axis data, format &quot;[0:1]&quot;
  -h | -help            Display short help and exit

Monitor data with Gnuplot from time-value(s) graphs written by OpenFOAM
e.g. by functionObjects. For example,

    foamMonitor -l postProcessing/residuals/0/residuals.dat</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamMonitor">源码与说明</a> · <a href="/assets/command-help/foammonitor.txt">帮助文本</a></p>
