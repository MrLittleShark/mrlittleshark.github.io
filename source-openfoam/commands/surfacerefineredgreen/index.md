---
title: "surfaceRefineRedGreen · -steps 指定细分次数"
layout: reference
description: "-steps 指定细分次数。"
cms_slug: "command-surfacerefineredgreen"
---

<p>-steps 指定细分次数。</p><h2>开始前</h2>
<p>准备三角表面。红绿细化增加三角面数量，主要改变离散密度；新顶点位于原三角形上。</p>
<h2>示例 1：细化一次</h2>
<pre><code class="language-bash">surfaceRefineRedGreen body.stl body-refined.stl
</code></pre>
<p>使用默认一次细化，将表面的三角形继续细分。输出面数增加，原有表面外形保持为同一个分片线性几何。</p>
<h2>示例 2：连续细化两次</h2>
<pre><code class="language-bash">surfaceRefineRedGreen body.stl body-refined2.stl -steps 2
</code></pre>
<p>在第一轮结果上继续细分，获得更密的表面离散。运行前评估面数和内存，避免对已经很密的 CAD 曲面重复加密。</p>
<h2>示例 3：转换格式并细化</h2>
<pre><code class="language-bash">surfaceRefineRedGreen body.obj body-refined.stl -steps 1
</code></pre>
<p>从受支持的三角表面格式读取并输出 STL。适合已有 OBJ 三角面需要进一步细分的场景。</p>
<h2>示例 4：检查细化后的拓扑</h2>
<pre><code class="language-bash">surfaceRefineRedGreen coarse.stl fine.stl -steps 1
surfaceCheck coarse.stl
surfaceCheck fine.stl
</code></pre>
<p>对比面数、开放边和连通性。细分应保留原来的边界结构；开放几何经过细化后仍需按开放表面使用。</p>
<h2>示例 5：细化后再进行平滑</h2>
<pre><code class="language-bash">surfaceRefineRedGreen faceted.stl dense.stl -steps 1
surfaceLambdaMuSmooth dense.stl 0.5 0.53 5 smooth.stl
</code></pre>
<p>先增加离散点，再做五轮 λ–μ 平滑。结果会改变几何形状，应对照原始轮廓和关键尺寸选择平滑强度。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-steps &lt;N&gt;</code></td><td>Number of refinement steps (default: 1)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceRefineRedGreen [OPTIONS] &lt;input&gt; &lt;output&gt;
Arguments:
  &lt;input&gt;           The input surface file
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
  -steps &lt;N&gt;        Number of refinement steps (default: 1)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Refine by splitting all three edges of triangle

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceRefineRedGreen/surfaceRefineRedGreen.C">源码与说明</a> · <a href="/assets/command-help/surfacerefineredgreen.txt">帮助文本</a></p>
