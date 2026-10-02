---
title: "foamMeshToFluent · 导出范围为网格数据，求解配置在 Fluent 中设置"
layout: reference
description: "导出范围为网格数据，求解配置在 Fluent 中设置。"
cms_slug: "command-foammeshtofluent"
---

<p>导出范围为网格数据，求解配置在 Fluent 中设置。</p><h2>开始前</h2>
<p>案例已有体网格；该工具导出 Fluent 网格，输出文件位置以终端报告为准。场结果的交换需要另选结果导出工具。</p>
<h2>示例 1：导出已有网格</h2>
<pre><code class="language-bash">foamMeshToFluent
</code></pre>
<p>读取当前案例的网格，生成 Fluent .msh 文件。接收端读取后应核对长度单位和边界区域。</p>
<h2>示例 2：从 blockMesh 建网格后导出</h2>
<pre><code class="language-bash">blockMesh
checkMesh -constant
foamMeshToFluent
</code></pre>
<p>先生成结构化块网格，再检查并导出。适合使用 OpenFOAM 的 blockMesh 建网格、在 Fluent 中进行后续计算。</p>
<h2>示例 3：导出指定案例</h2>
<pre><code class="language-bash">foamMeshToFluent -case ../channel
</code></pre>
<p>在当前目录直接指定 channel 案例，输出网格对应该案例。查看日志中的文件路径，避免把其他案例的导出文件混用。</p>
<h2>示例 4：整理边界后导出</h2>
<pre><code class="language-bash">createPatch -overwrite
foamMeshToFluent
</code></pre>
<p>前提是 createPatchDict 已定义目标分组。先合并或命名入口、出口和壁面，导出的 Fluent 边界区域更便于分配物理条件。</p>
<h2>示例 5：重新编号后导出</h2>
<pre><code class="language-bash">renumberMesh -overwrite
checkMesh -constant
foamMeshToFluent
</code></pre>
<p>在案例副本中重新编号，再导出通过检查的网格。几何形状保持不变，输出连接编号随之更新，适合比较外部软件读取与计算效率。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamMeshToFluent [OPTIONS]
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
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Write an OpenFOAM mesh in Fluent mesh format

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/foamMeshToFluent/fluentFvMesh.C">源码与说明</a> · <a href="/assets/command-help/foammeshtofluent.txt">帮助文本</a></p>
