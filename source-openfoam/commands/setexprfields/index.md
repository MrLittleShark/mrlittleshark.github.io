---
title: "setExprFields  按表达式设置体场"
layout: reference
description: "示例修改已有 T 场；采用 -create 新建场时需设置 dimensions。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>示例修改已有 T 场；采用 -create 新建场时需设置 dimensions。</p><h2>v2512 源码中的用途</h2><p>Set values on a selected set of cells/patch-faces via a dictionary.</p><h2>使用入口</h2><pre><code class="language-bash">setExprFields -field T -expression &#x27;300 + 10*pos().x()&#x27;</code></pre><h2>使用条件与核对</h2><p>示例修改已有 T 场；采用 -create 新建场时需设置 dimensions。 用法：setExprFields [-dict 文件] 或表达式选项 示例：setExprFields -field T -expression &#x27;300 + 10*pos().x()&#x27;
源码说明：Set values on a selected set of cells/patch-faces via a dictionary.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-ascii -case -create -debug-parser -debug-switch -decomposeParDict -dict -dimensions -doc -doc-source -dry-run -dummy-phi -expression -field -field-mask -fileHandler -help -help-compat -help-full -help-man -help-notes -hostRoots -info-switch -keepPatches -latestTime -lib -load-fields -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -no-variable-cache -noZero -opt-switch -parallel -region -roots -time -value-patches -verbose -withFunctionObjects -world</p><p>关联配置：<a href="/dictionaries/system-setexprfieldsdict/">setExprFieldsDict</a></p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/setexprfields.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: setExprFields
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/setExprFields/setExprFields.C


Usage: setExprFields [OPTIONS]
Options:
  -ascii            Write in ASCII format instead of the controlDict setting
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -create           Create a new field (command-line operation)
  -debug-parser     Additional debugging information
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative dictionary for setExprFieldsDict
  -dimensions &lt;dims&gt;
                    The dimensions for created fields (command-line operation)
  -dry-run          Evaluate but do not write
  -dummy-phi        Provide a zero phi field (command-line operation)
  -expression &lt;expr&gt;
                    The expression to evaluate (command-line operation)
  -field &lt;name&gt;     The field to create/overwrite (command-line operation)
  -field-mask &lt;logic&gt;
                    The field mask (logical condition) when to apply the
                    expression (command-line operation)
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -keepPatches      Leave patches unaltered (command-line operation)
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -load-fields &lt;wordList&gt;
                    Specify field or fields to preload. Eg, &#x27;T&#x27; or &#x27;(p T U)&#x27;
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -no-variable-cache
                    Disable caching of expression variables
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -value-patches &lt;(patches)&gt;
                    A list of patches that receive a fixed value (command-line
                    operation)
  -verbose          Additional verbosity
  -withFunctionObjects
                    Execute functionObjects
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/setExprFields/setExprFields.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/setExprFields/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
