---
title: "mshToFoam · 输入须符合该转换器定义的 MSH 结构；Gmsh 网格使用 gmshToFoam"
layout: reference
description: "输入须符合该转换器定义的 MSH 结构；Gmsh 网格使用 gmshToFoam。"
cms_slug: "command-mshtofoam"
---

<p>输入须符合该转换器定义的 MSH 结构；Gmsh 网格使用 gmshToFoam。</p><h2>开始前</h2>
<p>准备 Adventure 格式的 .msh 文件。默认读取四面体网格，六面体使用 -hex；Gmsh 文件应使用 gmshToFoam。</p>
<h2>示例 1：导入四面体网格</h2>
<pre><code class="language-bash">mshToFoam mesh.msh
</code></pre>
<p>按 Adventure 四面体连接格式读取网格，建立 polyMesh。检查单元数与原始网格是否一致。</p>
<h2>示例 2：导入六面体网格</h2>
<pre><code class="language-bash">mshToFoam hexMesh.msh -hex
</code></pre>
<p>切换到六面体单元格式。该选项改变单元连接的读取方式，应与输入每个单元的节点数对应。</p>
<h2>示例 3：在目标案例检查连接</h2>
<pre><code class="language-bash">mshToFoam /data/mesh.msh -case ../adventureCase
checkMesh -case ../adventureCase -constant -allTopology
</code></pre>
<p>将转换限制到独立案例，并检查外边界及内部面的连接。适合先验证输入格式再配置求解。</p>
<h2>示例 4：将毫米网格换算为米</h2>
<pre><code class="language-bash">mshToFoam mesh-mm.msh
transformPoints -scale '(0.001 0.001 0.001)'
</code></pre>
<p>转换后统一缩放坐标。确认边界框尺寸与后续使用的米制速度、黏度参数一致。</p>
<h2>示例 5：按几何棱边划分边界</h2>
<pre><code class="language-bash">mshToFoam mesh.msh
autoPatch 45 -overwrite
checkMesh -constant
</code></pre>
<p>根据 45° 特征角对边界进一步分区，适用于输入未提供所需物理边界名称的模型。分区后按几何位置命名并设置边界条件。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-hex</code></td><td>Treat input as containing hex instead of tet cells Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: mshToFoam [OPTIONS] &lt;.msh file&gt;
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hex              Treat input as containing hex instead of tet cells
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

Convert an Adventure .msh file to OpenFOAM

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/mshToFoam/mshToFoam.C">源码与说明</a> · <a href="/assets/command-help/mshtofoam.txt">帮助文本</a></p>
