---
title: "star4ToFoam · 按文件名前缀读取 mesh.vrt、mesh.cel 等配套文件"
layout: reference
description: "按文件名前缀读取 mesh.vrt、mesh.cel 等配套文件。"
cms_slug: "command-star4tofoam"
---

<p>按文件名前缀读取 mesh.vrt、mesh.cel 等配套文件。</p><h2>用法</h2><pre><code class="language-bash">star4ToFoam mesh</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">star4ToFoam mesh -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-ascii</td><td>Write in ASCII instead of binary format</td></tr><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-scale &lt;factor&gt;</td><td>Geometry scaling factor - default is 0.001 ([mm] to [m])</td></tr><tr><td>-solids</td><td>Retain solid cells and treat like fluid cells</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: star4ToFoam [OPTIONS] &lt;prefix&gt;
Arguments:
  &lt;prefix&gt;          The prefix for the input PROSTAR files
Options:
  -ascii            Write in ASCII instead of binary format
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
  -scale &lt;factor&gt;   Geometry scaling factor - default is 0.001 ([mm] to [m])
  -solids           Retain solid cells and treat like fluid cells
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Convert STARCD/PROSTAR (v4) mesh to OpenFOAM

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/star4ToFoam/star4ToFoam.C">源码与说明</a> · <a href="/assets/command-help/star4tofoam.txt">帮助文本</a></p>
