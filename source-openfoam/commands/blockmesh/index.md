---
title: "blockMesh · 读取 blockMeshDict，生成由六面体块组成的网格"
layout: reference
description: "读取 blockMeshDict，生成由六面体块组成的网格。"
cms_slug: "command-blockmesh"
---

<p>读取 blockMeshDict，生成由六面体块组成的网格。</p><h2>生成并检查网格</h2>
<pre><code class="language-bash">blockMesh
checkMesh -allTopology -allGeometry
</code></pre>
<p><code>blockMesh</code> 读取 <code>system/blockMeshDict</code>，通常将网格写入 <code>constant/polyMesh</code>。随后检查单元数、包围盒和网格质量；长度单位由字典中的 <code>scale</code> 决定。</p>
<h2>选择另一份网格配置</h2>
<pre><code class="language-bash">blockMesh -dict system/blockMeshDict.fine
</code></pre>
<p>这里使用名为 <code>blockMeshDict.fine</code> 的配置。可保留粗、细两份字典，分别改变 <code>blocks</code> 中的单元数；运行会更新当前算例的网格。</p>
<h2>从算例外运行</h2>
<pre><code class="language-bash">blockMesh -case ../cavity-fine
checkMesh -case ../cavity-fine
</code></pre>
<p><code>-case</code> 指定已有算例目录，命令仍使用该目录中的字典。它只改变工作对象，不会替你复制算例。</p>
<h2>查看块的连接</h2>
<pre><code class="language-bash">blockMesh -write-vtk
</code></pre>
<p>输出块拓扑的 VTK 文件并退出。用 ParaView 查看块连接和顶点方向，适合检查多块结构中的顶点编号。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-dict &lt;file&gt;</td><td>改用指定字典文件。</td></tr><tr><td>-merge-points</td><td>Geometric point merging instead of topological merging [default for 1912 and earlier].</td></tr><tr><td>-no-clean</td><td>保留已有 polyMesh 文件；默认行为见完整帮助。</td></tr><tr><td>-region &lt;name&gt;</td><td>指定网格区域名称。</td></tr><tr><td>-sets</td><td>同时将 cellZone 写成 cellSet。</td></tr><tr><td>-time &lt;time&gt;</td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td>-verbose</td><td>Force verbose output. (Can be used multiple times)</td></tr><tr><td>-write-obj</td><td>Write block edges and centres as obj files and exit</td></tr><tr><td>-write-vtk</td><td>输出块拓扑的 VTK 文件。</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-blockmeshdict/">blockMeshDict</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/sphere">mesh/blockMesh/sphere</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/sphere7">mesh/blockMesh/sphere7</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/mergePairs">mesh/blockMesh/mergePairs</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/spheroidProjected">mesh/blockMesh/spheroidProjected</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/spheroid7Projected">mesh/blockMesh/spheroid7Projected</a></li></ul><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: blockMesh [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dict &lt;file&gt;      Alternative blockMeshDict
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -merge-points     Geometric point merging instead of topological merging
                    [default for 1912 and earlier].
  -no-clean         Do not remove polyMesh/ directory or files
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -sets             Write cellZones as cellSets too (for processing purposes)
  -time &lt;time&gt;      Specify a time to write mesh to (default: constant)
  -verbose          Force verbose output. (Can be used multiple times)
  -write-obj        Write block edges and centres as obj files and exit
  -write-vtk        Write topology as VTU file and exit
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Block mesh generator.

  The ordering of vertex and face labels within a block as shown below.
  For the local vertex numbering in the sequence 0 to 7:
    Faces 0, 1 (x-direction) are left, right.
    Faces 2, 3 (y-direction) are front, back.
    Faces 4, 5 (z-direction) are bottom, top.

                        7 ---- 6
                 f5     |\     :\     f3
                 |      | 4 ---- 5     \
                 |      3.|....2 |      \
                 |       \|     \|      f2
                 f4       0 ---- 1
    Y  Z
     \ |                f0 ------ f1
      \|
       o--- X

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/blockMesh/blockMesh.C">源码与说明</a> · <a href="/assets/command-help/blockmesh.txt">帮助文本</a></p>
