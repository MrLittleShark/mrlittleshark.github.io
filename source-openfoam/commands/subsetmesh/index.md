---
title: "subsetMesh  提取指定单元集合或区域的子网格"
layout: reference
description: "默认读取已有单元集合，如 fluidCells；-zone 改为选择 cellZone。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>默认读取已有单元集合，如 fluidCells；-zone 改为选择 cellZone。</p><h2>v2512 源码中的用途</h2><p>Create a mesh subset for a particular region of interest based on a cellSet or cellZone. See setSet/topoSet utilities on how to define select cells based on various shapes. Will subset all points, faces and cells needed to make a sub-mesh, but not preserve attached boundary types.</p><h2>使用入口</h2><pre><code class="language-bash">subsetMesh fluidCells -overwrite</code></pre><h2>使用条件与核对</h2><p>默认读取已有单元集合，如 fluidCells；-zone 改为选择 cellZone。 用法：subsetMesh 选择名 [选项] 示例：subsetMesh fluidCells -overwrite
源码说明：Create a mesh subset for a particular region of interest based on a cellSet or cellZone. See setSet/topoSet utilities on how to define select cells based on various shapes. Will subset all points, faces and cells needed to make a sub-mesh, but not preserve attached boundary types.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -decomposeParDict -doc -doc-source -exclude-patches -fileHandler -help -help-compat -help-full -help-man -help-notes -hostRoots -info-switch -lib -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -opt-switch -overwrite -parallel -patch -patches -region -resultTime -roots -world -zone</p><h2>同版本官方教程</h2><p>以下链接直接指向 OpenFOAM-v2512 标签中的教程目录。先阅读 Allrun 确定网格生成、初始化和依赖，再在自己的工作目录运行。列出教程不表示本网站已执行它的全部计算。</p><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/overInterDyMFoam/floatingBody/floatingBody">multiphase/overInterDyMFoam/floatingBody/floatingBody</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/overInterDyMFoam/floatingBodyWithSpring/floatingBody">multiphase/overInterDyMFoam/floatingBodyWithSpring/floatingBody</a></li></ul><pre><code class="language-bash">mkdir -p &quot;&#36;FOAM_RUN&quot;
cd &quot;&#36;FOAM_RUN&quot;
# 先选择一个尚不存在的新目录；保留原教程
cp -r &quot;&#36;FOAM_TUTORIALS/multiphase/overInterDyMFoam/floatingBody/floatingBody&quot; ./subsetMesh-study
cd ./subsetMesh-study
ls
# 查看运行流程后，再决定执行哪些步骤
sed -n &#x27;1,200p&#x27; Allrun</code></pre><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/subsetmesh.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: subsetMesh
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/subsetMesh/subsetMesh.C


Usage: subsetMesh [OPTIONS] &lt;cell-selection&gt;
Arguments:
  &lt;cell-selection&gt;  The cellSet name, but with the -zone option this is
                    interpreted to be a cellZone selection by name(s) or regex.
                    Eg &#x27;mixer&#x27; or &#x27;( mixer &quot;moving.*&quot; )&#x27;
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -exclude-patches &lt;wordRes&gt;
                    Exclude single or multiple patches from the -patches
                    selection
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -parallel         Run in parallel
  -patch &lt;name&gt;     Add exposed internal faces to specified patch instead of
                    &quot;oldInternalFaces&quot;
  -patches &lt;wordRes&gt;
                    Add exposed internal faces to closest of specified patches
                    instead of &quot;oldInternalFaces&quot;
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -resultTime &lt;time&gt;
                    Specify a time for the resulting mesh
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -zone             Subset with cellZone(s) instead of cellSet. The command
                    argument may be a list of words or regexs
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Create a mesh subset for a particular region of interest based on a cellSet or
cellZone(s) specified as the first command argument.
See setSet/topoSet utilities on how to select cells based on various shapes.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/subsetMesh/subsetMesh.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/subsetMesh/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
