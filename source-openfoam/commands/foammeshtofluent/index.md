---
title: "foamMeshToFluent · 将 OpenFOAM 体网格导出为 Fluent 网格文件"
layout: reference
description: "将 OpenFOAM 体网格导出为 Fluent 网格文件。"
cms_slug: "command-foammeshtofluent"
---

<p>将 OpenFOAM 体网格导出为 Fluent 网格文件。</p><h2>开始前</h2>
<p>案例已有体网格；该工具导出 Fluent 网格，输出文件位置以终端报告为准。场结果的交换需要另选结果导出工具。</p>
<h2>示例 1：导出已有网格</h2>
<pre><code class="language-bash">foamMeshToFluent
</code></pre>
<p>读取当前案例的网格，生成 Fluent .msh 文件。接收端读取后应核对长度单位和边界区域。</p>
<h2>示例 2：从 blockMesh 建网格后导出</h2>
<pre><code class="language-bash">blockMesh
checkMesh -constant
foamMeshToFluent
</code></pre>
<p>先生成结构化块网格，再检查并导出。适合使用 OpenFOAM 的 blockMesh 建网格、在 Fluent 中进行后续计算。</p>
<h2>示例 3：导出指定案例</h2>
<pre><code class="language-bash">foamMeshToFluent -case ../channel
</code></pre>
<p>在当前目录直接指定 channel 案例，输出网格对应该案例。查看日志中的文件路径，避免把其他案例的导出文件混用。</p>
<h2>示例 4：整理边界后导出</h2>
<pre><code class="language-bash">createPatch -overwrite
foamMeshToFluent
</code></pre>
<p>前提是 createPatchDict 已定义目标分组。先合并或命名入口、出口和壁面，导出的 Fluent 边界区域更便于分配物理条件。</p>
<h2>示例 5：重新编号后导出</h2>
<pre><code class="language-bash">renumberMesh -overwrite
checkMesh -constant
foamMeshToFluent
</code></pre>
<p>在案例副本中重新编号，再导出通过检查的网格。几何形状保持不变，输出连接编号随之更新，适合比较外部软件读取与计算效率。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/foamMeshToFluent/fluentFvMesh.C">源码与说明</a> · <a href="/assets/command-help/foammeshtofluent.txt">帮助文本</a></p>
