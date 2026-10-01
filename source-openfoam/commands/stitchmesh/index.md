---
title: "stitchMesh  缝合两个网格边界"
layout: reference
description: "-perfect 要求几何匹配；其余接口可按相应条件采用 -partial 或 -integral。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>-perfect 要求几何匹配；其余接口可按相应条件采用 -partial 或 -integral。</p><h2>v2512 源码中的用途</h2><p>&#x27;Stitches&#x27; a mesh. Takes a mesh and two patches and merges the faces on the two patches (if geometrically possible) so the faces become internal. Can do - &#x27;perfect&#x27; match: faces and points on patches align exactly. Order might be different though. - &#x27;integral&#x27; match: where the surfaces on both patches exactly match but the individual faces not - &#x27;partial&#x27; match: where the non-overlapping part of the surface remains in the respective patch. Note : Is just a front-end to perfectInterface/slidingInterface. Comparable to running a meshModifier of the form (if masterPatch is called &quot;M&quot; and slavePatch &quot;S&quot;):</p><h2>使用入口</h2><pre><code class="language-bash">stitchMesh -perfect sideA sideB -overwrite</code></pre><h2>使用条件与核对</h2><p>-perfect 要求几何匹配；其余接口可按相应条件采用 -partial 或 -integral。 用法：stitchMesh [选项] 主patch 从patch 示例：stitchMesh -perfect sideA sideB -overwrite
源码说明：&#x27;Stitches&#x27; a mesh. Takes a mesh and two patches and merges the faces on the two patches (if geometrically possible) so the faces become internal. Can do - &#x27;perfect&#x27; match: faces and points on patches align exactly. Order might be different though. - &#x27;integral&#x27; match: where the surfaces on both patches exactly match but the individual faces not - &#x27;partial&#x27; match: where the non-overlapping part of the surface remains in the respective patch. Note : Is just a front-end to perfectInterface/slidingInterface. Comparable to running a meshModifier of the form (if masterPatch is called &quot;M&quot; and slavePatch &quot;S&quot;):
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -dict -doc -doc-source -fileHandler -help -help-compat -help-full -help-man -help-notes -info-switch -integral -intermediate -lib -no-libs -opt-switch -overwrite -partial -perfect -region -toleranceDict</p><h2>同版本官方教程</h2><p>以下链接直接指向 OpenFOAM-v2512 标签中的教程目录。先阅读 Allrun 确定网格生成、初始化和依赖，再在自己的工作目录运行。列出教程不表示本网站已执行它的全部计算。</p><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/stitchMesh/simple-cube1">mesh/stitchMesh/simple-cube1</a></li></ul><pre><code class="language-bash">mkdir -p &quot;&#36;FOAM_RUN&quot;
cd &quot;&#36;FOAM_RUN&quot;
# 先选择一个尚不存在的新目录；保留原教程
cp -r &quot;&#36;FOAM_TUTORIALS/mesh/stitchMesh/simple-cube1&quot; ./stitchMesh-study
cd ./stitchMesh-study
ls
# 查看运行流程后，再决定执行哪些步骤
sed -n &#x27;1,200p&#x27; Allrun</code></pre><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/stitchmesh.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: stitchMesh
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/stitchMesh/stitchMesh.C


Usage: stitchMesh [OPTIONS] [&lt;master&gt; &lt;slave&gt;]
Arguments:
  &lt;master&gt;          The master patch name (non-dictionary mode)
  &lt;slave&gt;           The slave patch name (non-dictionary mode)
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dict &lt;file&gt;      Alternative stitchMeshDict
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -integral         Couple integral master/slave patches (2 argument mode:
                    default)
  -intermediate     Write intermediate stages, not just the final result
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -partial          Couple partially overlapping master/slave patches (2
                    argument mode)
  -perfect          Couple perfectly aligned master/slave patches (2 argument
                    mode)
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -toleranceDict &lt;file&gt;
                    Dictionary file with tolerances
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Merge the faces on specified patches (if geometrically possible) so that the
faces become internal.
This utility can be called without arguments (uses stitchMeshDict) or with
two arguments (master/slave patch names).

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/stitchMesh/stitchMesh.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/stitchMesh/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
