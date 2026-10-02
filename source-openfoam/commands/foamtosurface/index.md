---
title: "foamToSurface · 用于几何检查及外部软件数据交换"
layout: reference
description: "用于几何检查及外部软件数据交换。"
cms_slug: "command-foamtosurface"
---

<p>用于几何检查及外部软件数据交换。</p><h2>开始前</h2>
<p>案例已有体网格；工具导出体网格边界表面，输出格式由文件扩展名决定。</p>
<h2>示例 1：导出初始边界</h2>
<pre><code class="language-bash">foamToSurface boundary.stl -constant
</code></pre>
<p>提取 constant 网格的边界并写成 STL。可在 CAD 或可视化软件中检查计算域外形。</p>
<h2>示例 2：保留多边形表面表示</h2>
<pre><code class="language-bash">foamToSurface boundary.obj -constant
</code></pre>
<p>输出 OBJ 表面，便于读取网格边界上的多边形。需要三角形表示时，可配合 -tri 选项。</p>
<h2>示例 3：显式三角化边界</h2>
<pre><code class="language-bash">foamToSurface boundary-tri.obj -constant -tri
</code></pre>
<p>将边界多边形分解为三角形后导出。适合需要三角表面的下游几何工具。</p>
<h2>示例 4：导出毫米坐标</h2>
<pre><code class="language-bash">foamToSurface boundary-mm.stl -constant -scale 1000
</code></pre>
<p>将米制网格的坐标乘 1000。接收端应使用毫米单位，并检查几何边界框。</p>
<h2>示例 5：导出最新变形边界</h2>
<pre><code class="language-bash">foamToSurface moved.stl -latestTime
</code></pre>
<p>提取最新时间对应的网格边界。与初始输出叠加，可检查动网格位移和变形范围。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Geometry scaling factor - default is 1</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-tri</code></td><td>Triangulate surface</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamToSurface [OPTIONS] &lt;output&gt;
Arguments:
  &lt;output&gt;          The output surface file
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -scale &lt;factor&gt;   Geometry scaling factor - default is 1
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -tri              Triangulate surface
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Extract boundaries from an OpenFOAM mesh and write in a surface format

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/foamToSurface/foamToSurface.C">源码与说明</a> · <a href="/assets/command-help/foamtosurface.txt">帮助文本</a></p>
