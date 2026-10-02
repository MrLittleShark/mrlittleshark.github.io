---
title: "decomposePar · 把网格和场划分到多个处理器子域"
layout: reference
description: "把网格和场划分到多个处理器子域。"
cms_slug: "command-decomposepar"
---

<p>把网格和场划分到多个处理器子域。</p><h2>开始前</h2>
<p>已有完整案例和system/decomposeParDict；numberOfSubdomains与后续MPI进程数一致。</p>
<h2>示例 1：按字典分区</h2>
<pre><code class="language-bash">decomposePar
</code></pre>
<p>读取分区方法与子域数量，生成processor目录及对应网格、场，供并行求解器使用。</p>
<h2>示例 2：先比较8分区方案</h2>
<pre><code class="language-bash">decomposePar -dry-run -domains 8 -method scotch -cellDist
</code></pre>
<p>-domains与-method在dry-run中临时覆盖设置；测试8个scotch子域并写可视化cellDist，保留原分区目录。</p>
<h2>示例 3：只划分网格</h2>
<pre><code class="language-bash">decomposePar -no-fields
</code></pre>
<p>创建几何分区和寻址关系，暂不分解体场与粒子场，适合后续单独准备字段。</p>
<h2>示例 4：复用网格分区更新场</h2>
<pre><code class="language-bash">decomposePar -fields -time 0
</code></pre>
<p>已有分区几何且原网格未改变时，只把0时刻场按已有寻址分配，适合调整初值后重复使用网格。</p>
<h2>示例 5：多区域并行准备</h2>
<pre><code class="language-bash">decomposePar -allRegions -cellDist
</code></pre>
<p>regionProperties已有各区域，按相应分区设置生成区域网格及cellDist，检查流体与固体的工作量分布。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allAreas</code></td><td>选择有限面积 regionProperties 中的全部区域。</td></tr><tr><td><code>-allRegions</code></td><td>处理 regionProperties 中的全部区域。</td></tr><tr><td><code>-area-region &lt;name&gt;</code></td><td>指定有限面积网格区域，例如 -area-region shell。</td></tr><tr><td><code>-area-regions &lt;wordRes&gt;</code></td><td>选择有限面积区域，例如 -area-regions film；也可按 regionProperties 中的名称匹配，如 -area-regions &#x27;(film &quot;solid.*&quot;)&#x27;。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-cellDist</code></td><td>将单元分区编号写为 labelList，供 manual 分区使用；同时写出 volScalarField，便于可视化。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-copyUniform</code></td><td>同时复制 uniform/ 目录。</td></tr><tr><td><code>-copyZero</code></td><td>直接将 0/ 复制到各 processor 目录，替代初始场分解。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-domains &lt;N&gt;</code></td><td>覆盖 numberOfSubdomains；仅在 -dry-run 下使用。</td></tr><tr><td><code>-dry-run</code></td><td>仅测试分区，保留原网格；此时 -cellDist 仅写出 VTK。</td></tr><tr><td><code>-fields</code></td><td>沿用已有网格分区，仅分解场数据。</td></tr><tr><td><code>-force</code></td><td>分解网格前删除已有 processor 子目录。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-decomposepardict/">decomposeParDict</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/preProcessing/decompositionConstraints/geometric">preProcessing/decompositionConstraints/geometric</a></li></ul><details class="command-more-options"><summary>更多参数（26 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-ifRequired</code></td><td>仅在子域数量发生变化时重新分解网格。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-method &lt;name&gt;</code></td><td>覆盖分区方法；仅在 -dry-run 下使用。</td></tr><tr><td><code>-no-fields</code></td><td>跳过体场、有限面积场和拉格朗日场的分解。</td></tr><tr><td><code>-no-finite-area</code></td><td>跳过有限面积网格及场的分解。</td></tr><tr><td><code>-no-lagrangian</code></td><td>跳过拉格朗日粒子云的分解。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-no-sets</code></td><td>跳过 cellSet、faceSet 和 pointSet 的分解。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，例如 -region gas。</td></tr><tr><td><code>-regions &lt;wordRes&gt;</code></td><td>指定一个区域或按 regionProperties 匹配多个区域，例如 -regions gas 或 -regions &#x27;(gas &quot;solid.*&quot;)&#x27;。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-verbose</code></td><td>显示更详细的输出；可重复使用以增加详细程度。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/parallelProcessing/decomposePar/decomposePar.C">源码与说明</a> · <a href="/assets/command-help/decomposepar.txt">帮助文本</a></p>
