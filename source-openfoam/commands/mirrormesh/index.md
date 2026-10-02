---
title: "mirrorMesh · 按字典定义的平面镜像并扩展网格"
layout: reference
description: "按字典定义的平面镜像并扩展网格。"
cms_slug: "command-mirrormesh"
---

<p>按字典定义的平面镜像并扩展网格。</p><h2>开始前</h2>
<p>已有半域网格和 system/mirrorMeshDict，字典定义镜像平面及 planeTolerance。</p>
<h2>示例 1：生成完整对称域</h2>
<pre><code class="language-bash">mirrorMesh
</code></pre>
<p>读取默认镜像平面，复制镜像侧单元；平面上的匹配边界转为内部连接，结果写入新网格时间。</p>
<h2>示例 2：采用另一镜像平面</h2>
<pre><code class="language-bash">mirrorMesh -dict system/mirrorMesh-yDict
</code></pre>
<p>替代字典描述另一个平面，可用于沿不同对称面扩展同一基础网格的副本。</p>
<h2>示例 3：镜像后直接继续预处理</h2>
<pre><code class="language-bash">mirrorMesh -overwrite
checkMesh
</code></pre>
<p>把完整域写回当前网格，检查镜像连接处的单元质量和边界分组。</p>
<h2>示例 4：调整平面识别容差</h2>
<pre><code class="language-bash">foamDictionary system/mirrorMeshDict -entry planeTolerance -set 1e-7
mirrorMesh
</code></pre>
<p>planeTolerance 用于判定点是否位于镜像平面上；1e-7 应结合本案例长度单位选择，结果中检查平面处是否出现细小缝隙。</p>
<h2>示例 5：镜像后修正周期配对</h2>
<pre><code class="language-bash">mirrorMesh -overwrite
createPatch -dict system/createPatch-cyclicDict -overwrite
</code></pre>
<p>输入网格带 cyclic 边界时，镜像可能改变面的对应顺序；替代 createPatchDict 重新建立周期配对，再用于后续计算。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 mirrorMeshDict 文件。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/mirrorMesh/mirrorFvMesh.C">源码与说明</a> · <a href="/assets/command-help/mirrormesh.txt">帮助文本</a></p>
