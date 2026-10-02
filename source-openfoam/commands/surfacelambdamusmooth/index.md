---
title: "surfaceLambdaMuSmooth · lambda 和 mu 均采用该程序定义的 [0,1] 系数"
layout: reference
description: "lambda 和 mu 均采用该程序定义的 [0,1] 系数。"
cms_slug: "command-surfacelambdamusmooth"
---

<p>lambda 和 mu 均采用该程序定义的 [0,1] 系数。</p><h2>开始前</h2>
<p>输入为三角表面，lambda与mu按工具接口取0到1；输出另存，比较轮廓和体积变化。</p>
<h2>示例 1：轻度拉普拉斯平滑</h2>
<pre><code class="language-bash">surfaceLambdaMuSmooth raw.stl 0.2 0 5 smooth5.stl
</code></pre>
<p>mu=0采用拉普拉斯平滑，lambda=0.2控制每次松弛量，先做5次观察。</p>
<h2>示例 2：增加平滑轮数</h2>
<pre><code class="language-bash">surfaceLambdaMuSmooth raw.stl 0.2 0 20 smooth20.stl
</code></pre>
<p>从同一原表面开始做20次，与5次结果比较噪声减少和轮廓收缩。</p>
<h2>示例 3：采用双参数平滑</h2>
<pre><code class="language-bash">surfaceLambdaMuSmooth raw.stl 0.3 0.31 10 smoothLM.stl
</code></pre>
<p>使用lambda/mu两步平滑，以不同参数对抗单步平滑造成的收缩；检查实际体积变化。</p>
<h2>示例 4：保护特征点和边</h2>
<pre><code class="language-bash">surfaceLambdaMuSmooth -featureFile body.eMesh raw.stl 0.3 0.31 10 preserved.stl
</code></pre>
<p>已有与表面对应的特征边文件时，固定其中指定的特征，保留关键棱角。</p>
<h2>示例 5：比较平滑后的质量</h2>
<pre><code class="language-bash">surfaceLambdaMuSmooth raw.stl 0.3 0.31 10 smooth.stl
surfaceCheck -checkSelfIntersection smooth.stl
</code></pre>
<p>查看自相交、开边和包围盒，判断平滑是否改善局部三角形而保留所需几何。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceLambdaMuSmooth [OPTIONS] &lt;input&gt; &lt;lambda&gt; &lt;mu&gt; &lt;iterations&gt; &lt;output&gt;
Arguments:
  &lt;input&gt;           The input surface file
  &lt;lambda&gt;          On the interval [0,1]
  &lt;mu&gt;              On the interval [0,1]
  &lt;iterations&gt;      The number of iterations to perform
  &lt;output&gt;          The output surface file
Options:
  -featureFile &lt;Fix points from a file containing feature points and edges&gt;
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Smooth a surface using lambda/mu smoothing.
For laplacian smoothing, set lambda to the relaxation factor and mu to zero.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceLambdaMuSmooth/surfaceLambdaMuSmooth.C">源码与说明</a> · <a href="/assets/command-help/surfacelambdamusmooth.txt">帮助文本</a></p>
