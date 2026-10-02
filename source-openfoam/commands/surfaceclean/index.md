---
title: "surfaceClean · 长度和质量阈值按几何尺度设置；清理会改变局部表面细节"
layout: reference
description: "长度和质量阈值按几何尺度设置；清理会改变局部表面细节。"
cms_slug: "command-surfaceclean"
---

<p>长度和质量阈值按几何尺度设置；清理会改变局部表面细节。</p><h2>开始前</h2>
<p>长度阈值使用缩放后的几何单位，quality为三角形质量阈值。先用surfaceCheck了解最小特征尺度，输出另存。</p>
<h2>示例 1：清理极短边</h2>
<pre><code class="language-bash">surfaceClean raw.stl 1e-6 1e-6 clean.stl
</code></pre>
<p>将短于1μm的边和质量极差的三角形纳入清理，输出clean.stl以供对照。</p>
<h2>示例 2：提高质量阈值</h2>
<pre><code class="language-bash">surfaceClean raw.stl 1e-6 0.01 cleanQuality.stl
</code></pre>
<p>保持长度阈值，提高最小质量要求到0.01，适合进一步处理狭长薄片三角形。</p>
<h2>示例 3：按毫米输入清理</h2>
<pre><code class="language-bash">surfaceClean -scale 0.001 raw_mm.stl 1e-5 0.01 clean_m.stl
</code></pre>
<p>先把毫米坐标换成米，再使用10μm的长度阈值清理。</p>
<h2>示例 4：跳过预清理比较主算法</h2>
<pre><code class="language-bash">surfaceClean -no-clean raw.stl 1e-6 0.01 cleanNoPrepass.stl
</code></pre>
<p>-no-clean跳过输入阶段的一轮检查清理，后续按长度与质量要求处理，适合诊断不同阶段的影响。</p>
<h2>示例 5：清理后核对闭合性</h2>
<pre><code class="language-bash">surfaceClean raw.stl 1e-6 0.01 clean.stl
surfaceCheck -checkSelfIntersection clean.stl
</code></pre>
<p>检查输出的开边、自相交与包围盒，确认清理后的表面仍符合预期几何。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-no-clean</code></td><td>保留已有 polyMesh 文件；默认行为见完整帮助。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Input geometry scaling factor</td></tr><tr><td><code>-verbose</code></td><td>Additional verbosity (can be used multiple times)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceClean [OPTIONS] &lt;input&gt; &lt;length&gt; &lt;quality&gt; &lt;output&gt;
Arguments:
  &lt;input&gt;           The input surface file
  &lt;length&gt;          The min length
  &lt;quality&gt;         The min quality
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
  -no-clean         Suppress surface checking/cleanup on the input surface
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -scale &lt;factor&gt;   Input geometry scaling factor
  -verbose          Additional verbosity (can be used multiple times)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Clean surface by removing baffles, sliver faces, collapsing small edges, etc.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceClean/collapseBase.C">源码与说明</a> · <a href="/assets/command-help/surfaceclean.txt">帮助文本</a></p>
