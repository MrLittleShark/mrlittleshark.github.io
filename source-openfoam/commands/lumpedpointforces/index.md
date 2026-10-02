---
title: "lumpedPointForces · 从压力场提取 lumped-point 运动区域的合力和力矩"
layout: reference
description: "从压力场提取 lumped-point 运动区域的合力和力矩。"
cms_slug: "command-lumpedpointforces"
---

<p>从压力场提取 lumped-point 运动区域的合力和力矩。</p><h2>开始前</h2>
<p>案例采用lumpedPoint边界及运动描述，所选时间已有p；压力积分区域与参考点设置完整。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：提取最终载荷</h2>
<pre><code class="language-bash">lumpedPointForces -latestTime
</code></pre>
<p>读取最新压力，按集中点控制区计算合力、力矩并打印，适合核对结构输入载荷。</p>
<h2>示例 2：输出载荷可视化</h2>
<pre><code class="language-bash">lumpedPointForces -latestTime -vtk
</code></pre>
<p>额外生成力和力矩的VTP几何及文件序列，便于查看各控制点的载荷方向。</p>
<h2>示例 3：提取整个载荷阶段</h2>
<pre><code class="language-bash">lumpedPointForces -time '0.1:1' -vtk
</code></pre>
<p>对区间内已有时刻计算，形成载荷随时间变化的可视化序列。</p>
<h2>示例 4：只处理指定流体区域</h2>
<pre><code class="language-bash">lumpedPointForces -region fluid -latestTime -vtk
</code></pre>
<p>多区域案例中从fluid的p与耦合边界提取载荷，结果对应该区域的控制点。</p>
<h2>示例 5：并行场的载荷积分</h2>
<pre><code class="language-bash">mpirun -np 4 lumpedPointForces -parallel -latestTime -vtk
</code></pre>
<p>已有4分区且lumped-point设置一致；归集各分区压力贡献，得到全局控制区合力和力矩。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-vtk</code></td><td>Create visualization files of the forces</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: lumpedPointForces [OPTIONS]
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
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -vtk              Create visualization files of the forces
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Extract force/moment information from simulation results that use the lumped
points movement description.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/lumped/lumpedPointForces/lumpedPointForces.C">源码与说明</a> · <a href="/assets/command-help/lumpedpointforces.txt">帮助文本</a></p>
