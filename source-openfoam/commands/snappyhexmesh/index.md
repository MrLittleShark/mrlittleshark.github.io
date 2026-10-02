---
title: "snappyHexMesh · 细化背景网格，贴合几何表面，并按设置生成边界层"
layout: reference
description: "细化背景网格，贴合几何表面，并按设置生成边界层。"
cms_slug: "command-snappyhexmesh"
---

<p>细化背景网格，贴合几何表面，并按设置生成边界层。</p><h2>开始前</h2>
<p>先有blockMesh背景网格、snappyHexMeshDict和表面几何。每个网格方案在独立副本生成。</p>
<h2>示例 1：检查几何输入</h2>
<pre><code class="language-bash">snappyHexMesh -checkGeometry
</code></pre>
<p>检查字典引用的几何与区域，先定位表面缺陷和尺寸问题。</p>
<h2>示例 2：检查算例设置</h2>
<pre><code class="language-bash">snappyHexMesh -dry-run
</code></pre>
<p>执行简化设置检查流程，便于发现缺失几何、字典条目和不合理选择。</p>
<h2>示例 3：生成贴体网格</h2>
<pre><code class="language-bash">snappyHexMesh
</code></pre>
<p>执行字典启用的细化、贴合、层生成阶段，默认保留各阶段对应的网格输出。</p>
<h2>示例 4：使用另一套控制</h2>
<pre><code class="language-bash">snappyHexMesh -dict system/snappyHexMeshDict.fine
</code></pre>
<p>已准备fine字典时选择它，比较表面细化等级、间隙分辨率和边界层厚度。</p>
<h2>示例 5：并行生成并检查</h2>
<pre><code class="language-bash">decomposePar
mpirun -np 4 snappyHexMesh -parallel
mpirun -np 4 checkMesh -parallel -latestTime
</code></pre>
<p>decomposeParDict的numberOfSubdomains设为4；在各分区生成最新网格，再检查并行网格质量。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-checkGeometry</code></td><td>检查全部表面几何的质量。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 snappyHexMeshDict 文件。</td></tr><tr><td><code>-dry-run</code></td><td>通过一个时间步检查算例设置。</td></tr><tr><td><code>-outFile &lt;file&gt;</code></td><td>指定简化后表面的输出文件名。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-patches &lt;(patch0 .. patchN)&gt;</code></td><td>仅对选中的边界面进行三角化；支持通配符。</td></tr><tr><td><code>-profiling</code></td><td>启用应用层性能分析。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-surfaceSimplify &lt;boundBox&gt;</code></td><td>从指定包围盒出发，用 snappyHexMesh 简化表面。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-snappyhexmeshdict/">snappyHexMeshDict</a> · <a href="/dictionaries/system-meshqualitydict/">meshQualityDict</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/refineMesh/cylinder">mesh/refineMesh/cylinder</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/snappyHexMesh/flange">mesh/snappyHexMesh/flange</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/snappyHexMesh/insidePoints">mesh/snappyHexMesh/insidePoints</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/snappyHexMesh/gap_detection">mesh/snappyHexMesh/gap_detection</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/snappyHexMesh/rotated_block">mesh/snappyHexMesh/rotated_block</a></li></ul><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/snappyHexMesh/snappyHexMesh.C">源码与说明</a> · <a href="/assets/command-help/snappyhexmesh.txt">帮助文本</a></p>
