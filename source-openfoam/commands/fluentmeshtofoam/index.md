---
title: "fluentMeshToFoam · 输入采用 Fluent mesh 格式；Gmsh 文件使用 gmshToFoam 转换"
layout: reference
description: "输入采用 Fluent mesh 格式；Gmsh 文件使用 gmshToFoam 转换。"
cms_slug: "command-fluentmeshtofoam"
---

<p>输入采用 Fluent mesh 格式；Gmsh 文件使用 gmshToFoam 转换。</p><h2>开始前</h2>
<p>准备 Fluent 网格文件和 OpenFOAM 案例。二维网格需提供有限厚度，场文件中相应前后边界应与二维模型一致。</p>
<h2>示例 1：导入三维网格</h2>
<pre><code class="language-bash">fluentMeshToFoam mesh.msh
</code></pre>
<p>把 Fluent 的面和单元连接转换为 polyMesh。检查生成的边界分区名称，并将其用于初始场文件。</p>
<h2>示例 2：导入毫米网格</h2>
<pre><code class="language-bash">fluentMeshToFoam mesh.msh -scale 0.001
</code></pre>
<p>节点坐标乘 0.001；输入长度 1000 将变为 1 m。通过 checkMesh 的 bounding box 检查换算结果。</p>
<h2>示例 3：为二维网格指定厚度</h2>
<pre><code class="language-bash">fluentMeshToFoam mesh2d.msh -2D 0.01
</code></pre>
<p>将二维网格处理为厚度 0.01 的网格。厚度先按输入坐标给出；如果同时设置 -scale，它也会一起缩放。</p>
<h2>示例 4：保留单元区域</h2>
<pre><code class="language-bash">fluentMeshToFoam mesh.msh -writeZones
</code></pre>
<p>把相应单元分组写成 cellZone，供多孔区、旋转区或多区域拆分使用。转换后检查 cellZones 中的名称和单元数量。</p>
<h2>示例 5：同时生成集合用于后续选区</h2>
<pre><code class="language-bash">fluentMeshToFoam mesh.msh -writeZones -writeSets
checkMesh -constant
</code></pre>
<p>额外将区域和边界信息写为集合，便于 topoSet、局部网格修改等工具使用。集合内容应与转换日志中的分组一致。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-2D &lt;thickness&gt;</code></td><td>Use when converting a 2-D mesh (applied before scale)</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Geometry scaling factor - default is 1</td></tr><tr><td><code>-writeSets</code></td><td>写出问题单元或面的集合，格式由参数指定。</td></tr><tr><td><code>-writeZones</code></td><td>Write cell zones as zones</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: fluentMeshToFoam [OPTIONS] &lt;Fluent mesh file&gt;
Options:
  -2D &lt;thickness&gt;   Use when converting a 2-D mesh (applied before scale)
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -scale &lt;factor&gt;   Geometry scaling factor - default is 1
  -writeSets        Write cell zones and patches as sets
  -writeZones       Write cell zones as zones
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Convert a Fluent mesh to OpenFOAM format, including multiple region and region
boundary handling

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/fluentMeshToFoam/extrudedTriangleCellShape.C">源码与说明</a> · <a href="/assets/command-help/fluentmeshtofoam.txt">帮助文本</a></p>
