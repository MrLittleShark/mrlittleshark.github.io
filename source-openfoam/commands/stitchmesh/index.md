---
title: "stitchMesh · -perfect 要求几何匹配；其余接口可按相应条件采用 -partial 或 -integra"
layout: reference
description: "-perfect 要求几何匹配；其余接口可按相应条件采用 -partial 或 -integral。"
cms_slug: "command-stitchmesh"
---

<p>-perfect 要求几何匹配；其余接口可按相应条件采用 -partial 或 -integral。</p><h2>用法</h2><pre><code class="language-bash">stitchMesh -perfect sideA sideB -overwrite</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">stitchMesh -perfect sideA sideB -overwrite -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-dict &lt;file&gt;</td><td>改用指定字典文件。</td></tr><tr><td>-integral</td><td>Couple integral master/slave patches (2 argument mode: default)</td></tr><tr><td>-intermediate</td><td>Write intermediate stages, not just the final result</td></tr><tr><td>-overwrite</td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td>-partial</td><td>Couple partially overlapping master/slave patches (2 argument mode)</td></tr><tr><td>-perfect</td><td>Couple perfectly aligned master/slave patches (2 argument mode)</td></tr><tr><td>-region &lt;name&gt;</td><td>指定网格区域名称。</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/stitchMesh/simple-cube1">mesh/stitchMesh/simple-cube1</a></li></ul><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: stitchMesh [OPTIONS] [&lt;master&gt; &lt;slave&gt;]
Arguments:
  &lt;master&gt;          The master patch name (non-dictionary mode)
  &lt;slave&gt;           The slave patch name (non-dictionary mode)
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dict &lt;file&gt;      Alternative stitchMeshDict
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -integral         Couple integral master/slave patches (2 argument mode:
                    default)
  -intermediate     Write intermediate stages, not just the final result
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -partial          Couple partially overlapping master/slave patches (2
                    argument mode)
  -perfect          Couple perfectly aligned master/slave patches (2 argument
                    mode)
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -toleranceDict &lt;file&gt;
                    Dictionary file with tolerances
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Merge the faces on specified patches (if geometrically possible) so that the
faces become internal.
This utility can be called without arguments (uses stitchMeshDict) or with
two arguments (master/slave patch names).

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/stitchMesh/stitchMesh.C">源码与说明</a> · <a href="/assets/command-help/stitchmesh.txt">帮助文本</a></p>
