---
title: "surfaceClean · 长度和质量阈值按几何尺度设置；清理会改变局部表面细节"
layout: reference
description: "长度和质量阈值按几何尺度设置；清理会改变局部表面细节。"
cms_slug: "command-surfaceclean"
---

<p>长度和质量阈值按几何尺度设置；清理会改变局部表面细节。</p><h2>用法</h2><pre><code class="language-bash">surfaceClean body.stl 1e-6 0.01 bodyClean.stl</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">surfaceClean body.stl 1e-6 0.01 bodyClean.stl -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-no-clean</td><td>保留已有 polyMesh 文件；默认行为见完整帮助。</td></tr><tr><td>-scale &lt;factor&gt;</td><td>Input geometry scaling factor</td></tr><tr><td>-verbose</td><td>Additional verbosity (can be used multiple times)</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceClean [OPTIONS] &lt;input&gt; &lt;length&gt; &lt;quality&gt; &lt;output&gt;
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
