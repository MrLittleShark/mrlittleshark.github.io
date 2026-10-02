---
title: "moveDynamicMesh · 运行动态网格更新，检查运动和拓扑变化"
layout: reference
description: "运行动态网格更新，检查运动和拓扑变化。"
cms_slug: "command-movedynamicmesh"
---

<p>运行动态网格更新，检查运动和拓扑变化。</p><h2>开始前</h2>
<p>已有 constant/dynamicMeshDict、所需位移或运动场，以及 controlDict 时间设置；运动边界与运动求解器一致。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：单独运行网格运动</h2>
<pre><code class="language-bash">moveDynamicMesh
</code></pre>
<p>按 controlDict 推进时间并调用 dynamicFvMesh 更新，写出设置的运动网格时间，便于先检查运动轨迹。</p>
<h2>示例 2：限制运动试验长度</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry endTime -set 0.1
moveDynamicMesh
</code></pre>
<p>将试验终止时间设为 0.1，仅生成起始运动阶段；检查最早出现的大变形或局部挤压。</p>
<h2>示例 3：检查 AMI 接口</h2>
<pre><code class="language-bash">moveDynamicMesh -checkAMI
</code></pre>
<p>用于存在 AMI 接口的动态网格；额外检查插值权重并写接口 VTK 文件，观察相对运动中的覆盖情况。</p>
<h2>示例 4：检查指定运动区域</h2>
<pre><code class="language-bash">moveDynamicMesh -region rotor
</code></pre>
<p>案例已经为 rotor 区域提供动态网格设置；只推进该区域，输出它的运动网格。</p>
<h2>示例 5：并行运动预演</h2>
<pre><code class="language-bash">decomposePar
mpirun -np 4 moveDynamicMesh -parallel -checkAMI
</code></pre>
<p>decomposeParDict 设置 4 个子域；运动在分区网格上执行，检查并行边界和 AMI 随运动的变化，结果写入 processor 目录。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-checkAMI</code></td><td>检查 AMI 插值权重，并将 AMI 边界写为 VTK 文件。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/pipe">mesh/blockMesh/pipe</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/moveDynamicMesh/badMove">mesh/moveDynamicMesh/badMove</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/moveDynamicMesh/bendJunction">mesh/moveDynamicMesh/bendJunction</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/moveDynamicMesh/faceZoneBlock">mesh/moveDynamicMesh/faceZoneBlock</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/moveDynamicMesh/twistingColumn">mesh/moveDynamicMesh/twistingColumn</a></li></ul><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/moveDynamicMesh/moveDynamicMesh.C">源码与说明</a> · <a href="/assets/command-help/movedynamicmesh.txt">帮助文本</a></p>
