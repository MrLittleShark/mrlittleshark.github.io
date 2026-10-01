---
title: "surfaceMeshExport  导出算例中的 surfaceMesh"
layout: reference
description: "输入为算例中已有的 surfaceMesh。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>输入为算例中已有的 surfaceMesh。</p><h2>v2512 源码中的用途</h2><p>Export from surfMesh to various third-party surface formats with optional scaling or transformations (rotate/translate) on a coordinateSystem.</p><h2>使用入口</h2><pre><code class="language-bash">surfaceMeshExport body.obj</code></pre><h2>使用条件与核对</h2><p>输入为算例中已有的 surfaceMesh。 用法：surfaceMeshExport 输出 [选项] 示例：surfaceMeshExport body.obj
源码说明：Export from surfMesh to various third-party surface formats with optional scaling or transformations (rotate/translate) on a coordinateSystem.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -clean -debug-switch -dict -doc -doc-source -fileHandler -from -help -help-compat -help-full -help-man -help-notes -info-switch -lib -name -no-libs -noFunctionObjects -opt-switch -read-scale -to -verbose -write-format -write-scale</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/surfacemeshexport.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: surfaceMeshExport
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceMeshExport/surfaceMeshExport.C


Usage: surfaceMeshExport [OPTIONS] &lt;output&gt;
Arguments:
  &lt;output&gt;          The output surface file
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
  -name &lt;name&gt;      Specify an alternative surface name when reading - default
                    is &#x27;default&#x27;
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -read-scale &lt;factor&gt;
                    Input geometry scaling factor
  -to &lt;system&gt;      The target coordinate system, applied before &#x27;-write-scale&#x27;
  -verbose          Additional verbosity (can be used multiple times)
  -write-format &lt;type&gt;
                    Output format (default: use file extension)
  -write-scale &lt;factor&gt;
                    Output geometry scaling factor
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Export from surfMesh to various third-party surface formats

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceMeshExport/surfaceMeshExport.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceMeshExport/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
