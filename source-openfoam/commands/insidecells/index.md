---
title: "insideCells · 按单元中心是否位于封闭表面内部创建 cellSet"
layout: reference
description: "按单元中心是否位于封闭表面内部创建 cellSet。"
cms_slug: "command-insidecells"
---

<p>按单元中心是否位于封闭表面内部创建 cellSet。</p><h2>开始前</h2>
<p>已生成体网格；输入曲面必须封闭、单连通，曲面与网格使用同一坐标和单位。</p>
<h2>示例 1：选出球体内的单元</h2>
<pre><code class="language-bash">insideCells constant/triSurface/sphere.stl sphereCells
</code></pre>
<p>第一个参数是封闭曲面，第二个是输出 cellSet 名；中心位于球内的单元写入 sphereCells。</p>
<h2>示例 2：检查选区位置</h2>
<pre><code class="language-bash">insideCells constant/triSurface/solid.stl solidCells
foamToVTK -cellSet solidCells -no-fields
</code></pre>
<p>先创建选区，再仅导出这些单元的几何，检查曲面与网格是否对齐。</p>
<h2>示例 3：将选区变成体区域</h2>
<pre><code class="language-bash">insideCells constant/triSurface/heater.stl heater
setsToZones -noFlipMap
</code></pre>
<p>建立 heater cellSet，再生成同名 cellZone，供体积热源或多孔区模型引用；-noFlipMap 简化可能同时存在的 faceSet 转换。</p>
<h2>示例 4：从曲面内提取子网格</h2>
<pre><code class="language-bash">insideCells constant/triSurface/core.stl coreCells
subsetMesh coreCells -resultTime 1
</code></pre>
<p>先选 coreCells，再把所选单元组成子网格并写到时间 1。新增切割面默认进入 oldInternalFaces。</p>
<h2>示例 5：选择另一个案例中的物体</h2>
<pre><code class="language-bash">insideCells -case ./fineMesh ./geometry/body.stl bodyCells
</code></pre>
<p>fineMesh 是已有细网格案例；曲面路径按当前工作目录提供，-case 指定 cellSet 写入的目标案例，用于网格细化后的同一几何选区。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: insideCells [OPTIONS] &lt;surfaceFile&gt; &lt;cellSet&gt;
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

Create a cellSet for cells with their centres &#x27;inside&#x27; the defined surface.
Surface must be closed and singly connected.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/insideCells/insideCells.C">源码与说明</a> · <a href="/assets/command-help/insidecells.txt">帮助文本</a></p>
