---
title: "foamListTimes · 列出符合条件的案例时间目录"
layout: reference
description: "列出符合条件的案例时间目录。"
cms_slug: "command-foamlisttimes"
---

<p>列出符合条件的案例时间目录。</p><h2>开始前</h2>
<p>已有案例或processor结果；以下实例只列目录，不执行删除。</p>
<h2>示例 1：列出计算结果时间</h2>
<pre><code class="language-bash">foamListTimes
</code></pre>
<p>输出标准时间选择范围内的数值目录，可用于了解已保存的结果时刻。</p>
<h2>示例 2：包含初始0目录</h2>
<pre><code class="language-bash">foamListTimes -withZero
</code></pre>
<p>把0纳入结果列表，适合检查初场和输出时间是否齐全。</p>
<h2>示例 3：查找最新结果</h2>
<pre><code class="language-bash">foamListTimes -latestTime
</code></pre>
<p>输出最后一个可用数值时刻，常用于后处理脚本选择最终状态。</p>
<h2>示例 4：筛选指定范围</h2>
<pre><code class="language-bash">foamListTimes -time '0.1:0.5,1:2' -noZero
</code></pre>
<p>只列两个时间区间内的目录，方便决定重构、转换或动画的处理范围。</p>
<h2>示例 5：查看并行输出时刻</h2>
<pre><code class="language-bash">foamListTimes -processor -latestTime
</code></pre>
<p>从processor0读取时间列表，确定并行计算已写出的最新时刻，再决定是否重构。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-processor</code></td><td>List times from processor0/ directory</td></tr><tr><td><code>-rm</code></td><td>Remove selected time directories</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-verbose</code></td><td>Report progress of -rm option</td></tr><tr><td><code>-withZero</code></td><td>Include &#x27;0/&#x27; dir in the times list</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamListTimes [OPTIONS]
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
  -processor        List times from processor0/ directory
  -rm               Remove selected time directories
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -verbose          Report progress of -rm option
  -withZero         Include &#x27;0/&#x27; dir in the times list
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

List times using the timeSelector, or use to remove selected time directories

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamListTimes/foamListTimes.C">源码与说明</a> · <a href="/assets/command-help/foamlisttimes.txt">帮助文本</a></p>
