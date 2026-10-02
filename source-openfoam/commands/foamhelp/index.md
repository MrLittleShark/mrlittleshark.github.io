---
title: "foamHelp · 查询边界条件、函数对象和求解器的帮助"
layout: reference
description: "查询边界条件、函数对象和求解器的帮助。"
cms_slug: "command-foamhelp"
---

<p>查询边界条件、函数对象和求解器的帮助。</p><h2>开始前</h2>
<p>已加载 v2512；在含网格及所查字段的算例中运行。boundary、solver 等类别放在选项之前；在线文档查询需要可访问文档索引。</p>
<h2>示例 1：查询速度可用边界</h2>
<pre><code class="language-bash">foamHelp boundary -field U
</code></pre>
<p>读取速度场 U 的类型，列出可用于该矢量场的边界条件，供填写 0/U 时选择。</p>
<h2>示例 2：查询压力可用边界</h2>
<pre><code class="language-bash">foamHelp boundary -field p
</code></pre>
<p>已有 0/p 时查询标量边界；所得类型列表与 U 的矢量边界列表可对照阅读。</p>
<h2>示例 3：筛选固定值速度边界</h2>
<pre><code class="language-bash">foamHelp boundary -field U -fixedValue
</code></pre>
<p>在速度边界中筛选定值类实现，适合寻找给定入口速度及其派生条件。</p>
<h2>示例 4：查询网格约束类型</h2>
<pre><code class="language-bash">foamHelp boundary -constraint
</code></pre>
<p>显示约束类边界信息，用于区分 empty、symmetry 等几何约束与普通场边界。</p>
<h2>示例 5：按当前算例查询求解器</h2>
<pre><code class="language-bash">foamHelp solver -read
</code></pre>
<p>从 system/controlDict 读取 application，再查询对应求解器文档；先确认该条目已设置为所用求解器。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamHelp/foamHelp.C">源码与说明</a> · <a href="/assets/command-help/foamhelp.txt">帮助文本</a></p>
