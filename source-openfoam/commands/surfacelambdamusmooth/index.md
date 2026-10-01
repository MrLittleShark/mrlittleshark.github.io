---
title: "surfaceLambdaMuSmooth  采用 lambda mu 算法平滑表面"
layout: reference
description: "lambda 和 mu 均采用该程序定义的 [0,1] 系数。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>lambda 和 mu 均采用该程序定义的 [0,1] 系数。</p><h2>v2512 源码中的用途</h2><p>Smooth a surface using lambda/mu smoothing. To get laplacian smoothing, set lambda to the relaxation factor and mu to zero. Provide an edgeMesh file containing points that are not to be moved during smoothing in order to preserve features. lambda/mu smoothing: G. Taubin, IBM Research report Rc-19923 (02/01/95) &quot;A signal processing approach to fair surface design&quot;</p><h2>使用入口</h2><pre><code class="language-bash">surfaceLambdaMuSmooth body.stl 0.5 0.5 10 smooth.stl</code></pre><h2>使用条件与核对</h2><p>lambda 和 mu 均采用该程序定义的 [0,1] 系数。 用法：surfaceLambdaMuSmooth 输入 lambda mu 迭代数 输出 示例：surfaceLambdaMuSmooth body.stl 0.5 0.5 10 smooth.stl
源码说明：Smooth a surface using lambda/mu smoothing. To get laplacian smoothing, set lambda to the relaxation factor and mu to zero. Provide an edgeMesh file containing points that are not to be moved during smoothing in order to preserve features. lambda/mu smoothing: G. Taubin, IBM Research report Rc-19923 (02/01/95) &quot;A signal processing approach to fair surface design&quot;
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-doc -doc-source -featureFile -help -help-full -help-man -help-notes</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/surfacelambdamusmooth.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: surfaceLambdaMuSmooth
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceLambdaMuSmooth/surfaceLambdaMuSmooth.C


Usage: surfaceLambdaMuSmooth [OPTIONS] &lt;input&gt; &lt;lambda&gt; &lt;mu&gt; &lt;iterations&gt; &lt;output&gt;
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
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceLambdaMuSmooth/surfaceLambdaMuSmooth.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceLambdaMuSmooth/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
