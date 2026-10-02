---
title: "mergeOrSplitBaffles · 检测共用顶点的挡板面，并合并或拆分它们"
layout: reference
description: "检测共用顶点的挡板面，并合并或拆分它们。"
cms_slug: "command-mergeorsplitbaffles"
---

<p>检测共用顶点的挡板面，并合并或拆分它们。</p><h2>开始前</h2>
<p>当前网格存在重合挡板面；拆分用于两侧独立拓扑，合并用于恢复内部面。</p>
<h2>示例 1：只查找挡板</h2>
<pre><code class="language-bash">mergeOrSplitBaffles -detectOnly
</code></pre>
<p>扫描共享顶点的重合面，报告检测结果并保留网格原状，适合先确认要处理的对象。</p>
<h2>示例 2：合并成内部面</h2>
<pre><code class="language-bash">mergeOrSplitBaffles
</code></pre>
<p>采用默认合并行为，把识别出的挡板面恢复成内部连接，结果写入新网格时间。</p>
<h2>示例 3：拆分两侧顶点</h2>
<pre><code class="language-bash">mergeOrSplitBaffles -split -overwrite
</code></pre>
<p>-split 复制两侧需要分离的顶点；-overwrite 写回当前网格，使挡板两侧具有独立拓扑。</p>
<h2>示例 4：用字典选择处理动作</h2>
<pre><code class="language-bash">mergeOrSplitBaffles -dict system/baffleActionsDict -overwrite
</code></pre>
<p>baffleActionsDict 已按该工具格式定义选定挡板及操作；用字典控制处理范围，结果写回网格。</p>
<h2>示例 5：在单一区域拆分并核查</h2>
<pre><code class="language-bash">mergeOrSplitBaffles -region fluid -split -overwrite
checkMesh -region fluid
</code></pre>
<p>多区域案例仅修改 fluid，检查该区域拆分后的边界、单元闭合和连通关系。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-detectOnly</code></td><td>仅检测挡板，保留其原有连接关系。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>从指定字典读取操作。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-split</code></td><td>在拓扑上拆开重复表面。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/mergeOrSplitBaffles/mergeOrSplitBaffles.C">源码与说明</a> · <a href="/assets/command-help/mergeorsplitbaffles.txt">帮助文本</a></p>
