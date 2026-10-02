---
title: "cfx4ToFoam · -scale 指定长度缩放系数"
layout: reference
description: "-scale 指定长度缩放系数。"
cms_slug: "command-cfx4tofoam"
---

<p>-scale 指定长度缩放系数。</p><h2>开始前</h2>
<p>准备 CFX4 的 .geo 几何文件和目标案例，输入格式应与 CFX4 转换器相符。</p>
<h2>示例 1：导入 CFX4 几何</h2>
<pre><code class="language-bash">cfx4ToFoam mesh.geo
</code></pre>
<p>转换节点、单元和边界到 polyMesh。查看终端输出，核对读取的块数和边界分区。</p>
<h2>示例 2：换算毫米坐标</h2>
<pre><code class="language-bash">cfx4ToFoam mesh.geo -scale 0.001
</code></pre>
<p>将输入节点坐标乘 0.001。转换后检查边界框尺寸，确保计算域长度与后续速度、黏度等 SI 制参数一致。</p>
<h2>示例 3：在目标案例中检查拓扑</h2>
<pre><code class="language-bash">cfx4ToFoam /data/mesh.geo -case ../cfxCase
checkMesh -case ../cfxCase -constant -allTopology
</code></pre>
<p>将网格写入指定案例后检查拓扑连接。关注内部面、边界面和不连通区域，判断多块网格是否正确连接。</p>
<h2>示例 4：整理转换后的边界</h2>
<pre><code class="language-bash">cfx4ToFoam mesh.geo
createPatch -overwrite
</code></pre>
<p>先依据转换得到的 patch 名称编写 createPatchDict，再合并同一物理边界的分区。检查 boundary 文件并同步配置各场的 boundaryField。</p>
<h2>示例 5：导出外表面核对形状</h2>
<pre><code class="language-bash">cfx4ToFoam mesh.geo -scale 0.001
foamToSurface cfx-boundary.stl -constant
</code></pre>
<p>把导入网格外边界写成 STL，便于与原始几何叠加检查。主要核对单位、朝向、孔洞以及入口出口的位置。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Geometry scaling factor - default is 1</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: cfx4ToFoam [OPTIONS] &lt;CFX geom file&gt;
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
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
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

Convert a CFX 4 mesh to OpenFOAM format

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/cfx4ToFoam/hexBlock.C">源码与说明</a> · <a href="/assets/command-help/cfx4tofoam.txt">帮助文本</a></p>
