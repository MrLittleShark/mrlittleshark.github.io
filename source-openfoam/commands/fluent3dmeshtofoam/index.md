---
title: "fluent3DMeshToFoam · 用于 Fluent 三维网格的专用转换，按输入格式选择"
layout: reference
description: "用于 Fluent 三维网格的专用转换，按输入格式选择。"
cms_slug: "command-fluent3dmeshtofoam"
---

<p>用于 Fluent 三维网格的专用转换，按输入格式选择。</p><h2>开始前</h2>
<p>准备三维 Fluent 网格文件；由 Cubit 生成的同类文件可使用专用选项。组名必须与输入网格实际名称一致。</p>
<h2>示例 1：导入三维 Fluent 网格</h2>
<pre><code class="language-bash">fluent3DMeshToFoam mesh.msh
</code></pre>
<p>建立体网格以及输入定义的边界分组。查看转换日志中 cell group 和 face group 的对应关系。</p>
<h2>示例 2：导入 Cubit 导出文件</h2>
<pre><code class="language-bash">fluent3DMeshToFoam cubit.msh -cubit
</code></pre>
<p>启用针对 Cubit 文件的处理路径。转换后核对单元数量及边界组，适合使用 Cubit 建网格的工作流程。</p>
<h2>示例 3：转换毫米坐标</h2>
<pre><code class="language-bash">fluent3DMeshToFoam mesh.msh -scale 0.001
</code></pre>
<p>将输入坐标换算为米。与 Fluent 界面显示单位不同，转换器使用的是文件里的实际数值，需在 checkMesh 中核对。</p>
<h2>示例 4：跳过指定单元组</h2>
<pre><code class="language-bash">fluent3DMeshToFoam mesh.msh -ignoreCellGroups '(solidSupport)'
</code></pre>
<p>前提是输入含名为 solidSupport 的可排除单元组。导入时跳过该组，随后核对保留单元数及由此产生的边界。</p>
<h2>示例 5：跳过指定面组并检查</h2>
<pre><code class="language-bash">fluent3DMeshToFoam mesh.msh -ignoreFaceGroups '(auxFaces)' -case ../fluentTest
checkMesh -case ../fluentTest -constant -allTopology
</code></pre>
<p>适用于已确认 auxFaces 属于可忽略辅助数据的输入。检查真实外边界是否仍完整，保留求解所需的面分区。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-cubit</code></td><td>Special parsing of (incorrect) cubit files Set named DebugSwitch (default value: 1). [Can be used multiple times] Override the file handler type Specify cell groups to ignore Specify face groups to ignore Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Geometry scaling factor - default is 1</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: fluent3DMeshToFoam [OPTIONS] &lt;Fluent mesh file&gt;
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -cubit            Special parsing of (incorrect) cubit files
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -ignoreCellGroups &lt;names&gt;
                    Specify cell groups to ignore
  -ignoreFaceGroups &lt;names&gt;
                    Specify face groups to ignore
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

Convert a Fluent mesh to OpenFOAM format

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/fluent3DMeshToFoam/Make/files">源码与说明</a> · <a href="/assets/command-help/fluent3dmeshtofoam.txt">帮助文本</a></p>
