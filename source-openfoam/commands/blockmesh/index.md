---
title: "blockMesh · 读取 blockMeshDict，生成由六面体块组成的网格"
layout: reference
description: "读取 blockMeshDict，生成由六面体块组成的网格。"
cms_slug: "command-blockmesh"
---

<p>读取 blockMeshDict，生成由六面体块组成的网格。</p><h2>开始前</h2>
<p>准备system/blockMeshDict；新网格会写入选定算例，已有网格的比较请使用独立副本。</p>
<h2>示例 1：生成方腔网格</h2>
<pre><code class="language-bash">blockMesh
checkMesh -constant
</code></pre>
<p>读取默认字典生成constant/polyMesh，再检查单元数、体积和边界；20×20×1块应得到400单元。</p>
<h2>示例 2：预览块拓扑</h2>
<pre><code class="language-bash">blockMesh -write-vtk
</code></pre>
<p>导出块拓扑VTU后退出，适合在实际细分前检查顶点连接与块的位置。</p>
<h2>示例 3：预览块边和中心</h2>
<pre><code class="language-bash">blockMesh -write-obj
</code></pre>
<p>导出块边及中心OBJ后退出，可排查弧线、边连接或顶点编号问题。</p>
<h2>示例 4：选择另一套划分</h2>
<pre><code class="language-bash">blockMesh -dict system/blockMeshDict.fine -time 1
</code></pre>
<p>用完整fine字典生成时间1的网格，便于与constant基准比较单元数量和分辨率。</p>
<h2>示例 5：创建命名区域及集合</h2>
<pre><code class="language-bash">blockMesh -region fluid -dict system/fluid/blockMeshDict -sets
</code></pre>
<p>为fluid区域生成网格；字典中命名的cellZones同时写成cellSets，便于后续集合操作。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-merge-points</code></td><td>Geometric point merging instead of topological merging [default for 1912 and earlier].</td></tr><tr><td><code>-no-clean</code></td><td>保留已有 polyMesh 文件；默认行为见完整帮助。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-sets</code></td><td>同时将 cellZone 写成 cellSet。</td></tr><tr><td><code>-time &lt;time&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-verbose</code></td><td>Force verbose output. (Can be used multiple times)</td></tr><tr><td><code>-write-obj</code></td><td>Write block edges and centres as obj files and exit</td></tr><tr><td><code>-write-vtk</code></td><td>输出块拓扑的 VTK 文件。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-blockmeshdict/">blockMeshDict</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/sphere">mesh/blockMesh/sphere</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/sphere7">mesh/blockMesh/sphere7</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/mergePairs">mesh/blockMesh/mergePairs</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/spheroidProjected">mesh/blockMesh/spheroidProjected</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/spheroid7Projected">mesh/blockMesh/spheroid7Projected</a></li></ul><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: blockMesh [OPTIONS]
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
