---
title: "surfaceAdd  合并表面数据"
layout: reference
description: "连接两个表面数据集，不执行几何布尔并集。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>连接两个表面数据集，不执行几何布尔并集。</p><h2>v2512 源码中的用途</h2><p>Add two surfaces. Does geometric merge on points. Does not check for overlapping/intersecting triangles. Keeps patches separate by renumbering.</p><h2>使用入口</h2><pre><code class="language-bash">surfaceAdd a.stl b.stl combined.stl</code></pre><h2>使用条件与核对</h2><p>连接两个表面数据集，不执行几何布尔并集。 用法：surfaceAdd 表面1 表面2 输出 示例：surfaceAdd a.stl b.stl combined.stl
源码说明：Add two surfaces. Does geometric merge on points. Does not check for overlapping/intersecting triangles. Keeps patches separate by renumbering.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -doc -doc-source -fileHandler -help -help-full -help-man -help-notes -info-switch -lib -mergeRegions -no-libs -noFunctionObjects -opt-switch -points -scale -verbose</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/surfaceadd.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: surfaceAdd
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceAdd/surfaceAdd.C


Usage: surfaceAdd [OPTIONS] &lt;surface1&gt; &lt;surface2&gt; &lt;output&gt;
Arguments:
  &lt;surface1&gt;        The input surface file 1
  &lt;surface2&gt;        The input surface file 2
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
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -mergeRegions     Combine regions from both surfaces
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -points &lt;file&gt;    Provide additional points
  -scale &lt;factor&gt;   Geometry scaling factor on input surfaces
  -verbose          Additional verbosity (can be used multiple times)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Add two surfaces via a geometric merge on points. Does not check for
overlapping/intersecting triangles.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceAdd/surfaceAdd.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceAdd/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
