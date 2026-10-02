---
title: "ccmToFoam · 需编译 CCM 支持"
layout: reference
description: "需编译 CCM 支持。-list 列出文件内容，移除该选项后执行转换。"
cms_slug: "command-ccmtofoam"
---

<p>需编译 CCM 支持。-list 列出文件内容，移除该选项后执行转换。</p><h2>开始前</h2>
<p>安装带 CCM 支持的 OpenFOAM 工具，准备 STAR-CCM+ 导出的 .ccm 文件；操作在单独案例目录进行。</p>
<h2>示例 1：导入 CCM 网格</h2>
<pre><code class="language-bash">ccmToFoam mesh.ccm
</code></pre>
<p>读取几何并生成 OpenFOAM 网格。检查转换日志中的区域、界面和边界名称，再配置物理场。</p>
<h2>示例 2：先查看区域与接口信息</h2>
<pre><code class="language-bash">ccmToFoam mesh.ccm -list
</code></pre>
<p>只列出 cellTable、boundaryRegion 和接口等几何信息后退出。先核对流固区域、边界名称与接口类型，再选择实际导入时的处理选项。</p>
<h2>示例 3：保留固体单元</h2>
<pre><code class="language-bash">ccmToFoam mesh.ccm -solids
</code></pre>
<p>将输入中的固体单元也保留到导入网格中。随后按 cellZone 划分流体和固体区域，配置多区域求解所需的材料参数。</p>
<h2>示例 4：合并就地接口</h2>
<pre><code class="language-bash">ccmToFoam mesh.ccm -merge
</code></pre>
<p>对可按原位置合并的接口执行合并。完成后检查内部面和 patch 数量，确认原本应连通的区域已经连接。</p>
<h2>示例 5：明确单位和输出格式</h2>
<pre><code class="language-bash">ccmToFoam mesh-mm.ccm -scale 0.001 -ascii -numbered
</code></pre>
<p>输入毫米坐标换算为米，网格以 ASCII 保存，并使用编号式 patch/zone 名称。适合原始名称需要统一处理的导入流程，后续按日志建立名称对应关系。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/ccm/ccmToFoam/ccmToFoam.C">源码与说明</a> · <a href="/assets/command-help/ccmtofoam.txt">帮助文本</a></p>
