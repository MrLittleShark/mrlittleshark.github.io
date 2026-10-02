---
title: "setsToZones · 把 pointSet、faceSet、cellSet 转成同名网格 zone"
layout: reference
description: "把 pointSet、faceSet、cellSet 转成同名网格 zone。"
cms_slug: "command-setstozones"
---

<p>把 pointSet、faceSet、cellSet 转成同名网格 zone。</p><h2>开始前</h2>
<p>已有集合文件；需要定向的 faceSet 通常还需同名 cellSet 确定方向。</p>
<h2>示例 1：把现有集合转成zone</h2>
<pre><code class="language-bash">setsToZones
</code></pre>
<p>遍历网格集合并创建相应zone；cellSet转cellZone，pointSet转pointZone，faceSet转faceZone。</p>
<h2>示例 2：仅需区域成员而不需方向</h2>
<pre><code class="language-bash">setsToZones -noFlipMap
</code></pre>
<p>关闭 faceSet 的方向判定，适合只关注集合成员的zone转换；由面通量方向参与计算时应另外校正定向。</p>
<h2>示例 3：转换初始恒定网格集合</h2>
<pre><code class="language-bash">setsToZones -constant -noFlipMap
</code></pre>
<p>把 constant 纳入选择，读取初始网格的集合，适合网格预处理后建立源项或旋转体区域。</p>
<h2>示例 4：转换最新状态的集合</h2>
<pre><code class="language-bash">setsToZones -latestTime
</code></pre>
<p>动网格最后时刻已有重新选择的集合；转换后zone对应最新网格拓扑和编号。</p>
<h2>示例 5：多区域源区生成流程</h2>
<pre><code class="language-bash">topoSet -region fluid -dict system/topoSet-heaterDict
setsToZones -region fluid -noFlipMap
</code></pre>
<p>先在 fluid 中生成 heater 等cellSet，再转为同名cellZone，供该区域体积源模型使用。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noFlipMap</code></td><td>按集合成员转换，忽略 faceSet 的方向。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noZero</code></td><td>排除 0/ 目录；当前实现会忽略此选项。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-time &lt;value&gt;</code></td><td>选择最接近给定数值的时刻。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/setsToZones/setsToZones.C">源码与说明</a> · <a href="/assets/command-help/setstozones.txt">帮助文本</a></p>
