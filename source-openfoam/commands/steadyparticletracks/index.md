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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-constant</code></td><td>将 constant 目录加入选择。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-latestTime</code></td><td>选择最近的结果时刻。</td></tr><tr><td><code>-noZero</code></td><td>跳过 0 时刻。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-time &lt;ranges&gt;</code></td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td><code>-verbose</code></td><td>Additional verbosity (can be used multiple times)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: steadyParticleTracks [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dict &lt;file&gt;      Alternative particleTrackDict dictionary
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -verbose          Additional verbosity (can be used multiple times)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Generate a legacy VTK file of particle tracks for cases that were computed
using a steady-state cloud

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/lagrangian/steadyParticleTracks/steadyParticleTracks.C">源码与说明</a> · <a href="/assets/command-help/steadyparticletracks.txt">帮助文本</a></p>
