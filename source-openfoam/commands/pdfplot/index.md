---
title: "pdfPlot · 对选定概率分布随机采样并输出直方图数据"
layout: reference
description: "对选定概率分布随机采样并输出直方图数据。"
cms_slug: "command-pdfplot"
---

<p>对选定概率分布随机采样并输出直方图数据。</p><h2>开始前</h2>
<p>已有最小OpenFOAM案例及constant/pdfDict；nSamples为抽样数，nIntervals为分箱数，writeData控制是否保存原始样本。</p>
<h2>示例 1：生成均匀分布样本</h2>
<pre><code class="language-bash">cat &gt; constant/pdfDict &lt;&lt;'EOF'
FoamFile { version 2.0; format ascii; class dictionary; object pdfDict; }
type uniform;
uniformDistribution { minValue 1e-5; maxValue 5e-5; }
nSamples 10000;
nIntervals 40;
writeData false;
EOF
pdfPlot
</code></pre>
<p>在10至50微米数值范围内抽样10000次，写pdf目录下的分箱计数图数据。该输出是计数，归一化后才是概率密度。</p>
<h2>示例 2：增加样本数量</h2>
<pre><code class="language-bash">foamDictionary constant/pdfDict -entry nSamples -set 100000
pdfPlot
</code></pre>
<p>分箱不变时增加到10万次抽样，比较随机起伏随样本数的降低趋势。</p>
<h2>示例 3：提高分箱分辨率</h2>
<pre><code class="language-bash">foamDictionary constant/pdfDict -entry nIntervals -set 100
pdfPlot
</code></pre>
<p>将区间细分为100箱，能显示更细的分布形状，同时每箱样本数减少。</p>
<h2>示例 4：保存每个随机样本</h2>
<pre><code class="language-bash">foamDictionary constant/pdfDict -entry writeData -set true
pdfPlot
</code></pre>
<p>额外写pdf/uniform.data，便于自行计算均值、方差或制作归一化概率密度图。</p>
<h2>示例 5：扩大分布范围</h2>
<pre><code class="language-bash">foamDictionary constant/pdfDict -entry uniformDistribution/maxValue -set 1e-4
pdfPlot
</code></pre>
<p>上界改为100微米，重新采样并比较均值和宽度，适合检查粒径分布参数。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/miscellaneous/pdfPlot/pdfPlot.C">源码与说明</a> · <a href="/assets/command-help/pdfplot.txt">帮助文本</a></p>
