---
title: "foamListRegions · 列出算例中的体网格区域或有限面积区域"
layout: reference
description: "列出算例中的体网格区域或有限面积区域。"
cms_slug: "command-foamlistregions"
---

<p>列出算例中的体网格区域或有限面积区域。</p><h2>开始前</h2>
<p>体区域名称与分类来自 constant/regionProperties；有限面积区域来自 constant/finite-area/regionProperties。</p>
<h2>示例 1：列出全部体区域</h2>
<pre><code class="language-bash">foamListRegions
</code></pre>
<p>读取区域清单并输出各区域名，便于核对多区域目录。</p>
<h2>示例 2：只列流体区域</h2>
<pre><code class="language-bash">foamListRegions fluid
</code></pre>
<p>选择名为 fluid 的分类，输出其中的区域，例如 air、water；分类名称以字典实际内容为准。</p>
<h2>示例 3：只列固体区域</h2>
<pre><code class="language-bash">foamListRegions solid
</code></pre>
<p>输出 solid 分类下的 heater 等区域，可据此逐个检查固体材料设置。</p>
<h2>示例 4：读取有限面积区域</h2>
<pre><code class="language-bash">foamListRegions -finite-area
</code></pre>
<p>切换到有限面积区域清单，用于薄膜、壳体等面积网格的区域管理。</p>
<h2>示例 5：兼容单区域与多区域目录</h2>
<pre><code class="language-bash">foamListRegions -case ../candidateCase -optional -verbose
</code></pre>
<p>显式选择算例并显示读取细节；缺少 regionProperties 时允许继续，适合批量检查不同算例。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dry-run</code></td><td>允许配置文件缺失，并显示更详细的信息。</td></tr><tr><td><code>-finite-area</code></td><td>列出 constant/finite-area/regionProperties 中的区域（文件存在时）。</td></tr><tr><td><code>-optional</code></td><td>允许 regionProperties 文件缺失。</td></tr><tr><td><code>-verbose</code></td><td>显示更详细的输出。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamListRegions/foamListRegions.C">源码与说明</a> · <a href="/assets/command-help/foamlistregions.txt">帮助文本</a></p>
