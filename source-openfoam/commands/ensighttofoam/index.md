---
title: "ensightToFoam · 转换范围为几何网格，物理模型在目标算例中配置"
layout: reference
description: "转换范围为几何网格，物理模型在目标算例中配置。"
cms_slug: "command-ensighttofoam"
---

<p>转换范围为几何网格，物理模型在目标算例中配置。</p><h2>开始前</h2>
<p>准备 EnSight Gold 几何 .geo 文件；转换几何后，求解器的初始场和数值设置需在案例中另行配置。</p>
<h2>示例 1：导入几何</h2>
<pre><code class="language-bash">ensightToFoam mesh.geo
</code></pre>
<p>读取 EnSight 几何并建立体网格。检查转换报告中的单元类型和区域数量。</p>
<h2>示例 2：导入毫米模型</h2>
<pre><code class="language-bash">ensightToFoam mesh.geo -scale 0.001
</code></pre>
<p>缩放节点坐标到米。导入后使用 checkMesh 核对边界框，与原始模型的实际尺寸对应。</p>
<h2>示例 3：合并几乎重合的顶点</h2>
<pre><code class="language-bash">ensightToFoam mesh.geo -mergeTol 1e-6
</code></pre>
<p>使用相对模型包围盒尺度的合并容差，处理分块几何中的近重合点。检查接缝是否连接，同时核对细小间隙是否保留。</p>
<h2>示例 4：保留输入单元的手性</h2>
<pre><code class="language-bash">ensightToFoam mesh.geo -keepHandedness
</code></pre>
<p>保留输入单元方向而关闭自动方向调整，适用于已经确认输入连接顺序符合预期的网格。随后检查负体积和面方向。</p>
<h2>示例 5：在副本组合缩放与合并</h2>
<pre><code class="language-bash">ensightToFoam /data/mesh.geo -case ../ensightCase -scale 0.001 -mergeTol 1e-7
checkMesh -case ../ensightCase -constant -allTopology
</code></pre>
<p>在独立案例内同时处理单位和小接缝。通过连接检查确认各部分构成预期流体域，再继续设置边界条件。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-keepHandedness</code></td><td>Do not automatically flip inverted cells (default is to do a geometric test)</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Geometry scaling factor - default is 1</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: ensightToFoam [OPTIONS] &lt;.geo file&gt;
Arguments:
  &lt;.geo file&gt;       The file containing the geometry
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -keepHandedness   Do not automatically flip inverted cells (default is to do
                    a geometric test)
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -mergeTol &lt;factor&gt;
                    Merge tolerance as a fraction of bounding box - 0 to
                    disable merging
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -scale &lt;factor&gt;   Geometry scaling factor - default is 1
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Convert Ensight mesh to OpenFOAM

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/ensightToFoam/ensightMeshReader.C">源码与说明</a> · <a href="/assets/command-help/ensighttofoam.txt">帮助文本</a></p>
