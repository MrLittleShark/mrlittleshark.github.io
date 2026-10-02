---
title: "cumulativeDisplacement · 计算各时刻网格点相对 constant 参考网格的位移及法向分量"
layout: reference
description: "计算各时刻网格点相对 constant 参考网格的位移及法向分量。"
cms_slug: "command-cumulativedisplacement"
---

<p>计算各时刻网格点相对 constant 参考网格的位移及法向分量。</p><h2>开始前</h2>
<p>constant保存初始points，各结果时刻点编号和点数与其相容；适合无重编号、无拓扑改变的形变序列。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：计算最终几何变化</h2>
<pre><code class="language-bash">cumulativeDisplacement -latestTime
</code></pre>
<p>生成点向量场displacement及边界点法向位移normalDisplacement，以constant网格为参考。</p>
<h2>示例 2：处理整个形变阶段</h2>
<pre><code class="language-bash">cumulativeDisplacement -time '0.1:1'
</code></pre>
<p>对区间内每个已有网格状态计算参考位移，便于观察变形如何随时间积累。</p>
<h2>示例 3：只处理某个区域</h2>
<pre><code class="language-bash">cumulativeDisplacement -region solid -latestTime
</code></pre>
<p>对solid区域网格计算位移，适合多区域中的结构形变检查。</p>
<h2>示例 4：计算分区网格的位移</h2>
<pre><code class="language-bash">mpirun -np 4 cumulativeDisplacement -parallel -latestTime
</code></pre>
<p>已有4分区且各时间点寻址一致；在分区上计算并同步边界点法向信息。</p>
<h2>示例 5：导出变形场</h2>
<pre><code class="language-bash">cumulativeDisplacement -latestTime
foamToVTK -latestTime -fields '(displacement normalDisplacement)' -name VTK-displacement
</code></pre>
<p>将生成的点场与网格一起导出，用法向位移检查表面局部鼓起或收缩，用向量场查看整体方向。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: cumulativeDisplacement [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
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
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/optimisation/cumulativeDisplacement/cumulativeDisplacement.C">源码与说明</a> · <a href="/assets/command-help/cumulativedisplacement.txt">帮助文本</a></p>
