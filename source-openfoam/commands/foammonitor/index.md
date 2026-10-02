---
title: "foamMonitor · 用绘图工具查看并更新时序数据"
layout: reference
description: "用绘图工具查看并更新时序数据。"
cms_slug: "command-foammonitor"
---

<p>用绘图工具查看并更新时序数据。</p><h2>开始前</h2>
<p>需要带 X11 支持的 gnuplot。输入是一个时间—数据表，不是原始求解日志；下例路径按实际函数对象输出调整。每次调用接收一个文件。</p>
<h2>示例 1：监视残差</h2>
<pre><code class="language-bash">foamMonitor -logscale caseA/postProcessing/residuals/0/residuals.dat
</code></pre>
<p>对数纵轴便于观察多个数量级的残差衰减。</p>
<h2>示例 2：监视力系数</h2>
<pre><code class="language-bash">foamMonitor -grid caseA/postProcessing/forceCoeffs/0/coefficient.dat
</code></pre>
<p>绘制数据列并增加网格线，方便读取系数振荡。</p>
<h2>示例 3：提高刷新频率</h2>
<pre><code class="language-bash">foamMonitor -refresh 2 caseA/postProcessing/residuals/0/residuals.dat
</code></pre>
<p>每两秒重新读文件，适用于较快写出的计算。</p>
<h2>示例 4：聚焦一个时间窗</h2>
<pre><code class="language-bash">foamMonitor -xrange "[0.2:0.5]" caseA/postProcessing/residuals/0/residuals.dat
</code></pre>
<p>用给定范围限制横轴，便于观察局部阶段。</p>
<h2>示例 5：等待较慢的输出</h2>
<pre><code class="language-bash">foamMonitor -idle 600 -refresh 10 -logscale caseA/postProcessing/residuals/0/residuals.dat
</code></pre>
<p>文件连续 600 秒无变化才停止，避免长时间步被默认超时中断。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-g | -grid</code></td><td>Draw grid lines</td></tr><tr><td><code>-i | -idle &lt;time&gt;</code></td><td>Stop if &lt;file&gt; unchanging for &lt;time&gt; sec (default = 60)</td></tr><tr><td><code>-l | -logscale</code></td><td>Plot y-axis data on log scale</td></tr><tr><td><code>-r | -refresh &lt;time&gt;</code></td><td>Refresh display every &lt;time&gt; sec (default = 10)</td></tr><tr><td><code>-x | -xrange &lt;range&gt;</code></td><td>Set &lt;range&gt; of x-axis data, format &quot;[0:1]&quot;</td></tr><tr><td><code>-y | -yrange &lt;range&gt;</code></td><td>Set &lt;range&gt; of y-axis data, format &quot;[0:1]&quot;</td></tr><tr><td><code>-h | -help</code></td><td>Display short help and exit</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamMonitor [OPTIONS] &lt;file&gt;
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
