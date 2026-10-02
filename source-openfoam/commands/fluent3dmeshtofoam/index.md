---
title: "fluent3DMeshToFoam · 用于 Fluent 三维网格的专用转换，按输入格式选择"
layout: reference
description: "用于 Fluent 三维网格的专用转换，按输入格式选择。"
cms_slug: "command-fluent3dmeshtofoam"
---

<p>用于 Fluent 三维网格的专用转换，按输入格式选择。</p><h2>用法</h2><pre><code class="language-bash">fluent3DMeshToFoam mesh.msh</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">fluent3DMeshToFoam mesh.msh -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-cubit</td><td>Special parsing of (incorrect) cubit files Set named DebugSwitch (default value: 1). [Can be used multiple times] Override the file handler type Specify cell groups to ignore Specify face groups to ignore Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-scale &lt;factor&gt;</td><td>Geometry scaling factor - default is 1</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: fluent3DMeshToFoam [OPTIONS] &lt;Fluent mesh file&gt;
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -cubit            Special parsing of (incorrect) cubit files
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -ignoreCellGroups &lt;names&gt;
                    Specify cell groups to ignore
  -ignoreFaceGroups &lt;names&gt;
                    Specify face groups to ignore
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
  -scale &lt;factor&gt;   Geometry scaling factor - default is 1
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Convert a Fluent mesh to OpenFOAM format

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/fluent3DMeshToFoam/Make/files">源码与说明</a> · <a href="/assets/command-help/fluent3dmeshtofoam.txt">帮助文本</a></p>
