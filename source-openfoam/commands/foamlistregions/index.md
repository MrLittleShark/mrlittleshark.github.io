---
title: "foamListRegions · 可按 fluid、solid 等 regionType 筛选，-finite-area 选择有限"
layout: reference
description: "可按 fluid、solid 等 regionType 筛选，-finite-area 选择有限面积区域。"
cms_slug: "command-foamlistregions"
---

<p>可按 fluid、solid 等 regionType 筛选，-finite-area 选择有限面积区域。</p><h2>用法</h2><pre><code class="language-bash">foamListRegions</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">foamListRegions -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-dry-run</td><td>Make reading optional and add verbosity Override the file handler type</td></tr><tr><td>-finite-area</td><td>List constant/finite-area/regionProperties (if available) Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-optional</td><td>A missing regionProperties is not treated as an error</td></tr><tr><td>-verbose</td><td>Additional verbosity</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamListRegions [OPTIONS] [&lt;regionType ... regionType&gt;]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dry-run          Make reading optional and add verbosity
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -finite-area      List constant/finite-area/regionProperties (if available)
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -optional         A missing regionProperties is not treated as an error
  -verbose          Additional verbosity
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

List volume regions from constant/regionProperties,
or area regions from constant/finite-area/regionProperties

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamListRegions/foamListRegions.C">源码与说明</a> · <a href="/assets/command-help/foamlistregions.txt">帮助文本</a></p>
