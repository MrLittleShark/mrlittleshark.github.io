---
title: "snappyRefineMesh · 输入为待处理表面及细化字典"
layout: reference
description: "输入为待处理表面及细化字典。"
cms_slug: "command-snappyrefinemesh"
---

<p>输入为待处理表面及细化字典。</p><h2>开始前</h2>
<p>准备适用于 snappyRefineMesh 的完整 system/snappyRefineMeshDict、背景网格及三角表面。该字典使用 surface、minEdgeLen、maxEdgeLen 等条目，与 snappyHexMeshDict 分别配置。</p>
<h2>示例 1：按现有表面细化设置运行</h2>
<pre><code class="language-bash">snappyRefineMesh
</code></pre>
<p>读取表面和细化规则，在表面附近逐步细分网格。日志给出每轮选中的单元及网格规模，可查看最终表面附近的分辨率。</p>
<h2>示例 2：减小目标最小边长</h2>
<pre><code class="language-bash">foamDictionary system/snappyRefineMeshDict -entry minEdgeLen -set 0.001
snappyRefineMesh
</code></pre>
<p>在全新背景网格副本中把细化停止相关的最小边长设为 0.001。长度使用网格坐标单位；与原方案比较近表面网格密度和单元总数。</p>
<h2>示例 3：设置单元规模阈值</h2>
<pre><code class="language-bash">foamDictionary system/snappyRefineMeshDict -entry cellLimit -set 200000
snappyRefineMesh
</code></pre>
<p>将细化流程的单元数量阈值设为 20 万。程序在细化前根据当前单元数与候选数量估计新增规模，并据此决定是否继续；日志会说明因数量阈值停止的情况。</p>
<h2>示例 4：选择内部和相交区域</h2>
<pre><code class="language-bash">foamDictionary system/snappyRefineMeshDict -entry nCutLayers -set 0
foamDictionary system/snappyRefineMeshDict -entry selectInside -set true
foamDictionary system/snappyRefineMeshDict -entry selectCut -set true
foamDictionary system/snappyRefineMeshDict -entry selectOutside -set false
snappyRefineMesh
</code></pre>
<p>以闭合表面内部为目标，保留内部及相交单元。outsidePoints 应位于表面外部，随后查看 selected 集合和最终边界。</p>
<h2>示例 5：保存中间细化网格</h2>
<pre><code class="language-bash">foamDictionary system/snappyRefineMeshDict -entry writeMesh -set true
snappyRefineMesh
checkMesh -latestTime
</code></pre>
<p>把中间细化阶段的网格也写到时间目录，便于逐步观察细化区域变化。最终用 checkMesh 检查最新网格。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/snappyRefineMesh/snappyRefineMesh.C">源码与说明</a> · <a href="/assets/command-help/snappyrefinemesh.txt">帮助文本</a></p>
