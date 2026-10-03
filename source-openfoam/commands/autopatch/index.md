---
title: "autoPatch · 根据面法向夹角自动将外边界划分为多个 patch"
layout: reference
description: "根据面法向夹角自动将外边界划分为多个 patch。"
cms_slug: "command-autopatch"
---

<p>根据面法向夹角自动将外边界划分为多个 patch。</p><h2>开始前</h2>
<p>已有体网格外边界；工具按外表面折角划分 patch。每个角度对比示例应从同一原始网格的独立副本开始。</p>
<h2>示例 1：按常见特征角分区</h2>
<pre><code class="language-bash">autoPatch 45
</code></pre>
<p>使用 45° 特征角划分外部面，默认写入新的网格实例。按 patch 着色查看入口、出口和壁面是否形成可识别区域。</p>
<h2>示例 2：识别较小折角</h2>
<pre><code class="language-bash">autoPatch 20
</code></pre>
<p>较小阈值会保留更多细微折角，通常产生更多区域。适合检查浅台阶和小倒角，同时关注曲面三角离散带来的过度分区。</p>
<h2>示例 3：只保留较明显棱边</h2>
<pre><code class="language-bash">autoPatch 80
</code></pre>
<p>较大阈值强调明显的形状转折。与 45° 方案比较 patch 数量，确认重要物理边界仍可区分。</p>
<h2>示例 4：更新案例副本并检查</h2>
<pre><code class="language-bash">autoPatch 45 -overwrite
checkMesh -constant
</code></pre>
<p>直接在副本原网格位置写入分区结果。随后更新场文件中的边界名称和条件，保持与新 boundary 文件一致。</p>
<h2>示例 5：为新分区赋予物理名称</h2>
<pre><code class="language-bash">autoPatch 45 -overwrite
createPatch -overwrite
</code></pre>
<p>先按几何分区，再根据实际结果编写 createPatchDict，把相关 patch 合并或命名为 inlet、outlet、walls。两步之间需检查自动生成的名称和空间位置。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-overwrite</code></td><td>覆盖已有网格或结果文件。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/autoPatch/autoPatch.C">源码与说明</a> · <a href="/assets/command-help/autopatch.txt">帮助文本</a></p>
