---
title: "chemFoam · 单单元化学反应积分"
layout: reference
description: "单单元化学反应积分。具体方程、物理假设和所需字段见下方源码与教程。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>单单元化学反应积分。具体方程、物理假设和所需字段见下方源码与教程。</p><h2>v2512 源码中的用途</h2><p>Solver for chemistry problems, designed for use on single cell cases to provide comparison against other chemistry solvers, that uses a single cell mesh, and fields created from the initial conditions.</p><h2>使用入口</h2><pre><code class="language-bash">chemFoam -help-full</code></pre><h2>使用条件与核对</h2><p>
源码说明：Solver for chemistry problems, designed for use on single cell cases to provide comparison against other chemistry solvers, that uses a single cell mesh, and fields created from the initial conditions.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -doc -doc-source -fileHandler -help -help-full -help-man -help-notes -info-switch -lib -listFunctionObjects -listRegisteredSwitches -listScalarBCs -listSwitches -listUnsetSwitches -listVectorBCs -no-libs -noFunctionObjects -opt-switch -postProcess</p><p>关联配置：<a href="/dictionaries/system-controldict/">controlDict</a> · <a href="/dictionaries/system-fvschemes/">fvSchemes</a> · <a href="/dictionaries/system-fvsolution/">fvSolution</a></p><h2>同版本官方教程</h2><p>以下链接直接指向 OpenFOAM-v2512 标签中的教程目录。先阅读 Allrun 确定网格生成、初始化和依赖，再在自己的工作目录运行。列出教程不表示本网站已执行它的全部计算。</p><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/h2">combustion/chemFoam/h2</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/gri">combustion/chemFoam/gri</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/ic8h18">combustion/chemFoam/ic8h18</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/nc7h16">combustion/chemFoam/nc7h16</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/chemFoam/ic8h18_TDAC">combustion/chemFoam/ic8h18_TDAC</a></li></ul><pre><code class="language-bash">mkdir -p &quot;&#36;FOAM_RUN&quot;
cd &quot;&#36;FOAM_RUN&quot;
# 先选择一个尚不存在的新目录；保留原教程
cp -r &quot;&#36;FOAM_TUTORIALS/combustion/chemFoam/h2&quot; ./chemFoam-study
cd ./chemFoam-study
ls
# 查看运行流程后，再决定执行哪些步骤
sed -n &#x27;1,200p&#x27; Allrun</code></pre><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/chemfoam.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: chemFoam
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/combustion/chemFoam/chemFoam.C


Usage: chemFoam [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -listFunctionObjects
                    List functionObjects
  -listRegisteredSwitches
                    List switches registered for run-time modification (see
                    -listUnsetSwitches option)
  -listScalarBCs    List scalar field boundary conditions (fvPatchField&lt;scalar&gt;)
  -listSwitches     List switches declared in libraries (see -listUnsetSwitches
                    option)
  -listUnsetSwitches
                    Modifies switch listing to display values not set in
                    etc/controlDict
  -listVectorBCs    List vector field boundary conditions (fvPatchField&lt;vector&gt;)
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -postProcess      Execute functionObjects only
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Solver for chemistry problems, designed for use on single cell cases to provide
comparison against other chemistry solvers

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/combustion/chemFoam/chemFoam.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/solvers/combustion/chemFoam/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
