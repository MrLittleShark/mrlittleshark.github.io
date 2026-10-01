---
title: "reconstructPar  将并行场重构为串行结果"
layout: reference
description: "-fields 指定场。动网格结果按需先重构网格。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>-fields 指定场。动网格结果按需先重构网格。</p><h2>v2512 源码中的用途</h2><p>Reconstructs fields of a case that is decomposed for parallel execution of OpenFOAM.</p><h2>使用入口</h2><pre><code class="language-bash">reconstructPar -latestTime</code></pre><h2>使用条件与核对</h2><p>-fields 指定场。动网格结果按需先重构网格。 用法：reconstructPar [选项] 示例：reconstructPar -latestTime
源码说明：Reconstructs fields of a case that is decomposed for parallel execution of OpenFOAM.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-allAreas -allRegions -area-region -area-regions -case -constant -debug-switch -doc -doc-source -fields -fileHandler -help -help-compat -help-full -help-man -help-notes -info-switch -lagrangianFields -latestTime -lib -newTimes -no-fields -no-lagrangian -no-libs -no-sets -noFunctionObjects -noZero -opt-switch -region -regions -time -verbose -withZero</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/reconstructpar.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: reconstructPar
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/parallelProcessing/reconstructPar/reconstructPar.C


Usage: reconstructPar [OPTIONS]
Options:
  -allAreas         Use all regions in finite-area regionProperties
  -allRegions       Use all regions in regionProperties
  -area-region &lt;name&gt;
                    Specify area-mesh region. Eg, -area-region shell
  -area-regions &lt;wordRes&gt;
                    Use specified area region. Eg, -area-regions film
                    Or from regionProperties.  Eg, -area-regions &#x27;(film
                    &quot;solid.*&quot;)&#x27;
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fields &lt;wordRes&gt;
                    Specify single or multiple fields to reconstruct (all by
                    default). Eg, &#x27;T&#x27; or &#x27;(p T U &quot;alpha.*&quot;)&#x27;
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lagrangianFields &lt;wordRes&gt;
                    Specify single or multiple lagrangian fields to reconstruct
                    (all by default). Eg, &#x27;(U d)&#x27; - Positions are always
                    included.
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -newTimes         Only reconstruct new times (i.e. that do not exist already)
  -no-fields        Skip reconstructing fields
  -no-lagrangian    Skip reconstructing lagrangian positions and fields
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -no-sets          Skip reconstructing cellSets, faceSets, pointSets
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times list, has precedence over
                    the -withZero option
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -region &lt;name&gt;    Use specified mesh region. Eg, -region gas
  -regions &lt;wordRes&gt;
                    Use specified mesh region. Eg, -regions gas
                    Or from regionProperties.  Eg, -regions &#x27;(gas &quot;solid.*&quot;)&#x27;
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -verbose          Additional verbosity (can be used multiple times)
  -withZero         Include &#x27;0/&#x27; dir in the times list
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Reconstruct fields of a parallel case

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/parallelProcessing/reconstructPar/reconstructPar.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/parallelProcessing/reconstructPar/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
