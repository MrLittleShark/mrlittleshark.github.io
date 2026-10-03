---
title: "foamyQuadMesh · 生成以四边形为主的二维网格"
layout: reference
description: "生成以四边形为主的二维网格。"
cms_slug: "command-foamyquadmesh"
---

<p>生成以四边形为主的二维网格。</p><h2>开始前</h2>
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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/foamyQuadMesh/OpenCFD">mesh/foamyQuadMesh/OpenCFD</a></li></ul><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/foamyMesh/foamyQuadMesh/CV2D.C">源码与说明</a> · <a href="/assets/command-help/foamyquadmesh.txt">帮助文本</a></p>
