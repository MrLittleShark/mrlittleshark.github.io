---
title: "paraFoam  在 ParaView 中打开算例"
layout: reference
description: "-builtin 选择 ParaView 内置 OpenFOAM 读取器，运行需具备 ParaView 和图形环境。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>-builtin 选择 ParaView 内置 OpenFOAM 读取器，运行需具备 ParaView 和图形环境。</p><h2>v2512 源码中的用途</h2><p>Start paraview with OpenFOAM libraries and reader modules.</p><h2>使用入口</h2><pre><code class="language-bash">paraFoam -builtin</code></pre><h2>使用条件与核对</h2><p>-builtin 选择 ParaView 内置 OpenFOAM 读取器，运行需具备 ParaView 和图形环境。 用法：paraFoam [选项] 示例：paraFoam -builtin
Start paraview with OpenFOAM libraries and reader modules.
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-block -case -help -help-build -help-full -help-paraview -plugin-path -region -touch -touch-all -touch-proc -vtk</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/parafoam.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: paraFoam
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/paraFoam

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Possible way to build supplementary ParaView/OpenFOAM reader modules

    cd \&#36;WM_PROJECT_DIR/modules/visualization/src/paraview-plugins
    ./Allwclean
    ./Allwmake


Usage: paraFoam [OPTION] [--] [PARAVIEW_OPTION]
options:
  -block            Use blockMesh reader (.blockMesh extension)
  -vtk              Use VTK builtin reader (.foam extension)
  -case &lt;dir&gt;       Specify alternative case directory, default is the cwd
  -region &lt;name&gt;    Specify alternative mesh region
  -touch            Create the file (eg, .blockMesh, .foam, .OpenFOAM, ...)
  -touch-all        Create .blockMesh, .foam, .OpenFOAM files (for all regions)

  -touch-proc       Same as &#x27;-touch&#x27; but for each processor
  -plugin-path=DIR  Define plugin directory (default: \&#36;PV_PLUGIN_PATH)
  -help-build       Display help for building reader module and exit
  -help-paraview    Display ParaView help
  --help            Display ParaView help

  -help             Display short help and exit
  -help-full        Display full help and exit

Start paraview with the OpenFOAM libraries and reader modules,
or with the builtin VTK reader.
Note that paraview options begin with double dashes.

Uses paraview=&#36;(command -v paraview)

Equivalent options:
  -touch-all     -touchAll
  -vtk           -builtin</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/paraFoam">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
