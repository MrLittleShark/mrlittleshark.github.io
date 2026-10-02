---
title: "PDRsetFields · 输入为 PDR 阻塞模型等专用数据"
layout: reference
description: "输入为 PDR 阻塞模型等专用数据。"
cms_slug: "command-pdrsetfields"
---

<p>输入为 PDR 阻塞模型等专用数据。</p><h2>用法</h2><pre><code class="language-bash">PDRsetFields</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">PDRsetFields -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-dict &lt;file&gt;</td><td>改用指定字典文件。</td></tr><tr><td>-dry-run</td><td>Read obstacles and write VTK only Override the file handler type Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-legacy</td><td>Force use of legacy obstacles table</td></tr><tr><td>-time &lt;time&gt;</td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: PDRsetFields [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dict &lt;file&gt;      Alternative PDRsetFieldsDict
  -dry-run          Read obstacles and write VTK only
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -legacy           Force use of legacy obstacles table
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -time &lt;time&gt;      Specify a time
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Processes a set of geometrical obstructions to determine the equivalent
blockage effects when setting cases for PDRFoam

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/PDR/PDRsetFields/PDRsetFields.C">源码与说明</a> · <a href="/assets/command-help/pdrsetfields.txt">帮助文本</a></p>
