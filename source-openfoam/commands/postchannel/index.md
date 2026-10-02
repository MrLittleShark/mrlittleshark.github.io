---
title: "postChannel · 把通道湍流统计场沿均匀方向平均为壁法向剖面"
layout: reference
description: "把通道湍流统计场沿均匀方向平均为壁法向剖面。"
cms_slug: "command-postchannel"
---

<p>把通道湍流统计场沿均匀方向平均为壁法向剖面。</p><h2>开始前</h2>
<p>已有constant/postChannelDict、运动黏度及UMean、UPrime2Mean、pPrime2Mean；通道分层和对称设置与网格一致。</p>
<h2>示例 1：处理最新统计结果</h2>
<pre><code class="language-bash">postChannel -latestTime
</code></pre>
<p>读取统计场并沿通道均匀方向归并，输出平均速度、雷诺应力等壁法向曲线。</p>
<h2>示例 2：处理指定统计时刻</h2>
<pre><code class="language-bash">postChannel -time 100
</code></pre>
<p>时间100已包含完整平均场时，导出该统计积累阶段的通道剖面。</p>
<h2>示例 3：比较多个平均窗口结果</h2>
<pre><code class="language-bash">postChannel -time '100,200,300'
</code></pre>
<p>依次处理三个保存时刻，比较平均剖面随统计样本增加是否趋于稳定。</p>
<h2>示例 4：跳过初始未统计场</h2>
<pre><code class="language-bash">postChannel -noZero -time '100:300'
</code></pre>
<p>只对所选后期结果进行通道平均，避免把初始场当作统计结果。</p>
<h2>示例 5：先重构统计场再处理</h2>
<pre><code class="language-bash">reconstructPar -latestTime -fields '(UMean UPrime2Mean pPrime2Mean)'
postChannel -latestTime
</code></pre>
<p>postChannel为串行工具；先从分区结果重构它实际需要的三个统计场，再生成全通道曲线。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: postChannel [OPTIONS]
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

Post-process data from channel flow calculations

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/miscellaneous/postChannel/postChannel.C">源码与说明</a> · <a href="/assets/command-help/postchannel.txt">帮助文本</a></p>
