---
title: "collapseEdges · 读取 collapseDict 或指定字典，折叠操作可改变网格拓扑"
layout: reference
description: "读取 collapseDict 或指定字典，折叠操作可改变网格拓扑。"
cms_slug: "command-collapseedges"
---

<p>读取 collapseDict 或指定字典，折叠操作可改变网格拓扑。</p><h2>开始前</h2>
<p>准备网格和 system/collapseDict，至少含 collapseEdgesCoeffs.minimumEdgeLength 与 maximumMergeAngle；长度采用网格单位。在独立副本试验。</p>
<h2>示例 1：按现有阈值合并短边</h2>
<pre><code class="language-bash">collapseEdges
</code></pre>
<p>读取 collapseDict 合并满足条件的短边，并写出修改后的网格。检查点数、面数及质量变化，判断简化是否保留目标结构。</p>
<h2>示例 2：设置绝对短边阈值</h2>
<pre><code class="language-bash">foamDictionary system/collapseDict -entry collapseEdgesCoeffs.minimumEdgeLength -set 0.0001
collapseEdges
</code></pre>
<p>米制网格以 0.1 mm 为短边阈值。该长度应小于需要保留的真实几何细节，结果需核对薄壁和窄间隙。</p>
<h2>示例 3：使用另一份简化参数</h2>
<pre><code class="language-bash">collapseEdges -dict system/collapseConservativeDict
</code></pre>
<p>从独立字典读取更保守的长度与角度设置，便于在相同原始网格副本上比较不同简化强度。</p>
<h2>示例 4：同时处理可折叠的面</h2>
<pre><code class="language-bash">collapseEdges -collapseFaces
</code></pre>
<p>前提是 collapseDict 中也已配置 collapseFacesCoeffs。允许按面形状把部分面折叠为边或点，适合处理细长小面，之后检查单元质量。</p>
<h2>示例 5：限定间接处理面集</h2>
<pre><code class="language-bash">collapseEdges -collapseFaceSet targetFaces -overwrite
checkMesh -constant -allGeometry
</code></pre>
<p>使用已有 targetFaces 指定需要处理的面集合，并把结果写回原实例。-collapseFaceSet 与 -collapseFaces 是两种互斥的面处理方式；短边过滤仍会先进行，完成后检查集合邻域及网格质量。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-collapseFaces</code></td><td>Collapse small and sliver faces as well as small edges</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: collapseEdges [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -collapseFaceSet &lt;faceSet&gt;
                    Collapse faces that are in the supplied face set
  -collapseFaces    Collapse small and sliver faces as well as small edges
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative collapseDict
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
  -overwrite        Overwrite existing mesh/results files
  -parallel         Run in parallel
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

Collapses small edges to a point.
Optionally collapse small faces to a point and thin faces to an edge.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/collapseEdges/collapseEdges.C">源码与说明</a> · <a href="/assets/command-help/collapseedges.txt">帮助文本</a></p>
