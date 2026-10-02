---
title: "surfaceBooleanFeatures · 支持 intersection、union 和 difference，相关构建可依赖 CGAL"
layout: reference
description: "支持 intersection、union 和 difference，相关构建可依赖 CGAL。"
cms_slug: "command-surfacebooleanfeatures"
---

<p>支持 intersection、union 和 difference，相关构建可依赖 CGAL。</p><h2>开始前</h2>
<p>准备相交的两个表面，并在含controlDict的工作算例中运行。输出是布尔界面的extendedFeatureEdgeMesh特征线。</p>
<h2>示例 1：提取并集的交界特征</h2>
<pre><code class="language-bash">surfaceBooleanFeatures union body.stl boss.stl
</code></pre>
<p>按并集关系识别两表面相交处的特征边，供后续特征控制使用。</p>
<h2>示例 2：提取交集特征</h2>
<pre><code class="language-bash">surfaceBooleanFeatures intersection body.stl box.stl
</code></pre>
<p>选择两个实体重叠部分的布尔界面，观察被box限定区域的交界线。</p>
<h2>示例 3：提取差集特征</h2>
<pre><code class="language-bash">surfaceBooleanFeatures difference body.stl cutter.stl
</code></pre>
<p>按第一个实体减去第二个实体的关系生成特征线，输入顺序决定差集含义。</p>
<h2>示例 4：处理退化交点</h2>
<pre><code class="language-bash">surfaceBooleanFeatures -perturb union body.stl boss.stl
</code></pre>
<p>两表面局部共面或交点退化导致求交困难时，小幅扰动点位以尝试获得稳定交线。</p>
<h2>示例 5：限制交线保留范围</h2>
<pre><code class="language-bash">surfaceBooleanFeatures -trim '((clip.stl inside))' union body.stl boss.stl
</code></pre>
<p>clip.stl为额外闭合选择表面，仅保留位于其内部的交线段，适合局部特征提取。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-invertedSpace</code></td><td>Do the surfaces have inverted space orientation, i.e. a point at infinity is considered inside. This is only sensible for union and intersection.</td></tr><tr><td><code>-no-cgal</code></td><td>Do not use CGAL algorithms</td></tr><tr><td><code>-perturb</code></td><td>Perturb surface points to escape degenerate intersections</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Geometry scaling factor (both surfaces)</td></tr><tr><td><code>-surf1Baffle</code></td><td>Mark surface 1 as a baffle</td></tr><tr><td><code>-surf2Baffle</code></td><td>Mark surface 2 as a baffle Trim resulting intersection with additional surfaces; volumeType is &#x27;inside&#x27; (keep (parts of) edges that are inside), &#x27;outside&#x27; (keep (parts of) edges that are outside) or &#x27;mixed&#x27; (keep all)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceBooleanFeatures [OPTIONS] &lt;action&gt; &lt;surface1&gt; &lt;surface2&gt;
Arguments:
  &lt;action&gt;          One of (intersection | union | difference)
  &lt;surface1&gt;        The input surface file 1
  &lt;surface2&gt;        The input surface file 2
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
  -invertedSpace    Do the surfaces have inverted space orientation, i.e. a
                    point at infinity is considered inside. This is only
                    sensible for union and intersection.
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-cgal          Do not use CGAL algorithms
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -perturb          Perturb surface points to escape degenerate intersections
  -scale &lt;factor&gt;   Geometry scaling factor (both surfaces)
  -surf1Baffle      Mark surface 1 as a baffle
  -surf2Baffle      Mark surface 2 as a baffle
  -trim &lt;((surface1 volumeType) .. (surfaceN volumeType))&gt;
                    Trim resulting intersection with additional surfaces;
                    volumeType is &#x27;inside&#x27; (keep (parts of) edges that are
                    inside), &#x27;outside&#x27; (keep (parts of) edges that are outside)
                    or &#x27;mixed&#x27; (keep all)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Generates a extendedFeatureEdgeMesh for the interface created by a boolean
operation on two surfaces. [Compiled with CGAL]

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceBooleanFeatures/surfaceBooleanFeatures.C">源码与说明</a> · <a href="/assets/command-help/surfacebooleanfeatures.txt">帮助文本</a></p>
