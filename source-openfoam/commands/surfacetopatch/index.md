---
title: "surfaceToPatch  按给定表面重划体网格边界"
layout: reference
description: "修改后同步检查场文件中的边界条目。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>修改后同步检查场文件中的边界条目。</p><h2>v2512 源码中的用途</h2><p>Reads surface and applies surface regioning to a mesh. Uses boundaryMesh to do the hard work.</p><h2>使用入口</h2><pre><code class="language-bash">surfaceToPatch body.stl</code></pre><h2>使用条件与核对</h2><p>修改后同步检查场文件中的边界条目。 用法：surfaceToPatch 表面文件 [选项] 示例：surfaceToPatch body.stl
源码说明：Reads surface and applies surface regioning to a mesh. Uses boundaryMesh to do the hard work.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -doc -doc-source -faceSet -fileHandler -help -help-full -help-man -help-notes -info-switch -lib -no-libs -noFunctionObjects -opt-switch -tol</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/surfacetopatch.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: surfaceToPatch
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceToPatch/surfaceToPatch.C


Usage: surfaceToPatch [OPTIONS] &lt;surfaceFile&gt;
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -faceSet &lt;name&gt;   Only repatch the faces in specified faceSet
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
  -tol &lt;scalar&gt;     Search tolerance as fraction of mesh size (default 1e-3)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Reads surface and applies surface regioning to a mesh

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceToPatch/surfaceToPatch.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceToPatch/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
