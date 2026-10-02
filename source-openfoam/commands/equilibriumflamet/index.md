---
title: "equilibriumFlameT · 扫描燃料当量比和初温，同时计算包含部分产物解离的平衡火焰温度"
layout: reference
description: "扫描燃料当量比和初温，同时计算包含部分产物解离的平衡火焰温度。"
cms_slug: "command-equilibriumflamet"
---

<p>扫描燃料当量比和初温，同时计算包含部分产物解离的平衡火焰温度。</p><h2>开始前</h2>
<p>独立控制文件提供P、fuel、n、m；v2512源码扫描phi=0.6至1.35、初温300至3000K，并考虑CO2与H2O解离。</p>
<h2>示例 1：计算甲烷的温度扫描</h2>
<pre><code class="language-bash">cat &gt; equilibrium-methane.in &lt;&lt;'EOF'
P 100000;
fuel CH4___ANHARMONIC;
n 1;
m 4;
EOF
equilibriumFlameT equilibrium-methane.in
</code></pre>
<p>使用实际存在的甲烷热物性键，输出每个phi和T0下的Tad、Teq、温差及剩余氧摩尔分数。</p>
<h2>示例 2：比较较高压力</h2>
<pre><code class="language-bash">cp equilibrium-methane.in equilibrium-10bar.in
foamDictionary equilibrium-10bar.in -entry P -set 1000000
equilibriumFlameT equilibrium-10bar.in
</code></pre>
<p>将压力改为10bar，比较同一phi、T0下产物解离与Teq的变化。</p>
<h2>示例 3：换成丙烷</h2>
<pre><code class="language-bash">cp equilibrium-methane.in equilibrium-propane.in
foamDictionary equilibrium-propane.in -entry fuel -set C3H8
foamDictionary equilibrium-propane.in -entry n -set 3
foamDictionary equilibrium-propane.in -entry m -set 8
equilibriumFlameT equilibrium-propane.in
</code></pre>
<p>燃料键与原子数同时修改，程序重算理论需氧量并输出丙烷扫描结果。</p>
<h2>示例 4：提取300K初温的数据行</h2>
<pre><code class="language-bash">equilibriumFlameT equilibrium-methane.in | awk 'NF==7 &amp;&amp; $3==300 {print $1,$4,$5,$6}'
</code></pre>
<p>按输出表结构提取phi、Tad、Teq和温差，得到初温300K时的当量比曲线数据。</p>
<h2>示例 5：批量压力扫描</h2>
<pre><code class="language-bash">for pressurePa in 100000 500000 1000000; do
    cp equilibrium-methane.in "equilibrium-${pressurePa}.in"
    foamDictionary "equilibrium-${pressurePa}.in" -entry P -set "$pressurePa"
    equilibriumFlameT "equilibrium-${pressurePa}.in" &gt; "equilibrium-${pressurePa}.out"
done
</code></pre>
<p>保持同一燃料和源码扫描范围，在1、5、10bar分别输出完整表，便于比较压力与解离影响。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/thermophysical/equilibriumFlameT/equilibriumFlameT.C">源码与说明</a> · <a href="/assets/command-help/equilibriumflamet.txt">帮助文本</a></p>
