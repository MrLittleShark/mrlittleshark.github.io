---
title: "plot3dToFoam · -singleBlock 和 -2D 等选项用于指定输入网格形式"
layout: reference
description: "-singleBlock 和 -2D 等选项用于指定输入网格形式。"
cms_slug: "command-plot3dtofoam"
---

<p>-singleBlock 和 -2D 等选项用于指定输入网格形式。</p><h2>开始前</h2>
<p>准备 ASCII 格式 Plot3D 几何文件，确认文件是单块还是多块、是否包含 iblank 数据。</p>
<h2>示例 1：导入多块几何</h2>
<pre><code class="language-bash">plot3dToFoam mesh.xyz
</code></pre>
<p>按默认多块格式读取，生成 OpenFOAM 网格。检查各块相邻界面的连接情况。</p>
<h2>示例 2：读取单块格式</h2>
<pre><code class="language-bash">plot3dToFoam single.xyz -singleBlock
</code></pre>
<p>输入文件使用单块格式时添加此选项，避免把块尺寸行误读为块数量。</p>
<h2>示例 3：读取不含空白标志的数据</h2>
<pre><code class="language-bash">plot3dToFoam mesh.xyz -noBlank
</code></pre>
<p>用于文件中没有 iblank 数据的情况。该选项控制输入记录的读取方式，应根据导出格式选择。</p>
<h2>示例 4：将二维数据处理为有限厚度</h2>
<pre><code class="language-bash">plot3dToFoam planar.xyz -2D 0.01 -noBlank
</code></pre>
<p>为二维网格指定 0.01 的厚度，输入应为无 iblank 的对应格式。检查前后边界和单元层数，再配置二维场边界。</p>
<h2>示例 5：组合格式与单位设置</h2>
<pre><code class="language-bash">plot3dToFoam single-mm.xyz -singleBlock -noBlank -scale 0.001
checkMesh -constant
</code></pre>
<p>读取单块、无 iblank 的毫米制输入，转换为米并检查网格。二维厚度如另行指定，也会随 -scale 一起缩放。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-2D &lt;thickness&gt;</code></td><td>指定二维网格的厚度，在几何缩放前应用。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noBlank</code></td><td>跳过空白项。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>设置几何缩放系数，默认为 1。</td></tr><tr><td><code>-singleBlock</code></td><td>按单块网格读取输入。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/plot3dToFoam/hexBlock.C">源码与说明</a> · <a href="/assets/command-help/plot3dtofoam.txt">帮助文本</a></p>
