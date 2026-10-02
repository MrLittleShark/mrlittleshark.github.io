---
title: "surfaceMeshExtract · -patches 指定网格中已有的边界名称"
layout: reference
description: "-patches 指定网格中已有的边界名称。"
cms_slug: "command-surfacemeshextract"
---

<p>-patches 指定网格中已有的边界名称。</p><h2>开始前</h2>
<p>案例已有体网格和边界名称；含 faceZone 的示例还需先建立相应面区域。</p>
<h2>示例 1：提取全部边界</h2>
<pre><code class="language-bash">surfaceMeshExtract boundary.obj -constant
</code></pre>
<p>读取 constant 中的网格边界，输出表面文件。可在几何软件中查看计算域外形以及各边界的分区。</p>
<h2>示例 2：只提取壁面</h2>
<pre><code class="language-bash">surfaceMeshExtract walls.stl -patches '(walls)' -constant
</code></pre>
<p>仅提取名为 walls 的 patch。括号表示名称列表；将名称换成 constant/polyMesh/boundary 中的实际边界名。</p>
<h2>示例 3：按名称匹配并排除</h2>
<pre><code class="language-bash">surfaceMeshExtract body.obj -patches '("wall.*")' -exclude-patches '(wallAux)' -constant
</code></pre>
<p>先匹配 wall 开头的边界，再排除 wallAux。输出用于检查主要壁面，避免把辅助封口面一并导出。</p>
<h2>示例 4：提取内部面区域</h2>
<pre><code class="language-bash">surfaceMeshExtract interface.obj -faceZones '(interfaceZone)' -constant
</code></pre>
<p>把 interfaceZone 中的内部面也加入提取范围。适合查看耦合界面或风扇面的位置；需要该 faceZone 已存在。</p>
<h2>示例 5：提取末时刻移动边界</h2>
<pre><code class="language-bash">surfaceMeshExtract moved.obj -latestTime -patches '(movingWall)'
</code></pre>
<p>读取最新时间对应的网格位置，导出 movingWall。与初始位置的表面对比，可检查动网格位移方向和量级。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-writeOBJ</code></td><td>Write added pointPatch points to .obj files</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceMeshExtract [OPTIONS] &lt;output&gt;
Arguments:
  &lt;output&gt;          The output surface file
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -exclude-patches &lt;wordRes&gt;
                    Specify single patch or multiple patches to exclude from
                    -patches. Eg, &#x27;outlet&#x27; or &#x27;( inlet &quot;.*Wall&quot; )&#x27;
  -excludeProcPatches
                    Exclude processor patches
  -extractZonePoints
                    Extract point-patches for selected faceZones
  -faceZones &lt;wordRes&gt;
                    Specify single or multiple faceZones to extract
                    Eg, &#x27;cells&#x27; or &#x27;( slice &quot;mfp-.*&quot; )&#x27;
  -featureAngle &lt;angle&gt;
                    Auto-extract feature edges/points and put into separate
                    point-patches
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
  -patches &lt;wordRes&gt;
                    Specify single patch or multiple patches to extract.
                    Eg, &#x27;top&#x27; or &#x27;( front &quot;.*back&quot; )&#x27;
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -world &lt;name&gt;     Name of the local world for parallel communication
  -writeOBJ         Write added pointPatch points to .obj files
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Extract patch or faceZone surfaces from a polyMesh.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceMeshExtract/surfaceMeshExtract.C">源码与说明</a> · <a href="/assets/command-help/surfacemeshextract.txt">帮助文本</a></p>
