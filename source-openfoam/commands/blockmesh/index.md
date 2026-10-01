---
title: "blockMesh  根据块拓扑生成六面体网格"
layout: reference
description: "读取 system/blockMeshDict，生成后使用 checkMesh 检查。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>读取 system/blockMeshDict，生成后使用 checkMesh 检查。</p><h2>v2512 源码中的用途</h2><p>A multi-block mesh generator. Uses the block mesh description found in - \c system/blockMeshDict - \c system/\&lt;region\&gt;/blockMeshDict - \c constant/polyMesh/blockMeshDict - \c constant/\&lt;region\&gt;/polyMesh/blockMeshDict</p><h2>使用入口</h2><pre><code class="language-bash">blockMesh</code></pre><h2>使用条件与核对</h2><p>读取 system/blockMeshDict，生成后使用 checkMesh 检查。 用法：blockMesh [-dict 文件] [-case 目录] 示例：blockMesh
源码说明：A multi-block mesh generator. Uses the block mesh description found in - \c system/blockMeshDict - \c system/\&lt;region\&gt;/blockMeshDict - \c constant/polyMesh/blockMeshDict - \c constant/\&lt;region\&gt;/polyMesh/blockMeshDict
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -dict -doc -doc-source -fileHandler -help -help-compat -help-full -help-man -help-notes -info-switch -lib -merge-points -no-clean -no-libs -opt-switch -region -sets -time -verbose -write-obj -write-vtk</p><p>关联配置：<a href="/dictionaries/system-blockmeshdict/">blockMeshDict</a></p><h2>同版本官方教程</h2><p>以下链接直接指向 OpenFOAM-v2512 标签中的教程目录。先阅读 Allrun 确定网格生成、初始化和依赖，再在自己的工作目录运行。列出教程不表示本网站已执行它的全部计算。</p><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/sphere">mesh/blockMesh/sphere</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/sphere7">mesh/blockMesh/sphere7</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/mergePairs">mesh/blockMesh/mergePairs</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/spheroidProjected">mesh/blockMesh/spheroidProjected</a></li><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/blockMesh/spheroid7Projected">mesh/blockMesh/spheroid7Projected</a></li></ul><pre><code class="language-bash">mkdir -p &quot;&#36;FOAM_RUN&quot;
cd &quot;&#36;FOAM_RUN&quot;
# 先选择一个尚不存在的新目录；保留原教程
cp -r &quot;&#36;FOAM_TUTORIALS/mesh/blockMesh/sphere&quot; ./blockMesh-study
cd ./blockMesh-study
ls
# 查看运行流程后，再决定执行哪些步骤
sed -n &#x27;1,200p&#x27; Allrun</code></pre><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/blockmesh.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: blockMesh
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/blockMesh/blockMesh.C


Usage: blockMesh [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dict &lt;file&gt;      Alternative blockMeshDict
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -merge-points     Geometric point merging instead of topological merging
                    [default for 1912 and earlier].
  -no-clean         Do not remove polyMesh/ directory or files
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -sets             Write cellZones as cellSets too (for processing purposes)
  -time &lt;time&gt;      Specify a time to write mesh to (default: constant)
  -verbose          Force verbose output. (Can be used multiple times)
  -write-obj        Write block edges and centres as obj files and exit
  -write-vtk        Write topology as VTU file and exit
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Block mesh generator.

  The ordering of vertex and face labels within a block as shown below.
  For the local vertex numbering in the sequence 0 to 7:
    Faces 0, 1 (x-direction) are left, right.
    Faces 2, 3 (y-direction) are front, back.
    Faces 4, 5 (z-direction) are bottom, top.

                        7 ---- 6
                 f5     |\     :\     f3
                 |      | 4 ---- 5     \
                 |      3.|....2 |      \
                 |       \|     \|      f2
                 f4       0 ---- 1
    Y  Z
     \ |                f0 ------ f1
      \|
       o--- X

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/blockMesh/blockMesh.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/blockMesh/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
