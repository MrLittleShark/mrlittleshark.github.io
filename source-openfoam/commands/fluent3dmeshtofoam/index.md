---
title: "fluent3DMeshToFoam · 将 Fluent 三维网格文件转换为 OpenFOAM 体网格"
layout: reference
description: "将 Fluent 三维网格文件转换为 OpenFOAM 体网格。"
cms_slug: "command-fluent3dmeshtofoam"
---

<p>将 Fluent 三维网格文件转换为 OpenFOAM 体网格。</p><h2>开始前</h2>
<p>准备三维 Fluent 网格文件；由 Cubit 生成的同类文件可使用专用选项。组名必须与输入网格实际名称一致。</p>
<h2>示例 1：导入三维 Fluent 网格</h2>
<pre><code class="language-bash">fluent3DMeshToFoam mesh.msh
</code></pre>
<p>建立体网格以及输入定义的边界分组。查看转换日志中 cell group 和 face group 的对应关系。</p>
<h2>示例 2：导入 Cubit 导出文件</h2>
<pre><code class="language-bash">fluent3DMeshToFoam cubit.msh -cubit
</code></pre>
<p>启用针对 Cubit 文件的处理路径。转换后核对单元数量及边界组，适合使用 Cubit 建网格的工作流程。</p>
<h2>示例 3：转换毫米坐标</h2>
<pre><code class="language-bash">fluent3DMeshToFoam mesh.msh -scale 0.001
</code></pre>
<p>将输入坐标换算为米。与 Fluent 界面显示单位不同，转换器使用的是文件里的实际数值，需在 checkMesh 中核对。</p>
<h2>示例 4：跳过指定单元组</h2>
<pre><code class="language-bash">fluent3DMeshToFoam mesh.msh -ignoreCellGroups '(solidSupport)'
</code></pre>
<p>前提是输入含名为 solidSupport 的可排除单元组。导入时跳过该组，随后核对保留单元数及由此产生的边界。</p>
<h2>示例 5：跳过指定面组并检查</h2>
<pre><code class="language-bash">fluent3DMeshToFoam mesh.msh -ignoreFaceGroups '(auxFaces)' -case ../fluentTest
checkMesh -case ../fluentTest -constant -allTopology
</code></pre>
<p>适用于已确认 auxFaces 属于可忽略辅助数据的输入。检查真实外边界是否仍完整，保留求解所需的面分区。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-cubit</code></td><td>采用针对异常 Cubit 文件的特殊解析方式。</td></tr><tr><td><code>-ignoreCellGroups &lt;names&gt;</code></td><td>指定要忽略的单元组。</td></tr><tr><td><code>-ignoreFaceGroups &lt;names&gt;</code></td><td>指定要忽略的面组。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>设置几何缩放系数，默认为 1。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/fluent3DMeshToFoam/Make/files">源码与说明</a> · <a href="/assets/command-help/fluent3dmeshtofoam.txt">帮助文本</a></p>
