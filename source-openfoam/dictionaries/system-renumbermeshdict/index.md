---
title: "system/renumberMeshDict"
layout: "reference"
description: "renumberMethod 指定网格编号算法，如 CuthillMcKee；算法参数置于对应系数字典。运行 renumberMesh -list-renumber 可查询可用方法。重新编号用于调整稀疏矩阵带宽，网格几何分辨率保持不变。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/renumberMeshDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>renumberMethod</code> · <code>CuthillMcKee</code></p><h2>关联命令</h2><p><a href="/commands/?q=renumberMesh">renumberMesh</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/renumberMeshDict -keywords
renumberMesh -help</code></pre><h2>8.5 system/renumberMeshDict 与文件处理器</h2><p>renumberMethod 指定网格编号算法，如 CuthillMcKee；算法参数置于对应系数字典。运行 renumberMesh -list-renumber 可查询可用方法。重新编号用于调整稀疏矩阵带宽，网格几何分辨率保持不变。</p>
<p>FOAM_FILEHANDLER 设置默认文件处理器，常用值为 uncollated 和 collated；命令行 -fileHandler 可覆盖该设置。collated 通过合并并行 I/O 减少文件数量，其性能取决于文件系统、MPI 和缓冲策略。结果读取及重分配应使用支持该格式的工具。</p>
{% endraw %}