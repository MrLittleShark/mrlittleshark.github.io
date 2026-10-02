---
title: "collapseEdges · 读取 collapseDict 或指定字典，折叠操作可改变网格拓扑"
layout: reference
description: "读取 collapseDict 或指定字典，折叠操作可改变网格拓扑。"
cms_slug: "command-collapseedges"
---

<p>读取 collapseDict 或指定字典，折叠操作可改变网格拓扑。</p><h2>开始前</h2>
<p>准备网格和 system/collapseDict，至少含 collapseEdgesCoeffs.minimumEdgeLength 与 maximumMergeAngle；长度采用网格单位。在独立副本试验。</p>
<h2>示例 1：按现有阈值合并短边</h2>
<pre><code class="language-bash">collapseEdges
</code></pre>
<p>读取 collapseDict 合并满足条件的短边，并写出修改后的网格。检查点数、面数及质量变化，判断简化是否保留目标结构。</p>
<h2>示例 2：设置绝对短边阈值</h2>
<pre><code class="language-bash">foamDictionary system/collapseDict -entry collapseEdgesCoeffs.minimumEdgeLength -set 0.0001
collapseEdges
</code></pre>
<p>米制网格以 0.1 mm 为短边阈值。该长度应小于需要保留的真实几何细节，结果需核对薄壁和窄间隙。</p>
<h2>示例 3：使用另一份简化参数</h2>
<pre><code class="language-bash">collapseEdges -dict system/collapseConservativeDict
</code></pre>
<p>从独立字典读取更保守的长度与角度设置，便于在相同原始网格副本上比较不同简化强度。</p>
<h2>示例 4：同时处理可折叠的面</h2>
<pre><code class="language-bash">collapseEdges -collapseFaces
</code></pre>
<p>前提是 collapseDict 中也已配置 collapseFacesCoeffs。允许按面形状把部分面折叠为边或点，适合处理细长小面，之后检查单元质量。</p>
<h2>示例 5：限定间接处理面集</h2>
<pre><code class="language-bash">collapseEdges -collapseFaceSet targetFaces -overwrite
checkMesh -constant -allGeometry
</code></pre>
<p>使用已有 targetFaces 指定需要处理的面集合，并把结果写回原实例。-collapseFaceSet 与 -collapseFaces 是两种互斥的面处理方式；短边过滤仍会先进行，完成后检查集合邻域及网格质量。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-collapseFaceSet &lt;faceSet&gt;</code></td><td>折叠指定 faceSet 中的面。</td></tr><tr><td><code>-collapseFaces</code></td><td>同时折叠短边、小面和狭长面。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 collapseDict 文件。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/collapseEdges/collapseEdges.C">源码与说明</a> · <a href="/assets/command-help/collapseedges.txt">帮助文本</a></p>
