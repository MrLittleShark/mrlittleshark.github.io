---
title: "surfaceSplitByPatch  按区域拆分表面文件"
layout: reference
description: "-patches 指定待拆分区域。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>-patches 指定待拆分区域。</p><h2>v2512 源码中的用途</h2><p>Writes surface regions to separate files.</p><h2>使用入口</h2><pre><code class="language-bash">surfaceSplitByPatch body.stl</code></pre><h2>使用条件与核对</h2><p>-patches 指定待拆分区域。 用法：surfaceSplitByPatch 输入 [选项] 示例：surfaceSplitByPatch body.stl
源码说明：Writes surface regions to separate files.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -doc -doc-source -exclude-patches -fileHandler -help -help-compat -help-full -help-man -help-notes -info-switch -lib -no-libs -noFunctionObjects -opt-switch -patches</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/surfacesplitbypatch.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: surfaceSplitByPatch
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceSplitByPatch/surfaceSplitByPatch.C


Usage: surfaceSplitByPatch [OPTIONS] &lt;input&gt;
Arguments:
  &lt;input&gt;           The input surface file
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -exclude-patches &lt;wordRes&gt;
                    Exclude single or multiple patches (name or regex) from
                    extracting.
                    Eg, &#x27;outlet&#x27; or &#x27;( inlet &quot;.*Wall&quot; )&#x27;
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
  -patches &lt;wordRes&gt;
                    Specify single patch or multiple patches to extract
                    Eg, &#x27;top&#x27; or &#x27;( front &quot;.*back&quot; )&#x27;
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Write surface mesh regions to separate files

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceSplitByPatch/surfaceSplitByPatch.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceSplitByPatch/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
