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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/miscellaneous/postChannel/postChannel.C">源码与说明</a> · <a href="/assets/command-help/postchannel.txt">帮助文本</a></p>
