---
title: "splitCells  按边角度拆分单元"
layout: reference
description: "用于网格单元的拓扑修复。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>用于网格单元的拓扑修复。</p><h2>v2512 源码中的用途</h2><p>Utility to split cells with flat faces. Uses a geometric cut with a plane dividing the edge angle into two so might produce funny cells. For hexes it will use by default a cut from edge onto opposite edge (i.e. purely topological). Options: - split cells from cellSet only - use geometric cut for hexes as well The angle is the angle between two faces sharing an edge as seen from inside each cell. So a cube will have all angles 90. If you want to split cells with cell centre outside use e.g. angle 200</p><h2>使用入口</h2><pre><code class="language-bash">splitCells 90</code></pre><h2>使用条件与核对</h2><p>用于网格单元的拓扑修复。 用法：splitCells 边角度 [选项] 示例：splitCells 90
源码说明：Utility to split cells with flat faces. Uses a geometric cut with a plane dividing the edge angle into two so might produce funny cells. For hexes it will use by default a cut from edge onto opposite edge (i.e. purely topological). Options: - split cells from cellSet only - use geometric cut for hexes as well The angle is the angle between two faces sharing an edge as seen from inside each cell. So a cube will have all angles 90. If you want to split cells with cell centre outside use e.g. angle 200
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -doc -doc-source -fileHandler -geometry -help -help-compat -help-full -help-man -help-notes -info-switch -lib -no-libs -opt-switch -overwrite -set -tol</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/splitcells.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: splitCells
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/splitCells/splitCells.C


Usage: splitCells [OPTIONS] &lt;edgeAngle&gt;
Arguments:
  &lt;edgeAngle&gt;       in degrees [0-360]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -geometry         Use geometric cut for hexes as well
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -set &lt;name&gt;       Split cells from specified cellSet only
  -tol &lt;scalar&gt;     Edge snap tolerance (default 0.2)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Split cells with flat faces

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/splitCells/splitCells.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/splitCells/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
