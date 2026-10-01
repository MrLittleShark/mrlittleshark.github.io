---
title: "surfaceSplitNonManifolds  拆分表面非流形连接"
layout: reference
description: "拆分后使用 surfaceCheck 检查表面。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>拆分后使用 surfaceCheck 检查表面。</p><h2>v2512 源码中的用途</h2><p>Takes multiply connected surface and tries to split surface at multiply connected edges by duplicating points. Introduces concept of - borderEdge. Edge with 4 faces connected to it. - borderPoint. Point connected to exactly 2 borderEdges. - borderLine. Connected list of borderEdges. By duplicating borderPoints this will split &#x27;borderLines&#x27;. As a preprocessing step it can detect borderEdges without any borderPoints and explicitly split these triangles. The problems in this algorithm are: - determining which two (of the four) faces form a surface. Done by walking face-edge-face while keeping and edge or point on the borderEdge borderPoint. - determining the outwards pointing normal to be used to slightly offset the duplicated point. Uses sortedEdgeFaces quite a bit. Is tested on simple borderLines resulting from extracting a surface from a hex mesh. Will quite possibly go wrong on more complicated border lines (i.e. ones forming a loop). Dumps surface every so often since might take a long time to complete.</p><h2>使用入口</h2><pre><code class="language-bash">surfaceSplitNonManifolds body.stl manifold.stl</code></pre><h2>使用条件与核对</h2><p>拆分后使用 surfaceCheck 检查表面。 用法：surfaceSplitNonManifolds 输入 输出 示例：surfaceSplitNonManifolds body.stl manifold.stl
源码说明：Takes multiply connected surface and tries to split surface at multiply connected edges by duplicating points. Introduces concept of - borderEdge. Edge with 4 faces connected to it. - borderPoint. Point connected to exactly 2 borderEdges. - borderLine. Connected list of borderEdges. By duplicating borderPoints this will split &#x27;borderLines&#x27;. As a preprocessing step it can detect borderEdges without any borderPoints and explicitly split these triangles. The problems in this algorithm are: - determining which two (of the four) faces form a surface. Done by walking face-edge-face while keeping and edge or point on the borderEdge borderPoint. - determining the outwards pointing normal to be used to slightly offset the duplicated point. Uses sortedEdgeFaces quite a bit. Is tested on simple borderLines resulting from extracting a surface from a hex mesh. Will quite possibly go wrong on more complicated border lines (i.e. ones forming a loop). Dumps surface every so often since might take a long time to complete.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug -debug-switch -doc -doc-source -fileHandler -help -help-full -help-man -help-notes -info-switch -lib -no-libs -noFunctionObjects -opt-switch</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/surfacesplitnonmanifolds.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: surfaceSplitNonManifolds
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceSplitNonManifolds/surfaceSplitNonManifolds.C


Usage: surfaceSplitNonManifolds [OPTIONS] &lt;input&gt; &lt;output&gt;
Arguments:
  &lt;input&gt;           The input surface file
  &lt;output&gt;          The output surface file
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug            Add debugging output
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
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Split multiply connected surface edges by duplicating points

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceSplitNonManifolds/surfaceSplitNonManifolds.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceSplitNonManifolds/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
