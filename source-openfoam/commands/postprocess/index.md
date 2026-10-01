---
title: "postProcess  执行函数对象后处理"
layout: reference
description: "-list 列出预配置函数。依赖湍流或热物性的函数通过相应求解器的 -postProcess 选项执行。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>-list 列出预配置函数。依赖湍流或热物性的函数通过相应求解器的 -postProcess 选项执行。</p><h2>v2512 源码中的用途</h2><p>Execute the set of functionObjects specified in the selected dictionary (which defaults to system/controlDict) or on the command-line for the selected set of times on the selected set of fields.</p><h2>使用入口</h2><pre><code class="language-bash">postProcess -func &#x27;mag(U)&#x27; -latestTime</code></pre><h2>使用条件与核对</h2><p>-list 列出预配置函数。依赖湍流或热物性的函数通过相应求解器的 -postProcess 选项执行。 用法：postProcess [-func 名称] [-time 范围] [-latestTime] 示例：postProcess -func &#x27;mag(U)&#x27; -latestTime
源码说明：Execute the set of functionObjects specified in the selected dictionary (which defaults to system/controlDict) or on the command-line for the selected set of times on the selected set of fields.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -constant -debug-switch -decomposeParDict -dict -doc -doc-source -field -fields -fileHandler -func -funcs -help -help-full -help-man -help-notes -hostRoots -info-switch -latestTime -lib -list -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -noFunctionObjects -noZero -opt-switch -parallel -profiling -region -roots -time -world</p><p>关联配置：<a href="/dictionaries/functions-probes/">probes</a> · <a href="/dictionaries/functions-sets/">sets</a> · <a href="/dictionaries/functions-surfaces/">surfaces</a> · <a href="/dictionaries/functions-forces/">forces</a> · <a href="/dictionaries/functions-forcecoeffs/">forceCoeffs</a> · <a href="/dictionaries/functions-fieldaverage/">fieldAverage</a> · <a href="/dictionaries/functions-volfieldvalue/">volFieldValue</a> · <a href="/dictionaries/functions-surfacefieldvalue/">surfaceFieldValue</a> · <a href="/dictionaries/functions-yplus/">yPlus</a> · <a href="/dictionaries/functions-q/">Q</a></p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/postprocess.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: postProcess
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/postProcess/postProcess.C


Usage: postProcess [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Read control dictionary from specified location
  -field &lt;name&gt;     Specify the name of the field to be processed, e.g. U
  -fields &lt;list&gt;    Specify a list of fields to be processed, e.g. &#x27;(U T p)&#x27;
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -func &lt;name&gt;      Specify the name of the functionObject to execute, e.g. Q
  -funcs &lt;list&gt;     Specify the names of the functionObjects to execute, e.g.
                    &#x27;(Q div(U))&#x27;
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -list             List the available configured functionObjects
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -profiling        Activate application-level profiling
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

Execute the set of functionObjects specified in the selected dictionary or on
the command-line for the selected set of times on the selected set of fields

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/postProcess/postProcess.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/postProcess/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
