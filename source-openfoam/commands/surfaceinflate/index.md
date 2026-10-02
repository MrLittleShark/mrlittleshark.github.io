---
title: "surfaceInflate · 安全因子范围为 [1,10]，膨胀后检查表面自相交"
layout: reference
description: "安全因子范围为 [1,10]，膨胀后检查表面自相交。"
cms_slug: "command-surfaceinflate"
---

<p>安全因子范围为 [1,10]，膨胀后检查表面自相交。</p><h2>开始前</h2>
<p>在工作算例中准备表面及controlDict；distance按几何长度单位填写，factor为额外延伸安全系数，常用1～2。</p>
<h2>示例 1：生成小幅外偏移</h2>
<pre><code class="language-bash">surfaceInflate body.stl 0.001 1.2
</code></pre>
<p>沿点法向膨胀约1mm，并使用1.2安全系数；查看日志列出的表面与迭代输出。</p>
<h2>示例 2：增大包络距离</h2>
<pre><code class="language-bash">surfaceInflate body.stl 0.005 1.2
</code></pre>
<p>对同一原始几何生成5mm级外包络，适合比较间隙或外围包络。</p>
<h2>示例 3：减少法向平滑次数</h2>
<pre><code class="language-bash">surfaceInflate -nSmooth 5 body.stl 0.001 1.2
</code></pre>
<p>将平滑迭代数设为5，比较棱角附近法向传播与局部偏移形状。</p>
<h2>示例 4：设置特征角</h2>
<pre><code class="language-bash">surfaceInflate -featureAngle 45 -nSmooth 2 body.stl 0.002 1.5
</code></pre>
<p>用45°特征角和两次平滑处理有棱角表面，观察锐边附近的膨胀效果。</p>
<h2>示例 5：加入自相交检查</h2>
<pre><code class="language-bash">surfaceInflate -checkSelfIntersection body.stl 0.002 1.2
</code></pre>
<p>狭窄间隙或凹角处启用自相交检查，检查偏移是否导致表面互相穿过。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-debug</code></td><td>Switch on additional debug information Set named DebugSwitch (default value: 1). [Can be used multiple times] Feature angle Override the file handler type Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceInflate [OPTIONS] &lt;input&gt; &lt;distance&gt; &lt;factor&gt;
Arguments:
  &lt;input&gt;           The input surface file
  &lt;distance&gt;        The inflate distance
  &lt;factor&gt;          The extend safety factor [1,10]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -checkSelfIntersection
                    Also check for self-intersection
  -debug            Switch on additional debug information
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -featureAngle &lt;scalar&gt;
                    Feature angle
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -nSmooth &lt;integer&gt;
                    Number of smoothing iterations (default 20)
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

Inflates surface according to point normals.
Creates inflated version of surface using point normals. Takes surface,
distance to inflate and additional safety factor

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceInflate/surfaceInflate.C">源码与说明</a> · <a href="/assets/command-help/surfaceinflate.txt">帮助文本</a></p>
