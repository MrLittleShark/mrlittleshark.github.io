---
title: "gmshToFoam · 常用输入为 ASCII MSH2"
layout: reference
description: "常用输入为 ASCII MSH2。转换后检查物理组与边界名称。"
cms_slug: "command-gmshtofoam"
---

<p>常用输入为 ASCII MSH2。转换后检查物理组与边界名称。</p><h2>开始前</h2>
<p>准备 Gmsh 的 ASCII MSH 2 格式网格；建议在 Gmsh 中定义 Physical Volume 和 Physical Surface 来表达体区及边界。</p>
<h2>示例 1：导入现有 Gmsh 网格</h2>
<pre><code class="language-bash">gmshToFoam mesh.msh
</code></pre>
<p>读取节点、单元和物理分组，生成 polyMesh。转换后查看 boundary 和 cellZones，核对 Physical 分组是否完整。</p>
<h2>示例 2：从几何文件生成再导入</h2>
<pre><code class="language-bash">gmsh channel.geo -3 -format msh2 -o channel.msh
gmshToFoam channel.msh
</code></pre>
<p>需要系统已安装 gmsh。第一步生成三维 MSH 2 网格，第二步转换为 OpenFOAM，适合可重复的几何—网格工作流程。</p>
<h2>示例 3：导入命名区域</h2>
<pre><code class="language-bash">gmshToFoam solid.msh -region solid
</code></pre>
<p>将网格写到名为 solid 的区域路径。适合多区域案例中单独准备固体网格，随后需要相应的 constant/solid 和 system/solid 配置。</p>
<h2>示例 4：保留输入的单元方向</h2>
<pre><code class="language-bash">gmshToFoam mesh.msh -keepOrientation
</code></pre>
<p>保留输入棱柱和六面体的方向信息。适用于已确认节点顺序的网格，之后用 checkMesh 查看负体积和面方向。</p>
<h2>示例 5：换算毫米模型并检查</h2>
<pre><code class="language-bash">gmshToFoam mesh-mm.msh
transformPoints -scale '(0.001 0.001 0.001)'
checkMesh -constant -allGeometry
</code></pre>
<p>转换器通过输入坐标建立网格；第二步统一缩放为米。检查单元质量和尺寸，再配置求解器物性。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-keepOrientation</code></td><td>Retain raw orientation for prisms/hexs</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: gmshToFoam [OPTIONS] &lt;.msh file&gt;
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
  -keepOrientation  Retain raw orientation for prisms/hexs
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Convert a gmsh .msh file to OpenFOAM

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/gmshToFoam/gmshToFoam.C">源码与说明</a> · <a href="/assets/command-help/gmshtofoam.txt">帮助文本</a></p>
