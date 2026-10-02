---
title: "particleTracks · 把瞬态粒子位置历史连接成轨迹并导出"
layout: reference
description: "把瞬态粒子位置历史连接成轨迹并导出。"
cms_slug: "command-particletracks"
---

<p>把瞬态粒子位置历史连接成轨迹并导出。</p><h2>开始前</h2>
<p>已有多个时间的粒子位置及身份信息；默认字典实际为constant/particleTrackProperties，包含cloud、sampleFrequency、maxPositions等。</p>
<h2>示例 1：导出完整时间轨迹</h2>
<pre><code class="language-bash">particleTracks
</code></pre>
<p>按字典选择粒子云和采样频率，依据粒子身份关联不同时间的位置，输出轨迹文件。</p>
<h2>示例 2：截取特定时间段</h2>
<pre><code class="language-bash">particleTracks -time '0.1:0.5'
</code></pre>
<p>只连接0.1至0.5区间的数据，适合查看喷射初期或指定运动阶段。</p>
<h2>示例 3：减少所跟踪粒子数量</h2>
<pre><code class="language-bash">particleTracks -stride 10 -time '0:1'
</code></pre>
<p>-stride覆盖字典sampleFrequency，对粒子编号按指定采样间隔抽取轨迹，减少密集粒子云的显示量。</p>
<h2>示例 4：给轨迹附加字段</h2>
<pre><code class="language-bash">particleTracks -fields '(U d T)' -format vtk
</code></pre>
<p>云中已有U、d、T时，随轨迹写速度、粒径和温度，便于沿路径着色分析。</p>
<h2>示例 5：采用另一云的轨迹方案</h2>
<pre><code class="language-bash">particleTracks -dict constant/particleTrackProperties-spray -region gas -time '0.1:1'
</code></pre>
<p>替代字典指定喷雾云；从gas区域读取粒子，生成该云在指定时段内的轨迹。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 particleTracksProperties 文件。</td></tr><tr><td><code>-fields &lt;wordRes&gt;</code></td><td>选择要写出的场；默认使用字典的 fields 设置或全部场，例如 T 或 &#x27;(&quot;U.*&quot;)&#x27;。</td></tr><tr><td><code>-format &lt;name&gt;</code></td><td>指定输出格式，默认使用字典中的 setFormat，或采用 VTK。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-stride &lt;int&gt;</code></td><td>覆盖采样间隔。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-verbose</code></td><td>显示更详细的输出；可重复使用以增加详细程度。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（18 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/lagrangian/particleTracks/particleTracks.C">源码与说明</a> · <a href="/assets/command-help/particletracks.txt">帮助文本</a></p>
