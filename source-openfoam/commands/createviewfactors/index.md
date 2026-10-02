---
title: "createViewFactors · 按 viewFactorsDict 选择的模型计算辐射视角因子"
layout: reference
description: "按 viewFactorsDict 选择的模型计算辐射视角因子。"
cms_slug: "command-createviewfactors"
---

<p>按 viewFactorsDict 选择的模型计算辐射视角因子。</p><h2>开始前</h2>
<p>已有辐射边界、constant/viewFactorsDict，以及所选模型需要的面聚合或几何输入。 并行示例采用 4 个子域，分区设置与进程数一致。</p>
<h2>示例 1：计算默认区域视角因子</h2>
<pre><code class="language-bash">createViewFactors
</code></pre>
<p>从constant/viewFactorsDict创建视角因子模型并执行计算，输出后续辐射模型所需数据。</p>
<h2>示例 2：为辐射区域单独计算</h2>
<pre><code class="language-bash">createViewFactors -region enclosure
</code></pre>
<p>enclosure区域已有完整辐射设置；只处理该封闭腔体的表面关系。</p>
<h2>示例 3：先生成粗面映射</h2>
<pre><code class="language-bash">faceAgglomerate
createViewFactors
</code></pre>
<p>使用依赖面聚合的模型时，先生成fine-to-coarse映射，再计算粗面之间的视角因子，降低计算量。</p>
<h2>示例 4：在并行分区上计算</h2>
<pre><code class="language-bash">decomposePar
mpirun -np 4 createViewFactors -parallel
</code></pre>
<p>decomposeParDict已设置4分区；在对应分区几何上计算视角因子，输出与并行布局配套的数据。</p>
<h2>示例 5：几何修改后重新生成</h2>
<pre><code class="language-bash">blockMesh -case ./enclosure-wide
faceAgglomerate -case ./enclosure-wide
createViewFactors -case ./enclosure-wide
</code></pre>
<p>enclosure-wide是改变腔体宽度后的独立案例；重建网格、聚合和因子，使结果反映新的可见关系。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/createViewFactors/createViewFactors/createViewFactors.C">源码与说明</a> · <a href="/assets/command-help/createviewfactors.txt">帮助文本</a></p>
