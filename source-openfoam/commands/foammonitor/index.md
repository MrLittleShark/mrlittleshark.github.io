---
title: "foamMonitor  实时绘制数值文件曲线"
layout: reference
description: "调用 Gnuplot 读取数值列文件。-r 2 将刷新间隔设为 2 s。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>调用 Gnuplot 读取数值列文件。-r 2 将刷新间隔设为 2 s。</p><h2>v2512 源码中的用途</h2><p>Monitor data with Gnuplot from time-value(s) graphs written by OpenFOAM e.g. by functionObjects - requires gnuplot, gnuplot_x11, sed, awk</p><h2>使用入口</h2><pre><code class="language-bash">foamLog log.simpleFoam
foamMonitor -l logs/p_0</code></pre><h2>使用条件与核对</h2><p>调用 Gnuplot 读取数值列文件。-r 2 将刷新间隔设为 2 s。 用法：foamMonitor [选项] 数据文件 示例：foamLog log.simpleFoam；foamMonitor -l logs/p_0
Monitor data with Gnuplot from time-value(s) graphs written by OpenFOAM e.g. by functionObjects - requires gnuplot, gnuplot_x11, sed, awk
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-g -h -i -l -r -x -y</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foammonitor.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamMonitor
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamMonitor

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamMonitor [OPTIONS] &lt;file&gt;
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

    foamMonitor -l postProcessing/residuals/0/residuals.dat</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamMonitor">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
