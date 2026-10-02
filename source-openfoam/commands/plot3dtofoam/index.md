---
title: "plot3dToFoam · -singleBlock 和 -2D 等选项用于指定输入网格形式"
layout: reference
description: "-singleBlock 和 -2D 等选项用于指定输入网格形式。"
cms_slug: "command-plot3dtofoam"
---

<p>-singleBlock 和 -2D 等选项用于指定输入网格形式。</p><h2>用法</h2><pre><code class="language-bash">plot3dToFoam mesh.xyz</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">plot3dToFoam mesh.xyz -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-2D &lt;thickness&gt;</td><td>Use when converting a 2-D mesh (applied before scale)</td></tr><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-noBlank</td><td>Skip blank items Do not execute function objects Set named OptimisationSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-scale &lt;factor&gt;</td><td>Geometry scaling factor - default is 1</td></tr><tr><td>-singleBlock</td><td>Input is a single block</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: plot3dToFoam [OPTIONS] &lt;PLOT3D geom file&gt;
Options:
  -2D &lt;thickness&gt;   Use when converting a 2-D mesh (applied before scale)
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
  -noBlank          Skip blank items
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -scale &lt;factor&gt;   Geometry scaling factor - default is 1
  -singleBlock      Input is a single block
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Plot3d mesh (ascii/formatted format) converter

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/plot3dToFoam/hexBlock.C">源码与说明</a> · <a href="/assets/command-help/plot3dtofoam.txt">帮助文本</a></p>
