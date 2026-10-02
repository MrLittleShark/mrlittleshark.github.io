---
title: "postProcess · 在已有结果上执行功能对象"
layout: reference
description: "在已有结果上执行功能对象。"
cms_slug: "command-postprocess"
---

<p>在已有结果上执行功能对象。</p><h2>开始前</h2>
<p>已有所需字段和网格；-func使用预配置功能对象，-dict使用包含functions的控制字典。</p>
<h2>示例 1：计算速度大小</h2>
<pre><code class="language-bash">postProcess -func 'mag(U)' -latestTime
</code></pre>
<p>读取最新U，生成速度模场，适合查看流速分布或提取极值。</p>
<h2>示例 2：计算速度梯度</h2>
<pre><code class="language-bash">postProcess -func 'grad(U)' -time '0.1:0.5'
</code></pre>
<p>对区间内已有U逐时刻计算梯度张量，输出与各时刻对应的grad(U)。</p>
<h2>示例 3：同时计算涡量和Q</h2>
<pre><code class="language-bash">postProcess -funcs '(vorticity Q)' -latestTime
</code></pre>
<p>使用现有速度场生成涡量与Q判据，便于区分旋转强度与涡结构。</p>
<h2>示例 4：执行自定义采样方案</h2>
<pre><code class="language-bash">postProcess -dict system/postProcess-linesDict -time '1:2'
</code></pre>
<p>替代字典的functions已配置采样线或积分对象；对1至2秒已有结果执行，输出通常位于postProcessing。</p>
<h2>示例 5：后处理特定区域</h2>
<pre><code class="language-bash">postProcess -region fluid -func 'mag(U)' -latestTime
</code></pre>
<p>只读取fluid的U与网格，生成该区域速度大小，适合多区域案例。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>从指定位置读取控制字典。</td></tr><tr><td><code>-field &lt;name&gt;</code></td><td>指定要处理的场，例如 U。</td></tr><tr><td><code>-fields &lt;list&gt;</code></td><td>指定要处理的场列表，例如 &#x27;(U T p)&#x27;。</td></tr><tr><td><code>-func &lt;name&gt;</code></td><td>指定要执行的函数对象，例如 Q。</td></tr><tr><td><code>-funcs &lt;list&gt;</code></td><td>指定要执行的函数对象列表，例如 &#x27;(Q div(U))&#x27;，分别计算 Q 准则和速度散度。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-list</code></td><td>列出已配置、可直接调用的函数对象。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-profiling</code></td><td>启用应用层性能分析。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/functions-probes/">probes</a> · <a href="/dictionaries/functions-sets/">sets</a> · <a href="/dictionaries/functions-surfaces/">surfaces</a> · <a href="/dictionaries/functions-forces/">forces</a> · <a href="/dictionaries/functions-forcecoeffs/">forceCoeffs</a> · <a href="/dictionaries/functions-fieldaverage/">fieldAverage</a> · <a href="/dictionaries/functions-volfieldvalue/">volFieldValue</a> · <a href="/dictionaries/functions-surfacefieldvalue/">surfaceFieldValue</a> · <a href="/dictionaries/functions-yplus/">yPlus</a> · <a href="/dictionaries/functions-q/">Q</a></p><details class="command-more-options"><summary>更多参数（20 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/postProcess/postProcess.C">源码与说明</a> · <a href="/assets/command-help/postprocess.txt">帮助文本</a></p>
