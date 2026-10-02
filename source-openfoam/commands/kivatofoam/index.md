---
title: "kivaToFoam · 输入为 KIVA3v 发动机网格"
layout: reference
description: "输入为 KIVA3v 发动机网格。"
cms_slug: "command-kivatofoam"
---

<p>输入为 KIVA3v 发动机网格。</p><h2>开始前</h2>
<p>准备 KIVA3 或 KIVA3v 网格文件；目标案例是独立副本，转换后需核对缸体、活塞及缸盖边界。</p>
<h2>示例 1：导入默认文件</h2>
<pre><code class="language-bash">kivaToFoam
</code></pre>
<p>从当前目录读取 otape17，默认采用 KIVA3v 处理方式。日志显示各类边界和单元数量。</p>
<h2>示例 2：指定输入文件</h2>
<pre><code class="language-bash">kivaToFoam -file engine.otape17
</code></pre>
<p>读取明确命名的网格，便于同时保存不同曲轴位置或不同几何版本的输入。</p>
<h2>示例 3：导入 KIVA3 格式</h2>
<pre><code class="language-bash">kivaToFoam -file engine3.otape17 -version kiva3
</code></pre>
<p>选择 KIVA3 解析路径。版本参数应与输入文件格式一致，转换后核对活塞和缸套相关边界。</p>
<h2>示例 4：显式选择 KIVA3v</h2>
<pre><code class="language-bash">kivaToFoam -file engine3v.otape17 -version kiva3v -case ../engineCase
</code></pre>
<p>把 KIVA3v 网格转换到 engineCase。适合在多个发动机案例之间明确输入版本与目标目录。</p>
<h2>示例 5：调整缸盖边界识别高度</h2>
<pre><code class="language-bash">kivaToFoam -file engine.otape17 -zHeadMin 0.1
checkMesh -constant
</code></pre>
<p>按 z 高度阈值把相应缸套面转入缸盖分组；0.1 应按输入几何坐标确定。检查转换后的缸盖范围和网格质量。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-file &lt;name&gt;</code></td><td>指定输入文件名，默认为 otape17。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-version &lt;version&gt;</code></td><td>指定 KIVA 版本 kiva3 或 kiva3v，默认采用 3v。</td></tr><tr><td><code>-zHeadMin &lt;scalar&gt;</code></td><td>设置将缸套面归入缸盖的最低 z 坐标。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（10 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/kivaToFoam/kivaToFoam.C">源码与说明</a> · <a href="/assets/command-help/kivatofoam.txt">帮助文本</a></p>
