---
title: "ansysToFoam · 输入采用转换器支持的 ANSYS 文件格式"
layout: reference
description: "输入采用转换器支持的 ANSYS 文件格式。"
cms_slug: "command-ansystofoam"
---

<p>输入采用转换器支持的 ANSYS 文件格式。</p><h2>开始前</h2>
<p>准备由 I-DEAS 导出的 ANSYS 网格输入文件，以及目标 OpenFOAM 案例；该转换器按这一网格格式读取数据。</p>
<h2>示例 1：导入米制网格</h2>
<pre><code class="language-bash">ansysToFoam mesh.ans
</code></pre>
<p>读取节点、单元和边界信息，在案例中生成 polyMesh。默认坐标缩放因子为 1，适用于输入已经采用米的情况。</p>
<h2>示例 2：导入毫米网格</h2>
<pre><code class="language-bash">ansysToFoam mesh-mm.ans -scale 0.001
</code></pre>
<p>将节点坐标乘 0.001。导入后在 checkMesh 的 bounding box 中核对长度，原 100 mm 应对应 0.1 m。</p>
<h2>示例 3：导入指定案例</h2>
<pre><code class="language-bash">ansysToFoam /data/mesh.ans -case ../ansysCase
checkMesh -case ../ansysCase -constant
</code></pre>
<p>从明确的输入路径读取，并把网格写入 ansysCase。检查器报告单元类型、质量和边界数量，可定位转换后的连接问题。</p>
<h2>示例 4：调整导入后的边界组织</h2>
<pre><code class="language-bash">ansysToFoam mesh.ans
createPatch -overwrite
</code></pre>
<p>前提是 system/createPatchDict 已按转换得到的 patch 名称配置。第二步合并或重命名边界，形成求解器需要的 inlet、outlet、walls 等分区。</p>
<h2>示例 5：检查并优化网格编号</h2>
<pre><code class="language-bash">ansysToFoam mesh.ans -scale 0.001
checkMesh -constant -allTopology -allGeometry
renumberMesh -overwrite
</code></pre>
<p>先对转换结果做较全面的几何和拓扑检查，再重新编号以改善矩阵带宽。重新编号改变网格索引，已有按编号创建的集合应重新核对。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Geometry scaling factor - default is 1</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: ansysToFoam [OPTIONS] &lt;ANSYS input file&gt;
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

Convert an ANSYS input mesh file (exported from I-DEAS) to OpenFOAM format

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/ansysToFoam/Make/files">源码与说明</a> · <a href="/assets/command-help/ansystofoam.txt">帮助文本</a></p>
