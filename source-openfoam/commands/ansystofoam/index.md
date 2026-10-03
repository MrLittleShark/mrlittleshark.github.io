---
title: "ansysToFoam · 将支持的 ANSYS 网格文件转换为 OpenFOAM 体网格"
layout: reference
description: "将支持的 ANSYS 网格文件转换为 OpenFOAM 体网格。"
cms_slug: "command-ansystofoam"
---

<p>将支持的 ANSYS 网格文件转换为 OpenFOAM 体网格。</p><h2>开始前</h2>
<p>准备由 I-DEAS 导出的 ANSYS 网格输入文件，以及目标 OpenFOAM 案例；该转换器按这一网格格式读取数据。</p>
<h2>示例 1：导入米制网格</h2>
<pre><code class="language-bash">ansysToFoam mesh.ans
</code></pre>
<p>读取节点、单元和边界信息，在案例中生成 polyMesh。默认坐标缩放因子为 1，适用于输入已经采用米的情况。</p>
<h2>示例 2：导入毫米网格</h2>
<pre><code class="language-bash">ansysToFoam mesh-mm.ans -scale 0.001
</code></pre>
<p>将节点坐标乘 0.001。导入后在 checkMesh 的 bounding box 中核对长度，原 100 mm 应对应 0.1 m。</p>
<h2>示例 3：导入指定案例</h2>
<pre><code class="language-bash">ansysToFoam /data/mesh.ans -case ../ansysCase
checkMesh -case ../ansysCase -constant
</code></pre>
<p>从明确的输入路径读取，并把网格写入 ansysCase。检查器报告单元类型、质量和边界数量，可定位转换后的连接问题。</p>
<h2>示例 4：调整导入后的边界组织</h2>
<pre><code class="language-bash">ansysToFoam mesh.ans
createPatch -overwrite
</code></pre>
<p>前提是 system/createPatchDict 已按转换得到的 patch 名称配置。第二步合并或重命名边界，形成求解器需要的 inlet、outlet、walls 等分区。</p>
<h2>示例 5：检查并优化网格编号</h2>
<pre><code class="language-bash">ansysToFoam mesh.ans -scale 0.001
checkMesh -constant -allTopology -allGeometry
renumberMesh -overwrite
</code></pre>
<p>先对转换结果做较全面的几何和拓扑检查，再重新编号以改善矩阵带宽。重新编号改变网格索引，已有按编号创建的集合应重新核对。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>设置几何缩放系数，默认为 1。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/ansysToFoam/Make/files">源码与说明</a> · <a href="/assets/command-help/ansystofoam.txt">帮助文本</a></p>
