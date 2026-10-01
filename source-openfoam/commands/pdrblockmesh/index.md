---
title: "PDRblockMesh  生成 PDR 专用直角单块网格"
layout: reference
description: "读取 PDRblockMeshDict。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>读取 PDRblockMeshDict。</p><h2>v2512 源码中的用途</h2><p>A specialized single-block mesh generator for a rectilinear mesh in x-y-z. Uses the mesh description found in - \c system/PDRblockMeshDict</p><h2>使用入口</h2><pre><code class="language-bash">PDRblockMesh</code></pre><h2>使用条件与核对</h2><p>读取 PDRblockMeshDict。 用法：PDRblockMesh [-dict 文件] 示例：PDRblockMesh
源码说明：A specialized single-block mesh generator for a rectilinear mesh in x-y-z. Uses the mesh description found in - \c system/PDRblockMeshDict
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -dict -doc -doc-source -fileHandler -help -help-compat -help-full -help-man -help-notes -info-switch -lib -no-clean -no-libs -no-outer -opt-switch -print-dict -time -write-dict</p><h2>同版本官方教程</h2><p>以下链接直接指向 OpenFOAM-v2512 标签中的教程目录。先阅读 Allrun 确定网格生成、初始化和依赖，再在自己的工作目录运行。列出教程不表示本网站已执行它的全部计算。</p><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/PDRblockMesh/box0">mesh/PDRblockMesh/box0</a></li></ul><pre><code class="language-bash">mkdir -p &quot;&#36;FOAM_RUN&quot;
cd &quot;&#36;FOAM_RUN&quot;
# 先选择一个尚不存在的新目录；保留原教程
cp -r &quot;&#36;FOAM_TUTORIALS/mesh/PDRblockMesh/box0&quot; ./PDRblockMesh-study
cd ./PDRblockMesh-study
ls
# 查看运行流程后，再决定执行哪些步骤
sed -n &#x27;1,200p&#x27; Allrun</code></pre><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/pdrblockmesh.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: PDRblockMesh
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/PDRblockMesh/PDRblockMesh.C


Usage: PDRblockMesh [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dict &lt;file&gt;      Alternative PDRblockMeshDict
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-clean         Do not remove polyMesh/ directory or files
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -no-outer         Create without any other region
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -print-dict       Print blockMeshDict equivalent and exit
  -time &lt;time&gt;      Specify a time to write mesh to (default: constant)
  -write-dict       Write system/blockMeshDict.PDRblockMesh and exit
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

A block mesh generator for a rectilinear mesh in x-y-z.
  The ordering of vertex and face labels within a block as shown below.
  For the local vertex numbering in the sequence 0 to 7:
    Faces 0, 1  ==  x-min, x-max.
    Faces 2, 3  ==  y-min, y-max.
    Faces 4, 5  ==  z-min, z-max.

                        7 ---- 6
                 f5     |\     |\     f3
                 |      | 4 ---- 5     \
                 |      3 |--- 2 |      \
                 |       \|     \|      f2
                 f4       0 ---- 1
    Y  Z
     \ |                f0 ------ f1
      \|
       O--- X

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/PDRblockMesh/PDRblockMesh.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/PDRblockMesh/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
