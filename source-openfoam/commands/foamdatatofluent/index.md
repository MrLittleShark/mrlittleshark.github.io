---
title: "foamDataToFluent · 按映射字典把场数据导出为 Fluent 数据文件"
layout: reference
description: "按映射字典把场数据导出为 Fluent 数据文件。"
cms_slug: "command-foamdatatofluent"
---

<p>按映射字典把场数据导出为 Fluent 数据文件。</p><h2>开始前</h2>
<p>已有匹配的OpenFOAM网格和字段，以及system/foamDataToFluentDict；Fluent端使用与之对应的网格。</p>
<h2>示例 1：转换已有结果</h2>
<pre><code class="language-bash">foamDataToFluent
</code></pre>
<p>读取字段映射规则并转换选中的时间，输出Fluent可读取的数据文件。</p>
<h2>示例 2：只转换最后时刻</h2>
<pre><code class="language-bash">foamDataToFluent -latestTime
</code></pre>
<p>仅写最新结果，适合把最终解传给对应Fluent网格继续分析。</p>
<h2>示例 3：转换明确时刻</h2>
<pre><code class="language-bash">foamDataToFluent -time 1
</code></pre>
<p>选择已有时间1，便于把同一物理时刻的解在不同后处理软件中对照。</p>
<h2>示例 4：转换一段瞬态结果</h2>
<pre><code class="language-bash">foamDataToFluent -time '0.1:0.5' -noZero
</code></pre>
<p>导出0.1到0.5的已有结果并排除初值，输出可用于瞬态场对比。</p>
<h2>示例 5：并行计算后再转换</h2>
<pre><code class="language-bash">reconstructPar -latestTime
foamDataToFluent -latestTime
</code></pre>
<p>先把processor场重构成完整场，再按Fluent映射规则导出，保证字段对应完整网格。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamDataToFluent [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
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
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Translate OpenFOAM data to Fluent format

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/dataConversion/foamDataToFluent/writeFluentScalarField.C">源码与说明</a> · <a href="/assets/command-help/foamdatatofluent.txt">帮助文本</a></p>
