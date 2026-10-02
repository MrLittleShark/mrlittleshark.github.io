---
title: "surfaceOrient · 默认按物体外部观察点定向，-inside 将指定点按内部点处理"
layout: reference
description: "默认按物体外部观察点定向，-inside 将指定点按内部点处理。"
cms_slug: "command-surfaceorient"
---

<p>默认按物体外部观察点定向，-inside 将指定点按内部点处理。</p><h2>用法</h2><pre><code class="language-bash">surfaceOrient body.stl &#x27;(10 10 10)&#x27; bodyOriented.stl</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">surfaceOrient body.stl &#x27;(10 10 10)&#x27; bodyOriented.stl -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-inside</td><td>Treat provided point as being inside</td></tr><tr><td>-scale &lt;factor&gt;</td><td>Input geometry scaling factor</td></tr><tr><td>-usePierceTest</td><td>Determine orientation by counting number of intersections</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceOrient [OPTIONS] &lt;input&gt; &lt;point&gt; &lt;output&gt;
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
