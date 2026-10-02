---
title: "surfaceCoarsen · 简化因子取值范围为 [0,1)，简化后检查几何完整性"
layout: reference
description: "简化因子取值范围为 [0,1)，简化后检查几何完整性。"
cms_slug: "command-surfacecoarsen"
---

<p>简化因子取值范围为 [0,1)，简化后检查几何完整性。</p><h2>开始前</h2>
<p>输入为三角表面。源码按factor×原顶点数确定目标顶点数；使用0到1之间的正因子，输出另存。</p>
<h2>示例 1：温和减少顶点</h2>
<pre><code class="language-bash">surfaceCoarsen fine.stl 0.8 coarse80.stl
</code></pre>
<p>目标约保留80%的原顶点，先观察主要轮廓和小圆角是否保持。</p>
<h2>示例 2：减半顶点数</h2>
<pre><code class="language-bash">surfaceCoarsen fine.stl 0.5 coarse50.stl
</code></pre>
<p>目标顶点数约减为一半，适合降低可视化或初步几何检查成本。</p>
<h2>示例 3：较强粗化对照</h2>
<pre><code class="language-bash">surfaceCoarsen fine.stl 0.25 coarse25.stl
</code></pre>
<p>约保留四分之一顶点，与0.8和0.5方案比较细节损失，避免直接用最粗表面替代精细几何。</p>
<h2>示例 4：缩放后粗化</h2>
<pre><code class="language-bash">surfaceCoarsen -scale 0.001 fine_mm.stl 0.5 coarse_m.stl
</code></pre>
<p>先将毫米坐标转换为米，再按相同顶点保留比例粗化。</p>
<h2>示例 5：检查粗化结果</h2>
<pre><code class="language-bash">surfaceCoarsen fine.stl 0.5 coarse.stl
surfaceCheck coarse.stl
</code></pre>
<p>比较输入输出面数、开边及包围盒；factor控制顶点目标，三角面数随重建结果变化。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Input geometry scaling factor</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceCoarsen [OPTIONS] &lt;input&gt; &lt;factor&gt; &lt;output&gt;
Arguments:
  &lt;input&gt;           The input surface file
  &lt;factor&gt;          The reduction factor [0,1)
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
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -scale &lt;factor&gt;   Input geometry scaling factor
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Surface coarsening using &#x27;bunnylod&#x27;

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceCoarsen/surfaceCoarsen.C">源码与说明</a> · <a href="/assets/command-help/surfacecoarsen.txt">帮助文本</a></p>
