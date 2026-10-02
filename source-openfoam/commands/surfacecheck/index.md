---
title: "surfaceCheck · 检查三角化表面的范围、连通性和质量"
layout: reference
description: "检查三角化表面的范围、连通性和质量。"
cms_slug: "command-surfacecheck"
---

<p>检查三角化表面的范围、连通性和质量。</p><h2>开始前</h2>
<p>输入为STL、OBJ等支持的表面；检查会输出统计，部分选项还生成问题集合或分割结果。</p>
<h2>示例 1：检查基本质量</h2>
<pre><code class="language-bash">surfaceCheck body.stl
</code></pre>
<p>查看点数、三角面数、包围盒、开边及区域数，先确认几何尺度和闭合状态。</p>
<h2>示例 2：检查自相交</h2>
<pre><code class="language-bash">surfaceCheck -checkSelfIntersection body.stl
</code></pre>
<p>额外检测相互穿过的三角形，适合CAD修补或表面平滑之后检查。</p>
<h2>示例 3：输出缺陷集合</h2>
<pre><code class="language-bash">surfaceCheck -checkSelfIntersection -writeSets vtk body.stl
</code></pre>
<p>把问题三角形或边转换为VTK数据，便于在ParaView定位具体缺陷。</p>
<h2>示例 4：限制诊断文件数量</h2>
<pre><code class="language-bash">surfaceCheck -outputThreshold 0 body.stl
</code></pre>
<p>输出统计但抑制诊断文件写出，适合只需快速读取质量信息的大型表面。</p>
<h2>示例 5：识别并拆分非流形连接</h2>
<pre><code class="language-bash">surfaceCheck -splitNonManifold -writeSets vtk body.stl
</code></pre>
<p>针对多重连接边检查并分开相应表面连接，查看分割结果后再确定所需几何拓扑。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-blockMesh</code></td><td>Write vertices/blocks for blockMeshDict</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-verbose</code></td><td>Additional verbosity (can be used multiple times) Reconstruct and write problem triangles/edges in selected format</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceCheck [OPTIONS] &lt;input&gt;
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
