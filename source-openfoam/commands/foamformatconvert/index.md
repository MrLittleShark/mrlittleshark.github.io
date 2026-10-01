---
title: "foamFormatConvert  按指定格式重写场和网格"
layout: reference
description: "输出格式由 controlDict 中的 writeFormat 指定，可设为 ascii 或 binary。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>输出格式由 controlDict 中的 writeFormat 指定，可设为 ascii 或 binary。</p><h2>v2512 源码中的用途</h2><p>Converts all IOobjects associated with a case into the format specified in the controlDict. Mainly used to convert binary mesh/field files to ASCII. Problem: any zero-size List written binary gets written as &#x27;0&#x27;. When reading the file as a dictionary this is interpreted as a label. This is (usually) not a problem when doing patch fields since these get the &#x27;uniform&#x27;, &#x27;nonuniform&#x27; prefix. However zone contents are labelLists not labelFields and these go wrong. For now hacked a solution where we detect the keywords in zones and redo the dictionary entries to be labelLists.</p><h2>使用入口</h2><pre><code class="language-bash">foamFormatConvert -latestTime</code></pre><h2>使用条件与核对</h2><p>输出格式由 controlDict 中的 writeFormat 指定，可设为 ascii 或 binary。 用法：foamFormatConvert [选项] 示例：foamFormatConvert -latestTime
源码说明：Converts all IOobjects associated with a case into the format specified in the controlDict. Mainly used to convert binary mesh/field files to ASCII. Problem: any zero-size List written binary gets written as &#x27;0&#x27;. When reading the file as a dictionary this is interpreted as a label. This is (usually) not a problem when doing patch fields since these get the &#x27;uniform&#x27;, &#x27;nonuniform&#x27; prefix. However zone contents are labelLists not labelFields and these go wrong. For now hacked a solution where we detect the keywords in zones and redo the dictionary entries to be labelLists.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -constant -debug-switch -decomposeParDict -doc -doc-source -enableFunctionEntries -fileHandler -help -help-full -help-man -help-notes -hostRoots -info-switch -latestTime -lib -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -noConstant -noFunctionObjects -noZero -opt-switch -parallel -region -roots -time -world</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamformatconvert.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: foamFormatConvert
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamFormatConvert/foamFormatConvert.C


Usage: foamFormatConvert [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -enableFunctionEntries
                    Enable expansion of dictionary directives - #include,
                    #codeStream etc
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noConstant       Exclude the &#x27;constant/&#x27; dir in the times list
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Converts all IOobjects associated with a case into the format specified in the
controlDict

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamFormatConvert/foamFormatConvert.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/foamFormatConvert/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
