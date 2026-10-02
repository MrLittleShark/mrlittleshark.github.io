---
title: "polyDualMesh · 把体网格转成保留几何特征的对偶多面体网格"
layout: reference
description: "把体网格转成保留几何特征的对偶多面体网格。"
cms_slug: "command-polydualmesh"
---

<p>把体网格转成保留几何特征的对偶多面体网格。</p><h2>开始前</h2>
<p>已有可转换的 polyMesh；featureAngle 以度表示。各比较案例使用相同原始网格副本。</p>
<h2>示例 1：按30度特征角生成对偶网格</h2>
<pre><code class="language-bash">polyDualMesh 30
</code></pre>
<p>位置参数30控制边界特征识别；程序沿特征边与patch边界构造对偶单元，输出新网格时间。</p>
<h2>示例 2：保留更细的几何转折</h2>
<pre><code class="language-bash">polyDualMesh 15
</code></pre>
<p>较小特征角把更多法向变化识别为特征，适合比较对偶网格对较缓转折的保留程度。</p>
<h2>示例 3：处理凹边附近的单元</h2>
<pre><code class="language-bash">polyDualMesh 30 -concaveMultiCells
</code></pre>
<p>在凹边界边附近允许生成多个单元，改善该位置的对偶拓扑表达，随后检查凹角网格。</p>
<h2>示例 4：让相邻单元之间保留多个面</h2>
<pre><code class="language-bash">polyDualMesh 30 -splitAllFaces
</code></pre>
<p>-splitAllFaces 允许相邻对偶单元之间存在多个面，适合研究对偶拓扑及面拆分方式。</p>
<h2>示例 5：忽略原 faceZone 保留并更新</h2>
<pre><code class="language-bash">polyDualMesh 30 -doNotPreserveFaceZones -overwrite
checkMesh
</code></pre>
<p>关闭默认的 faceZone 特殊保留策略，写回当前网格；用于不需要原面区约束的转换流程，随后检查网格。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-concaveMultiCells</code></td><td>将凹边界边处的单元拆分为多个单元。</td></tr><tr><td><code>-doNotPreserveFaceZones</code></td><td>关闭通过单元间多个面保留 faceZone 的默认行为。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-splitAllFaces</code></td><td>在单元之间保留多个面。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/polyDualMesh/meshDualiser.C">源码与说明</a> · <a href="/assets/command-help/polydualmesh.txt">帮助文本</a></p>
