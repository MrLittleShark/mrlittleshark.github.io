---
title: "reconstructPar · 把并行结果的字段重构到完整案例"
layout: reference
description: "把并行结果的字段重构到完整案例。"
cms_slug: "command-reconstructpar"
---

<p>把并行结果的字段重构到完整案例。</p><h2>开始前</h2>
<p>已有processor结果和匹配的完整网格/寻址信息；网格需重构时先使用reconstructParMesh。</p>
<h2>示例 1：重构全部可选结果</h2>
<pre><code class="language-bash">reconstructPar
</code></pre>
<p>将分区场按寻址信息拼回完整场，在原案例对应时间目录写结果。</p>
<h2>示例 2：仅重构最新时刻</h2>
<pre><code class="language-bash">reconstructPar -latestTime
</code></pre>
<p>适合只查看最终计算状态，减少大量历史结果的读写。</p>
<h2>示例 3：仅提取速度和压力</h2>
<pre><code class="language-bash">reconstructPar -latestTime -fields '(U p)' -no-lagrangian
</code></pre>
<p>只处理U、p，跳过粒子数据，适合快速查看流场。</p>
<h2>示例 4：补齐新产生的时间</h2>
<pre><code class="language-bash">reconstructPar -newTimes -time '1:5'
</code></pre>
<p>只重构1至5区间内尚未在完整案例中存在的时间，适合计算继续推进后的增量整理。</p>
<h2>示例 5：重构所有区域的初值与结果</h2>
<pre><code class="language-bash">reconstructPar -allRegions -withZero
</code></pre>
<p>包括0时刻，并对regionProperties中的全部区域处理，适合多区域案例完整交付。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allAreas</code></td><td>选择有限面积 regionProperties 中的全部区域。</td></tr><tr><td><code>-allRegions</code></td><td>处理 regionProperties 中的全部区域。</td></tr><tr><td><code>-area-region &lt;name&gt;</code></td><td>指定有限面积网格区域，例如 -area-region shell。</td></tr><tr><td><code>-area-regions &lt;wordRes&gt;</code></td><td>选择有限面积区域，例如 -area-regions film；也可按 regionProperties 中的名称匹配，如 -area-regions &#x27;(film &quot;solid.*&quot;)&#x27;。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-fields &lt;wordRes&gt;</code></td><td>选择要处理的一个或多个场，默认全部；例如 T 或 &#x27;(p T U &quot;alpha.*&quot;)&#x27;。</td></tr><tr><td><code>-lagrangianFields &lt;wordRes&gt;</code></td><td>选择要重建的粒子场，默认全部，例如 &#x27;(U d)&#x27;；粒子位置始终包含在内。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-newTimes</code></td><td>仅重建尚不存在的时间目录。</td></tr><tr><td><code>-no-fields</code></td><td>跳过场数据的重建。</td></tr><tr><td><code>-no-lagrangian</code></td><td>跳过拉格朗日粒子位置和场的重建。</td></tr><tr><td><code>-no-sets</code></td><td>跳过 cellSet、faceSet 和 pointSet 的重建。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（19 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-noZero</code></td><td>排除 0/ 目录；此选项优先于 -withZero。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，例如 -region gas。</td></tr><tr><td><code>-regions &lt;wordRes&gt;</code></td><td>指定一个区域或按 regionProperties 匹配多个区域，例如 -regions gas 或 -regions &#x27;(gas &quot;solid.*&quot;)&#x27;。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-verbose</code></td><td>显示更详细的输出；可重复使用以增加详细程度。</td></tr><tr><td><code>-withZero</code></td><td>将 0/ 目录加入时间选择。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/parallelProcessing/reconstructPar/reconstructPar.C">源码与说明</a> · <a href="/assets/command-help/reconstructpar.txt">帮助文本</a></p>
