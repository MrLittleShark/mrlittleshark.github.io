---
title: "surfaceMeshImport · 将外部表面网格导入为 OpenFOAM 的 surfMesh"
layout: reference
description: "将外部表面网格导入为 OpenFOAM 的 surfMesh。"
cms_slug: "command-surfacemeshimport"
---

<p>将外部表面网格导入为 OpenFOAM 的 surfMesh。</p><h2>开始前</h2>
<p>准备表面文件和包含 system/controlDict 的案例目录；命名导入可在同一案例保存多个 surfMesh。</p>
<h2>示例 1：导入默认表面</h2>
<pre><code class="language-bash">surfaceMeshImport body.stl
</code></pre>
<p>将 STL 转为案例内的 surfMesh 存储。随后 surfaceMeshExport body.obj 可将这一表面重新导出检查。</p>
<h2>示例 2：给表面指定名称</h2>
<pre><code class="language-bash">surfaceMeshImport blade.obj -name blade
</code></pre>
<p>以 blade 为名称保存表面，之后通过 surfaceMeshExport -name blade 选择它。适合分开管理多个零件。</p>
<h2>示例 3：导入毫米模型</h2>
<pre><code class="language-bash">surfaceMeshImport body-mm.stl -read-scale 0.001 -name body
</code></pre>
<p>读取时将坐标换算为米，再保存为 body 表面。查看终端边界框，应与目标计算域尺寸一致。</p>
<h2>示例 4：清理后导入</h2>
<pre><code class="language-bash">surfaceMeshImport body.obj -clean -name bodyClean
</code></pre>
<p>对输入表面执行清理再存储。对照原始与导出文件的点、面数量，确认清理处理了哪些实体。</p>
<h2>示例 5：从局部坐标导入另一案例</h2>
<pre><code class="language-bash">surfaceMeshImport blade.obj -case ../surfaceCase -name blade -from local
</code></pre>
<p>从指定案例的坐标系字典读取 local，将局部几何变换到案例坐标。导出检查叶片原点及轴向是否符合装配位置。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-clean</code></td><td>对输入表面执行检查与清理。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 coordinateSystems 文件。</td></tr><tr><td><code>-from &lt;system&gt;</code></td><td>指定源坐标系；在 -read-scale 缩放后应用。</td></tr><tr><td><code>-name &lt;name&gt;</code></td><td>指定写出的表面名称，默认为 default。</td></tr><tr><td><code>-noFunctionObjects</code></td><td>跳过函数对象的执行。</td></tr><tr><td><code>-read-format &lt;type&gt;</code></td><td>指定输入格式；默认由文件扩展名判断。</td></tr><tr><td><code>-read-scale &lt;factor&gt;</code></td><td>设置输入几何的缩放系数。</td></tr><tr><td><code>-to &lt;system&gt;</code></td><td>指定目标坐标系；在 -write-scale 缩放前应用。</td></tr><tr><td><code>-verbose</code></td><td>显示更详细的输出；可重复使用以增加详细程度。</td></tr><tr><td><code>-write-scale &lt;factor&gt;</code></td><td>设置输出几何的缩放系数。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（11 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceMeshImport/surfaceMeshImport.C">源码与说明</a> · <a href="/assets/command-help/surfacemeshimport.txt">帮助文本</a></p>
