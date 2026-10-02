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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-block</code></td><td>Use blockMesh reader (.blockMesh extension)</td></tr><tr><td><code>-vtk</code></td><td>Use VTK builtin reader (.foam extension)</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-touch</code></td><td>Create the file (eg, .blockMesh, .foam, .OpenFOAM, ...)</td></tr><tr><td><code>-touch-all</code></td><td>Create .blockMesh, .foam, .OpenFOAM files (for all regions)</td></tr><tr><td><code>-touch-proc</code></td><td>Same as &#x27;-touch&#x27; but for each processor</td></tr><tr><td><code>-plugin-path=DIR</code></td><td>Define plugin directory (default: \$PV_PLUGIN_PATH)</td></tr><tr><td><code>-help-build</code></td><td>Display help for building reader module and exit</td></tr><tr><td><code>-help-paraview</code></td><td>Display ParaView help</td></tr><tr><td><code>--help</code></td><td>Display ParaView help</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr><tr><td><code>-touch-all</code></td><td>-touchAll</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: paraFoam [OPTION] [--] [PARAVIEW_OPTION]
options:
  -block            Use blockMesh reader (.blockMesh extension)
  -vtk              Use VTK builtin reader (.foam extension)
  -case &lt;dir&gt;       Specify alternative case directory, default is the cwd
  -region &lt;name&gt;    Specify alternative mesh region
  -touch            Create the file (eg, .blockMesh, .foam, .OpenFOAM, ...)
  -touch-all        Create .blockMesh, .foam, .OpenFOAM files (for all regions)

  -touch-proc       Same as &#x27;-touch&#x27; but for each processor
  -plugin-path=DIR  Define plugin directory (default: \$PV_PLUGIN_PATH)
  -help-build       Display help for building reader module and exit
  -help-paraview    Display ParaView help
  --help            Display ParaView help

  -help             Display short help and exit
  -help-full        Display full help and exit

Start paraview with the OpenFOAM libraries and reader modules,
or with the builtin VTK reader.
Note that paraview options begin with double dashes.

Uses paraview=$(command -v paraview)

Equivalent options:
  -touch-all     -touchAll
  -vtk           -builtin</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/paraFoam">源码与说明</a> · <a href="/assets/command-help/parafoam.txt">帮助文本</a></p>
