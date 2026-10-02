---
title: "chemFoam · 单单元化学反应积分"
layout: reference
description: "单单元化学反应积分。"
cms_slug: "command-chemfoam"
---

<p>单单元化学反应积分。</p><h2>开始前</h2>
<p>使用已经建立单单元网格、反应机理、热物性和 <code>constant/initialConditions</code> 的化学算例 <code>baseCase</code>。以下温度和压力实验从各自的初始条件重新开始，保持同一反应机理与组成。 <code>foamCloneCase</code> 将最早时刻的场和 <code>constant</code>、<code>system</code> 复制到实验目录，各组对照从同一初态开始。</p>
<h2>示例 1：计算单单元反应过程</h2>
<pre><code class="language-bash">chemFoam -case baseCase &gt; baseCase/log.chemFoam 2&gt;&amp;1
head -n 6 baseCase/chemFoam.out
</code></pre>
<p>程序积分反应过程，<code>chemFoam.out</code> 前三列为时间、温度 K 和压力 Pa。用这三列可以绘制点火升温及压力变化曲线。</p>
<h2>示例 2：延长反应观察时间</h2>
<pre><code class="language-bash">foamDictionary baseCase/system/controlDict -entry endTime -set 0.1
chemFoam -case baseCase
</code></pre>
<p>将计算结束时间设成 0.1 s，从 <code>initialConditions</code> 给定的初态重新积分。适用于原观察区间更短、需要查看后续升温或趋近平衡的案例。</p>
<h2>示例 3：提高初始温度</h2>
<pre><code class="language-bash">foamCloneCase baseCase hot-study
foamDictionary hot-study/constant/initialConditions -entry T -set 1200
chemFoam -case hot-study &gt; hot-study/log.chemFoam 2&gt;&amp;1
</code></pre>
<p>将初温设为 1200 K，其余压力、组成和机理保持一致。对适用温度范围内的同一混合物，比较两条温度曲线的点火延迟。</p>
<h2>示例 4：提高初始压力</h2>
<pre><code class="language-bash">foamCloneCase baseCase pressure-study
foamDictionary pressure-study/constant/initialConditions -entry p -set 200000
chemFoam -case pressure-study &gt; pressure-study/log.chemFoam 2&gt;&amp;1
</code></pre>
<p><code>p</code> 的单位是 Pa，200000 Pa 为 2 bar。与基准算例比较时保留相同初温和组成，可单独观察压力对反应进程的影响。</p>
<h2>示例 5：进行初始温度扫描</h2>
<pre><code class="language-bash">for temperature in 1000 1100 1200; do
    caseDir="chem-${temperature}K"
    foamCloneCase baseCase "$caseDir"
    foamDictionary "$caseDir/constant/initialConditions" -entry T -set "$temperature"
    chemFoam -case "$caseDir" &gt; "$caseDir/log.chemFoam" 2&gt;&amp;1
done
</code></pre>
<p>循环创建三个独立算例，分别在 1000、1100、1200 K 下求解。每个目录各有一份 <code>chemFoam.out</code>，可把曲线画在同一坐标系，并按统一的温升或升温速率标准提取点火延迟。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-listFunctionObjects</code></td><td>列出可用的函数对象。</td></tr><tr><td><code>-listScalarBCs</code></td><td>列出标量场的边界条件类型，即 fvPatchField&lt;scalar&gt;。</td></tr><tr><td><code>-listVectorBCs</code></td><td>列出向量场的边界条件类型，即 fvPatchField&lt;vector&gt;。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-postProcess</code></td><td>仅执行函数对象后处理。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/h2">combustion/chemFoam/h2</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/gri">combustion/chemFoam/gri</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/ic8h18">combustion/chemFoam/ic8h18</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/nc7h16">combustion/chemFoam/nc7h16</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/ic8h18_TDAC">combustion/chemFoam/ic8h18_TDAC</a></li></ul><pre><code class="language-bash">mkdir -p &quot;$FOAM_RUN&quot;
cd &quot;$FOAM_RUN&quot;
cp -r &quot;$FOAM_TUTORIALS/combustion/chemFoam/h2&quot; chemFoam-study
cd chemFoam-study
ls</code></pre><p>使用一个新的目录名。算例中的 Allrun 列出网格、初始化和求解顺序；含多级网格或跨目录数据的教程，需要同时保留相邻文件。</p><details class="command-more-options"><summary>更多参数（13 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-listRegisteredSwitches</code></td><td>列出已注册、支持运行时修改的开关；可配合 -listUnsetSwitches。</td></tr><tr><td><code>-listSwitches</code></td><td>列出库中声明的开关；可配合 -listUnsetSwitches。</td></tr><tr><td><code>-listUnsetSwitches</code></td><td>将开关列表限定为 etc/controlDict 尚未设置的项。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/combustion/chemFoam/chemFoam.C">源码与说明</a> · <a href="/assets/command-help/chemfoam.txt">帮助文本</a></p>
