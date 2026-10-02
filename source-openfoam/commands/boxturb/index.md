---
title: "boxTurb · 在规则盒网格上生成符合指定能谱的无散湍流速度"
layout: reference
description: "在规则盒网格上生成符合指定能谱的无散湍流速度。"
cms_slug: "command-boxturb"
---

<p>在规则盒网格上生成符合指定能谱的无散湍流速度。</p><h2>开始前</h2>
<p>已有规则盒网格、U初始场和 constant/boxTurbDict，其中 Ea 为谱幅参数、k0 为特征波数。</p>
<h2>示例 1：生成基准湍流盒</h2>
<pre><code class="language-bash">boxTurb
</code></pre>
<p>按Ea、k0生成U并写能谱图数据到graphs/当前时间/Ek，日志报告生成场的能量统计。</p>
<h2>示例 2：增加谱能量幅值</h2>
<pre><code class="language-bash">foamDictionary constant/boxTurbDict -entry Ea -set 0.02
boxTurb
</code></pre>
<p>在独立案例中把Ea设为0.02，生成更改谱幅后的速度；与原Ea结果比较速度幅值和Ek曲线。</p>
<h2>示例 3：改变主要涡尺度</h2>
<pre><code class="language-bash">foamDictionary constant/boxTurbDict -entry k0 -set 8
boxTurb
</code></pre>
<p>k0控制输入谱的特征波数，修改后观察能量峰值位置；波数尺度应与盒长及网格分辨率匹配。</p>
<h2>示例 4：生成后检查离散散度</h2>
<pre><code class="language-bash">boxTurb
postProcess -func 'div(U)' -time 0
</code></pre>
<p>初始时间为0时，计算生成速度的离散散度场，查看空间分布及局部离散误差。</p>
<h2>示例 5：细网格湍流盒对照</h2>
<pre><code class="language-bash">blockMesh -case ./turbFine
boxTurb -case ./turbFine
foamToVTK -case ./turbFine -time 0 -fields '(U)'
</code></pre>
<p>turbFine已配置更细的规则网格和相同物理谱参数；生成后导出U，比较可表达的小尺度结构。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/boxTurb/boxTurb.C">源码与说明</a> · <a href="/assets/command-help/boxturb.txt">帮助文本</a></p>
