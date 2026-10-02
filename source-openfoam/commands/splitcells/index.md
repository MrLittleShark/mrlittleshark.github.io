---
title: "splitCells · 用于网格单元的拓扑修复"
layout: reference
description: "用于网格单元的拓扑修复。"
cms_slug: "command-splitcells"
---

<p>用于网格单元的拓扑修复。</p><h2>用法</h2><pre><code class="language-bash">splitCells 90</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">splitCells 90 -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-geometry</td><td>Use geometric cut for hexes as well Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-overwrite</td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td>-set &lt;name&gt;</td><td>设置条目值，会修改文件。</td></tr><tr><td>-tol &lt;scalar&gt;</td><td>Edge snap tolerance (default 0.2)</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: splitCells [OPTIONS] &lt;edgeAngle&gt;
Arguments:
  &lt;edgeAngle&gt;       in degrees [0-360]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -geometry         Use geometric cut for hexes as well
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -set &lt;name&gt;       Split cells from specified cellSet only
  -tol &lt;scalar&gt;     Edge snap tolerance (default 0.2)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Split cells with flat faces

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/splitCells/splitCells.C">源码与说明</a> · <a href="/assets/command-help/splitcells.txt">帮助文本</a></p>
