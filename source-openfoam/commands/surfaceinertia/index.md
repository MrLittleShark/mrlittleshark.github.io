---
title: "surfaceInertia  计算封闭表面的惯性参数"
layout: reference
description: "按选项采用实体或薄壳模型，密度单位与几何长度单位保持一致。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>按选项采用实体或薄壳模型，密度单位与几何长度单位保持一致。</p><h2>v2512 源码中的用途</h2><p>Calculates the inertia tensor, principal axes and moments of a command line specified triSurface. Inertia can either be of the solid body or of a thin shell.</p><h2>使用入口</h2><pre><code class="language-bash">surfaceInertia body.stl -density 1000</code></pre><h2>使用条件与核对</h2><p>按选项采用实体或薄壳模型，密度单位与几何长度单位保持一致。 用法：surfaceInertia 输入 [选项] 示例：surfaceInertia body.stl -density 1000
源码说明：Calculates the inertia tensor, principal axes and moments of a command line specified triSurface. Inertia can either be of the solid body or of a thin shell.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -density -doc -doc-source -fileHandler -help -help-full -help-man -help-notes -info-switch -lib -no-libs -noFunctionObjects -opt-switch -referencePoint -shellProperties</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/surfaceinertia.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: surfaceInertia
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceInertia/surfaceInertia.C


Usage: surfaceInertia [OPTIONS] &lt;input&gt;
Arguments:
  &lt;input&gt;           The input surface file
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -density &lt;scalar&gt;
                    Specify density, kg/m3 for solid properties, kg/m2 for
                    shell properties
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -referencePoint &lt;vector&gt;
                    Inertia relative to this point, not the centre of mass
  -shellProperties  Inertia of a thin shell
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Calculates the inertia tensor and principal axes and moments of the specified
surface.
Inertia can either be of the solid body or of a thin shell.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceInertia/surfaceInertia.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceInertia/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
