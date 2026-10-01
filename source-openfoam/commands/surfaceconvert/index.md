---
title: "surfaceConvert  转换三角表面文件格式"
layout: reference
description: "-scale 指定几何缩放系数，按输入与输出长度单位换算。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>-scale 指定几何缩放系数，按输入与输出长度单位换算。</p><h2>v2512 源码中的用途</h2><p>Converts from one surface mesh format to another.</p><h2>使用入口</h2><pre><code class="language-bash">surfaceConvert body.obj body.stl</code></pre><h2>使用条件与核对</h2><p>-scale 指定几何缩放系数，按输入与输出长度单位换算。 用法：surfaceConvert 输入 输出 [选项] 示例：surfaceConvert body.obj body.stl
源码说明：Converts from one surface mesh format to another.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -clean -debug-switch -doc -doc-source -fileHandler -group -help -help-compat -help-full -help-man -help-notes -info-switch -lib -no-libs -noFunctionObjects -opt-switch -precision -read-format -scale -verbose -write-format</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/surfaceconvert.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: surfaceConvert
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceConvert/surfaceConvert.C


Usage: surfaceConvert [OPTIONS] &lt;input&gt; &lt;output&gt;
Arguments:
  &lt;input&gt;           The input surface file
  &lt;output&gt;          The output surface file
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -clean            Perform some surface checking/cleanup on the input surface
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -group            Reorder faces into groups; one per region
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
  -precision &lt;int&gt;  The output precision
  -read-format &lt;type&gt;
                    The input format (default: use file extension)
  -scale &lt;factor&gt;   Input geometry scaling factor
  -verbose          Additional verbosity (can be used multiple times)
  -write-format &lt;type&gt;
                    The output format (default: use file extension)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Convert between surface formats, using triSurface library components

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceConvert/surfaceConvert.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceConvert/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
