---
title: "surfaceTransformPoints · -read-scale 和 -write-scale 分别指定读取和写出时的缩放系数"
layout: reference
description: "-read-scale 和 -write-scale 分别指定读取和写出时的缩放系数。"
cms_slug: "command-surfacetransformpoints"
---

<p>-read-scale 和 -write-scale 分别指定读取和写出时的缩放系数。</p><h2>开始前</h2>
<p>准备受支持的表面文件；输入与输出使用不同文件名，便于直接比较变换前后的边界框。</p>
<h2>示例 1：将毫米转换为米</h2>
<pre><code class="language-bash">surfaceTransformPoints body-mm.stl body-m.stl -read-scale 0.001
</code></pre>
<p>读取坐标时统一乘 0.001。长度 100 的零件变为 0.1，与 OpenFOAM 算例常用的米制输入对应。</p>
<h2>示例 2：平移几何</h2>
<pre><code class="language-bash">surfaceTransformPoints body.stl shifted.stl -translate '(0.1 0 0)'
</code></pre>
<p>将全部顶点沿 x 正方向移动 0.1 个坐标单位。形状和尺寸保持不变，边界框的 x 范围整体平移。</p>
<h2>示例 3：绕指定轴旋转</h2>
<pre><code class="language-bash">surfaceTransformPoints blade.stl blade-rotated.stl -rotate-angle '((0 0 1) 45)'
</code></pre>
<p>绕过原点的 z 轴旋转 45°。查看叶片与入口方向的关系，确认旋转正向符合右手规则。</p>
<h2>示例 4：绕几何中心旋转</h2>
<pre><code class="language-bash">surfaceTransformPoints body.stl body-rotated.stl -auto-centre -rotate-z 90
</code></pre>
<p>自动使用几何中心作为旋转中心，绕 z 轴转 90°。适合改变零件方向，同时保持其中心位置。</p>
<h2>示例 5：缩放并对齐方向</h2>
<pre><code class="language-bash">surfaceTransformPoints body-mm.stl aligned.stl -read-scale 0.001 -rotate '((1 0 0) (0 0 1))'
</code></pre>
<p>先转换长度单位，再将原 x 方向转到 z 方向。组合变换后检查包围盒和关键定位点，供后续网格划分使用。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-auto-centre</code></td><td>Use bounding box centre as centre for rotations</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-centre &lt;point&gt;</code></td><td>Use specified &lt;point&gt; as centre for rotations Tranform cylindrical coordinates to cartesian coordinates Set named DebugSwitch (default value: 1). [Can be used multiple times] Override the file handler type Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-recentre</code></td><td>Recentre the bounding box before other operations Rotate by &#x27;(roll pitch yaw)&#x27; degrees Rotate from &lt;vectorA&gt; to &lt;vectorB&gt; - eg, &#x27;((1 0 0) (0 0 1))&#x27; Rotate &lt;angle&gt; degrees about &lt;vector&gt; - eg, &#x27;((1 0 0) 45)&#x27;</td></tr><tr><td><code>-rotate-x &lt;deg&gt;</code></td><td>Rotate (degrees) about x-axis</td></tr><tr><td><code>-rotate-y &lt;deg&gt;</code></td><td>Rotate (degrees) about y-axis</td></tr><tr><td><code>-rotate-z &lt;deg&gt;</code></td><td>Rotate (degrees) about z-axis Translate by specified &lt;vector&gt; before rotations Output format (default: use file extension) Uniform or non-uniform output scaling Rotate by &#x27;(yaw pitch roll)&#x27; degrees</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceTransformPoints [OPTIONS] &lt;input&gt; &lt;output&gt;
Arguments:
  &lt;input&gt;           The input surface file
  &lt;output&gt;          The output surface file
Options:
  -auto-centre      Use bounding box centre as centre for rotations
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -centre &lt;point&gt;   Use specified &lt;point&gt; as centre for rotations
  -cylToCart &lt;(originVec axisVec directionVec)&gt;
                    Tranform cylindrical coordinates to cartesian coordinates
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
  -read-format &lt;type&gt;
                    Input format (default: use file extension)
  -read-scale &lt;scalar | vector&gt;
                    Uniform or non-uniform input scaling
  -recentre         Recentre the bounding box before other operations
  -rollPitchYaw &lt;vector&gt;
                    Rotate by &#x27;(roll pitch yaw)&#x27; degrees
  -rotate &lt;(vectorA vectorB)&gt;
                    Rotate from &lt;vectorA&gt; to &lt;vectorB&gt; - eg, &#x27;((1 0 0) (0 0 1))&#x27;
  -rotate-angle &lt;(vector angle)&gt;
                    Rotate &lt;angle&gt; degrees about &lt;vector&gt; - eg, &#x27;((1 0 0) 45)&#x27;
  -rotate-x &lt;deg&gt;   Rotate (degrees) about x-axis
  -rotate-y &lt;deg&gt;   Rotate (degrees) about y-axis
  -rotate-z &lt;deg&gt;   Rotate (degrees) about z-axis
  -translate &lt;vector&gt;
                    Translate by specified &lt;vector&gt; before rotations
  -write-format &lt;type&gt;
                    Output format (default: use file extension)
  -write-scale &lt;scalar | vector&gt;
                    Uniform or non-uniform output scaling
  -yawPitchRoll &lt;vector&gt;
                    Rotate by &#x27;(yaw pitch roll)&#x27; degrees
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Transform (translate / rotate / scale) surface points.
Like transformPoints but for surfaces.
Note: roll=rotate about x, pitch=rotate about y, yaw=rotate about z

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceTransformPoints/surfaceTransformPoints.C">源码与说明</a> · <a href="/assets/command-help/surfacetransformpoints.txt">帮助文本</a></p>
