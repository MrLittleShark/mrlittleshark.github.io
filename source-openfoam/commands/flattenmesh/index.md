---
title: "flattenMesh · 把二维笛卡尔网格的前后顶点校正到两个平面"
layout: reference
description: "把二维笛卡尔网格的前后顶点校正到两个平面。"
cms_slug: "command-flattenmesh"
---

<p>把二维笛卡尔网格的前后顶点校正到两个平面。</p><h2>开始前</h2>
<p>网格已有正确的二维 empty 边界，前后面沿同一坐标方向；程序直接重写所读 points。</p>
<h2>示例 1：校正轻微不共面的顶点</h2>
<pre><code class="language-bash">flattenMesh
</code></pre>
<p>程序识别二维法向，把两侧顶点分别放到包围盒的两个端平面，输出修正后的 points 路径。</p>
<h2>示例 2：在案例副本上比较几何</h2>
<pre><code class="language-bash">cp -r planarCase planarCase-flat
flattenMesh -case planarCase-flat
</code></pre>
<p>输入 planarCase 为现有薄层二维网格；结果写在独立副本，便于并排查看前后面平整程度。</p>
<h2>示例 3：和网格检查连续使用</h2>
<pre><code class="language-bash">flattenMesh
checkMesh -allGeometry
</code></pre>
<p>完成平面校正后检查几何，重点观察二维方向、面平面性和单元体积。拓扑仍来自原网格。</p>
<h2>示例 4：处理导入的二维网格</h2>
<pre><code class="language-bash">fluentMeshToFoam channel.msh
flattenMesh
checkMesh
</code></pre>
<p>channel.msh 已按薄层二维方式生成并含可识别的 empty 边界；导入后校正坐标舍入误差，再检查网格。</p>
<h2>示例 5：导出校正后的几何</h2>
<pre><code class="language-bash">flattenMesh
foamToVTK -no-fields -name VTK-flat
</code></pre>
<p>将校正后的网格导出到 VTK-flat，关闭场输出；可在 ParaView 中检查前后平面和薄层厚度。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: flattenMesh [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
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
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Flattens the front and back planes of a 2D cartesian mesh

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/flattenMesh/flattenMesh.C">源码与说明</a> · <a href="/assets/command-help/flattenmesh.txt">帮助文本</a></p>
