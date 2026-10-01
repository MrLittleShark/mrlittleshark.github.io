---
title: "surfaceBooleanFeatures  提取表面布尔运算特征线"
layout: reference
description: "支持 intersection、union 和 difference，相关构建可依赖 CGAL。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>支持 intersection、union 和 difference，相关构建可依赖 CGAL。</p><h2>v2512 源码中的用途</h2><p>Generates the extendedFeatureEdgeMesh for the interface between a boolean operation on two surfaces. Assumes that the orientation of the surfaces is correct: - if the operation is union or intersection, that both surface&#x27;s normals (n) have the same orientation with respect to a point, i.e. surfaces A and B are orientated the same with respect to point x:</p><h2>使用入口</h2><pre><code class="language-bash">surfaceBooleanFeatures intersection a.stl b.stl</code></pre><h2>使用条件与核对</h2><p>支持 intersection、union 和 difference，相关构建可依赖 CGAL。 用法：surfaceBooleanFeatures 操作 表面1 表面2 示例：surfaceBooleanFeatures intersection a.stl b.stl
源码说明：Generates the extendedFeatureEdgeMesh for the interface between a boolean operation on two surfaces. Assumes that the orientation of the surfaces is correct: - if the operation is union or intersection, that both surface&#x27;s normals (n) have the same orientation with respect to a point, i.e. surfaces A and B are orientated the same with respect to point x:
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -doc -doc-source -fileHandler -help -help-full -help-man -help-notes -info-switch -invertedSpace -lib -no-cgal -no-libs -noFunctionObjects -opt-switch -perturb -scale -surf1Baffle -surf2Baffle -trim</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/surfacebooleanfeatures.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: surfaceBooleanFeatures
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceBooleanFeatures/surfaceBooleanFeatures.C


Usage: surfaceBooleanFeatures [OPTIONS] &lt;action&gt; &lt;surface1&gt; &lt;surface2&gt;
Arguments:
  &lt;action&gt;          One of (intersection | union | difference)
  &lt;surface1&gt;        The input surface file 1
  &lt;surface2&gt;        The input surface file 2
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
  -invertedSpace    Do the surfaces have inverted space orientation, i.e. a
                    point at infinity is considered inside. This is only
                    sensible for union and intersection.
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-cgal          Do not use CGAL algorithms
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -perturb          Perturb surface points to escape degenerate intersections
  -scale &lt;factor&gt;   Geometry scaling factor (both surfaces)
  -surf1Baffle      Mark surface 1 as a baffle
  -surf2Baffle      Mark surface 2 as a baffle
  -trim &lt;((surface1 volumeType) .. (surfaceN volumeType))&gt;
                    Trim resulting intersection with additional surfaces;
                    volumeType is &#x27;inside&#x27; (keep (parts of) edges that are
                    inside), &#x27;outside&#x27; (keep (parts of) edges that are outside)
                    or &#x27;mixed&#x27; (keep all)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Generates a extendedFeatureEdgeMesh for the interface created by a boolean
operation on two surfaces. [Compiled with CGAL]

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceBooleanFeatures/surfaceBooleanFeatures.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceBooleanFeatures/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
