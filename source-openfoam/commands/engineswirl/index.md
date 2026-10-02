---
title: "engineSwirl · 根据发动机几何参数生成初始旋流速度场"
layout: reference
description: "根据发动机几何参数生成初始旋流速度场。"
cms_slug: "command-engineswirl"
---

<p>根据发动机几何参数生成初始旋流速度场。</p><h2>开始前</h2>
<p>已有U场和constant/engineGeometry，包含swirlAxis、swirlCenter、swirlRPMRatio、swirlProfile、bore及rpm。</p>
<h2>示例 1：生成基准旋流</h2>
<pre><code class="language-bash">engineSwirl
</code></pre>
<p>按缸径、转速和旋流剖面更新U，日志输出Umax，便于核对初始速度量级。</p>
<h2>示例 2：提高旋流比</h2>
<pre><code class="language-bash">foamDictionary constant/engineGeometry -entry swirlRPMRatio -set 1.5
engineSwirl
</code></pre>
<p>旋流比设为1.5，保持发动机转速和几何不变；生成的切向速度幅值随旋流比改变。</p>
<h2>示例 3：改变旋流中心</h2>
<pre><code class="language-bash">foamDictionary constant/engineGeometry -entry swirlCenter -set '(0.01 0 0)'
engineSwirl
</code></pre>
<p>将旋流轴中心平移到指定坐标，适合检查偏心初始旋流的空间分布。</p>
<h2>示例 4：改为绕y轴旋转</h2>
<pre><code class="language-bash">foamDictionary constant/engineGeometry -entry swirlAxis -set '(0 1 0)'
engineSwirl
</code></pre>
<p>swirlAxis给出旋转轴方向；程序构造垂直于该轴的横截面，并在其中生成切向速度。</p>
<h2>示例 5：导出初始旋流进行检查</h2>
<pre><code class="language-bash">engineSwirl
foamToVTK -time 0 -fields '(U)' -name VTK-swirl
</code></pre>
<p>初始时间为0时生成并导出U；用箭头或截面查看旋向、旋流中心和缸壁附近速度。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/engineSwirl/engineSwirl.C">源码与说明</a> · <a href="/assets/command-help/engineswirl.txt">帮助文本</a></p>
