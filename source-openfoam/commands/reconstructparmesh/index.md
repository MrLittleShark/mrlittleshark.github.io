---
title: "reconstructParMesh · 从处理器子域重构网格和寻址关系"
layout: reference
description: "从处理器子域重构网格和寻址关系。"
cms_slug: "command-reconstructparmesh"
---

<p>从处理器子域重构网格和寻址关系。</p><h2>开始前</h2>
<p>已有匹配的分区网格；动网格或并行网格生成的各时间拓扑需要分别处理。</p>
<h2>示例 1：重构恒定网格</h2>
<pre><code class="language-bash">reconstructParMesh -constant
</code></pre>
<p>从各processor的constant网格恢复全域网格，适合并行网格生成结束后的整理。</p>
<h2>示例 2：恢复最新动网格</h2>
<pre><code class="language-bash">reconstructParMesh -latestTime
</code></pre>
<p>选择最后保存的分区网格状态，重构完整几何和连接关系。</p>
<h2>示例 3：按处理器接口匹配</h2>
<pre><code class="language-bash">reconstructParMesh -constant -procMatch
</code></pre>
<p>只在processor边界上进行几何匹配，适合接口定义可靠的标准分区网格。</p>
<h2>示例 4：采用全边界几何匹配</h2>
<pre><code class="language-bash">reconstructParMesh -constant -fullMatch -mergeTol 1e-7
</code></pre>
<p>在全部边界上做更全面的匹配；mergeTol是相对包围盒尺寸的合并容差。</p>
<h2>示例 5：先恢复寻址再拼场</h2>
<pre><code class="language-bash">reconstructParMesh -latestTime -addressing-only
reconstructPar -latestTime
</code></pre>
<p>完整网格已存在且与分区几何一致时，只建立procAddressing而保留网格，再利用寻址重构字段。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-addressing-only</code></td><td>仅生成 procAddressing，保留已有网格。</td></tr><tr><td><code>-allAreas</code></td><td>选择有限面积 regionProperties 中的全部区域。</td></tr><tr><td><code>-allRegions</code></td><td>处理 regionProperties 中的全部区域。</td></tr><tr><td><code>-area-region &lt;name&gt;</code></td><td>指定有限面积网格区域，例如 -area-region shell。</td></tr><tr><td><code>-area-regions &lt;wordRes&gt;</code></td><td>选择有限面积区域，例如 -area-regions film；也可按 regionProperties 中的名称匹配，如 -area-regions &#x27;(film &quot;solid.*&quot;)&#x27;。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-cellDist</code></td><td>输出单元分区编号：labelList 可用于 manual 分区，volScalarField 可用于后处理。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-fullMatch</code></td><td>对全部边界面进行几何匹配，计算量较大。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-mergeTol &lt;scalar&gt;</code></td><td>设置合并距离，以包围盒尺寸的比例表示，默认为 1e-7。</td></tr><tr><td><code>-no-finite-area</code></td><td>跳过有限面积网格的重建。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noZero</code></td><td>排除 0/ 目录；此选项优先于 -withZero。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（19 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-procMatch</code></td><td>仅对进程间的边界面进行匹配。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，例如 -region gas。</td></tr><tr><td><code>-regions &lt;wordRes&gt;</code></td><td>指定一个区域或按 regionProperties 匹配多个区域，例如 -regions gas 或 -regions &#x27;(gas &quot;solid.*&quot;)&#x27;。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-verbose</code></td><td>显示更详细的输出；可重复使用以增加详细程度。</td></tr><tr><td><code>-withZero</code></td><td>将 0/ 目录加入时间选择。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/parallelProcessing/reconstructParMesh/reconstructParMesh.C">源码与说明</a> · <a href="/assets/command-help/reconstructparmesh.txt">帮助文本</a></p>
