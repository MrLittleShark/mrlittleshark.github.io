---
title: "profilingSummary · 读取启用 profiling 后生成的性能统计文件"
layout: reference
description: "读取启用 profiling 后生成的性能统计文件。"
cms_slug: "command-profilingsummary"
---

<p>读取启用 profiling 后生成的性能统计文件。</p><h2>用法</h2><pre><code class="language-bash">profilingSummary</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">profilingSummary -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-constant</td><td>将 constant 目录加入选择。</td></tr><tr><td>-latestTime</td><td>选择最近的结果时刻。</td></tr><tr><td>-noZero</td><td>跳过 0 时刻。</td></tr><tr><td>-time &lt;ranges&gt;</td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td>-withZero</td><td>Include &#x27;0/&#x27; dir in the times list</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: profilingSummary [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noZero           Exclude &#x27;0/&#x27; dir from the times list, has precedence over
                    the -withZero option
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -withZero         Include &#x27;0/&#x27; dir in the times list
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Collect profiling information from processor directories and summarize time
spent and number of calls as (max avg min) values.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/miscellaneous/profilingSummary/profilingSummary.C">源码与说明</a> · <a href="/assets/command-help/profilingsummary.txt">帮助文本</a></p>
