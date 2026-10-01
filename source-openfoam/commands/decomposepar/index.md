---
title: "decomposePar  将网格和场分解为并行子域"
layout: reference
description: "读取 decomposeParDict，-force 替换已有 processor 目录。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>读取 decomposeParDict，-force 替换已有 processor 目录。</p><h2>v2512 源码中的用途</h2><p>Automatically decomposes a mesh and fields of a case for parallel execution of OpenFOAM.</p><h2>使用入口</h2><pre><code class="language-bash">decomposePar</code></pre><h2>使用条件与核对</h2><p>读取 decomposeParDict，-force 替换已有 processor 目录。 用法：decomposePar [选项] 示例：decomposePar
源码说明：Automatically decomposes a mesh and fields of a case for parallel execution of OpenFOAM.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-allAreas -allRegions -area-region -area-regions -case -cellDist -constant -copyUniform -copyZero -debug-switch -decomposeParDict -doc -doc-source -domains -dry-run -fields -fileHandler -force -help -help-compat -help-full -help-man -help-notes -ifRequired -info-switch -latestTime -lib -method -no-fields -no-finite-area -no-lagrangian -no-libs -no-sets -noFunctionObjects -noZero -opt-switch -region -regions -time -verbose</p><p>关联配置：<a href="/dictionaries/system-decomposepardict/">decomposeParDict</a></p><h2>同版本官方教程</h2><p>以下链接直接指向 OpenFOAM-v2512 标签中的教程目录。先阅读 Allrun 确定网格生成、初始化和依赖，再在自己的工作目录运行。列出教程不表示本网站已执行它的全部计算。</p><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/preProcessing/decompositionConstraints/geometric">preProcessing/decompositionConstraints/geometric</a></li></ul><pre><code class="language-bash">mkdir -p &quot;&#36;FOAM_RUN&quot;
cd &quot;&#36;FOAM_RUN&quot;
# 先选择一个尚不存在的新目录；保留原教程
cp -r &quot;&#36;FOAM_TUTORIALS/preProcessing/decompositionConstraints/geometric&quot; ./decomposePar-study
cd ./decomposePar-study
ls
# 查看运行流程后，再决定执行哪些步骤
sed -n &#x27;1,200p&#x27; Allrun</code></pre><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/decomposepar.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: decomposePar
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/parallelProcessing/decomposePar/decomposePar.C


Usage: decomposePar [OPTIONS]
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
  -cellDist         Write cell distribution as a labelList - for use with
                    &#x27;manual&#x27; decomposition method and as a volScalarField for
                    visualization.
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -copyUniform      Copy any uniform/ directories too
  -copyZero         Copy 0/ directory to processor*/ rather than decompose the
                    fields
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -domains &lt;N&gt;      Override numberOfSubdomains (-dry-run only)
  -dry-run          Test without writing the decomposition. Changes -cellDist
                    to only write VTK output.
  -fields           Use existing geometry decomposition and convert fields only
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -force            Remove existing processor*/ subdirs before decomposing the
                    geometry
  -ifRequired       Only decompose geometry if the number of domains has changed
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -method &lt;name&gt;    Override decomposition method (-dry-run only)
  -no-fields        Suppress conversion of fields (volume, finite-area,
                    lagrangian)
  -no-finite-area   Suppress finiteArea mesh/field decomposition
  -no-lagrangian    Suppress lagrangian (cloud) decomposition
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -no-sets          Skip decomposing cellSets, faceSets, pointSets
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -region &lt;name&gt;    Use specified mesh region. Eg, -region gas
  -regions &lt;wordRes&gt;
                    Use specified mesh region. Eg, -regions gas
                    Or from regionProperties.  Eg, -regions &#x27;(gas &quot;solid.*&quot;)&#x27;
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -verbose          Additional verbosity (can be used multiple times)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Decompose a mesh and fields of a case for parallel execution

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/parallelProcessing/decomposePar/decomposePar.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/parallelProcessing/decomposePar/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
