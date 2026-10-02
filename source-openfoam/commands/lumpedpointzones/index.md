---
title: "lumpedPointZones · 显示集中点压力积分区域及插值权重关系"
layout: reference
description: "显示集中点压力积分区域及插值权重关系。"
cms_slug: "command-lumpedpointzones"
---

<p>显示集中点压力积分区域及插值权重关系。</p><h2>开始前</h2>
<p>已有lumpedPoint运动和边界配置；完整模式需要原始网格。</p>
<h2>示例 1：检查初始控制点</h2>
<pre><code class="language-bash">lumpedPointZones -dry-run
</code></pre>
<p>只读取初始集中点状态并写state.vtp，可先检查参考位置与转角设置。</p>
<h2>示例 2：显示积分区域与插值关系</h2>
<pre><code class="language-bash">lumpedPointZones
</code></pre>
<p>生成state.vtp和lumpedPointZones.vtp，并报告每个控制点对应面积，检查边界分段。</p>
<h2>示例 3：仅查看区域分组</h2>
<pre><code class="language-bash">lumpedPointZones -no-interpolate
</code></pre>
<p>保留压力积分区域显示，关闭插值器计算和显示，让区域归属更容易观察。</p>
<h2>示例 4：调整控制平面显示大小</h2>
<pre><code class="language-bash">lumpedPointZones -visual-length 0.05
</code></pre>
<p>将用于显示方向的三角平面长度设为0.05个几何长度单位，避免小模型被标记遮挡。</p>
<h2>示例 5：检查某一区域并显示过程</h2>
<pre><code class="language-bash">lumpedPointZones -region fluid -verbose
</code></pre>
<p>只处理fluid耦合边界，输出更详细的区域和控制点信息，便于核对多区域设置。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dry-run</code></td><td>直接测试集中点的初始状态，无需网格。</td></tr><tr><td><code>-no-interpolate</code></td><td>跳过点插值器的计算与显示。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-verbose</code></td><td>显示更详细的输出；可重复使用以增加详细程度。</td></tr><tr><td><code>-visual-length &lt;len&gt;</code></td><td>设置平面的显示长度；平面以三角形表示。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/lumped/lumpedPointZones/lumpedPointZones.C">源码与说明</a> · <a href="/assets/command-help/lumpedpointzones.txt">帮助文本</a></p>
