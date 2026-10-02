---
title: "foamToTetDualMesh · 把单元场和边界面场映射为已有 tetDualMesh 的点场"
layout: reference
description: "把单元场和边界面场映射为已有 tetDualMesh 的点场。"
cms_slug: "command-foamtotetdualmesh"
---

<p>把单元场和边界面场映射为已有 tetDualMesh 的点场。</p><h2>开始前</h2>
<p>算例中已有原 polyMesh、目标区域 tetDualMesh/polyMesh 及其 pointDualAddressing。该映射表的长度须等于目标点数，正值对应原单元编号加 1，负值对应原边界面编号取负再减 1，0 对应未映射点。以下处理的是配套的网格与字段。</p>
<h2>示例 1：映射初始时刻的场</h2>
<pre><code class="language-bash">foamToTetDualMesh -time 0
</code></pre>
<p>读取 0 目录内的体标量、体矢量及张量场，按 pointDualAddressing 写出 0/tetDualMesh 下的同名点场。例如单元压力 p 转成目标网格的 pointScalarField。</p>
<h2>示例 2：映射指定结果时刻</h2>
<pre><code class="language-bash">foamToTetDualMesh -time 0.5
</code></pre>
<p>-time 选择最接近 0.5 的已有时间。各目标点从对应原单元或边界面取得数值；映射表中为 0 的点写入零值。适合把某一计算结果交给使用对偶点数据的后处理。</p>
<h2>示例 3：处理另一算例的最终结果</h2>
<pre><code class="language-bash">foamToTetDualMesh -case ./dualView -latestTime
</code></pre>
<p>dualView 已包含两套匹配网格和寻址表。-case 指定目录，-latestTime 选最后一个结果时间；输出仍位于这个时间的 tetDualMesh 区域下，原单元场保留。</p>
<h2>示例 4：转换一组已有时间</h2>
<pre><code class="language-bash">for t in 0.1 0.2 0.3; do
    foamToTetDualMesh -time "$t"
done
</code></pre>
<p>三个时间均已存在，并共享有效的对偶寻址关系。工具每次只选择一个时间，因此用循环分别产生三个时间的点场；网格拓扑改变时，应为该时刻准备匹配的目标网格和映射表。</p>
<h2>示例 5：检查目标网格和转换后的场类型</h2>
<pre><code class="language-bash">checkMesh -region tetDualMesh -constant
foamToTetDualMesh -time 0.5
foamDictionary 0.5/tetDualMesh/p -entry FoamFile/class -value
</code></pre>
<p>此例的两套网格保存在 constant，且 0.5/p 已存在。先检查目标区域网格，再映射压力；最后应读到 pointScalarField，可继续检查点数和映射表是否一致。转换程序读取目标网格，仅写转换后的场。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>排除 0/ 目录；当前实现会忽略此选项。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-time &lt;value&gt;</code></td><td>选择最接近给定数值的时刻。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/dataConversion/foamToTetDualMesh/foamToTetDualMesh.C">源码与说明</a> · <a href="/assets/command-help/foamtotetdualmesh.txt">帮助文本</a></p>
