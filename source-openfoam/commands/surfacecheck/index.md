---
title: "surfaceCheck · 检查三角化表面的范围、连通性和质量"
layout: reference
description: "检查三角化表面的范围、连通性和质量。"
cms_slug: "command-surfacecheck"
---

<p>检查三角化表面的范围、连通性和质量。</p><h2>检查 STL 文件</h2>
<pre><code class="language-bash">surfaceCheck constant/triSurface/body.stl
</code></pre>
<p>把 <code>body.stl</code> 换成实际文件。关注包围盒是否符合单位、表面是否封闭以及是否存在多个不连通区域。</p>
<h2>保存检查记录</h2>
<pre><code class="language-bash">surfaceCheck constant/triSurface/body.stl &gt; log.surfaceCheck 2&gt;&amp;1
less log.surfaceCheck
</code></pre>
<p>日志适合与修复后的表面比较。CFD 封闭流体域还要求各边界面组合形成完整包围面。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-blockMesh</td><td>Write vertices/blocks for blockMeshDict</td></tr><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-verbose</td><td>Additional verbosity (can be used multiple times) Reconstruct and write problem triangles/edges in selected format</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceCheck [OPTIONS] &lt;input&gt;
Arguments:
  &lt;input&gt;           The input surface file
Options:
  -blockMesh        Write vertices/blocks for blockMeshDict
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -checkSelfIntersection
                    Also check for self-intersection
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
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -outputThreshold &lt;number&gt;
                    Upper limit on the number of files written. Default is 10,
                    using 0 suppresses file writing.
  -splitNonManifold
                    Split surface along non-manifold edges (default split is
                    fully disconnected)
  -verbose          Additional verbosity (can be used multiple times)
  -writeSets &lt;surfaceFormat&gt;
                    Reconstruct and write problem triangles/edges in selected
                    format
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Check geometric and topological quality of a surface

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceCheck/surfaceCheck.C">源码与说明</a> · <a href="/assets/command-help/surfacecheck.txt">帮助文本</a></p>
