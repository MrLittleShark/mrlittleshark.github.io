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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: equilibriumFlameT [OPTIONS] &lt;controlFile&gt;
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Calculate the equilibrium flame temperature for a given fuel and pressure for a
range of unburnt gas temperatures and equivalence ratios.
Includes the effects of dissociation on O2, H2O and CO2.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/thermophysical/equilibriumFlameT/equilibriumFlameT.C">源码与说明</a> · <a href="/assets/command-help/equilibriumflamet.txt">帮助文本</a></p>
