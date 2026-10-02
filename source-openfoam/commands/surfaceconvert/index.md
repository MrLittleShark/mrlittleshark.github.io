---
title: "surfaceConvert · -scale 指定几何缩放系数，按输入与输出长度单位换算"
layout: reference
description: "-scale 指定几何缩放系数，按输入与输出长度单位换算。"
cms_slug: "command-surfaceconvert"
---

<p>-scale 指定几何缩放系数，按输入与输出长度单位换算。</p><h2>用法</h2><pre><code class="language-bash">surfaceConvert body.obj body.stl</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">surfaceConvert body.obj body.stl -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-clean</td><td>Perform some surface checking/cleanup on the input surface Set named DebugSwitch (default value: 1). [Can be used multiple times] Override the file handler type</td></tr><tr><td>-group</td><td>Reorder faces into groups; one per region Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-precision &lt;int&gt;</td><td>The output precision The input format (default: use file extension)</td></tr><tr><td>-scale &lt;factor&gt;</td><td>Input geometry scaling factor</td></tr><tr><td>-verbose</td><td>Additional verbosity (can be used multiple times) The output format (default: use file extension)</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceConvert [OPTIONS] &lt;input&gt; &lt;output&gt;
Arguments:
  &lt;input&gt;           The input surface file
  &lt;output&gt;          The output surface file
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -clean            Perform some surface checking/cleanup on the input surface
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -group            Reorder faces into groups; one per region
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
  -precision &lt;int&gt;  The output precision
  -read-format &lt;type&gt;
                    The input format (default: use file extension)
  -scale &lt;factor&gt;   Input geometry scaling factor
  -verbose          Additional verbosity (can be used multiple times)
  -write-format &lt;type&gt;
                    The output format (default: use file extension)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Convert between surface formats, using triSurface library components

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceConvert/surfaceConvert.C">源码与说明</a> · <a href="/assets/command-help/surfaceconvert.txt">帮助文本</a></p>
