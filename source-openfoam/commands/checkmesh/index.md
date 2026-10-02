---
title: "checkMesh · 检查网格拓扑、几何形状与质量，并定位问题区域"
layout: reference
description: "检查网格拓扑、几何形状与质量，并定位问题区域。"
cms_slug: "command-checkmesh"
---

<p>检查网格拓扑、几何形状与质量，并定位问题区域。</p><h2>开始前</h2>
<p>算例已有网格。检查时刻和区域应与实际求解或待使用的网格一致。</p>
<h2>示例 1：检查初始网格</h2>
<pre><code class="language-bash">checkMesh -constant
</code></pre>
<p>检查constant网格的体积、边界和基本拓扑，首先查看单元数与Mesh OK或失败项目。</p>
<h2>示例 2：运行完整检查</h2>
<pre><code class="language-bash">checkMesh -constant -allTopology -allGeometry
</code></pre>
<p>增加拓扑和包围盒等几何检查，适合导入、拼接或自编程生成的网格。</p>
<h2>示例 3：使用项目质量标准</h2>
<pre><code class="language-bash">checkMesh -meshQuality
</code></pre>
<p>读取system/meshQualityDict，以项目设定的非正交性、扭曲等阈值检查。</p>
<h2>示例 4：输出质量字段</h2>
<pre><code class="language-bash">checkMesh -latestTime -writeAllFields -writeSets vtk
</code></pre>
<p>检查最新网格，保存质量标量场和问题集合，可在ParaView定位坏单元。</p>
<h2>示例 5：检查多区域并行网格</h2>
<pre><code class="language-bash">mpirun -np 4 checkMesh -parallel -allRegions
</code></pre>
<p>前提4个分区及regionProperties完整；分别检查流体、固体区域和分区耦合关系。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allGeometry</code></td><td>执行包括包围盒检查在内的完整几何检查。</td></tr><tr><td><code>-allRegions</code></td><td>处理 regionProperties 中的全部区域。</td></tr><tr><td><code>-allTopology</code></td><td>执行额外的网格拓扑检查。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-meshQuality</code></td><td>从 system/meshQualityDict 读取自定义网格质量标准。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noTopology</code></td><td>仅检查几何，跳过网格拓扑检查。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，例如 -region gas。</td></tr><tr><td><code>-regions &lt;wordRes&gt;</code></td><td>指定一个区域或按 regionProperties 匹配多个区域，例如 -regions gas 或 -regions &#x27;(gas &quot;solid.*&quot;)&#x27;。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-meshqualitydict/">meshQualityDict</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/polyDualMesh/missingCorner">mesh/polyDualMesh/missingCorner</a></li></ul><details class="command-more-options"><summary>更多参数（26 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-write-edges</code></td><td>将有问题的边写为 VTK 文件，便于检查有限面积网格等问题。</td></tr><tr><td><code>-writeAllFields</code></td><td>将各项网格质量指标写为体场。</td></tr><tr><td><code>-writeAllSurfaceFields</code></td><td>将各项网格质量指标写为面场。</td></tr><tr><td><code>-writeChecks &lt;word&gt;</code></td><td>将检查结果写为字典或 JSON 格式。</td></tr><tr><td><code>-writeFields &lt;wordList&gt;</code></td><td>将选中的网格质量指标写为体场。</td></tr><tr><td><code>-writeSets &lt;surfaceFormat&gt;</code></td><td>重建全部 faceSet、cellSet，并按指定表面格式输出。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/checkMesh/writeFields.C">源码与说明</a> · <a href="/assets/command-help/checkmesh.txt">帮助文本</a></p>
