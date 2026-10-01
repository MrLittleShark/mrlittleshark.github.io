---
title: "surfaceOrient  统一表面法向"
layout: reference
description: "默认按物体外部观察点定向，-inside 将指定点按内部点处理。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>默认按物体外部观察点定向，-inside 将指定点按内部点处理。</p><h2>v2512 源码中的用途</h2><p>Set normal consistent with respect to a user provided &#x27;outside&#x27; point. If the -inside option is used the point is considered inside.</p><h2>使用入口</h2><pre><code class="language-bash">surfaceOrient body.stl &#x27;(10 10 10)&#x27; bodyOriented.stl</code></pre><h2>使用条件与核对</h2><p>默认按物体外部观察点定向，-inside 将指定点按内部点处理。 用法：surfaceOrient 输入 外部点 输出 示例：surfaceOrient body.stl &#x27;(10 10 10)&#x27; bodyOriented.stl
源码说明：Set normal consistent with respect to a user provided &#x27;outside&#x27; point. If the -inside option is used the point is considered inside.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -doc -doc-source -fileHandler -help -help-full -help-man -help-notes -info-switch -inside -lib -no-libs -noFunctionObjects -opt-switch -scale -usePierceTest</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/surfaceorient.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: surfaceOrient
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceOrient/surfaceOrient.C


Usage: surfaceOrient [OPTIONS] &lt;input&gt; &lt;point&gt; &lt;output&gt;
Arguments:
  &lt;input&gt;           The input surface file
  &lt;point&gt;           The visible &#x27;outside&#x27; point
  &lt;output&gt;          The output surface file
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
  -inside           Treat provided point as being inside
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -scale &lt;factor&gt;   Input geometry scaling factor
  -usePierceTest    Determine orientation by counting number of intersections
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Set face normals consistent with a user-provided &#x27;outside&#x27; point

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceOrient/surfaceOrient.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceOrient/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
