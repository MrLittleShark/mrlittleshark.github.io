---
title: "ensightToFoam · 转换范围为几何网格，物理模型在目标算例中配置"
layout: reference
description: "转换范围为几何网格，物理模型在目标算例中配置。"
cms_slug: "command-ensighttofoam"
---

<p>转换范围为几何网格，物理模型在目标算例中配置。</p><h2>开始前</h2>
<p>准备 EnSight Gold 几何 .geo 文件；转换几何后，求解器的初始场和数值设置需在案例中另行配置。</p>
<h2>示例 1：导入几何</h2>
<pre><code class="language-bash">ensightToFoam mesh.geo
</code></pre>
<p>读取 EnSight 几何并建立体网格。检查转换报告中的单元类型和区域数量。</p>
<h2>示例 2：导入毫米模型</h2>
<pre><code class="language-bash">ensightToFoam mesh.geo -scale 0.001
</code></pre>
<p>缩放节点坐标到米。导入后使用 checkMesh 核对边界框，与原始模型的实际尺寸对应。</p>
<h2>示例 3：合并几乎重合的顶点</h2>
<pre><code class="language-bash">ensightToFoam mesh.geo -mergeTol 1e-6
</code></pre>
<p>使用相对模型包围盒尺度的合并容差，处理分块几何中的近重合点。检查接缝是否连接，同时核对细小间隙是否保留。</p>
<h2>示例 4：保留输入单元的手性</h2>
<pre><code class="language-bash">ensightToFoam mesh.geo -keepHandedness
</code></pre>
<p>保留输入单元方向而关闭自动方向调整，适用于已经确认输入连接顺序符合预期的网格。随后检查负体积和面方向。</p>
<h2>示例 5：在副本组合缩放与合并</h2>
<pre><code class="language-bash">ensightToFoam /data/mesh.geo -case ../ensightCase -scale 0.001 -mergeTol 1e-7
checkMesh -case ../ensightCase -constant -allTopology
</code></pre>
<p>在独立案例内同时处理单位和小接缝。通过连接检查确认各部分构成预期流体域，再继续设置边界条件。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-keepHandedness</code></td><td>保留反向单元的原始朝向；默认会进行几何检查并翻转这类单元。</td></tr><tr><td><code>-mergeTol &lt;factor&gt;</code></td><td>设置点合并容差，以包围盒尺寸的比例表示；设为 0 时保留各点。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>设置几何缩放系数，默认为 1。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/ensightToFoam/ensightMeshReader.C">源码与说明</a> · <a href="/assets/command-help/ensighttofoam.txt">帮助文本</a></p>
