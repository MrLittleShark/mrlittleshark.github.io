---
title: "surfaceSplitByTopology · 用于分离拓扑不连通的部件"
layout: reference
description: "用于分离拓扑不连通的部件。"
cms_slug: "command-surfacesplitbytopology"
---

<p>用于分离拓扑不连通的部件。</p><h2>用法</h2><pre><code class="language-bash">surfaceSplitByTopology body.stl split.stl</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceSplitByTopology [OPTIONS] &lt;input&gt; &lt;output&gt;
Arguments:
  &lt;input&gt;           The input surface file
  &lt;output&gt;          The output surface file
Options:
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Strips any baffle parts of a surface.
A baffle region is one which is reached by walking from an open edge, and
stopping when a multiply connected edge is reached.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceSplitByTopology/surfaceSplitByTopology.C">源码与说明</a> · <a href="/assets/command-help/surfacesplitbytopology.txt">帮助文本</a></p>
