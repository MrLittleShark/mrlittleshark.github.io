---
title: "checkMesh · 检查网格拓扑、几何形状与质量，并定位问题区域"
layout: reference
description: "检查网格拓扑、几何形状与质量，并定位问题区域。"
cms_slug: "command-checkmesh"
---

<p>检查网格拓扑、几何形状与质量，并定位问题区域。</p><h2>读取基本检查结果</h2>
<pre><code class="language-bash">checkMesh
</code></pre>
<p>先看网格范围、单元数、边界数，再看非正交、偏斜和体积等指标。<code>Failed ... mesh checks</code> 后的名称指向具体问题。</p>
<h2>执行完整几何和拓扑检查</h2>
<pre><code class="language-bash">checkMesh -allTopology -allGeometry &gt; log.checkMesh 2&gt;&amp;1
</code></pre>
<p><code>-allTopology</code> 增加连接关系检查，<code>-allGeometry</code> 增加几何检查。重定向将完整信息写入日志，方便比较两次网格修改。</p>
<h2>导出异常集合</h2>
<pre><code class="language-bash">checkMesh -allTopology -allGeometry -writeSets vtk
</code></pre>
<p>将检查产生的面或单元集合写成 VTK，便于在 ParaView 中定位异常。先查出问题位置，再决定修改表面、细化等级或边界层参数。</p>
<h2>检查并行网格</h2>
<pre><code class="language-bash">mpirun -np 4 checkMesh -parallel
</code></pre>
<p>在已经分成 4 个子域的算例中运行。检查结果还包含分区边界及各处理器之间的连接。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-allGeometry</td><td>执行更完整的网格几何检查。</td></tr><tr><td>-allRegions</td><td>处理 regionProperties 中列出的所有区域。</td></tr><tr><td>-allTopology</td><td>执行更完整的网格拓扑检查。</td></tr><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-constant</td><td>将 constant 目录加入选择。</td></tr><tr><td>-latestTime</td><td>选择最近的结果时刻。</td></tr><tr><td>-meshQuality</td><td>Read user-defined mesh quality criteria from system/meshQualityDict</td></tr><tr><td>-noTopology</td><td>Skip checking the mesh topology</td></tr><tr><td>-noZero</td><td>跳过 0 时刻。</td></tr><tr><td>-parallel</td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td>-region &lt;name&gt;</td><td>指定网格区域名称。</td></tr><tr><td>-time &lt;ranges&gt;</td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td>-write-edges</td><td>Write bad edges (possibly relevant for finite-area) in vtk format</td></tr><tr><td>-writeAllFields</td><td>Write volFields with mesh quality parameters Write surfaceFields with mesh quality parameters Write checks to file in dictionary or JSON format Write volFields with selected mesh quality parameters Reconstruct and write all faceSets and cellSets in selected format</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-meshqualitydict/">meshQualityDict</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/polyDualMesh/missingCorner">mesh/polyDualMesh/missingCorner</a></li></ul><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: checkMesh [OPTIONS]
Options:
  -allGeometry      Include bounding box checks
  -allRegions       Use all regions in regionProperties
  -allTopology      Include extra topology checks
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
  -meshQuality      Read user-defined mesh quality criteria from
                    system/meshQualityDict
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -noTopology       Skip checking the mesh topology
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -region &lt;name&gt;    Use specified mesh region. Eg, -region gas
  -regions &lt;wordRes&gt;
                    Use specified mesh region. Eg, -regions gas
                    Or from regionProperties.  Eg, -regions &#x27;(gas &quot;solid.*&quot;)&#x27;
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -world &lt;name&gt;     Name of the local world for parallel communication
  -write-edges      Write bad edges (possibly relevant for finite-area) in vtk
                    format
  -writeAllFields   Write volFields with mesh quality parameters
  -writeAllSurfaceFields
                    Write surfaceFields with mesh quality parameters
  -writeChecks &lt;word&gt;
                    Write checks to file in dictionary or JSON format
  -writeFields &lt;wordList&gt;
                    Write volFields with selected mesh quality parameters
  -writeSets &lt;surfaceFormat&gt;
                    Reconstruct and write all faceSets and cellSets in selected
                    format
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Checks validity of a mesh

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/checkMesh/writeFields.C">源码与说明</a> · <a href="/assets/command-help/checkmesh.txt">帮助文本</a></p>
