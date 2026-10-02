---
title: "singleCellMesh · 将场映射到内部面被移除的 singleCell 区域网格"
layout: reference
description: "将场映射到内部面被移除的 singleCell 区域网格。"
cms_slug: "command-singlecellmesh"
---

<p>将场映射到内部面被移除的 singleCell 区域网格。</p><h2>开始前</h2>
<p>已有体网格和结果场；输出区域名为 singleCell，适合保留边界信息并压缩内部表示。</p>
<h2>示例 1：生成简化区域</h2>
<pre><code class="language-bash">singleCellMesh
</code></pre>
<p>读取选择的结果时间，创建 singleCell 网格并映射场，输出到该区域的对应时间位置。</p>
<h2>示例 2：只处理最终结果</h2>
<pre><code class="language-bash">singleCellMesh -latestTime
</code></pre>
<p>选择最后一个保存时刻，减少转换量，适合展示最终边界分布。</p>
<h2>示例 3：转换一段结果历史</h2>
<pre><code class="language-bash">singleCellMesh -time '0.1:0.5'
</code></pre>
<p>处理区间内已有时刻，保留这一段的简化场时间序列。</p>
<h2>示例 4：跳过初始状态</h2>
<pre><code class="language-bash">singleCellMesh -noZero
</code></pre>
<p>处理已有结果而排除0时刻，适合只整理求解后的边界数据。</p>
<h2>示例 5：导出简化区域</h2>
<pre><code class="language-bash">singleCellMesh -latestTime
foamToVTK -region singleCell -latestTime -name VTK-singleCell
</code></pre>
<p>先创建最后状态的简化区域，再导出该区域到独立VTK目录，用于边界数据可视化。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: singleCellMesh [OPTIONS]
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

Map fields to a mesh with all internal faces removed (singleCellFvMesh) which
gets written to region &#x27;singleCell&#x27;

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/singleCellMesh/singleCellMesh.C">源码与说明</a> · <a href="/assets/command-help/singlecellmesh.txt">帮助文本</a></p>
