---
title: "modifyMesh · 按配置字典执行拓扑修改"
layout: reference
description: "按配置字典执行拓扑修改。"
cms_slug: "command-modifymesh"
---

<p>按配置字典执行拓扑修改。</p><h2>开始前</h2>
<p>准备 system/modifyMeshDict，含 pointsToMove、edgesToSplit、facesToTriangulate、edgesToCollapse、cellsToSplit 五个列表。下列坐标以 0–1 的单六面体为说明，每例从独立原始副本开始，先清空其他操作列表。</p>
<h2>示例 1：移动一个边界点</h2>
<pre><code class="language-bash">foamDictionary system/modifyMeshDict -entry pointsToMove -set '(((0 0 0) (-0.01 0 0)))'
modifyMesh
</code></pre>
<p>每个元素包含两个点：第一个定位原边界点，第二个给出新坐标。这里把原点沿负 x 移动 0.01，输出后检查相邻单元体积和面质量。</p>
<h2>示例 2：在边界边上插入切点</h2>
<pre><code class="language-bash">foamDictionary system/modifyMeshDict -entry edgesToSplit -set '(((0.5 0 0) (0.25 0 0)))'
modifyMesh
</code></pre>
<p>第一个点用于查找 x 轴上的边，第二个点是插入位置。在该边的四分之一处增加切点，检查相关边界面的顶点连接。</p>
<h2>示例 3：把边界面分解为三角面</h2>
<pre><code class="language-bash">foamDictionary system/modifyMeshDict -entry facesToTriangulate -set '(((0.5 0.5 0) (0.5 0.5 0)))'
modifyMesh
</code></pre>
<p>用底面中心定位边界面，并以同一位置作为分解中心。查看生成三角面的数量、方向和总面积。</p>
<h2>示例 4：将单元分为锥形子单元</h2>
<pre><code class="language-bash">foamDictionary system/modifyMeshDict -entry cellsToSplit -set '(((0.5 0.5 0.5) (0.5 0.5 0.5)))'
modifyMesh
</code></pre>
<p>第一个点定位目标单元，第二个指定内部公共顶点。单元按各面与内部顶点构成锥形子单元，检查子单元体积之和与原体积。</p>
<h2>示例 5：使用独立字典并检查结果</h2>
<pre><code class="language-bash">modifyMesh -dict system/modifyMesh-testDict
checkMesh -latestTime -allGeometry -allTopology
</code></pre>
<p>在该字典中明确选择一种修改操作，默认写到新的时间实例。对最新网格检查几何和拓扑，再决定是否把方案用于正式案例。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: modifyMesh [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative modifyMeshDict
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
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -parallel         Run in parallel
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Manipulate mesh elements.
For example, moving points, splitting/collapsing edges etc.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/modifyMesh/cellSplitter.C">源码与说明</a> · <a href="/assets/command-help/modifymesh.txt">帮助文本</a></p>
