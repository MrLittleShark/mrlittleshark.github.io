---
title: "checkMesh · 检查网格拓扑、几何形状与质量，并定位问题区域"
layout: reference
description: "检查网格拓扑、几何形状与质量，并定位问题区域。"
cms_slug: "command-checkmesh"
---

<p>检查网格拓扑、几何形状与质量，并定位问题区域。</p><h2>开始前</h2>
<p>算例已有网格。检查时刻和区域应与实际求解或待使用的网格一致。</p>
<h2>示例 1：检查初始网格</h2>
<pre><code class="language-bash">checkMesh -constant
</code></pre>
<p>检查constant网格的体积、边界和基本拓扑，首先查看单元数与Mesh OK或失败项目。</p>
<h2>示例 2：运行完整检查</h2>
<pre><code class="language-bash">checkMesh -constant -allTopology -allGeometry
</code></pre>
<p>增加拓扑和包围盒等几何检查，适合导入、拼接或自编程生成的网格。</p>
<h2>示例 3：使用项目质量标准</h2>
<pre><code class="language-bash">checkMesh -meshQuality
</code></pre>
<p>读取system/meshQualityDict，以项目设定的非正交性、扭曲等阈值检查。</p>
<h2>示例 4：输出质量字段</h2>
<pre><code class="language-bash">checkMesh -latestTime -writeAllFields -writeSets vtk
</code></pre>
<p>检查最新网格，保存质量标量场和问题集合，可在ParaView定位坏单元。</p>
<h2>示例 5：检查多区域并行网格</h2>
<pre><code class="language-bash">mpirun -np 4 checkMesh -parallel -allRegions
</code></pre>
<p>前提4个分区及regionProperties完整；分别检查流体、固体区域和分区耦合关系。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allGeometry</code></td><td>执行更完整的网格几何检查。</td></tr><tr><td><code>-allRegions</code></td><td>处理 regionProperties 中列出的所有区域。</td></tr><tr><td><code>-allTopology</code></td><td>执行更完整的网格拓扑检查。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-meshQuality</code></td><td>Read user-defined mesh quality criteria from system/meshQualityDict</td></tr><tr><td><code>-noTopology</code></td><td>Skip checking the mesh topology</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-write-edges</code></td><td>Write bad edges (possibly relevant for finite-area) in vtk format</td></tr><tr><td><code>-writeAllFields</code></td><td>Write volFields with mesh quality parameters Write surfaceFields with mesh quality parameters Write checks to file in dictionary or JSON format Write volFields with selected mesh quality parameters Reconstruct and write all faceSets and cellSets in selected format</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-meshqualitydict/">meshQualityDict</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/polyDualMesh/missingCorner">mesh/polyDualMesh/missingCorner</a></li></ul><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: checkMesh [OPTIONS]
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
