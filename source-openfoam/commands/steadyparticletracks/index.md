---
title: "steadyParticleTracks · 按稳态粒子云记录的 age 将路径点排序并导出轨迹"
layout: reference
description: "按稳态粒子云记录的 age 将路径点排序并导出轨迹。"
cms_slug: "command-steadyparticletracks"
---

<p>按稳态粒子云记录的 age 将路径点排序并导出轨迹。</p><h2>开始前</h2>
<p>已有稳态云保存的轨迹采样、origId/origProc和age；constant/particleTrackDict定义cloud与fields。</p>
<h2>示例 1：导出最终稳态轨迹</h2>
<pre><code class="language-bash">steadyParticleTracks -latestTime
</code></pre>
<p>对最新时间内同一粒子的路径样本按age排序，生成VTK/该时间/particleTracks.vtk。</p>
<h2>示例 2：处理指定计算状态</h2>
<pre><code class="language-bash">steadyParticleTracks -time 100
</code></pre>
<p>在已保存时间100中重建轨迹，适合比较不同稳态迭代阶段的粒子运动。</p>
<h2>示例 3：使用另一云配置</h2>
<pre><code class="language-bash">steadyParticleTracks -dict constant/particleTrackDict-coal -latestTime
</code></pre>
<p>替代字典指定coal云及输出字段；输出该云的路径和粒径、温度等属性。</p>
<h2>示例 4：只导出需要的轨迹属性</h2>
<pre><code class="language-bash">foamDictionary constant/particleTrackDict -entry fields -set '(U d)'
steadyParticleTracks -latestTime
</code></pre>
<p>fields设为U、d后，几何轨迹保持相同，只附带速度和直径数据，减少输出体积。</p>
<h2>示例 5：多区域中的粒子轨迹</h2>
<pre><code class="language-bash">steadyParticleTracks -region gas -latestTime -verbose
</code></pre>
<p>从gas区域读取云，并显示更详细的读取和写出信息，便于核对轨迹数量与输出位置。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant/ 目录加入时间选择。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 particleTrackDict 文件。</td></tr><tr><td><code>-latestTime</code></td><td>选择最新的结果时刻。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-noZero</code></td><td>在时间选择中排除 0/ 目录。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>指定时间范围列表，例如 &#x27;:10,20 40:70 1000:&#x27;；none 表示空选择。</td></tr><tr><td><code>-verbose</code></td><td>显示更详细的输出；可重复使用以增加详细程度。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/lagrangian/steadyParticleTracks/steadyParticleTracks.C">源码与说明</a> · <a href="/assets/command-help/steadyparticletracks.txt">帮助文本</a></p>
