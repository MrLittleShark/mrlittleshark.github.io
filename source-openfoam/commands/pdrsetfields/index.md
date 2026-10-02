---
title: "PDRsetFields · 把几何障碍物转换成 PDRFoam 所需的等效阻塞场"
layout: reference
description: "把几何障碍物转换成 PDRFoam 所需的等效阻塞场。"
cms_slug: "command-pdrsetfields"
---

<p>把几何障碍物转换成 PDRFoam 所需的等效阻塞场。</p><h2>开始前</h2>
<p>已有PDR网格、障碍物输入和 system/PDRsetFieldsDict；几何尺度与网格单位一致。</p>
<h2>示例 1：先预览障碍物</h2>
<pre><code class="language-bash">PDRsetFields -dry-run
</code></pre>
<p>读取障碍物并写VTK预览，适合核对位置、尺寸和物体组，再生成阻塞场。</p>
<h2>示例 2：生成等效阻塞字段</h2>
<pre><code class="language-bash">PDRsetFields
</code></pre>
<p>按默认字典处理几何障碍物，计算对应网格上的等效阻塞影响，供PDRFoam使用。</p>
<h2>示例 3：使用另一障碍物方案</h2>
<pre><code class="language-bash">PDRsetFields -dict system/PDRsetFields-denseDict
</code></pre>
<p>替代字典描述更密集的障碍物布置；在案例副本中比较生成场的空间分布。</p>
<h2>示例 4：在指定时间初始化</h2>
<pre><code class="language-bash">PDRsetFields -time 0
</code></pre>
<p>明确把设置作用于0时刻，适合统一初始场目录的自动化流程。</p>
<h2>示例 5：读取旧式障碍物表</h2>
<pre><code class="language-bash">PDRsetFields -legacy -dict system/PDRsetFields-legacyDict -dry-run
</code></pre>
<p>输入确为legacy表时用-legacy强制该读取方式；先用VTK确认解析出的障碍物。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 PDRsetFieldsDict 文件。</td></tr><tr><td><code>-dry-run</code></td><td>仅读取障碍物并输出 VTK。</td></tr><tr><td><code>-legacy</code></td><td>强制使用旧式障碍物表格。</td></tr><tr><td><code>-time &lt;time&gt;</code></td><td>指定时间。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/PDR/PDRsetFields/PDRsetFields.C">源码与说明</a> · <a href="/assets/command-help/pdrsetfields.txt">帮助文本</a></p>
