---
title: "fluentMeshToFoam · 输入采用 Fluent mesh 格式；Gmsh 文件使用 gmshToFoam 转换"
layout: reference
description: "输入采用 Fluent mesh 格式；Gmsh 文件使用 gmshToFoam 转换。"
cms_slug: "command-fluentmeshtofoam"
---

<p>输入采用 Fluent mesh 格式；Gmsh 文件使用 gmshToFoam 转换。</p><h2>开始前</h2>
<p>准备 Fluent 网格文件和 OpenFOAM 案例。二维网格需提供有限厚度，场文件中相应前后边界应与二维模型一致。</p>
<h2>示例 1：导入三维网格</h2>
<pre><code class="language-bash">fluentMeshToFoam mesh.msh
</code></pre>
<p>把 Fluent 的面和单元连接转换为 polyMesh。检查生成的边界分区名称，并将其用于初始场文件。</p>
<h2>示例 2：导入毫米网格</h2>
<pre><code class="language-bash">fluentMeshToFoam mesh.msh -scale 0.001
</code></pre>
<p>节点坐标乘 0.001；输入长度 1000 将变为 1 m。通过 checkMesh 的 bounding box 检查换算结果。</p>
<h2>示例 3：为二维网格指定厚度</h2>
<pre><code class="language-bash">fluentMeshToFoam mesh2d.msh -2D 0.01
</code></pre>
<p>将二维网格处理为厚度 0.01 的网格。厚度先按输入坐标给出；如果同时设置 -scale，它也会一起缩放。</p>
<h2>示例 4：保留单元区域</h2>
<pre><code class="language-bash">fluentMeshToFoam mesh.msh -writeZones
</code></pre>
<p>把相应单元分组写成 cellZone，供多孔区、旋转区或多区域拆分使用。转换后检查 cellZones 中的名称和单元数量。</p>
<h2>示例 5：同时生成集合用于后续选区</h2>
<pre><code class="language-bash">fluentMeshToFoam mesh.msh -writeZones -writeSets
checkMesh -constant
</code></pre>
<p>额外将区域和边界信息写为集合，便于 topoSet、局部网格修改等工具使用。集合内容应与转换日志中的分组一致。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-2D &lt;thickness&gt;</code></td><td>指定二维网格的厚度，在几何缩放前应用。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>设置几何缩放系数，默认为 1。</td></tr><tr><td><code>-writeSets</code></td><td>将单元区域与边界写为集合。</td></tr><tr><td><code>-writeZones</code></td><td>将单元区域写为 cellZone。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/fluentMeshToFoam/extrudedTriangleCellShape.C">源码与说明</a> · <a href="/assets/command-help/fluentmeshtofoam.txt">帮助文本</a></p>
