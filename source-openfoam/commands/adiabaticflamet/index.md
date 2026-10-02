---
title: "adiabaticFlameT · 按给定燃料和初温扫描当量比，计算绝热火焰温度"
layout: reference
description: "按给定燃料和初温扫描当量比，计算绝热火焰温度。"
cms_slug: "command-adiabaticflamet"
---

<p>按给定燃料和初温扫描当量比，计算绝热火焰温度。</p><h2>开始前</h2>
<p>读取位置参数给出的独立控制文件；P以Pa、T0以K填写，n/m为烃分子中的C/H原子数，fuel必须匹配安装版thermoData物种键。</p>
<h2>示例 1：创建甲烷基准输入</h2>
<pre><code class="language-bash">cat &gt; flame-300K.in &lt;&lt;'EOF'
P 100000;
T0 300;
fuel CH4___ANHARMONIC;
n 1;
m 4;
EOF
adiabaticFlameT flame-300K.in
</code></pre>
<p>采用v2512热物性库实际存在的甲烷键，初温300K、压力1bar；程序按源码扫描当量比0.01至3，输出phi、混合分数和Tad。</p>
<h2>示例 2：比较反应物预热</h2>
<pre><code class="language-bash">cp flame-300K.in flame-600K.in
foamDictionary flame-600K.in -entry T0 -set 600
adiabaticFlameT flame-600K.in
</code></pre>
<p>只把初温提高到600K，比较同一当量比下的Tad；其余燃料与热物性输入保持相同。</p>
<h2>示例 3：切换为乙烷</h2>
<pre><code class="language-bash">cp flame-300K.in flame-ethane.in
foamDictionary flame-ethane.in -entry fuel -set C2H6
foamDictionary flame-ethane.in -entry n -set 2
foamDictionary flame-ethane.in -entry m -set 6
adiabaticFlameT flame-ethane.in
</code></pre>
<p>同时修改物种名称和C/H原子数，工具由n、m重新计算理论需氧量，输出乙烷的当量比扫描。</p>
<h2>示例 4：给出另一压力条件</h2>
<pre><code class="language-bash">cp flame-300K.in flame-5bar.in
foamDictionary flame-5bar.in -entry P -set 500000
adiabaticFlameT flame-5bar.in
</code></pre>
<p>压力改为5bar；该工具采用给定产物组合的焓平衡，与包含解离的平衡温度模型区别在产物处理方式。</p>
<h2>示例 5：批量比较预热温度</h2>
<pre><code class="language-bash">for tempK in 300 450 600; do
    cp flame-300K.in "flame-${tempK}K.in"
    foamDictionary "flame-${tempK}K.in" -entry T0 -set "$tempK"
    adiabaticFlameT "flame-${tempK}K.in" &gt; "flame-${tempK}K.out"
done
</code></pre>
<p>建立三份独立输入并各自扫描当量比，输出可用于绘制Tad–phi曲线族，比较预热对整个燃烧范围的影响。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/thermophysical/adiabaticFlameT/adiabaticFlameT.C">源码与说明</a> · <a href="/assets/command-help/adiabaticflamet.txt">帮助文本</a></p>
