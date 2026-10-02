---
title: "surfaceMeshInfo · -areas 输出面积统计，可用于核查几何尺度"
layout: reference
description: "-areas 输出面积统计，可用于核查几何尺度。"
cms_slug: "command-surfacemeshinfo"
---

<p>-areas 输出面积统计，可用于核查几何尺度。</p><h2>开始前</h2>
<p>准备受支持的表面文件。该工具读取表面并报告信息，适合转换和修复前后比较。</p>
<h2>示例 1：查看点面统计</h2>
<pre><code class="language-bash">surfaceMeshInfo body.stl
</code></pre>
<p>显示点数、面数等表面统计信息。可先判断输入是否为空，以及三角化后的规模是否符合预期。</p>
<h2>示例 2：查看每个面的面积</h2>
<pre><code class="language-bash">surfaceMeshInfo body.stl -areas
</code></pre>
<p>额外输出各面的面积。很小的面积常对应细碎三角形，可结合可视化定位需要清理的区域。</p>
<h2>示例 3：以米制坐标检查毫米模型</h2>
<pre><code class="language-bash">surfaceMeshInfo body-mm.stl -scale 0.001 -areas
</code></pre>
<p>按缩放后的几何计算面积：长度乘 0.001，面积相应乘 10⁻⁶。适合直接核对 CAD 导出模型的物理尺度。</p>
<h2>示例 4：导出结构化统计</h2>
<pre><code class="language-bash">surfaceMeshInfo body.obj -xml &gt; body-info.xml
</code></pre>
<p>将统计输出为 XML 格式，便于脚本读取点数、面数等指标。文件用于批量几何检查记录。</p>
<h2>示例 5：比较修复前后的面积</h2>
<pre><code class="language-bash">surfaceMeshInfo body-original.stl -areas -xml &gt; original.xml
surfaceMeshInfo body-clean.stl -areas -xml &gt; clean.xml
</code></pre>
<p>分别记录原始与清理后表面的面面积。比较面数和面积分布，可发现修复时是否丢失了较大的实体面。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-areas</code></td><td>Display area of each face</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Input geometry scaling factor</td></tr><tr><td><code>-xml</code></td><td>Write output in XML format</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceMeshInfo [OPTIONS] &lt;surface&gt;
Arguments:
  &lt;surface&gt;         The input surface file
Options:
  -areas            Display area of each face
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
  -scale &lt;factor&gt;   Input geometry scaling factor
  -xml              Write output in XML format
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Information about surface meshes

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceMeshInfo/surfaceMeshInfo.C">源码与说明</a> · <a href="/assets/command-help/surfacemeshinfo.txt">帮助文本</a></p>
