---
title: "surfaceOrient · 默认按物体外部观察点定向，-inside 将指定点按内部点处理"
layout: reference
description: "默认按物体外部观察点定向，-inside 将指定点按内部点处理。"
cms_slug: "command-surfaceorient"
---

<p>默认按物体外部观察点定向，-inside 将指定点按内部点处理。</p><h2>开始前</h2>
<p>准备三角表面和一个坐标明确的观察点；闭合表面可选择已知内部点或外部点确定朝向。</p>
<h2>示例 1：按外部点统一法向</h2>
<pre><code class="language-bash">surfaceOrient body.stl '(10 10 10)' body-oriented.stl
</code></pre>
<p>假设给定点位于模型外部，按该外部参考确定表面方向。输出另存，使用 ParaView 的法向显示检查外表面朝向。</p>
<h2>示例 2：按内部点确定方向</h2>
<pre><code class="language-bash">surfaceOrient sphere.stl '(0 0 0)' sphere-oriented.stl -inside
</code></pre>
<p>适用于以原点为中心的闭合球面。-inside 明确该点在实体内部，程序据此判断表面内外。</p>
<h2>示例 3：复杂闭合表面使用穿透测试</h2>
<pre><code class="language-bash">surfaceOrient cavity.stl '(5 5 5)' cavity-oriented.stl -usePierceTest
</code></pre>
<p>通过射线与三角面的交点关系判断方向，适合常规判定效果不理想的几何。输入闭合性应先用 surfaceCheck 检查。</p>
<h2>示例 4：同时进行尺度转换</h2>
<pre><code class="language-bash">surfaceOrient body-mm.stl '(1 1 1)' body-m.stl -scale 0.001
</code></pre>
<p>表面坐标缩放到米后进行方向处理，参考点也按缩放后的坐标选择。输出边界框应缩小为原来的千分之一。</p>
<h2>示例 5：为表面惯性计算准备朝向</h2>
<pre><code class="language-bash">surfaceOrient closed.stl '(10 10 10)' oriented.stl
surfaceInertia oriented.stl
</code></pre>
<p>先统一闭合外表面的方向，再计算体积、质心和惯性参数。查看结果体积与尺寸是否一致，可帮助发现几何朝向问题。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-inside</code></td><td>Treat provided point as being inside</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Input geometry scaling factor</td></tr><tr><td><code>-usePierceTest</code></td><td>Determine orientation by counting number of intersections</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceOrient [OPTIONS] &lt;input&gt; &lt;point&gt; &lt;output&gt;
Arguments:
  &lt;input&gt;           The input surface file
  &lt;point&gt;           The visible &#x27;outside&#x27; point
  &lt;output&gt;          The output surface file
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
  -inside           Treat provided point as being inside
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -scale &lt;factor&gt;   Input geometry scaling factor
  -usePierceTest    Determine orientation by counting number of intersections
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Set face normals consistent with a user-provided &#x27;outside&#x27; point

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceOrient/surfaceOrient.C">源码与说明</a> · <a href="/assets/command-help/surfaceorient.txt">帮助文本</a></p>
