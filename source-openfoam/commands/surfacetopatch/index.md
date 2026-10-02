---
title: "surfaceToPatch · 修改后同步检查场文件中的边界条目"
layout: reference
description: "修改后同步检查场文件中的边界条目。"
cms_slug: "command-surfacetopatch"
---

<p>修改后同步检查场文件中的边界条目。</p><h2>开始前</h2>
<p>已有体网格及带区域名称的三角表面，二者坐标和单位一致。该工具按表面分区重新分配网格边界，建议在独立案例副本运行。</p>
<h2>示例 1：按几何区域重划边界</h2>
<pre><code class="language-bash">surfaceToPatch constant/triSurface/body.stl
</code></pre>
<p>把表面的区域信息映射到现有网格边界面上。处理后查看 polyMesh/boundary，并为新增边界补齐各场文件的边界条件。</p>
<h2>示例 2：指定匹配容差</h2>
<pre><code class="language-bash">surfaceToPatch constant/triSurface/body.stl -tol 0.0001
</code></pre>
<p>容差是相对网格尺度的比例，较小值要求网格面与表面更接近。检查未能匹配的区域，避免把几何错位当作容差问题。</p>
<h2>示例 3：对离散误差稍大的表面匹配</h2>
<pre><code class="language-bash">surfaceToPatch constant/triSurface/body.stl -tol 0.002
</code></pre>
<p>适用于已确认几何一致、但表面离散产生小偏差的情况。提高容差后检查相邻区域边界，确认没有跨越窄间隙误匹配。</p>
<h2>示例 4：只处理选定的面集</h2>
<pre><code class="language-bash">surfaceToPatch constant/triSurface/body.stl -faceSet targetFaces
</code></pre>
<p>使用已存在的 targetFaces 限定处理面。适合只重划某个零件或一组边界，保留其余网格面的分区。</p>
<h2>示例 5：在副本重划并检查</h2>
<pre><code class="language-bash">surfaceToPatch -case ../patchTest ../patchTest/constant/triSurface/body.stl -tol 0.001
checkMesh -case ../patchTest -latestTime
</code></pre>
<p>将试验限制在 patchTest 副本。工具有边界变更时把新网格写到后续时间，因此检查最新网格；核对边界名称、网格连接并配置相应场文件后再继续求解。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-faceSet &lt;name&gt;</code></td><td>Only repatch the faces in specified faceSet Override the file handler type Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-tol &lt;scalar&gt;</code></td><td>Search tolerance as fraction of mesh size (default 1e-3)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceToPatch [OPTIONS] &lt;surfaceFile&gt;
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -faceSet &lt;name&gt;   Only repatch the faces in specified faceSet
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -tol &lt;scalar&gt;     Search tolerance as fraction of mesh size (default 1e-3)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Reads surface and applies surface regioning to a mesh

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceToPatch/surfaceToPatch.C">源码与说明</a> · <a href="/assets/command-help/surfacetopatch.txt">帮助文本</a></p>
