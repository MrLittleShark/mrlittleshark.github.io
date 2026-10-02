---
title: "dsmcInitialise · 按数密度、温度和平均速度初始化 DSMC 模拟粒子"
layout: reference
description: "按数密度、温度和平均速度初始化 DSMC 模拟粒子。"
cms_slug: "command-dsmcinitialise"
---

<p>按数密度、温度和平均速度初始化 DSMC 模拟粒子。</p><h2>开始前</h2>
<p>已有网格、system/dsmcInitialiseDict、constant/dsmcProperties；物种名称与属性一致，粒子权重已设置。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：生成初始DSMC云</h2>
<pre><code class="language-bash">dsmcInitialise
</code></pre>
<p>读取numberDensities、temperature、velocity，生成dsmc云并写初始粒子数据，日志报告模拟粒子数量。</p>
<h2>示例 2：初始化更高温气体</h2>
<pre><code class="language-bash">foamDictionary system/dsmcInitialiseDict -entry temperature -set 600
dsmcInitialise
</code></pre>
<p>在初始案例副本中改为600K；随机热运动速度分布随温度改变，平均速度仍取velocity。</p>
<h2>示例 3：加入定向平均流</h2>
<pre><code class="language-bash">foamDictionary system/dsmcInitialiseDict -entry velocity -set '(500 0 0)'
dsmcInitialise
</code></pre>
<p>平均速度设为沿x方向500米每秒，在此基础上叠加热运动；输出粒子用于研究有来流的稀薄气体。</p>
<h2>示例 4：比较不同数密度</h2>
<pre><code class="language-bash">foamDictionary system/dsmcInitialiseDict -entry numberDensities/N2 -set 1e20
dsmcInitialise
</code></pre>
<p>字典已有N2物种时增改其数密度；固定体积与粒子权重下，模拟粒子数量随数密度变化。</p>
<h2>示例 5：直接在分区网格中初始化</h2>
<pre><code class="language-bash">decomposePar
mpirun -np 4 dsmcInitialise -parallel
</code></pre>
<p>已有4分区设置；各进程生成本地粒子，日志汇总全域数量，供随后并行dsmcFoam读取。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/dsmcInitialise/dsmcInitialise.C">源码与说明</a> · <a href="/assets/command-help/dsmcinitialise.txt">帮助文本</a></p>
