---
title: "gambitToFoam · 将 GAMBIT 网格转换为 OpenFOAM 体网格"
layout: reference
description: "将 GAMBIT 网格转换为 OpenFOAM 体网格。"
cms_slug: "command-gambittofoam"
---

<p>将 GAMBIT 网格转换为 OpenFOAM 体网格。</p><h2>开始前</h2>
<p>准备 GAMBIT Neutral 网格文件；该输入与 Fluent .msh 文件采用不同的格式。</p>
<h2>示例 1：导入 Neutral 网格</h2>
<pre><code class="language-bash">gambitToFoam mesh.neu
</code></pre>
<p>读取中性格式中的节点、单元和边界分组，建立 OpenFOAM 网格。核对转换日志中的组名及单元数。</p>
<h2>示例 2：导入毫米模型</h2>
<pre><code class="language-bash">gambitToFoam mesh.neu -scale 0.001
</code></pre>
<p>节点坐标换算为米，便于直接使用 SI 制物性参数。检查 bounding box 是否与实际尺寸一致。</p>
<h2>示例 3：转换到目标案例并检查</h2>
<pre><code class="language-bash">gambitToFoam /data/mesh.neu -case ../gambitCase
checkMesh -case ../gambitCase -constant -allTopology
</code></pre>
<p>把网格写入指定案例并检查连接关系。关注多块网格之间是否出现意外的断开区域。</p>
<h2>示例 4：将分散边界归并</h2>
<pre><code class="language-bash">gambitToFoam mesh.neu
createPatch -overwrite
</code></pre>
<p>前提是 createPatchDict 已按导入 patch 名称配置。将同一物理壁面对应的多个分组归并，减少后续边界条件重复配置。</p>
<h2>示例 5：导出表面核对入口出口</h2>
<pre><code class="language-bash">gambitToFoam mesh.neu -scale 0.001
surfaceMeshExtract ports.obj -patches '(inlet outlet)' -constant
</code></pre>
<p>输入需包含 inlet 和 outlet 分组。单独导出两个端面，检查法向、面积和间距是否符合实际流动通道。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>设置几何缩放系数，默认为 1。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/gambitToFoam/Make/files">源码与说明</a> · <a href="/assets/command-help/gambittofoam.txt">帮助文本</a></p>
