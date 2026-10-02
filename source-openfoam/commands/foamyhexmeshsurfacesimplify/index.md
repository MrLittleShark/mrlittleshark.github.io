---
title: "foamyHexMeshSurfaceSimplify · 输出用于 triSurface 表面处理"
layout: reference
description: "输出用于 triSurface 表面处理。"
cms_slug: "command-foamyhexmeshsurfacesimplify"
---

<p>输出用于 triSurface 表面处理。</p><h2>开始前</h2>
<p>该开发工具需在本机可用；输入表面来自system/foamyHexMeshDict的geometry，两个位置参数为三方向采样数和输出表面名。</p>
<h2>示例 1：进行粗采样</h2>
<pre><code class="language-bash">foamyHexMeshSurfaceSimplify '(40 40 40)' body40.stl
</code></pre>
<p>以40×40×40采样设置重建表面，输出到constant/triSurface/body40.stl，适合初步检查轮廓。</p>
<h2>示例 2：提高表面分辨率</h2>
<pre><code class="language-bash">foamyHexMeshSurfaceSimplify '(80 80 80)' body80.stl
</code></pre>
<p>保持相同几何，将各方向采样数加倍；细节更充分，计算和表面数据量也增加。</p>
<h2>示例 3：按长轴增加采样</h2>
<pre><code class="language-bash">foamyHexMeshSurfaceSimplify '(120 40 40)' longBody.stl
</code></pre>
<p>适合x方向较长的几何，分方向设置采样数，避免各方向分辨率差距过大。</p>
<h2>示例 4：对比两个算例几何</h2>
<pre><code class="language-bash">foamyHexMeshSurfaceSimplify -case ../variant '(80 80 80)' variant80.stl
</code></pre>
<p>读取variant的几何与控制配置，把重采样结果保存在该算例中。</p>
<h2>示例 5：检查重建表面</h2>
<pre><code class="language-bash">foamyHexMeshSurfaceSimplify '(80 80 80)' rebuilt.stl
surfaceCheck constant/triSurface/rebuilt.stl
</code></pre>
<p>重建后检查闭合性、面数和包围盒，再决定是否用于后续网格生成。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/foamyMesh/foamyHexMeshSurfaceSimplify/foamyHexMeshSurfaceSimplify_non_octree.C">源码与说明</a> · <a href="/assets/command-help/foamyhexmeshsurfacesimplify.txt">帮助文本</a></p>
