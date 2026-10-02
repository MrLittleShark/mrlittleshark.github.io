---
title: "mixtureAdiabaticFlameT · 根据给定反应物与产物组成，通过热物性焓关系估算绝热温度"
layout: reference
description: "根据给定反应物与产物组成，通过热物性焓关系估算绝热温度。"
cms_slug: "command-mixtureadiabaticflamet"
---

<p>根据给定反应物与产物组成，通过热物性焓关系估算绝热温度。</p><h2>开始前</h2>
<p>控制文件含P、T0、reactants、products；组分以物种名和权重成对列出，两组权重各自和为1，列表后还需混合物名称。</p>
<h2>示例 1：建立甲烷空气组成输入</h2>
<pre><code class="language-bash">cat &gt; mixture.in &lt;&lt;'EOF'
P 100000;
T0 300;
reactants (CH4___ANHARMONIC 0.095057 O2 0.190114 N2 0.714829) methaneAir;
products (CO2 0.095057 H2O 0.190114 N2 0.714829) burntGas;
EOF
mixtureAdiabaticFlameT mixture.in
</code></pre>
<p>列出近化学计量甲烷空气的给定组成，物种键匹配安装热物性库；工具按源码的混合焓组合求出单个温度，输出单位K。</p>
<h2>示例 2：比较反应物预热</h2>
<pre><code class="language-bash">cp mixture.in mixture-hot.in
foamDictionary mixture-hot.in -entry T0 -set 600
mixtureAdiabaticFlameT mixture-hot.in
</code></pre>
<p>保留两组组成，把初温改为600K，查看初始焓提高后的计算温度。</p>
<h2>示例 3：在另一压力下计算</h2>
<pre><code class="language-bash">cp mixture.in mixture-5bar.in
foamDictionary mixture-5bar.in -entry P -set 500000
mixtureAdiabaticFlameT mixture-5bar.in
</code></pre>
<p>压力改为5bar，输入的产物组成仍固定；适合分析该焓计算对压力参数的响应。</p>
<h2>示例 4：设置过量空气的组成</h2>
<pre><code class="language-bash">cp mixture.in mixture-lean.in
foamDictionary mixture-lean.in -entry reactants -set '(CH4___ANHARMONIC 0.0499002 O2 0.1996008 N2 0.7504990) leanReactants'
foamDictionary mixture-lean.in -entry products -set '(CO2 0.0499002 H2O 0.0998004 O2 0.0998004 N2 0.7504990) leanProducts'
mixtureAdiabaticFlameT mixture-lean.in
</code></pre>
<p>示例按较稀甲烷空气配比同时调整两组组成，产物保留剩余O2；比较给定组成变化对计算温度的影响。</p>
<h2>示例 5：建立温压参数表</h2>
<pre><code class="language-bash">for pressurePa in 100000 500000; do
    for tempK in 300 600; do
        cp mixture.in "mix-${pressurePa}-${tempK}.in"
        foamDictionary "mix-${pressurePa}-${tempK}.in" -entry P -set "$pressurePa"
        foamDictionary "mix-${pressurePa}-${tempK}.in" -entry T0 -set "$tempK"
        mixtureAdiabaticFlameT "mix-${pressurePa}-${tempK}.in"
    done
done
</code></pre>
<p>对同一给定组成计算四个温压组合，输出可整理为温度响应表；组成由输入指定，扩展时应同步维护反应物与产物配比。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/thermophysical/mixtureAdiabaticFlameT/mixtureAdiabaticFlameT.C">源码与说明</a> · <a href="/assets/command-help/mixtureadiabaticflamet.txt">帮助文本</a></p>
