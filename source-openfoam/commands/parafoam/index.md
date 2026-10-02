---
title: "paraFoam · 打开算例的 ParaView 可视化入口"
layout: reference
description: "打开算例的 ParaView 可视化入口。"
cms_slug: "command-parafoam"
---

<p>打开算例的 ParaView 可视化入口。</p><h2>开始前</h2>
<p>加载 v2512 环境，使用个人算例副本 caseA。并行示例先配置 decomposeParDict 并完成 decomposePar，程序和字典须匹配。 图形模式需要 ParaView；仅 -touch 的示例用于生成阅读器入口文件。</p>
<h2>示例 1：打开算例</h2>
<pre><code class="language-bash">paraFoam -case caseA
</code></pre>
<p>启动 ParaView 并加载 OpenFOAM 阅读器，点击 Apply 后显示网格。</p>
<h2>示例 2：使用内置 VTK 阅读器</h2>
<pre><code class="language-bash">paraFoam -vtk -case caseA
</code></pre>
<p>使用 .foam 入口和 ParaView 自带阅读器，常用于没有额外插件的安装。</p>
<h2>示例 3：仅创建入口</h2>
<pre><code class="language-bash">paraFoam -vtk -touch -case caseA
</code></pre>
<p>生成 .foam 文件后退出，可在其他图形工作站手动打开。</p>
<h2>示例 4：查看 blockMesh 定义</h2>
<pre><code class="language-bash">paraFoam -block -case caseA
</code></pre>
<p>使用 blockMesh 阅读器，适合检查块结构；需要对应阅读器插件。</p>
<h2>示例 5：选择多区域网格</h2>
<pre><code class="language-bash">paraFoam -vtk -region fluid -case caseA
</code></pre>
<p>fluid 须为实际区域名，以该区域网格和字段作为读取对象。</p>
<h2>示例 6：为各子域生成入口</h2>
<pre><code class="language-bash">paraFoam -vtk -touch-proc -case caseA
</code></pre>
<p>为分区算例创建各 processor 阅读器文件，用于单独检查子域。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-block</code></td><td>使用 blockMesh 读取器，对应 .blockMesh 扩展名。</td></tr><tr><td><code>-vtk</code></td><td>使用 VTK 内置读取器，对应 .foam 扩展名。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；默认使用当前目录。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域。</td></tr><tr><td><code>-touch</code></td><td>创建 .blockMesh、.foam 或 .OpenFOAM 等读取入口文件。</td></tr><tr><td><code>-touch-all</code></td><td>为全部区域创建 .blockMesh、.foam 和 .OpenFOAM 读取入口文件。</td></tr><tr><td><code>-touch-proc</code></td><td>为每个并行进程创建读取入口文件。</td></tr><tr><td><code>-plugin-path=DIR</code></td><td>指定插件目录，默认使用 $PV_PLUGIN_PATH。</td></tr><tr><td><code>-help-build</code></td><td>显示读取器模块的编译帮助并退出。</td></tr><tr><td><code>-help-paraview</code></td><td>显示 ParaView 帮助。</td></tr><tr><td><code>--help</code></td><td>显示 ParaView 帮助。</td></tr><tr><td><code>-help</code></td><td>显示简要帮助并退出。</td></tr><tr><td><code>-help-full</code></td><td>显示完整帮助并退出。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/paraFoam">源码与说明</a> · <a href="/assets/command-help/parafoam.txt">帮助文本</a></p>
