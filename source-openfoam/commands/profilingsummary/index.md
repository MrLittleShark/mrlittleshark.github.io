---
title: "profilingSummary · 汇总各处理器的性能剖析记录"
layout: reference
description: "汇总各处理器的性能剖析记录。"
cms_slug: "command-profilingsummary"
---

<p>汇总各处理器的性能剖析记录。</p><h2>开始前</h2>
<p>计算时已启用并写出profiling数据；工具读取对应时间中的记录，汇总调用数、耗时及可用内存信息。</p>
<h2>示例 1：汇总最新性能记录</h2>
<pre><code class="language-bash">profilingSummary -latestTime
</code></pre>
<p>选最后保存的profiling记录，对各处理器统计做汇总，写入postProcessing/profiling。</p>
<h2>示例 2：汇总指定时刻</h2>
<pre><code class="language-bash">profilingSummary -time 100
</code></pre>
<p>时间100已有性能记录时，生成该阶段的摘要，便于定位计算成本。</p>
<h2>示例 3：比较多个阶段</h2>
<pre><code class="language-bash">profilingSummary -time '100,200,300'
</code></pre>
<p>分别汇总三个时刻，比较网格更新、压力求解等模块的耗时变化。</p>
<h2>示例 4：忽略初始阶段</h2>
<pre><code class="language-bash">profilingSummary -time '200:500' -noZero
</code></pre>
<p>只整理后期时间段，适合分析进入稳定工作状态后的并行负载。</p>
<h2>示例 5：比较另一并行规模</h2>
<pre><code class="language-bash">profilingSummary -case ./run-16cores -latestTime
</code></pre>
<p>run-16cores已保存16核案例的profiling数据；与其他规模的摘要比较最大、平均、最小耗时，检查负载差异。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-withZero</code></td><td>Include &#x27;0/&#x27; dir in the times list</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: profilingSummary [OPTIONS]
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
