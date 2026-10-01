---
title: "ideasUnvToFoam  导入 I-DEAS 通用网格"
layout: reference
description: "转换后检查边界、长度单位和单元类型。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>转换后检查边界、长度单位和单元类型。</p><h2>v2512 源码中的用途</h2><p>I-Deas unv format mesh conversion. Uses either - DOF sets (757) or - face groups (2452(Cubit), 2467) to do patching. Works without but then puts all faces in defaultFaces patch.</p><h2>使用入口</h2><pre><code class="language-bash">ideasUnvToFoam mesh.unv</code></pre><h2>使用条件与核对</h2><p>转换后检查边界、长度单位和单元类型。 用法：ideasUnvToFoam 网格.unv 示例：ideasUnvToFoam mesh.unv
源码说明：I-Deas unv format mesh conversion. Uses either - DOF sets (757) or - face groups (2452(Cubit), 2467) to do patching. Works without but then puts all faces in defaultFaces patch.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -doc -doc-source -dump -fileHandler -help -help-full -help-man -help-notes -info-switch -lib -no-libs -noFunctionObjects -opt-switch</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/ideasunvtofoam.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: ideasUnvToFoam
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/ideasUnvToFoam/ideasUnvToFoam.C


Usage: ideasUnvToFoam [OPTIONS] &lt;.unv file&gt;
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dump             Dump boundary faces as boundaryFaces.obj (for debugging)
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
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Convert I-Deas unv format to OpenFOAM

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/ideasUnvToFoam/ideasUnvToFoam.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/ideasUnvToFoam/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
