---
title: "foamFormatConvert · 按 controlDict 写出设置转换现有场和网格文件格式"
layout: reference
description: "按 controlDict 写出设置转换现有场和网格文件格式。"
cms_slug: "command-foamformatconvert"
---

<p>按 controlDict 写出设置转换现有场和网格文件格式。</p><h2>开始前</h2>
<p>已有结果；目标格式、精度与压缩由controlDict中的writeFormat、writePrecision、writeCompression决定，文件会重写。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：把最新结果转成ASCII</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry writeFormat -set ascii
foamFormatConvert -latestTime
</code></pre>
<p>修改目标写格式后转换最新状态，便于直接查看字段数值。</p>
<h2>示例 2：把一段结果转成二进制</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry writeFormat -set binary
foamFormatConvert -time '1:2' -noConstant
</code></pre>
<p>将1至2秒结果改为二进制并跳过constant，适合减小场文件体积和读写时间。</p>
<h2>示例 3：提高文本输出精度</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry writeFormat -set ascii
foamDictionary system/controlDict -entry writePrecision -set 12
foamFormatConvert -latestTime
</code></pre>
<p>以12位精度重写当前可读数据；输出精度提高，已有低精度文件丢失的数值位数仍无法补回。</p>
<h2>示例 4：只转换流体区域</h2>
<pre><code class="language-bash">foamFormatConvert -region fluid -latestTime
</code></pre>
<p>用当前controlDict写出设置处理fluid最新文件，保持其他区域原格式。</p>
<h2>示例 5：转换并行结果格式</h2>
<pre><code class="language-bash">mpirun -np 4 foamFormatConvert -parallel -latestTime
</code></pre>
<p>已有4分区，分别重写各processor的最新场，适合直接改变并行重启数据格式。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-enableFunctionEntries</code></td><td>展开 #include、#codeStream 等字典指令。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noConstant</code></td><td>在时间选择中排除 constant/ 目录。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamFormatConvert/foamFormatConvert.C">源码与说明</a> · <a href="/assets/command-help/foamformatconvert.txt">帮助文本</a></p>
