---
title: "foamHasLibrary · -detail 输出详细信息"
layout: reference
description: "-detail 输出详细信息。"
cms_slug: "command-foamhaslibrary"
---

<p>-detail 输出详细信息。</p><h2>开始前</h2>
<p>共享库位于当前 OpenFOAM 或用户库搜索路径。工具用退出状态表示装载是否成功，适合编译后的依赖检查。</p>
<h2>示例 1：检查有限体积库</h2>
<pre><code class="language-bash">foamHasLibrary libfiniteVolume.so
</code></pre>
<p>尝试装载有限体积库；成功退出表示当前环境能够找到并加载它。</p>
<h2>示例 2：同时检查两个依赖</h2>
<pre><code class="language-bash">foamHasLibrary libfiniteVolume.so libmeshTools.so
</code></pre>
<p>默认要求两个库都能加载，适合检查依赖有限体积与网格工具的自定义程序。</p>
<h2>示例 3：显示加载细节</h2>
<pre><code class="language-bash">foamHasLibrary -detail -verbose libsampling.so
</code></pre>
<p>查看采样库的详细装载信息，帮助定位库文件或其依赖缺失。</p>
<h2>示例 4：检查任一候选实现</h2>
<pre><code class="language-bash">foamHasLibrary -or libcustomModelA.so libcustomModelB.so
</code></pre>
<p>已编译两个候选插件时，任一个可加载即可成功；两个名称都仍会检查。</p>
<h2>示例 5：在运行前验证自定义边界库</h2>
<pre><code class="language-bash">if foamHasLibrary libfoamLabPulsedInlet.so; then icoFoam; fi
</code></pre>
<p>在已配置该边界的算例中，仅在库加载成功后启动求解器。该检查关注装载，边界参数由求解器继续读取。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-detail</code></td><td>显示更多详细信息。</td></tr><tr><td><code>-or</code></td><td>任意一个库可加载即视为成功；仍会检查其余库。</td></tr><tr><td><code>-verbose</code></td><td>显示更详细的输出；可重复使用以增加详细程度。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamHasLibrary/foamHasLibrary.C">源码与说明</a> · <a href="/assets/command-help/foamhaslibrary.txt">帮助文本</a></p>
