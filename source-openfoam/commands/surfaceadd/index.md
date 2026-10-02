---
title: "surfaceAdd · 连接两个表面数据集，不执行几何布尔并集"
layout: reference
description: "连接两个表面数据集，不执行几何布尔并集。"
cms_slug: "command-surfaceadd"
---

<p>连接两个表面数据集，不执行几何布尔并集。</p><h2>用法</h2><pre><code class="language-bash">surfaceAdd a.stl b.stl combined.stl</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">surfaceAdd a.stl b.stl combined.stl -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-mergeRegions</td><td>Combine regions from both surfaces</td></tr><tr><td>-points &lt;file&gt;</td><td>Provide additional points</td></tr><tr><td>-scale &lt;factor&gt;</td><td>Geometry scaling factor on input surfaces</td></tr><tr><td>-verbose</td><td>Additional verbosity (can be used multiple times)</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceAdd [OPTIONS] &lt;surface1&gt; &lt;surface2&gt; &lt;output&gt;
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
