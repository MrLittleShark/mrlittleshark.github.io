---
title: "dnsFoam · 各向同性湍流盒中的直接数值模拟"
layout: reference
description: "各向同性湍流盒中的直接数值模拟。"
cms_slug: "command-dnsfoam"
---

<p>各向同性湍流盒中的直接数值模拟。</p><h2>开始前</h2>
<p>以下示例使用已完成网格和初始场准备的官方 boxTurb16 案例，目录记为 baseCase。其规则周期网格用于各向同性湍流盒，初始时间为 0，原时间步为 0.025，运动黏度为 0.025。每项对照从同一份初始数据开始，使用尚未存在的新目录。配套输入见<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/DNS/dnsFoam/boxTurb16">官方 boxTurb16 算例</a>。 <code>foamCloneCase</code> 将最早时刻的场和 <code>constant</code>、<code>system</code> 复制到实验目录，各组对照从同一初态开始。</p>
<h2>示例 1：运行湍流盒基准计算</h2>
<pre><code class="language-bash">dnsFoam -case baseCase &gt; baseCase/log.dnsFoam 2&gt;&amp;1
tail -n 30 baseCase/log.dnsFoam
</code></pre>
<p>按 controlDict 设置推进速度和压力，并在指定波数范围施加随机驱动力。官方设置从 0 计算到 10，步长 0.025，每 0.25 保存结果。查看日志中的 Number of forced K、速度与压力求解信息以及动能等统计量。</p>
<h2>示例 2：缩短计算区间检查初始演化</h2>
<pre><code class="language-bash">foamCloneCase baseCase short-study
foamDictionary short-study/system/controlDict -entry startFrom -set startTime
foamDictionary short-study/system/controlDict -entry startTime -set 0
foamDictionary short-study/system/controlDict -entry stopAt -set endTime
foamDictionary short-study/system/controlDict -entry endTime -set 1
dnsFoam -case short-study &gt; short-study/log.dnsFoam 2&gt;&amp;1
</code></pre>
<p>保持官方步长 0.025，将结束时刻设为 1，共推进 40 步。先观察速度场和能量统计的初始变化，适合检查周期边界、初始场以及驱动力设置。新目录保留完整输入，便于与基准结果比较。</p>
<h2>示例 3：减半时间步比较统计结果</h2>
<pre><code class="language-bash">foamCloneCase baseCase half-step-study
foamDictionary half-step-study/system/controlDict -entry startFrom -set startTime
foamDictionary half-step-study/system/controlDict -entry startTime -set 0
foamDictionary half-step-study/system/controlDict -entry deltaT -set 0.0125
foamDictionary half-step-study/system/controlDict -entry writeControl -set runTime
foamDictionary half-step-study/system/controlDict -entry writeInterval -set 0.25
dnsFoam -case half-step-study &gt; half-step-study/log.dnsFoam 2&gt;&amp;1
</code></pre>
<p>把时间步由 0.025 减为 0.0125，保留结束时刻，并保持每 0.25 输出一次。随机驱动的增量随时间步变化，适合比较动能均值、波动幅度和能谱等统计量；统计区间和采样长度也应保持一致。</p>
<h2>示例 4：增大黏度观察耗散变化</h2>
<pre><code class="language-bash">foamCloneCase baseCase viscosity-study
foamDictionary viscosity-study/system/controlDict -entry startFrom -set startTime
foamDictionary viscosity-study/system/controlDict -entry startTime -set 0
foamDictionary viscosity-study/constant/transportProperties -entry nu -set 0.05
dnsFoam -case viscosity-study &gt; viscosity-study/log.dnsFoam 2&gt;&amp;1
</code></pre>
<p>nu 是运动黏度，量纲为 m²/s；0.05 是官方基准值 0.025 的两倍。其余参数保持相同，比较稳定统计区间的动能、耗散及高波数能谱，观察黏性增强后小尺度波动的变化。</p>
<h2>示例 5：减半随机驱动力的幅度参数</h2>
<pre><code class="language-bash">foamCloneCase baseCase forcing-study
foamDictionary forcing-study/system/controlDict -entry startFrom -set startTime
foamDictionary forcing-study/system/controlDict -entry startTime -set 0
foamDictionary forcing-study/constant/turbulenceProperties -entry UOsigma -set 0.0451475
dnsFoam -case forcing-study &gt; forcing-study/log.dnsFoam 2&gt;&amp;1
</code></pre>
<p>UOsigma 乘在 UO 随机过程的增量幅度上，这里取原值 0.090295 的一半。保持 UOalpha=0.81532 和波数范围 7&lt;|K|&lt;10，比较动能与能谱对驱动强度的响应。波数范围由 UOKlower、UOKupper 控制，可在下一组独立试验中改变，以研究驱动尺度。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-listFunctionObjects</code></td><td>列出可用的函数对象。</td></tr><tr><td><code>-listScalarBCs</code></td><td>列出标量场的边界条件类型，即 fvPatchField&lt;scalar&gt;。</td></tr><tr><td><code>-listVectorBCs</code></td><td>列出向量场的边界条件类型，即 fvPatchField&lt;vector&gt;。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-postProcess</code></td><td>仅执行函数对象后处理。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/DNS/dnsFoam/boxTurb16">DNS/dnsFoam/boxTurb16</a></li></ul><pre><code class="language-bash">mkdir -p &quot;$FOAM_RUN&quot;
cd &quot;$FOAM_RUN&quot;
cp -r &quot;$FOAM_TUTORIALS/DNS/dnsFoam/boxTurb16&quot; dnsFoam-study
cd dnsFoam-study
ls</code></pre><p>使用一个新的目录名。算例中的 Allrun 列出网格、初始化和求解顺序；含多级网格或跨目录数据的教程，需要同时保留相邻文件。</p><details class="command-more-options"><summary>更多参数（19 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-listRegisteredSwitches</code></td><td>列出已注册、支持运行时修改的开关；可配合 -listUnsetSwitches。</td></tr><tr><td><code>-listSwitches</code></td><td>列出库中声明的开关；可配合 -listUnsetSwitches。</td></tr><tr><td><code>-listUnsetSwitches</code></td><td>将开关列表限定为 etc/controlDict 尚未设置的项。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/DNS/dnsFoam/dnsFoam.C">源码与说明</a> · <a href="/assets/command-help/dnsfoam.txt">帮助文本</a></p>
