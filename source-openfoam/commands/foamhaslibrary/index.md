---
title: "foamHasLibrary · -detail 输出详细信息"
layout: reference
description: "-detail 输出详细信息。"
cms_slug: "command-foamhaslibrary"
---

<p>-detail 输出详细信息。</p><h2>用法</h2><pre><code class="language-bash">foamHasLibrary libfieldFunctionObjects.so</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-detail</td><td>Additional detail Override the file handler type Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-or</td><td>Success if any of the libraries can be loaded (does not short-circuit)</td></tr><tr><td>-verbose</td><td>Additional verbosity (can be used multiple times)</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamHasLibrary [OPTIONS] [&lt;lib...&gt;]
Options:
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -detail           Additional detail
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -or               Success if any of the libraries can be loaded
                    (does not short-circuit)
  -verbose          Additional verbosity (can be used multiple times)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Test if given libraries can be loaded

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamHasLibrary/foamHasLibrary.C">源码与说明</a> · <a href="/assets/command-help/foamhaslibrary.txt">帮助文本</a></p>
