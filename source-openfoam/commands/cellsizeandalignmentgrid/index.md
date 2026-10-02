---
title: "cellSizeAndAlignmentGrid · 用于 foamyMesh 网格生成流程"
layout: reference
description: "用于 foamyMesh 网格生成流程。"
cms_slug: "command-cellsizeandalignmentgrid"
---

<p>用于 foamyMesh 网格生成流程。</p><h2>开始前</h2>
<p>该开发工具需在本机可用；读取system/foamyHexMeshDict的geometry、surfaceConformation和尺寸控制，使用独立foamy算例副本。</p>
<h2>示例 1：导出尺寸与方向控制数据</h2>
<pre><code class="language-bash">cellSizeAndAlignmentGrid
</code></pre>
<p>根据当前foamy定义生成constant中的points、sizes、alignments，分别记录采样点、目标尺寸和方向。</p>
<h2>示例 2：检查另一个几何方案</h2>
<pre><code class="language-bash">cellSizeAndAlignmentGrid -case ../foamyVariant
</code></pre>
<p>variant已包含完整几何和字典；导出该方案的控制数据，与原方案分别保存。</p>
<h2>示例 3：降低全局目标尺寸</h2>
<pre><code class="language-bash">foamDictionary system/foamyHexMeshDict -entry motionControl.defaultCellSize -set 0.003
cellSizeAndAlignmentGrid
</code></pre>
<p>在完整配置中将默认尺寸设为3mm，再生成sizes，观察远离局部加密区的尺度变化。</p>
<h2>示例 4：调整局部控制优先级</h2>
<pre><code class="language-bash">foamDictionary system/foamyHexMeshDict -entry motionControl.shapeControlFunctions.body.priority -set 2
cellSizeAndAlignmentGrid
</code></pre>
<p>前提已有body局部控制块；提高其优先级后重新导出，检查重叠控制区域采用的尺寸。</p>
<h2>示例 5：先检查控制再生成体网格</h2>
<pre><code class="language-bash">cellSizeAndAlignmentGrid
foamyHexMesh
</code></pre>
<p>先查看导出的控制场覆盖了几何细节，再用同一字典生成体网格；前者输出控制数据，后者生成实际单元。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/foamyMesh/cellSizeAndAlignmentGrid/cellSizeAndAlignmentGrid.C">源码与说明</a> · <a href="/assets/command-help/cellsizeandalignmentgrid.txt">帮助文本</a></p>
