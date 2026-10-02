---
title: "setTurbulenceFields · 按经验关系和壁距初始化选定的湍流字段"
layout: reference
description: "按经验关系和壁距初始化选定的湍流字段。"
cms_slug: "command-setturbulencefields"
---

<p>按经验关系和壁距初始化选定的湍流字段。</p><h2>开始前</h2>
<p>已有速度、湍流模型及system/setTurbulenceFieldsDict；initialiseK、initialiseOmega等开关决定写哪些字段。</p>
<h2>示例 1：应用默认初始化方案</h2>
<pre><code class="language-bash">setTurbulenceFields
</code></pre>
<p>读取字典并初始化其中启用的U、k、epsilon、omega或R，输出相应字段统计。</p>
<h2>示例 2：为k–omega方案初始化</h2>
<pre><code class="language-bash">foamDictionary system/setTurbulenceFieldsDict -entry initialiseK -set true
foamDictionary system/setTurbulenceFieldsDict -entry initialiseOmega -set true
setTurbulenceFields
</code></pre>
<p>其余必要经验参数和模型已配置；启用k和omega初场写入，适合给k–omega模型准备一致的起始量。</p>
<h2>示例 3：为k–epsilon方案初始化</h2>
<pre><code class="language-bash">setTurbulenceFields -dict system/setTurbulenceFields-kepsilonDict
</code></pre>
<p>替代字典启用initialiseK与initialiseEpsilon，并提供相应经验参数；生成配套的k与epsilon。</p>
<h2>示例 4：写出辅助分布f</h2>
<pre><code class="language-bash">foamDictionary system/setTurbulenceFieldsDict -entry writeF -set true
setTurbulenceFields
</code></pre>
<p>启用writeF后额外保存辅助场f，便于检查经验初始化随空间位置的变化。</p>
<h2>示例 5：处理指定流体区域</h2>
<pre><code class="language-bash">setTurbulenceFields -region fluid -dict system/setTurbulenceFields-fluidDict
</code></pre>
<p>在多区域fluid内使用专用参数初始化；检查输出字段与该区域选择的湍流模型匹配。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-decomposeParDict &lt;file&gt;</code></td><td>使用指定的 decomposeParDict 并行分解字典。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>使用指定的 setTurbulenceFieldsDict 文件。</td></tr><tr><td><code>-parallel</code></td><td>以并行模式运行，通常由 mpirun 启动。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域，默认为 region0。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（17 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-debug-switch &lt;name=val&gt;</code></td><td>设置指定的 DebugSwitch 调试开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-fileHandler &lt;handler&gt;</code></td><td>指定文件读写处理器类型。</td></tr><tr><td><code>-hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;</code></td><td>为分布式运行的各子进程指定主机与根目录；主机名支持正则表达式。</td></tr><tr><td><code>-info-switch &lt;name=val&gt;</code></td><td>设置指定的 InfoSwitch 信息输出开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-lib &lt;name&gt;</code></td><td>额外加载一个或一组共享库；可重复使用。</td></tr><tr><td><code>-mpi-no-comm-dup</code></td><td>跳过初始化时的 MPI_Comm_dup() 调用。</td></tr><tr><td><code>-mpi-split-by-appnum</code></td><td>按 APPNUM 对全局通信器进行分组。</td></tr><tr><td><code>-mpi-threads</code></td><td>请求启用 MPI 线程支持。</td></tr><tr><td><code>-no-libs</code></td><td>跳过 controlDict 中 libs 条目指定的库。</td></tr><tr><td><code>-opt-switch &lt;name=val&gt;</code></td><td>设置指定的 OptimisationSwitch 优化开关，默认值为 1；可重复使用。</td></tr><tr><td><code>-roots &lt;(dir1 .. dirN)&gt;</code></td><td>为分布式运行的各子进程指定根目录。</td></tr><tr><td><code>-world &lt;name&gt;</code></td><td>指定并行通信使用的局部通信域名称。</td></tr><tr><td><code>-doc</code></td><td>在浏览器中打开文档。</td></tr><tr><td><code>-doc-source</code></td><td>在浏览器中打开源码。</td></tr><tr><td><code>-help-compat</code></td><td>显示兼容性选项并退出。</td></tr><tr><td><code>-help-man</code></td><td>显示完整帮助，以 man 手册格式输出，然后退出。</td></tr><tr><td><code>-help-notes</code></td><td>显示程序功能说明并退出。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/setTurbulenceFields/setTurbulenceFields.C">源码与说明</a> · <a href="/assets/command-help/setturbulencefields.txt">帮助文本</a></p>
