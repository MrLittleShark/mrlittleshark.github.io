---
title: "financialFoam · 求解 Black–Scholes 方程，计算金融衍生品价格"
layout: reference
description: "求解 Black–Scholes 方程，计算金融衍生品价格。"
cms_slug: "command-financialfoam"
---

<p>求解 Black–Scholes 方程，计算金融衍生品价格。</p><h2>开始前</h2>
<p>使用欧洲看涨期权算例 <code>baseCase</code>。<code>financialFoam</code> 用网格横坐标表示标的价格，读取 <code>constant/financialProperties</code> 中的执行价、利率和波动率，初始化到期收益后求解 Black–Scholes 方程。以下各组从同一输入独立计算。 <code>foamCloneCase</code> 将最早时刻的场和 <code>constant</code>、<code>system</code> 复制到实验目录，各组对照从同一初态开始。</p>
<h2>示例 1：计算期权价值曲线</h2>
<pre><code class="language-bash">financialFoam -case baseCase &gt; baseCase/log.financialFoam 2&gt;&amp;1
</code></pre>
<p>结果 <code>V</code> 是期权价值，<code>delta</code> 是价值相对标的价格的导数。写出时刻还生成图线数据，便于比较不同剩余期限下的价格曲线。</p>
<h2>示例 2：改变执行价格</h2>
<pre><code class="language-bash">foamCloneCase baseCase strike-study
foamDictionary strike-study/constant/financialProperties -entry strike -set "[0 1 0 0 0 0 0] 100"
financialFoam -case strike-study
</code></pre>
<p>把执行价设为 100。此模型借用网格的长度维度表示价格，因此输入保留源码要求的量纲形式。网格的标的价格范围应覆盖执行价及其两侧，再观察收益曲线拐点如何移动。</p>
<h2>示例 3：改变无风险利率</h2>
<pre><code class="language-bash">foamCloneCase baseCase rate-study
foamDictionary rate-study/constant/financialProperties -entry r -set "[0 0 -1 0 0 0 0] 0.05"
financialFoam -case rate-study
</code></pre>
<p>当算例时间单位为年时，0.05 表示年化利率 5%。保持执行价、波动率和期限一致，可单独比较利率对期权价值的影响。</p>
<h2>示例 4：改变波动率</h2>
<pre><code class="language-bash">foamCloneCase baseCase volatility-study
foamDictionary volatility-study/constant/financialProperties -entry sigma -set "[0 0 -0.5 0 0 0 0] 0.2"
financialFoam -case volatility-study
</code></pre>
<p>按年计时的模型中，0.2 对应年化波动率 20%。波动率进入扩散项，比较相同期限定价曲线，可以观察波动性对价值的影响。</p>
<h2>示例 5：批量比较三种波动率</h2>
<pre><code class="language-bash">for sigma in 0.1 0.2 0.3; do
    caseDir="sigma-${sigma}"
    foamCloneCase baseCase "$caseDir"
    foamDictionary "$caseDir/constant/financialProperties" -entry sigma \
        -set "[0 0 -0.5 0 0 0 0] $sigma"
    financialFoam -case "$caseDir" &gt; "$caseDir/log.financialFoam" 2&gt;&amp;1
done
</code></pre>
<p>三个新目录使用同一网格、执行价和利率，只改变波动率。在同一输出时刻比较 <code>V</code> 和 <code>delta</code>，就能把波动率变化与价格、敏感度的变化联系起来。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dry-run</code></td><td>通过一个时间步检查算例设置。</td></tr><tr><td><code>-dry-run-write</code></td><td>用一个时间步检查算例设置，并写出结果。</td></tr><tr><td><code>-listFunctionObjects</code></td><td>列出可用的函数对象。</td></tr><tr><td><code>-listScalarBCs</code></td><td>列出标量场的边界条件类型，即 fvPatchField&lt;scalar&gt;。</td></tr><tr><td><code>-listVectorBCs</code></td><td>列出向量场的边界条件类型，即 fvPatchField&lt;vector&gt;。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-postProcess</code></td><td>仅执行函数对象后处理。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/financial/financialFoam/europeanCall">financial/financialFoam/europeanCall</a></li></ul><pre><code class="language-bash">mkdir -p &quot;$FOAM_RUN&quot;
cd &quot;$FOAM_RUN&quot;
cp -r &quot;$FOAM_TUTORIALS/financial/financialFoam/europeanCall&quot; financialFoam-study
cd financialFoam-study
ls</code></pre><p>使用一个新的目录名。算例中的 Allrun 列出网格、初始化和求解顺序；含多级网格或跨目录数据的教程，需要同时保留相邻文件。</p><details class="command-more-options"><summary>更多参数（19 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-listRegisteredSwitches</code></td><td>列出已注册、支持运行时修改的开关；可配合 -listUnsetSwitches。</td></tr><tr><td><code>-listSwitches</code></td><td>列出库中声明的开关；可配合 -listUnsetSwitches。</td></tr><tr><td><code>-listUnsetSwitches</code></td><td>将开关列表限定为 etc/controlDict 尚未设置的项。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/financial/financialFoam/financialFoam.C">源码与说明</a> · <a href="/assets/command-help/financialfoam.txt">帮助文本</a></p>
