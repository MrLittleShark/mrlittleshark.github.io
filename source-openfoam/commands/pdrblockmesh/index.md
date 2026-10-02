---
title: "PDRblockMesh · 读取 PDRblockMeshDict"
layout: reference
description: "读取 PDRblockMeshDict。"
cms_slug: "command-pdrblockmesh"
---

<p>读取 PDRblockMeshDict。</p><h2>开始前</h2>
<p>准备system/PDRblockMeshDict，其中包含x/y/z坐标分段、单元数与边界定义；生成操作在工作副本中进行。</p>
<h2>示例 1：生成直角分段网格</h2>
<pre><code class="language-bash">PDRblockMesh
</code></pre>
<p>按三个方向的坐标段生成网格，默认写入constant/polyMesh，日志给出单元数。</p>
<h2>示例 2：预览等价blockMesh配置</h2>
<pre><code class="language-bash">PDRblockMesh -print-dict
</code></pre>
<p>打印等价的blockMeshDict后退出，便于理解分段坐标怎样对应块和边界。</p>
<h2>示例 3：保存等价字典</h2>
<pre><code class="language-bash">PDRblockMesh -write-dict
</code></pre>
<p>写出system/blockMeshDict.PDRblockMesh后退出，可用它与手工blockMesh配置对照。</p>
<h2>示例 4：比较细网格定义</h2>
<pre><code class="language-bash">PDRblockMesh -dict system/PDRblockMeshDict.fine -time 1
</code></pre>
<p>已有完整fine字典时将其网格写到指定时间1，保留constant中的基准网格以便比较。</p>
<h2>示例 5：只生成主体区域</h2>
<pre><code class="language-bash">PDRblockMesh -no-outer
checkMesh -constant
</code></pre>
<p>字典另含外部扩展区域时跳过外部区域，随后检查主体网格尺寸、边界与质量。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 PDRblockMeshDict 文件。</td></tr><tr><td><code>-no-clean</code></td><td>保留 polyMesh/ 目录及已有文件。</td></tr><tr><td><code>-no-outer</code></td><td>仅创建内部区域。</td></tr><tr><td><code>-print-dict</code></td><td>输出等效的 blockMeshDict 内容并退出。</td></tr><tr><td><code>-time &lt;time&gt;</code></td><td>指定网格写入的时间目录，默认为 constant。</td></tr><tr><td><code>-write-dict</code></td><td>写出 system/blockMeshDict.PDRblockMesh 并退出。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/PDRblockMesh/box0">mesh/PDRblockMesh/box0</a></li></ul><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/PDRblockMesh/PDRblockMesh.C">源码与说明</a> · <a href="/assets/command-help/pdrblockmesh.txt">帮助文本</a></p>
