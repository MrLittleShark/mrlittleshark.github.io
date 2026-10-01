---
title: "refineMesh  全局或按集合定向加密体网格"
layout: reference
description: "缺少 refineMeshDict 时可执行全域细化。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>缺少 refineMeshDict 时可执行全域细化。</p><h2>v2512 源码中的用途</h2><p>Utility to refine cells in multiple directions. Command-line option handling: - If -all specified or no refineMeshDict exists or, refine all cells - If -dict \&lt;file\&gt; specified refine according to \&lt;file\&gt; - If refineMeshDict exists refine according to refineMeshDict When the refinement or all cells is selected apply 3D refinement for 3D cases and 2D refinement for 2D cases.</p><h2>使用入口</h2><pre><code class="language-bash">refineMesh -overwrite</code></pre><h2>使用条件与核对</h2><p>缺少 refineMeshDict 时可执行全域细化。 用法：refineMesh [-dict 文件] [-overwrite] 示例：refineMesh -overwrite
源码说明：Utility to refine cells in multiple directions. Command-line option handling: - If -all specified or no refineMeshDict exists or, refine all cells - If -dict \&lt;file\&gt; specified refine according to \&lt;file\&gt; - If refineMeshDict exists refine according to refineMeshDict When the refinement or all cells is selected apply 3D refinement for 3D cases and 2D refinement for 2D cases.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-all -case -debug-switch -decomposeParDict -dict -doc -doc-source -fileHandler -help -help-compat -help-full -help-man -help-notes -hostRoots -info-switch -lib -mpi-no-comm-dup -mpi-split-by-appnum -mpi-threads -no-libs -opt-switch -overwrite -parallel -region -roots -world</p><p>关联配置：<a href="/dictionaries/system-refinemeshdict/">refineMeshDict</a></p><h2>同版本官方教程</h2><p>以下链接直接指向 OpenFOAM-v2512 标签中的教程目录。先阅读 Allrun 确定网格生成、初始化和依赖，再在自己的工作目录运行。列出教程不表示本网站已执行它的全部计算。</p><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/refineMesh/refineFieldDirs">mesh/refineMesh/refineFieldDirs</a></li></ul><pre><code class="language-bash">mkdir -p &quot;&#36;FOAM_RUN&quot;
cd &quot;&#36;FOAM_RUN&quot;
# 先选择一个尚不存在的新目录；保留原教程
cp -r &quot;&#36;FOAM_TUTORIALS/mesh/refineMesh/refineFieldDirs&quot; ./refineMesh-study
cd ./refineMesh-study
ls
# 查看运行流程后，再决定执行哪些步骤
sed -n &#x27;1,200p&#x27; Allrun</code></pre><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/refinemesh.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: refineMesh
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/refineMesh/refineMesh.C


Usage: refineMesh [OPTIONS]
Options:
  -all              Refine all cells
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative refineMeshDict
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
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Refine cells in multiple directions

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/refineMesh/refineMesh.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/refineMesh/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
