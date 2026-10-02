---
title: "setFields · 按几何选区或拓扑集合给已有场设置初值"
layout: reference
description: "按几何选区或拓扑集合给已有场设置初值。"
cms_slug: "command-setfields"
---

<p>按几何选区或拓扑集合给已有场设置初值。</p><h2>开始前</h2>
<p>目标场已存在，system/setFieldsDict 定义 defaultFieldValues 和 regions。</p>
<h2>示例 1：执行初始场分区赋值</h2>
<pre><code class="language-bash">setFields -time 0
</code></pre>
<p>对0目录场先应用默认值，再按regions顺序设置局部值，常用于液位、热点或浓度团初始化。</p>
<h2>示例 2：采用另一液位方案</h2>
<pre><code class="language-bash">setFields -dict system/setFields-highWaterDict -time 0
</code></pre>
<p>替代字典定义另一液位选区，便于保持网格相同而比较不同初始水量。</p>
<h2>示例 3：在新网格上重新初始化</h2>
<pre><code class="language-bash">blockMesh
setFields -time 0
</code></pre>
<p>网格重建后重新执行几何选区，使非均匀初场与新单元数量匹配。</p>
<h2>示例 4：只对某个区域赋值</h2>
<pre><code class="language-bash">setFields -region fluid -dict system/setFields-fluidDict -time 0
</code></pre>
<p>多区域案例中只修改fluid的场，保持固体初始温度等设置不变。</p>
<h2>示例 5：设置有限面积场</h2>
<pre><code class="language-bash">setFields -area-region film -dict system/setFields-filmDict -time 0
</code></pre>
<p>已存在film有限面积网格及其场时，按专用字典设置表面初值，适用于薄膜或壳面计算。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allAreas</code></td><td>选择有限面积 regionProperties 中的全部区域。</td></tr><tr><td><code>-area-region &lt;name&gt;</code></td><td>指定有限面积网格区域，例如 -area-region shell。</td></tr><tr><td><code>-area-regions &lt;wordRes&gt;</code></td><td>选择有限面积区域，例如 -area-regions film；也可按 regionProperties 中的名称匹配，如 -area-regions &#x27;(film &quot;solid.*&quot;)&#x27;。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 setFieldsDict 文件。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-no-finite-area</code></td><td>跳过有限面积网格及其场数据。</td></tr><tr><td><code>-noZero</code></td><td>排除 0/ 目录；当前实现会忽略此选项。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-time &lt;value&gt;</code></td><td>选择最接近给定数值的时刻。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-setfieldsdict/">setFieldsDict</a> · <a href="/dictionaries/0-alpha-water/">alpha.water</a></p><details class="command-more-options"><summary>更多参数（18 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/setFields/setFields.C">源码与说明</a> · <a href="/assets/command-help/setfields.txt">帮助文本</a></p>
