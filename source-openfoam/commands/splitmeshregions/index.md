---
title: "splitMeshRegions · 按网格连通性或 cellZone 将网格拆分成多个区域"
layout: reference
description: "按网格连通性或 cellZone 将网格拆分成多个区域。"
cms_slug: "command-splitmeshregions"
---

<p>按网格连通性或 cellZone 将网格拆分成多个区域。</p><h2>开始前</h2>
<p>已有网格；按zone分区时先建立cellZones，按阻隔面分区时先建立faceSet。</p>
<h2>示例 1：先统计连通区域</h2>
<pre><code class="language-bash">splitMeshRegions -detectOnly
</code></pre>
<p>只识别区域并报告数量和大小，保留现有网格，适合检查导入网格是否含意外孤立块。</p>
<h2>示例 2：按连通性拆分</h2>
<pre><code class="language-bash">splitMeshRegions -overwrite
</code></pre>
<p>遍历单元连通关系，把互不连通部分写成区域网格，并直接写入当前网格实例。</p>
<h2>示例 3：按材料cellZone拆分</h2>
<pre><code class="language-bash">splitMeshRegions -cellZonesOnly -overwrite
</code></pre>
<p>以已有cellZone定义区域，适合流体与固体尚共用网格但材料分组已明确的传热案例。</p>
<h2>示例 4：仅保留指定点所在区域</h2>
<pre><code class="language-bash">splitMeshRegions -insidePoint '(0.5 0.5 0.5)' -overwrite
</code></pre>
<p>该点确定位于目标流体内部时，只写出包含它的区域，便于提取主流道。</p>
<h2>示例 5：用内部面集阻断搜索</h2>
<pre><code class="language-bash">splitMeshRegions -blockedFaces separatorFaces -useFaceZones -overwrite
</code></pre>
<p>separatorFaces 阻止连通搜索跨过指定面；已有faceZone用于给区域间界面分组，输出更明确的耦合边界。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-addZones &lt;lists of zones&gt;</code></td><td>在后续分析中组合指定的区域。</td></tr><tr><td><code>-blockedFaces &lt;faceSet&gt;</code></td><td>指定额外的区域分界面，连通性搜索将在这些面处停止。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-cellZones</code></td><td>同时按 cellZone 将网格拆成独立区域。</td></tr><tr><td><code>-cellZonesFileOnly &lt;file&gt;</code></td><td>仅按 cellZone 拆分，并从指定文件读取区域信息。</td></tr><tr><td><code>-cellZonesOnly</code></td><td>仅按 cellZone 拆分网格，跳过连通性搜索。</td></tr><tr><td><code>-combineZones &lt;lists of zones&gt;</code></td><td>在后续分析中组合指定的区域。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-detectOnly</code></td><td>仅检测区域，暂不写出网格。</td></tr><tr><td><code>-insidePoint &lt;point&gt;</code></td><td>仅写出包含指定点的区域。</td></tr><tr><td><code>-largestOnly</code></td><td>仅写出最大的区域。</td></tr><tr><td><code>-makeCellZones</code></td><td>将单元归入 cellZone，保留为同一套网格。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/constant-regionproperties/">regionProperties</a></p><details class="command-more-options"><summary>更多参数（23 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-prefixRegion</code></td><td>为所有边界名称添加区域名前缀，包括普通边界和耦合边界。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-sloppyCellZones</code></td><td>以启发式方法将连通区域匹配到已有 cellZone。</td></tr><tr><td><code>-useFaceZones</code></td><td>按 faceZone 划分区域间边界，替代统一的单个边界。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/splitMeshRegions/splitMeshRegions.C">源码与说明</a> · <a href="/assets/command-help/splitmeshregions.txt">帮助文本</a></p>
