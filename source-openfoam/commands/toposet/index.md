---
title: "topoSet · 按几何、网格属性和集合关系创建或修改 sets/zones"
layout: reference
description: "按几何、网格属性和集合关系创建或修改 sets/zones。"
cms_slug: "command-toposet"
---

<p>按几何、网格属性和集合关系创建或修改 sets/zones。</p><h2>开始前</h2>
<p>已有网格和 system/topoSetDict，actions 列表定义名称、类型、操作及选择源。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：执行标准选区字典</h2>
<pre><code class="language-bash">topoSet
</code></pre>
<p>按actions顺序建立集合或zone；日志列出各动作与选中数量，可据此核对几何选区。</p>
<h2>示例 2：使用另一选区方案</h2>
<pre><code class="language-bash">topoSet -dict system/topoSet-wakeDict
</code></pre>
<p>读取尾流选区专用字典，便于在同一网格上分别准备细化区、采样区和体积源区。</p>
<h2>示例 3：选最后时刻的运动网格</h2>
<pre><code class="language-bash">topoSet -latestTime -dict system/topoSet-probeDict
</code></pre>
<p>按最新顶点位置和拓扑重新执行几何选择，输出对应时刻的集合。</p>
<h2>示例 4：在时间区间内反复选区</h2>
<pre><code class="language-bash">topoSet -time '0.1:0.5' -dict system/topoSet-windowDict
</code></pre>
<p>对区间内已有时刻重复盒体或表面选择，适合跟踪固定空间窗口内的网格单元。</p>
<h2>示例 5：分区案例中建立区域集合</h2>
<pre><code class="language-bash">mpirun -np 4 topoSet -parallel -region fluid -dict system/topoSet-fluidDict
</code></pre>
<p>已有4分区fluid网格；每个进程执行选择并同步耦合边界信息，生成分区一致的集合。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 topoSetDict 文件。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noSync</code></td><td>保留耦合边界两侧各自的选择，跳过同步。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-toposetdict/">topoSetDict</a></p><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/topoSet/topoSet.C">源码与说明</a> · <a href="/assets/command-help/toposet.txt">帮助文本</a></p>
