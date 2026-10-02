---
title: "star4ToFoam · 按文件名前缀读取 mesh.vrt、mesh.cel 等配套文件"
layout: reference
description: "按文件名前缀读取 mesh.vrt、mesh.cel 等配套文件。"
cms_slug: "command-star4tofoam"
---

<p>按文件名前缀读取 mesh.vrt、mesh.cel 等配套文件。</p><h2>开始前</h2>
<p>准备 STAR-CD v4 的同名前缀 .vrt、.cel 和 .bnd 文件；默认缩放因子 0.001，通常把毫米转换为米。</p>
<h2>示例 1：按文件前缀导入</h2>
<pre><code class="language-bash">star4ToFoam mesh
</code></pre>
<p>读取 mesh.vrt、mesh.cel 和对应边界文件。默认将顶点坐标乘 0.001，检查输出尺寸是否符合输入单位。</p>
<h2>示例 2：导入已经为米制的网格</h2>
<pre><code class="language-bash">star4ToFoam mesh -scale 1
</code></pre>
<p>保持原始坐标数值，适用于顶点文件已采用米制的输入。显式比例能避免二次缩放。</p>
<h2>示例 3：写出文本格式网格</h2>
<pre><code class="language-bash">star4ToFoam mesh -ascii
</code></pre>
<p>导入后以 ASCII 保存 polyMesh，便于直接阅读连接和边界数据。大型网格需要预留更多磁盘空间。</p>
<h2>示例 4：保留固体单元</h2>
<pre><code class="language-bash">star4ToFoam mesh -solids
</code></pre>
<p>将输入中的固体单元也转换并保留。多区域传热应用需继续按区域拆分，并为各区域配置独立物性与求解设置。</p>
<h2>示例 5：在独立案例组合导入</h2>
<pre><code class="language-bash">star4ToFoam /data/engine -case ../starCase -scale 0.001 -ascii -solids
checkMesh -case ../starCase -constant -allTopology
</code></pre>
<p>从绝对前缀路径读取网格，保留全部目标区域并检查连接。核对区域之间的界面和外边界，作为后续多区域配置的依据。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-ascii</code></td><td>Write in ASCII instead of binary format</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Geometry scaling factor - default is 0.001 ([mm] to [m])</td></tr><tr><td><code>-solids</code></td><td>Retain solid cells and treat like fluid cells</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: star4ToFoam [OPTIONS] &lt;prefix&gt;
Arguments:
  &lt;prefix&gt;          The prefix for the input PROSTAR files
Options:
  -ascii            Write in ASCII instead of binary format
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
  -scale &lt;factor&gt;   Geometry scaling factor - default is 0.001 ([mm] to [m])
  -solids           Retain solid cells and treat like fluid cells
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Convert STARCD/PROSTAR (v4) mesh to OpenFOAM

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/star4ToFoam/star4ToFoam.C">源码与说明</a> · <a href="/assets/command-help/star4tofoam.txt">帮助文本</a></p>
