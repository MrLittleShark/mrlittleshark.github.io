---
title: "magneticFoam · 计算永磁体产生的磁场"
layout: reference
description: "计算永磁体产生的磁场。"
cms_slug: "command-magneticfoam"
---

<p>计算永磁体产生的磁场。</p><h2>开始前</h2>
<p><code>magneticFoam</code> 用于永磁体产生的磁场。以下操作使用已完成网格与初始化的串行算例 <code>baseCase</code>；将它换成自己的目录名。各例中的新目录用于保留不同设置，运行前使用尚未存在的目录名。</p>
<h2>示例 1：计算磁场</h2>
<pre><code class="language-bash">magneticFoam -case baseCase
</code></pre>
<p>准备网格、磁势 <code>psi</code>、磁体参数和 <code>fvSolution</code> 后运行。程序求解磁势，并写出磁场强度 <code>H</code> 与磁通密度 <code>B</code>；输出目录在起始时刻基础上推进一步。</p>
<h2>示例 2：只保存磁通密度</h2>
<pre><code class="language-bash">magneticFoam -case baseCase -noH
</code></pre>
<p><code>-noH</code> 省去 <code>H</code> 的写出，仍保存磁势和 <code>B</code>。只关心磁通密度分布时，可减少一个矢量场的存储。</p>
<h2>示例 3：只保存磁场强度</h2>
<pre><code class="language-bash">magneticFoam -case baseCase -noB
</code></pre>
<p><code>-noB</code> 省去 <code>B</code> 的写出，保留磁势和 <code>H</code>。这里改变的是输出选择，磁势方程和磁体设置保持原样。</p>
<h2>示例 4：计算磁场梯度作用项</h2>
<pre><code class="language-bash">magneticFoam -case baseCase -HdotGradH
</code></pre>
<p>额外生成 <code>HdotGradH</code>，其计算式为 <code>H &amp; fvc::grad(H)</code>，可用于分析顺磁颗粒受力所需的场量。实际颗粒力还需结合磁化率与体积等参数。</p>
<h2>示例 5：仅保留磁势与梯度作用项</h2>
<pre><code class="language-bash">magneticFoam -case baseCase -noH -noB -HdotGradH
</code></pre>
<p>三个选项组合后，程序仍在内存中计算构造梯度项所需的 <code>H</code>，最终只写磁势和 <code>HdotGradH</code>。适合只需要后者进行进一步受力计算的工作流程。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-HdotGradH</code></td><td>写出顺磁性粒子受力所需的磁场项。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dry-run</code></td><td>通过一个时间步检查算例设置。</td></tr><tr><td><code>-dry-run-write</code></td><td>用一个时间步检查算例设置，并写出结果。</td></tr><tr><td><code>-listFunctionObjects</code></td><td>列出可用的函数对象。</td></tr><tr><td><code>-listScalarBCs</code></td><td>列出标量场的边界条件类型，即 fvPatchField&lt;scalar&gt;。</td></tr><tr><td><code>-listVectorBCs</code></td><td>列出向量场的边界条件类型，即 fvPatchField&lt;vector&gt;。</td></tr><tr><td><code>-noB</code></td><td>跳过磁感应强度 B 场的输出。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noH</code></td><td>跳过磁场强度 H 场的输出。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><details class="command-more-options"><summary>更多参数（19 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-listRegisteredSwitches</code></td><td>列出已注册、支持运行时修改的开关；可配合 -listUnsetSwitches。</td></tr><tr><td><code>-listSwitches</code></td><td>列出库中声明的开关；可配合 -listUnsetSwitches。</td></tr><tr><td><code>-listUnsetSwitches</code></td><td>将开关列表限定为 etc/controlDict 尚未设置的项。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/electromagnetics/magneticFoam/magneticFoam.C">源码与说明</a> · <a href="/assets/command-help/magneticfoam.txt">帮助文本</a></p>
