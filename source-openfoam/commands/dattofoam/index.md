---
title: "datToFoam · 输入内容须符合该转换器定义的 DAT 网格结构"
layout: reference
description: "输入内容须符合该转换器定义的 DAT 网格结构。"
cms_slug: "command-dattofoam"
---

<p>输入内容须符合该转换器定义的 DAT 网格结构。</p><h2>开始前</h2>
<p>这是配合特定双锥结构化网格数据使用的 points 转换器。准备格式正确的 DAT 和顶点编号匹配的 blockMeshDict；工具会替换 constant/polyMesh/points，宜在副本操作。</p>
<h2>示例 1：用 DAT 坐标替换块网格顶点</h2>
<pre><code class="language-bash">blockMesh
datToFoam biconic.dat
</code></pre>
<p>先建立 faces、owner、neighbour 等拓扑，再写入 DAT 转换得到的 points。程序跳过输入 i、j 方向的首层点，并生成两侧楔形顶点，网格编号必须与此排列对应。</p>
<h2>示例 2：检查替换后的网格</h2>
<pre><code class="language-bash">blockMesh
datToFoam biconic.dat
checkMesh -constant -allGeometry
</code></pre>
<p>检查体积、面方向和单元形状。若出现负体积或严重扭曲，优先核对 DAT 的点排列与 blockMesh 的编号关系。</p>
<h2>示例 3：在独立案例测试坐标</h2>
<pre><code class="language-bash">blockMesh -case ../biconicTest
datToFoam /data/biconic.dat -case ../biconicTest
</code></pre>
<p>把坐标替换限制在 biconicTest。输出点数为 2×(iPoints−1)×(jPoints−1)，可与目标拓扑需要的点数进行对照。</p>
<h2>示例 4：换算输入坐标的单位</h2>
<pre><code class="language-bash">blockMesh
datToFoam biconic-mm.dat
transformPoints -scale '(0.001 0.001 0.001)'
</code></pre>
<p>DAT 转换器本身没有缩放选项，转换完成后统一缩放整个网格。该顺序使新生成的楔形顶点也按相同长度比例变换。</p>
<h2>示例 5：提取生成的楔形外表面</h2>
<pre><code class="language-bash">blockMesh
datToFoam biconic.dat
foamToSurface biconic-boundary.obj -constant
</code></pre>
<p>导出最终外表面，检查双锥轮廓、轴线和楔形两侧。程序按源码中固定的 0.1° 角构造两侧坐标，几何检查应与该设置一致。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: datToFoam [OPTIONS] &lt;dat file&gt;
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

Reads in a datToFoam mesh file and outputs a points file.
Used in conjunction with blockMesh.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/datToFoam/datToFoam.C">源码与说明</a> · <a href="/assets/command-help/dattofoam.txt">帮助文本</a></p>
