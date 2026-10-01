---
title: "foamDictionary  读取或修改字典条目"
layout: reference
description: "-value 读取条目值，-keywords 列出关键字，-expand 展开引用。子条目采用 solvers/p/tolerance 等路径表示。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>-value 读取条目值，-keywords 列出关键字，-expand 展开引用。子条目采用 solvers/p/tolerance 等路径表示。</p><h2>v2512 源码中的用途</h2><p>Interrogate and manipulate dictionaries.</p><h2>使用入口</h2><pre><code class="language-bash">foamDictionary system/controlDict -entry endTime -set 100</code></pre><h2>使用条件与核对</h2><p>-value 读取条目值，-keywords 列出关键字，-expand 展开引用。子条目采用 solvers/p/tolerance 等路径表示。 用法：foamDictionary 字典 [-entry 路径] [-value/-set 值] 示例：foamDictionary system/controlDict -entry endTime -set 100
源码说明：Interrogate and manipulate dictionaries.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-add -case -debug-switch -decomposeParDict -diff -diff-etc -disableFunctionEntries -doc -doc-source -entry -expand -fileHandler -help -help-compat -help-full -help-man -help-notes -hostRoots -includes -info-switch -keywords -lib -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -noFunctionObjects -opt-switch -parallel -precision -remove -roots -set -value -world</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamdictionary.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: foamDictionary
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamDictionary/foamDictionary.C


Usage: foamDictionary [OPTIONS] &lt;dict&gt;
Arguments:
  &lt;dict&gt;            The dictionary file to process
Options:
  -add &lt;value&gt;      Add a new entry
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -diff &lt;dict&gt;      Write differences with respect to the specified dictionary
  -diff-etc &lt;dict&gt;  As per -diff, but locate the file as per foamEtcFile
  -disableFunctionEntries
                    Disable expansion of dictionary directives - #include,
                    #codeStream etc
  -entry &lt;name&gt;     Report/select the named entry
  -expand           Read the specified dictionary file, expand the macros etc.
                    and write the resulting dictionary to standard output
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -includes         List the #include/#sinclude files to standard output
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -keywords         List keywords
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -precision &lt;int&gt;  Set default write precision for IOstreams
  -remove           Remove the entry
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -set &lt;value&gt;      Set entry value or add new entry
  -value            Print entry value
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Interrogate and manipulate dictionaries

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamDictionary/foamDictionary.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamDictionary/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
