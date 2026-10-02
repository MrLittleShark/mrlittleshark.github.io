---
title: "plot3dToFoam · -singleBlock 和 -2D 等选项用于指定输入网格形式"
layout: reference
description: "-singleBlock 和 -2D 等选项用于指定输入网格形式。"
cms_slug: "command-plot3dtofoam"
---

<p>-singleBlock 和 -2D 等选项用于指定输入网格形式。</p><h2>开始前</h2>
<p>准备 ASCII 格式 Plot3D 几何文件，确认文件是单块还是多块、是否包含 iblank 数据。</p>
<h2>示例 1：导入多块几何</h2>
<pre><code class="language-bash">plot3dToFoam mesh.xyz
</code></pre>
<p>按默认多块格式读取，生成 OpenFOAM 网格。检查各块相邻界面的连接情况。</p>
<h2>示例 2：读取单块格式</h2>
<pre><code class="language-bash">plot3dToFoam single.xyz -singleBlock
</code></pre>
<p>输入文件使用单块格式时添加此选项，避免把块尺寸行误读为块数量。</p>
<h2>示例 3：读取不含空白标志的数据</h2>
<pre><code class="language-bash">plot3dToFoam mesh.xyz -noBlank
</code></pre>
<p>用于文件中没有 iblank 数据的情况。该选项控制输入记录的读取方式，应根据导出格式选择。</p>
<h2>示例 4：将二维数据处理为有限厚度</h2>
<pre><code class="language-bash">plot3dToFoam planar.xyz -2D 0.01 -noBlank
</code></pre>
<p>为二维网格指定 0.01 的厚度，输入应为无 iblank 的对应格式。检查前后边界和单元层数，再配置二维场边界。</p>
<h2>示例 5：组合格式与单位设置</h2>
<pre><code class="language-bash">plot3dToFoam single-mm.xyz -singleBlock -noBlank -scale 0.001
checkMesh -constant
</code></pre>
<p>读取单块、无 iblank 的毫米制输入，转换为米并检查网格。二维厚度如另行指定，也会随 -scale 一起缩放。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-2D &lt;thickness&gt;</code></td><td>Use when converting a 2-D mesh (applied before scale)</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noBlank</code></td><td>Skip blank items Do not execute function objects Set named OptimisationSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Geometry scaling factor - default is 1</td></tr><tr><td><code>-singleBlock</code></td><td>Input is a single block</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: plot3dToFoam [OPTIONS] &lt;PLOT3D geom file&gt;
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
  -noBlank          Skip blank items
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -scale &lt;factor&gt;   Geometry scaling factor - default is 1
  -singleBlock      Input is a single block
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Plot3d mesh (ascii/formatted format) converter

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/plot3dToFoam/hexBlock.C">源码与说明</a> · <a href="/assets/command-help/plot3dtofoam.txt">帮助文本</a></p>
