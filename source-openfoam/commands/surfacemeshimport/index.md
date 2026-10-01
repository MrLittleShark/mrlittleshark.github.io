---
title: "surfaceMeshImport  导入表面至算例的 surfaceMesh"
layout: reference
description: "导入对象为表面网格，-name 指定名称。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>导入对象为表面网格，-name 指定名称。</p><h2>v2512 源码中的用途</h2><p>Import from various third-party surface formats into surfMesh with optional scaling or transformations (rotate/translate) on a coordinateSystem.</p><h2>使用入口</h2><pre><code class="language-bash">surfaceMeshImport body.stl</code></pre><h2>使用条件与核对</h2><p>导入对象为表面网格，-name 指定名称。 用法：surfaceMeshImport 输入 [选项] 示例：surfaceMeshImport body.stl
源码说明：Import from various third-party surface formats into surfMesh with optional scaling or transformations (rotate/translate) on a coordinateSystem.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -clean -debug-switch -dict -doc -doc-source -fileHandler -from -help -help-compat -help-full -help-man -help-notes -info-switch -lib -name -no-libs -noFunctionObjects -opt-switch -read-format -read-scale -to -verbose -write-scale</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/surfacemeshimport.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: surfaceMeshImport
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceMeshImport/surfaceMeshImport.C


Usage: surfaceMeshImport [OPTIONS] &lt;surface&gt;
Arguments:
  &lt;surface&gt;         The input surface file
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -clean            Perform some surface checking/cleanup on the input surface
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dict &lt;file&gt;      Alternative coordinateSystems
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -from &lt;system&gt;    The source coordinate system, applied after &#x27;-read-scale&#x27;
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -name &lt;name&gt;      The surface name when writing (default is &#x27;default&#x27;)
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -read-format &lt;type&gt;
                    Input format (default: use file extension)
  -read-scale &lt;factor&gt;
                    Input geometry scaling factor
  -to &lt;system&gt;      The target coordinate system, applied before &#x27;-write-scale&#x27;
  -verbose          Additional verbosity (can be used multiple times)
  -write-scale &lt;factor&gt;
                    Output geometry scaling factor
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Import from various third-party surface formats into surfMesh

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceMeshImport/surfaceMeshImport.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceMeshImport/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
