---
title: "foamyHexMeshBackgroundMesh · 为 foamyHexMesh 提供背景网格"
layout: reference
description: "为 foamyHexMesh 提供背景网格。"
cms_slug: "command-foamyhexmeshbackgroundmesh"
---

<p>为 foamyHexMesh 提供背景网格。</p><h2>开始前</h2>
<p>该开发工具需在本机可用；使用完整foamyHexMeshDict及表面几何，输出用于检查背景网格与距离表面。</p>
<h2>示例 1：生成几何表示</h2>
<pre><code class="language-bash">foamyHexMeshBackgroundMesh
</code></pre>
<p>根据foamy尺寸定义构造背景网格并计算表面距离表示，查看日志中的细化与表面输出位置。</p>
<h2>示例 2：保留网格和距离场</h2>
<pre><code class="language-bash">foamyHexMeshBackgroundMesh -writeMesh
</code></pre>
<p>同时写出背景网格及cellDistance、pointDistance，便于显示零距离附近的几何表示。</p>
<h2>示例 3：调整合并容差</h2>
<pre><code class="language-bash">foamyHexMeshBackgroundMesh -writeMesh -mergeTol 1e-7
</code></pre>
<p>将合并距离设为包围盒尺寸的1e-7，用于比较较近几何点是否被过早合并。</p>
<h2>示例 4：比较更细背景尺度</h2>
<pre><code class="language-bash">foamDictionary system/foamyHexMeshDict -entry motionControl.defaultCellSize -set 0.002
foamyHexMeshBackgroundMesh -writeMesh
</code></pre>
<p>已有完整配置时将基准尺寸改为2mm，检查狭小特征的距离场是否得到更好表达。</p>
<h2>示例 5：处理另一组表面</h2>
<pre><code class="language-bash">foamyHexMeshBackgroundMesh -case ../geometryStudy -writeMesh
</code></pre>
<p>geometryStudy中使用另一组geometry或局部尺度，输出其背景网格，供不同几何方案对照。</p>
<details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 command reference
Command: foamyHexMeshBackgroundMesh
Evidence: not-installed
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/foamyMesh/foamyHexMeshBackgroundMesh/foamyHexMeshBackgroundMesh.C

未取得运行时帮助。

源码路径：applications/utilities/mesh/generation/foamyMesh/foamyHexMeshBackgroundMesh/foamyHexMeshBackgroundMesh.C

Writes out background mesh as constructed by foamyHexMesh and constructs distanceSurface.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/foamyMesh/foamyHexMeshBackgroundMesh/foamyHexMeshBackgroundMesh.C">源码与说明</a> · <a href="/assets/command-help/foamyhexmeshbackgroundmesh.txt">帮助文本</a></p>
