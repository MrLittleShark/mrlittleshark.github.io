---
title: "surfaceLambdaMuSmooth · lambda 和 mu 均采用该程序定义的 [0,1] 系数"
layout: reference
description: "lambda 和 mu 均采用该程序定义的 [0,1] 系数。"
cms_slug: "command-surfacelambdamusmooth"
---

<p>lambda 和 mu 均采用该程序定义的 [0,1] 系数。</p><h2>用法</h2><pre><code class="language-bash">surfaceLambdaMuSmooth body.stl 0.5 0.5 10 smooth.stl</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceLambdaMuSmooth [OPTIONS] &lt;input&gt; &lt;lambda&gt; &lt;mu&gt; &lt;iterations&gt; &lt;output&gt;
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
