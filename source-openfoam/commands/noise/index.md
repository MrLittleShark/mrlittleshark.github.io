---
title: "noise · 对压力时间信号或表面压力数据做频谱与声压级分析"
layout: reference
description: "对压力时间信号或表面压力数据做频谱与声压级分析。"
cms_slug: "command-noise"
---

<p>对压力时间信号或表面压力数据做频谱与声压级分析。</p><h2>开始前</h2>
<p>system/noiseDict已选择模型、输入文件、列或表面格式，以及采样和窗口设置；输入压力单位与rhoRef约定匹配。</p>
<h2>示例 1：执行默认噪声分析</h2>
<pre><code class="language-bash">noise
</code></pre>
<p>读取noiseDict和压力数据，计算模型支持的频谱、功率谱或声压级，写到配置的输出位置。</p>
<h2>示例 2：选择另一测点方案</h2>
<pre><code class="language-bash">noise -dict system/noise-probe2Dict
</code></pre>
<p>替代字典指定第二测点数据和相同处理设置，便于比较不同位置的频谱峰值。</p>
<h2>示例 3：增加FFT采样长度</h2>
<pre><code class="language-bash">foamDictionary system/noiseDict -entry N -set 2048
noise
</code></pre>
<p>N设为2048，输入数据须足以覆盖窗口；在采样频率固定时，较长窗口提高频率分辨率。</p>
<h2>示例 4：只分析指定频段</h2>
<pre><code class="language-bash">foamDictionary system/noiseDict -entry minFreq -set 100
foamDictionary system/noiseDict -entry maxFreq -set 2000
noise
</code></pre>
<p>将关注频率设为100至2000Hz，检查该范围内的谱峰；上界应处于输入采样可解析范围。</p>
<h2>示例 5：比较A计权声压级</h2>
<pre><code class="language-bash">foamDictionary system/noiseDict -entry SPLweighting -set dBA
noise
</code></pre>
<p>在其他设置不变时采用A计权，得到按听觉频率响应加权的声压级，适合与未计权dB结果比较。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 noiseDict 文件。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-noisedict/">noiseDict</a></p><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/noise/noise.C">源码与说明</a> · <a href="/assets/command-help/noise.txt">帮助文本</a></p>
