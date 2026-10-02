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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-g | -grid</code></td><td>显示图中的网格线。</td></tr><tr><td><code>-i | -idle &lt;time&gt;</code></td><td>文件连续指定秒数未变化时停止监控，默认为 60 秒。</td></tr><tr><td><code>-l | -logscale</code></td><td>将 y 轴设为对数刻度。</td></tr><tr><td><code>-r | -refresh &lt;time&gt;</code></td><td>按指定秒数刷新图形，默认为 10 秒。</td></tr><tr><td><code>-x | -xrange &lt;range&gt;</code></td><td>设置 x 轴范围，例如 &#x27;[0:1]&#x27;。</td></tr><tr><td><code>-y | -yrange &lt;range&gt;</code></td><td>设置 y 轴范围，例如 &#x27;[0:1]&#x27;。</td></tr><tr><td><code>-h | -help</code></td><td>显示简要帮助并退出。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamMonitor">源码与说明</a> · <a href="/assets/command-help/foammonitor.txt">帮助文本</a></p>
