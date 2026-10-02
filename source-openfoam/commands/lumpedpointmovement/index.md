---
title: "lumpedPointMovement · 用响应表预览集中点运动，或测试外部耦合响应"
layout: reference
description: "用响应表预览集中点运动，或测试外部耦合响应。"
cms_slug: "command-lumpedpointmovement"
---

<p>用响应表预览集中点运动，或测试外部耦合响应。</p><h2>开始前</h2>
<p>已有lumpedPoint运动配置及responseFile响应表；带网格预览还需要对应耦合边界。</p>
<h2>示例 1：只预览响应点运动</h2>
<pre><code class="language-bash">lumpedPointMovement response.dat -dry-run
</code></pre>
<p>读取响应表并输出集中点状态VTP序列，-dry-run可在没有体网格时检查运动输入。</p>
<h2>示例 2：预览边界随控制点变形</h2>
<pre><code class="language-bash">lumpedPointMovement response.dat
</code></pre>
<p>已有耦合网格时同时写控制点状态和边界几何序列，查看结构响应如何传到表面。</p>
<h2>示例 3：只查看前20个状态</h2>
<pre><code class="language-bash">lumpedPointMovement response.dat -max 20
</code></pre>
<p>限制最多20个输出，适合先检查较长响应表的起始阶段。</p>
<h2>示例 4：抽样查看长时间序列</h2>
<pre><code class="language-bash">lumpedPointMovement response.dat -span 5 -max 100
</code></pre>
<p>每隔5个表项取一个，最多输出100帧，减少预览文件数量。</p>
<h2>示例 5：缩小运动幅度</h2>
<pre><code class="language-bash">lumpedPointMovement response.dat -scale 0.5 -visual-length 0.1
</code></pre>
<p>相对初始状态把运动幅度缩到一半，同时设控制平面显示长度0.1，便于分辨运动方向与局部转角。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dry-run</code></td><td>直接测试运动数据，无需网格。</td></tr><tr><td><code>-max &lt;N&gt;</code></td><td>限制输出次数。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-removeLock</code></td><td>从属程序结束时删除锁文件。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>设置运动的松弛或缩放系数，默认为 1。</td></tr><tr><td><code>-slave</code></td><td>作为从属响应程序运行，用于耦合测试。</td></tr><tr><td><code>-span &lt;N&gt;</code></td><td>每次将输入序号推进 N，默认为 1。</td></tr><tr><td><code>-visual-length &lt;len&gt;</code></td><td>设置平面的显示长度；平面以三角形表示。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/lumped/lumpedPointMovement/lumpedPointMovement.C">源码与说明</a> · <a href="/assets/command-help/lumpedpointmovement.txt">帮助文本</a></p>
