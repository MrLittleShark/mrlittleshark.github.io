---
title: "applyBoundaryLayer · 按七分之一次幂规律修正近壁速度及相应湍流场"
layout: reference
description: "按七分之一次幂规律修正近壁速度及相应湍流场。"
cms_slug: "command-applyboundarylayer"
---

<p>按七分之一次幂规律修正近壁速度及相应湍流场。</p><h2>开始前</h2>
<p>已有速度场、壁面和所需湍流模型输入；边界层厚度可用绝对长度 ybl 或相对系数 Cbl 指定。</p>
<h2>示例 1：设置明确的边界层厚度</h2>
<pre><code class="language-bash">applyBoundaryLayer -ybl 0.01
</code></pre>
<p>以0.01米厚度修正近壁速度，适合给外流案例构造初始速度剖面。</p>
<h2>示例 2：按网格平均壁距设置厚度</h2>
<pre><code class="language-bash">applyBoundaryLayer -Cbl 2
</code></pre>
<p>厚度取平均壁距的2倍，适合根据当前网格近壁尺度生成初始分布。</p>
<h2>示例 3：同时写湍流场</h2>
<pre><code class="language-bash">applyBoundaryLayer -ybl 0.01 -writeTurbulenceFields
</code></pre>
<p>更新速度并写相应湍流量，使初始湍流场与所构造近壁剖面配套。</p>
<h2>示例 4：比较更厚的入口发展层</h2>
<pre><code class="language-bash">applyBoundaryLayer -case ./thickLayer -ybl 0.02 -writeTurbulenceFields
</code></pre>
<p>thickLayer 是独立初始案例；厚度改为0.02米，可比较速度亏损范围与湍流场变化。</p>
<h2>示例 5：只处理流体区域</h2>
<pre><code class="language-bash">applyBoundaryLayer -region fluid -ybl 0.005 -writeTurbulenceFields
</code></pre>
<p>多区域中只修改fluid的近壁场，适合流固传热案例的流体初始状态准备。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-Cbl &lt;scalar&gt;</code></td><td>将边界层厚度设为 Cbl 乘以平均壁面距离。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-writeTurbulenceFields</code></td><td>写出湍流场。</td></tr><tr><td><code>-ybl &lt;scalar&gt;</code></td><td>直接指定边界层厚度。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/applyBoundaryLayer/applyBoundaryLayer.C">源码与说明</a> · <a href="/assets/command-help/applyboundarylayer.txt">帮助文本</a></p>
