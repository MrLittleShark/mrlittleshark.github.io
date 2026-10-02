---
title: "refineMesh · 沿指定方向细化全域或选定单元"
layout: reference
description: "沿指定方向细化全域或选定单元。"
cms_slug: "command-refinemesh"
---

<p>沿指定方向细化全域或选定单元。</p><h2>开始前</h2>
<p>已有网格；局部或定向细化需要 system/refineMeshDict 及其引用的cellSet。</p>
<h2>示例 1：全域细化</h2>
<pre><code class="language-bash">refineMesh -all
</code></pre>
<p>选择所有单元细化，生成新的网格时间；检查细化前后单元数量与最小尺寸。</p>
<h2>示例 2：按默认字典局部细化</h2>
<pre><code class="language-bash">refineMesh
</code></pre>
<p>读取 refineMeshDict 的选区和方向，对指定单元做定向细化，适合局部提高分辨率。</p>
<h2>示例 3：先选区再细化</h2>
<pre><code class="language-bash">topoSet -dict system/topoSet-wakeDict
refineMesh -dict system/refineMesh-wakeDict -overwrite
</code></pre>
<p>两个字典约定同一个尾流 cellSet；先选尾流单元，再按指定方向细化并更新当前网格。</p>
<h2>示例 4：细化多区域中的流体</h2>
<pre><code class="language-bash">refineMesh -region fluid -all -overwrite
</code></pre>
<p>只细化 fluid 区域的全部单元，适合独立检查流体网格分辨率变化。</p>
<h2>示例 5：连续两级全域细化</h2>
<pre><code class="language-bash">refineMesh -all -overwrite
refineMesh -all -overwrite
checkMesh
</code></pre>
<p>第二次读取第一次细化后的网格，获得两级细化结果；单元数和所需内存会随细化明显增加，最终检查质量。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-all</code></td><td>细化全部单元。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 refineMeshDict 文件。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-refinemeshdict/">refineMeshDict</a></p><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/refineMesh/refineFieldDirs">mesh/refineMesh/refineFieldDirs</a></li></ul><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/refineMesh/refineMesh.C">源码与说明</a> · <a href="/assets/command-help/refinemesh.txt">帮助文本</a></p>
