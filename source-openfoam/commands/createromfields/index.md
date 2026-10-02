---
title: "createROMfields · 根据已训练的降阶模型数据重建指定时刻的场"
layout: reference
description: "根据已训练的降阶模型数据重建指定时刻的场。"
cms_slug: "command-createromfields"
---

<p>根据已训练的降阶模型数据重建指定时刻的场。</p><h2>开始前</h2>
<p>已有网格、system/ROMfieldsDict、相应模态与系数数据；目标时间目录需要满足所选ROM模型的读取要求。</p>
<h2>示例 1：按默认ROM字典重建</h2>
<pre><code class="language-bash">createROMfields
</code></pre>
<p>读取ROMfieldsDict选择模型，使用现有降阶数据创建并写字段，省去重新求解完整CFD方程。</p>
<h2>示例 2：只重建最新已选时刻</h2>
<pre><code class="language-bash">createROMfields -latestTime
</code></pre>
<p>选择最新可用时间，根据模态与时间系数生成该状态的重建场。</p>
<h2>示例 3：重建一段时间序列</h2>
<pre><code class="language-bash">createROMfields -time '0.1:1'
</code></pre>
<p>对该区间内可选择的已有时间目录重建，适合与高保真结果逐时刻比较。</p>
<h2>示例 4：比较另一模态截断方案</h2>
<pre><code class="language-bash">createROMfields -dict system/ROMfields-lowRankDict -time '0.1:1'
</code></pre>
<p>替代字典已配置较少模态及对应数据；在独立案例比较重建细节与误差。</p>
<h2>示例 5：重建指定区域后导出</h2>
<pre><code class="language-bash">createROMfields -region fluid -latestTime
foamToVTK -region fluid -latestTime -fields '(U p)' -name VTK-ROM
</code></pre>
<p>ROM模型配置为重建U、p时，先生成fluid区域场，再导出检查模态重建的空间结构。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 ROMfieldsDict 文件。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（16 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/miscellaneous/createROMfields/ROMmodels/ROMmodel/ROMmodel.C">源码与说明</a> · <a href="/assets/command-help/createromfields.txt">帮助文本</a></p>
