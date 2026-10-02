---
title: "foamCleanFaMesh · 对应 constant/finite-area/faMesh，-area-region 指定有限"
layout: reference
description: "对应 constant/finite-area/faMesh，-area-region 指定有限面积区域。"
cms_slug: "command-foamcleanfamesh"
---

<p>对应 constant/finite-area/faMesh，-area-region 指定有限面积区域。</p><h2>开始前</h2>
<p>加载 v2512 环境，使用个人算例副本 caseA。并行示例先配置 decomposeParDict 并完成 decomposePar，程序和字典须匹配。 下列移除示例只在可重建网格的副本中使用；-dry-run 可先查看文件清单。</p>
<h2>示例 1：预览默认区域</h2>
<pre><code class="language-bash">foamCleanFaMesh -dry-run -case caseA
</code></pre>
<p>只报告默认网格位置中将处理的文件。</p>
<h2>示例 2：预览指定区域</h2>
<pre><code class="language-bash">foamCleanFaMesh -dry-run -area-region film -case caseA
</code></pre>
<p>-area-region 选择实际存在的 film 区域，其他区域不参与。</p>
<h2>示例 3：预览全部区域</h2>
<pre><code class="language-bash">foamCleanFaMesh -dry-run -allAreas -case caseA
</code></pre>
<p>-allAreas 遍历所有对应区域，并显示计划。</p>
<h2>示例 4：清理副本默认网格</h2>
<pre><code class="language-bash">cp -a caseA mesh-reset-copy
foamCleanFaMesh -case mesh-reset-copy
</code></pre>
<p>新副本内移除程序识别的网格文件，输入字典用于下一次重建。</p>
<h2>示例 5：清理副本中的指定区域</h2>
<pre><code class="language-bash">cp -a caseA region-reset-copy
foamCleanFaMesh -area-region film -case region-reset-copy
</code></pre>
<p>只清理选定区域，其他区域网格保留。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-allAreas</code></td><td>all area regions</td></tr><tr><td><code>-area-region &lt;name&gt;</code></td><td>area-mesh region</td></tr><tr><td><code>-dry-run | -n</code></td><td>report actions but do not remove</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamCleanFaMesh [OPTION]
options:
  -case &lt;dir&gt;           case directory, default is the cwd
  -allAreas             all area regions
  -area-region &lt;name&gt;   area-mesh region
  -dry-run | -n         report actions but do not remove
  -help                 print the usage

Remove the contents of the constant/finite-area/faMesh directory as per the
Foam::faMesh::removeFiles() method.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCleanFaMesh">源码与说明</a> · <a href="/assets/command-help/foamcleanfamesh.txt">帮助文本</a></p>
