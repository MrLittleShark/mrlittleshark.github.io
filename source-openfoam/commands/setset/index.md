---
title: "setSet · 交互式或批量创建、修改网格集合"
layout: reference
description: "交互式或批量创建、修改网格集合。"
cms_slug: "command-setset"
---

<p>交互式或批量创建、修改网格集合。</p><h2>开始前</h2>
<p>已有网格；批处理文件逐行使用 cellSet、faceSet 或 pointSet 的动作和选择源。</p>
<h2>示例 1：交互创建盒内单元集</h2>
<pre><code class="language-bash">setSet
# 在 setSet 提示符中输入：
# cellSet core new boxToCell (0 0 0) (1 1 1)
# quit
</code></pre>
<p>进入交互终端后，去掉示例注释符输入两条指令；new 创建 core，boxToCell 按单元中心选择指定盒内单元。</p>
<h2>示例 2：用批处理文件重复选区</h2>
<pre><code class="language-bash">printf 'cellSet core new boxToCell (0 0 0) (1 1 1)\nquit\n' &gt; select.setSet
setSet -batch select.setSet
</code></pre>
<p>把交互指令保存成文本，-batch 读取并执行，便于网格重建后重新生成相同几何选区。</p>
<h2>示例 3：把选区扩大到另一盒体</h2>
<pre><code class="language-bash">printf 'cellSet core new boxToCell (0 0 0) (1 1 1)\ncellSet core add boxToCell (1 0 0) (2 1 1)\nquit\n' &gt; twoBoxes.setSet
setSet -batch twoBoxes.setSet
</code></pre>
<p>第一条创建集合，第二条 add 做并集；最终 core 包含两盒范围内的单元。</p>
<h2>示例 4：只生成集合文件</h2>
<pre><code class="language-bash">setSet -batch select.setSet -noVTK
</code></pre>
<p>批处理已定义所需集合；-noVTK 关闭辅助VTK输出，保留供 topoSet、subsetMesh 等工具使用的集合。</p>
<h2>示例 5：在运动网格的多个状态重选</h2>
<pre><code class="language-bash">setSet -batch select.setSet -loop -time '0.1:0.5'
</code></pre>
<p>-loop 对选中的每个已有时间执行批指令；几何运动时，盒内单元集合会随各时刻位置更新。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-batch &lt;file&gt;</code></td><td>从指定文件读取命令并批量执行。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-loop</code></td><td>对全部时间步执行批处理命令。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noSync</code></td><td>保留耦合边界两侧各自的选择，跳过同步。</td></tr><tr><td><code>-noVTK</code></td><td>跳过 VTK 文件输出。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/setSet/setSet.C">源码与说明</a> · <a href="/assets/command-help/setset.txt">帮助文本</a></p>
