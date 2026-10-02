---
title: "mdInitialise · 按晶格、密度、温度和整体速度生成分子动力学初态"
layout: reference
description: "按晶格、密度、温度和整体速度生成分子动力学初态。"
cms_slug: "command-mdinitialise"
---

<p>按晶格、密度、温度和整体速度生成分子动力学初态。</p><h2>开始前</h2>
<p>已有MD网格、system/mdInitialiseDict、分子类型和势函数；初始化区域与字典中的分子分组一致。</p>
<h2>示例 1：生成基准分子云</h2>
<pre><code class="language-bash">mdInitialise
</code></pre>
<p>读取各分组的晶格与热运动参数，生成分子并写出初态，日志汇总分子数量。</p>
<h2>示例 2：提高初始温度</h2>
<pre><code class="language-bash">foamDictionary system/mdInitialiseDict -entry liquid/temperature -set 350
mdInitialise
</code></pre>
<p>字典已有liquid分组时，将热运动初始化温度设为350K，观察后续平衡过程。</p>
<h2>示例 3：给分子云加入整体平移</h2>
<pre><code class="language-bash">foamDictionary system/mdInitialiseDict -entry liquid/bulkVelocity -set '(100 0 0)'
mdInitialise
</code></pre>
<p>整体速度沿x方向为100米每秒，叠加在热运动上，可用于平移流或动量检查。</p>
<h2>示例 4：旋转初始晶格</h2>
<pre><code class="language-bash">foamDictionary system/mdInitialiseDict -entry liquid/orientationAngles -set '(0 0 45)'
mdInitialise
</code></pre>
<p>欧拉角按字典约定以度填写；改变晶格取向，适合研究结构相对边界的排列。</p>
<h2>示例 5：初始化后进行热平衡</h2>
<pre><code class="language-bash">mdInitialise
mdEquilibrationFoam
</code></pre>
<p>案例已配置mdEquilibrationFoam及温控参数；先建分子初态，再让系统按势函数松弛到目标状态。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/mdInitialise/mdInitialise.C">源码与说明</a> · <a href="/assets/command-help/mdinitialise.txt">帮助文本</a></p>
