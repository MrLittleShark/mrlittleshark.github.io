---
title: "temporalInterpolate · 在已有时间之间插值字段，增加可视化时间帧"
layout: reference
description: "在已有时间之间插值字段，增加可视化时间帧。"
cms_slug: "command-temporalinterpolate"
---

<p>在已有时间之间插值字段，增加可视化时间帧。</p><h2>开始前</h2>
<p>已有至少两个时间的相同字段，网格拓扑与字段寻址保持相容；插值结果用于时间数据重采样。</p>
<h2>示例 1：在相邻时刻增加中间帧</h2>
<pre><code class="language-bash">temporalInterpolate -time '0:1' -divisions 1
</code></pre>
<p>对所选已有时刻的每个相邻间隔插入1个中间时间，默认使用线性插值。</p>
<h2>示例 2：每个间隔增加三帧</h2>
<pre><code class="language-bash">temporalInterpolate -time '0:1' -divisions 3
</code></pre>
<p>原间隔被分成4段，写3个内部时刻，适合让动画变化更连续。</p>
<h2>示例 3：只插值速度与压力</h2>
<pre><code class="language-bash">temporalInterpolate -time '0:1' -fields '(U p)' -divisions 3
</code></pre>
<p>只创建U、p的中间数据，减少输出量，其余字段保留原时间分辨率。</p>
<h2>示例 4：采用样条时间插值</h2>
<pre><code class="language-bash">temporalInterpolate -time '0:2' -fields '(T)' -interpolationType spline -divisions 2
</code></pre>
<p>存在足够相邻温度快照时用样条方式，每间隔增加2帧；比较温度变化是否出现插值过冲。</p>
<h2>示例 5：插值多区域中的流体数据</h2>
<pre><code class="language-bash">temporalInterpolate -region fluid -time '0.1:0.5' -fields '(U)' -divisions 4
</code></pre>
<p>只给fluid速度添加时间帧，再用相同区域导出动画，保持其他区域数据不变。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: temporalInterpolate [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -divisions &lt;integer&gt;
                    Specify number of temporal sub-divisions to create (default
                    = 1).
  -fields &lt;wordRes&gt;
                    The fields (or field) to be interpolated. Eg, &#x27;(U T p
                    &quot;Y.*&quot;)&#x27; or a single field &#x27;U&#x27;
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -interpolationType &lt;word&gt;
                    The type of interpolation (linear or spline)
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Interpolate fields between time-steps. Eg, for animation.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/miscellaneous/temporalInterpolate/temporalInterpolate.C">源码与说明</a> · <a href="/assets/command-help/temporalinterpolate.txt">帮助文本</a></p>
