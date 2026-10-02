---
title: "gambitToFoam · 转换后运行 checkMesh"
layout: reference
description: "转换后运行 checkMesh。"
cms_slug: "command-gambittofoam"
---

<p>转换后运行 checkMesh。</p><h2>开始前</h2>
<p>准备 GAMBIT Neutral 网格文件；该输入与 Fluent .msh 文件采用不同的格式。</p>
<h2>示例 1：导入 Neutral 网格</h2>
<pre><code class="language-bash">gambitToFoam mesh.neu
</code></pre>
<p>读取中性格式中的节点、单元和边界分组，建立 OpenFOAM 网格。核对转换日志中的组名及单元数。</p>
<h2>示例 2：导入毫米模型</h2>
<pre><code class="language-bash">gambitToFoam mesh.neu -scale 0.001
</code></pre>
<p>节点坐标换算为米，便于直接使用 SI 制物性参数。检查 bounding box 是否与实际尺寸一致。</p>
<h2>示例 3：转换到目标案例并检查</h2>
<pre><code class="language-bash">gambitToFoam /data/mesh.neu -case ../gambitCase
checkMesh -case ../gambitCase -constant -allTopology
</code></pre>
<p>把网格写入指定案例并检查连接关系。关注多块网格之间是否出现意外的断开区域。</p>
<h2>示例 4：将分散边界归并</h2>
<pre><code class="language-bash">gambitToFoam mesh.neu
createPatch -overwrite
</code></pre>
<p>前提是 createPatchDict 已按导入 patch 名称配置。将同一物理壁面对应的多个分组归并，减少后续边界条件重复配置。</p>
<h2>示例 5：导出表面核对入口出口</h2>
<pre><code class="language-bash">gambitToFoam mesh.neu -scale 0.001
surfaceMeshExtract ports.obj -patches '(inlet outlet)' -constant
</code></pre>
<p>输入需包含 inlet 和 outlet 分组。单独导出两个端面，检查法向、面积和间距是否符合实际流动通道。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Geometry scaling factor - default is 1</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: gambitToFoam [OPTIONS] &lt;GAMBIT file&gt;
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

Convert a GAMBIT mesh to OpenFOAM format

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/gambitToFoam/Make/files">源码与说明</a> · <a href="/assets/command-help/gambittofoam.txt">帮助文本</a></p>
