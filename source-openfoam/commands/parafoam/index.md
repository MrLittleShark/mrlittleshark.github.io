---
title: "paraFoam · 打开算例的 ParaView 可视化入口"
layout: reference
description: "打开算例的 ParaView 可视化入口。"
cms_slug: "command-parafoam"
---

<p>打开算例的 ParaView 可视化入口。</p><h2>打开当前算例</h2>
<pre><code class="language-bash">paraFoam
</code></pre>
<p>在算例目录运行，使用环境中配置的 ParaView 和读取器。打开后选择需要的场并点击 Apply。</p>
<h2>使用 ParaView 内置读取器</h2>
<pre><code class="language-bash">paraFoam -builtin
</code></pre>
<p>使用内置 OpenFOAM Reader。需要远程读取或本地没有 OpenFOAM 插件时，这种方式通常更方便。</p>
<h2>仅创建入口文件</h2>
<pre><code class="language-bash">paraFoam -touch
</code></pre>
<p>创建读取器入口后退出，随后可在 ParaView 中手动打开。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-block</td><td>Use blockMesh reader (.blockMesh extension)</td></tr><tr><td>-vtk</td><td>Use VTK builtin reader (.foam extension)</td></tr><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-region &lt;name&gt;</td><td>指定网格区域名称。</td></tr><tr><td>-touch</td><td>Create the file (eg, .blockMesh, .foam, .OpenFOAM, ...)</td></tr><tr><td>-touch-all</td><td>Create .blockMesh, .foam, .OpenFOAM files (for all regions)</td></tr><tr><td>-touch-proc</td><td>Same as &#x27;-touch&#x27; but for each processor</td></tr><tr><td>-plugin-path=DIR</td><td>Define plugin directory (default: \$PV_PLUGIN_PATH)</td></tr><tr><td>-help-build</td><td>Display help for building reader module and exit</td></tr><tr><td>-help-paraview</td><td>Display ParaView help</td></tr><tr><td>--help</td><td>Display ParaView help</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr><tr><td>-touch-all</td><td>-touchAll</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: paraFoam [OPTION] [--] [PARAVIEW_OPTION]
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
