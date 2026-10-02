---
title: "mergeMeshes · 把两个独立网格合并到主案例中"
layout: reference
description: "把两个独立网格合并到主案例中。"
cms_slug: "command-mergemeshes"
---

<p>把两个独立网格合并到主案例中。</p><h2>开始前</h2>
<p>masterCase 与 addCase 都有有效网格；两套坐标已对齐。合并后若要把接触边界变成内部面，还需拼接步骤。</p>
<h2>示例 1：合并两个网格</h2>
<pre><code class="language-bash">mergeMeshes baseCase extensionCase
</code></pre>
<p>baseCase 是接收结果的主案例，extensionCase 提供追加网格；输出位于主案例的新网格时间。</p>
<h2>示例 2：指定结果时间</h2>
<pre><code class="language-bash">mergeMeshes baseCase extensionCase -resultTime 2
</code></pre>
<p>把合并网格写到 baseCase 的时间 2，便于保留并选择不同预处理阶段。</p>
<h2>示例 3：合并指定区域</h2>
<pre><code class="language-bash">mergeMeshes baseCase extensionCase -masterRegion fluid -addRegion fluid
</code></pre>
<p>两个案例均含 fluid 区域时，只读取并合并这两个区域网格，结果仍归主案例的 fluid 区域。</p>
<h2>示例 4：直接更新主网格并检查</h2>
<pre><code class="language-bash">mergeMeshes baseCase extensionCase -overwrite
checkMesh -case baseCase
</code></pre>
<p>-overwrite 更新主案例当前网格；随后检查合并后的单元数、连通区域和边界。</p>
<h2>示例 5：合并后缝合吻合界面</h2>
<pre><code class="language-bash">mergeMeshes baseCase extensionCase -overwrite
stitchMesh -case baseCase -perfect interfaceA interfaceB -overwrite
checkMesh -case baseCase
</code></pre>
<p>两个网格有完全吻合的 interfaceA/interfaceB 时，合并后将这对边界缝合成内部面，形成连通计算域。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-addRegion &lt;name&gt;</code></td><td>指定附加网格中的区域名称。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-masterRegion &lt;name&gt;</code></td><td>指定主网格中的区域名称。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-resultTime &lt;time&gt;</code></td><td>指定合并后网格的输出时间目录。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/mergeMeshes/mergePolyMesh.C">源码与说明</a> · <a href="/assets/command-help/mergemeshes.txt">帮助文本</a></p>
