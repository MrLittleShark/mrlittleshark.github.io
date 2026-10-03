---
title: "boundaryFoam · 求解一维湍流边界层，生成可用于入口边界的流动剖面"
layout: reference
description: "求解一维湍流边界层，生成可用于入口边界的流动剖面。"
cms_slug: "command-boundaryfoam"
---

<p>求解一维湍流边界层，生成可用于入口边界的流动剖面。</p><h2>开始前</h2>
<p>在已准备好一维网格、<code>U</code>、湍流量和 <code>constant/transportProperties</code> 的算例 <code>baseCase</code> 中学习。该求解器按指定平均速度迭代建立充分发展剖面；结果通过图线文件输出。新实验分别放入尚未存在的目录。 <code>foamCloneCase</code> 将最早时刻的场和 <code>constant</code>、<code>system</code> 复制到实验目录，各组对照从同一初态开始。</p>
<h2>示例 1：计算一维速度与湍流剖面</h2>
<pre><code class="language-bash">boundaryFoam -case baseCase &gt; baseCase/log.boundaryFoam 2&gt;&amp;1
</code></pre>
<p>程序以给定平均速度 <code>Ubar</code> 为目标，逐步修正驱动压力梯度，并在写出时刻生成剖面文件。日志中的 <code>pressure gradient</code> 给出维持该流量所需的压力梯度。</p>
<h2>示例 2：每十次迭代输出剖面</h2>
<pre><code class="language-bash">foamDictionary baseCase/system/controlDict -entry writeControl -set timeStep
foamDictionary baseCase/system/controlDict -entry writeInterval -set 10
boundaryFoam -case baseCase
</code></pre>
<p>将写出频率改成每 10 次迭代，可比较速度剖面如何趋于稳定。<code>deltaT</code> 沿用官方一维稳态教程中的迭代设置。</p>
<h2>示例 3：输出更高精度的文本剖面</h2>
<pre><code class="language-bash">foamDictionary baseCase/system/controlDict -entry writePrecision -set 10
foamDictionary baseCase/system/controlDict -entry graphFormat -set raw
boundaryFoam -case baseCase
</code></pre>
<p><code>raw</code> 保存便于绘图软件读取的坐标与场值列；<code>writePrecision 10</code> 保留更多有效数字。适合将入口剖面导入另一算例或比较两组结果。</p>
<h2>示例 4：增加迭代以比较剖面稳定性</h2>
<pre><code class="language-bash">foamCloneCase baseCase longer-study
foamDictionary longer-study/system/controlDict -entry startFrom -set startTime
foamDictionary longer-study/system/controlDict -entry endTime -set 2000
boundaryFoam -case longer-study &gt; longer-study/log.boundaryFoam 2&gt;&amp;1
</code></pre>
<p>这个例子适用于原设置 <code>deltaT 1</code>、<code>endTime 1000</code> 的一维教程。把迭代上限增加到 2000，再比较最后两次输出的速度、湍流量和压力梯度。</p>
<h2>示例 5：改变目标平均速度</h2>
<pre><code class="language-bash">foamCloneCase baseCase faster-study
foamDictionary faster-study/constant/transportProperties -entry Ubar -set "[0 1 -1 0 0 0 0] (20 0 0)"
boundaryFoam -case faster-study &gt; faster-study/log.boundaryFoam 2&gt;&amp;1
</code></pre>
<p>本例用于沿 x 方向流动、原平均速度低于 20 m/s 的教程。<code>Ubar</code> 是带量纲的目标平均速度。改变它后，比较壁面剪切、湍流剖面和日志中驱动压力梯度的变化。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dry-run</code></td><td>通过一个时间步检查算例设置。</td></tr><tr><td><code>-dry-run-write</code></td><td>用一个时间步检查算例设置，并写出结果。</td></tr><tr><td><code>-listFunctionObjects</code></td><td>列出可用的函数对象。</td></tr><tr><td><code>-listFvOptions</code></td><td>列出可用的 fvOptions 源项和约束。</td></tr><tr><td><code>-listScalarBCs</code></td><td>列出标量场的边界条件类型，即 fvPatchField&lt;scalar&gt;。</td></tr><tr><td><code>-listTurbulenceModels</code></td><td>列出可用的湍流模型。</td></tr><tr><td><code>-listVectorBCs</code></td><td>列出向量场的边界条件类型，即 fvPatchField&lt;vector&gt;。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/surfaceMountedCube/initChannel">incompressible/pimpleFoam/LES/surfaceMountedCube/initChannel</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/boundaryFoam/steadyBoundaryLayer/setups.orig/common">incompressible/boundaryFoam/steadyBoundaryLayer/setups.orig/common</a></li></ul><pre><code class="language-bash">mkdir -p &quot;$FOAM_RUN&quot;
cd &quot;$FOAM_RUN&quot;
cp -r &quot;$FOAM_TUTORIALS/incompressible/pimpleFoam/LES/surfaceMountedCube/initChannel&quot; boundaryFoam-study
cd boundaryFoam-study
ls</code></pre><p>使用一个新的目录名。算例中的 Allrun 列出网格、初始化和求解顺序；含多级网格或跨目录数据的教程，需要同时保留相邻文件。</p><details class="command-more-options"><summary>更多参数（13 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-listRegisteredSwitches</code></td><td>列出已注册、支持运行时修改的开关；可配合 -listUnsetSwitches。</td></tr><tr><td><code>-listSwitches</code></td><td>列出库中声明的开关；可配合 -listUnsetSwitches。</td></tr><tr><td><code>-listUnsetSwitches</code></td><td>将开关列表限定为 etc/controlDict 尚未设置的项。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/incompressible/boundaryFoam/boundaryFoam.C">源码与说明</a> · <a href="/assets/command-help/boundaryfoam.txt">帮助文本</a></p>
