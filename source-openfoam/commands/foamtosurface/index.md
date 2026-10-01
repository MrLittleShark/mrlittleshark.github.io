---
title: "foamToSurface  将体网格边界导出为表面文件"
layout: reference
description: "用于几何检查及外部软件数据交换。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>用于几何检查及外部软件数据交换。</p><h2>v2512 源码中的用途</h2><p>Extract boundaries from an OpenFOAM mesh and write in a surface format</p><h2>使用入口</h2><pre><code class="language-bash">foamToSurface boundary.stl</code></pre><h2>使用条件与核对</h2><p>用于几何检查及外部软件数据交换。 用法：foamToSurface 输出 [选项] 示例：foamToSurface boundary.stl
源码说明：Extract boundaries from an OpenFOAM mesh and write in a surface format
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -constant -debug-switch -doc -doc-source -fileHandler -help -help-full -help-man -help-notes -info-switch -latestTime -lib -no-libs -noFunctionObjects -noZero -opt-switch -scale -time -tri</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamtosurface.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: foamToSurface
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/foamToSurface/foamToSurface.C


Usage: foamToSurface [OPTIONS] &lt;output&gt;
Arguments:
  &lt;output&gt;          The output surface file
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -scale &lt;factor&gt;   Geometry scaling factor - default is 1
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -tri              Triangulate surface
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Extract boundaries from an OpenFOAM mesh and write in a surface format

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/foamToSurface/foamToSurface.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/foamToSurface/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
