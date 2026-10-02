---
title: "foamCleanFaMesh · 对应 constant/finite-area/faMesh，-area-region 指定有限"
layout: reference
description: "对应 constant/finite-area/faMesh，-area-region 指定有限面积区域。"
cms_slug: "command-foamcleanfamesh"
---

<p>对应 constant/finite-area/faMesh，-area-region 指定有限面积区域。</p><h2>用法</h2><pre><code class="language-bash">foamCleanFaMesh -dry-run</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">foamCleanFaMesh -dry-run -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-allAreas</td><td>all area regions</td></tr><tr><td>-area-region &lt;name&gt;</td><td>area-mesh region</td></tr><tr><td>-dry-run | -n</td><td>report actions but do not remove</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamCleanFaMesh [OPTION]
options:
  -case &lt;dir&gt;           case directory, default is the cwd
  -allAreas             all area regions
  -area-region &lt;name&gt;   area-mesh region
  -dry-run | -n         report actions but do not remove
  -help                 print the usage

Remove the contents of the constant/finite-area/faMesh directory as per the
Foam::faMesh::removeFiles() method.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCleanFaMesh">源码与说明</a> · <a href="/assets/command-help/foamcleanfamesh.txt">帮助文本</a></p>
