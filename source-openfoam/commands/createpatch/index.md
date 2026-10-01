---
title: "createPatch  创建或重组网格边界"
layout: reference
description: "读取 createPatchDict，修改后使场边界与新网格对应。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>读取 createPatchDict，修改后使场边界与新网格对应。</p><h2>v2512 源码中的用途</h2><p>Create patches out of selected boundary faces, which are either from existing patches or from a faceSet. More specifically it: - creates new patches (from selected boundary faces). Synchronise faces on coupled patches. - synchronises points on coupled boundaries - remove patches with 0 faces in them</p><h2>使用入口</h2><pre><code class="language-bash">createPatch -overwrite</code></pre><h2>使用条件与核对</h2><p>读取 createPatchDict，修改后使场边界与新网格对应。 用法：createPatch [-dict 文件] [-overwrite] 示例：createPatch -overwrite
源码说明：Create patches out of selected boundary faces, which are either from existing patches or from a faceSet. More specifically it: - creates new patches (from selected boundary faces). Synchronise faces on coupled patches. - synchronises points on coupled boundaries - remove patches with 0 faces in them
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-allRegions -case -debug-switch -decomposeParDict -dict -doc -doc-source -fileHandler -help -help-compat -help-full -help-man -help-notes -hostRoots -info-switch -lib -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -opt-switch -overwrite -parallel -region -regions -roots -world -writeObj</p><p>关联配置：<a href="/dictionaries/system-createpatchdict/">createPatchDict</a></p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/createpatch.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: createPatch
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/createPatch/createPatch.C


Usage: createPatch [OPTIONS]
Options:
  -allRegions       Use all regions in regionProperties
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative createPatchDict
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
  -region &lt;name&gt;    Use specified mesh region. Eg, -region gas
  -regions &lt;wordRes&gt;
                    Use specified mesh region. Eg, -regions gas
                    Or from regionProperties.  Eg, -regions &#x27;(gas &quot;solid.*&quot;)&#x27;
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -writeObj         Write obj files showing the cyclic matching process
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Create patches out of selected boundary faces, which are either from existing
patches or from a faceSet

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/createPatch/createPatch.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/createPatch/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
