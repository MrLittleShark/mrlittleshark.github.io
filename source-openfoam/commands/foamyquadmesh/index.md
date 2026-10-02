---
title: "foamyQuadMesh · 参数由专用字典定义，-pointsFile 可指定初始点"
layout: reference
description: "参数由专用字典定义，-pointsFile 可指定初始点。"
cms_slug: "command-foamyquadmesh"
---

<p>参数由专用字典定义，-pointsFile 可指定初始点。</p><h2>开始前</h2>
<p>已有system/foamyQuadMeshDict及所引用的闭合几何、特征边；二维平面由locationInMesh的z坐标确定。</p>
<h2>示例 1：生成平面网格</h2>
<pre><code class="language-bash">foamyQuadMesh
</code></pre>
<p>按默认字典生成二维Voronoi网格，查看边界贴合与短边过滤结果。</p>
<h2>示例 2：指定初始布点</h2>
<pre><code class="language-bash">foamyQuadMesh -pointsFile initialPoints
</code></pre>
<p>initialPoints为工具支持的点文件；使用相同初始点可比较不同平滑或尺寸设置的影响。</p>
<h2>示例 3：比较更小局部尺寸</h2>
<pre><code class="language-bash">foamDictionary system/foamyQuadMeshDict -entry motionControl.minCellSize -set 0.02
foamyQuadMesh
</code></pre>
<p>在副本中修改已有尺度参数后生成网格，重点比较狭缝和折角附近的单元分布。</p>
<h2>示例 4：处理独立几何副本</h2>
<pre><code class="language-bash">foamyQuadMesh -case ../letterMesh
</code></pre>
<p>letterMesh已有字典、STL及扩展特征边；结果保存在该副本，便于比较文字或复杂平面轮廓。</p>
<h2>示例 5：生成后拉伸成单层网格</h2>
<pre><code class="language-bash">foamyQuadMesh
extrude2DMesh polyMesh2D
</code></pre>
<p>前提已准备对应extrude2DMeshDict且前一步输出可用二维网格；第二步按厚度、层数生成求解用体网格。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyQuadMesh/OpenCFD">mesh/foamyQuadMesh/OpenCFD</a></li></ul><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamyQuadMesh [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
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
  -overwrite        Overwrite existing mesh/results files
  -pointsFile &lt;filename&gt;
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Conformal Voronoi 2D automatic mesh generator

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/foamyMesh/foamyQuadMesh/CV2D.C">源码与说明</a> · <a href="/assets/command-help/foamyquadmesh.txt">帮助文本</a></p>
