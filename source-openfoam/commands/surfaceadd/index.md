---
title: "surfaceAdd · 连接两个表面数据集，不执行几何布尔并集"
layout: reference
description: "连接两个表面数据集，不执行几何布尔并集。"
cms_slug: "command-surfaceadd"
---

<p>连接两个表面数据集，不执行几何布尔并集。</p><h2>开始前</h2>
<p>两个输入为可读取的表面文件，坐标系和长度单位一致；输出文件使用新名称。</p>
<h2>示例 1：合并两个部件</h2>
<pre><code class="language-bash">surfaceAdd housing.stl rotor.stl assembly.stl
</code></pre>
<p>把壳体和转子组合为一个表面文件，并对重合点做几何合并；保留各部件区域信息。</p>
<h2>示例 2：按同名区域合并</h2>
<pre><code class="language-bash">surfaceAdd -mergeRegions left.stl right.stl joined.stl
</code></pre>
<p>两块表面区域含相同名称时，将对应区域组合，适合被分成多个文件的同一边界。</p>
<h2>示例 3：合并毫米几何</h2>
<pre><code class="language-bash">surfaceAdd -scale 0.001 housing_mm.stl rotor_mm.stl assembly_m.stl
</code></pre>
<p>两个输入都以毫米表示时，先按0.001缩放再合并，输出坐标以米表示。</p>
<h2>示例 4：逐步组合三个部件</h2>
<pre><code class="language-bash">surfaceAdd body.stl inlet.stl bodyInlet.stl
surfaceAdd bodyInlet.stl outlet.stl complete.stl
</code></pre>
<p>通过中间文件组合三个表面，每一步均保留输入，便于判断区域在何时发生变化。</p>
<h2>示例 5：检查合并后的交叉</h2>
<pre><code class="language-bash">surfaceAdd a.stl b.stl combined.stl
surfaceCheck -checkSelfIntersection combined.stl
</code></pre>
<p>合并前两表面已在同一坐标系。第二步检查交叉三角形；surfaceAdd本身做组合与点合并，不执行实体布尔裁切。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-mergeRegions</code></td><td>Combine regions from both surfaces</td></tr><tr><td><code>-points &lt;file&gt;</code></td><td>Provide additional points</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Geometry scaling factor on input surfaces</td></tr><tr><td><code>-verbose</code></td><td>Additional verbosity (can be used multiple times)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceAdd [OPTIONS] &lt;surface1&gt; &lt;surface2&gt; &lt;output&gt;
Arguments:
  &lt;surface1&gt;        The input surface file 1
  &lt;surface2&gt;        The input surface file 2
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
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -mergeRegions     Combine regions from both surfaces
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -points &lt;file&gt;    Provide additional points
  -scale &lt;factor&gt;   Geometry scaling factor on input surfaces
  -verbose          Additional verbosity (can be used multiple times)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Add two surfaces via a geometric merge on points. Does not check for
overlapping/intersecting triangles.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceAdd/surfaceAdd.C">源码与说明</a> · <a href="/assets/command-help/surfaceadd.txt">帮助文本</a></p>
