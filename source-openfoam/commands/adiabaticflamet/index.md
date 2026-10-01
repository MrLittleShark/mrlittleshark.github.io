---
title: "adiabaticFlameT  计算绝热火焰温度"
layout: reference
description: "输入包括热物性和组分配置。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>输入包括热物性和组分配置。</p><h2>v2512 源码中的用途</h2><p>Calculate adiabatic flame temperature for a given fuel over a range of unburnt temperatures and equivalence ratios.</p><h2>使用入口</h2><pre><code class="language-bash">adiabaticFlameT adiabaticFlameTDict</code></pre><h2>使用条件与核对</h2><p>输入包括热物性和组分配置。 用法：adiabaticFlameT 控制文件 示例：adiabaticFlameT adiabaticFlameTDict
源码说明：Calculate adiabatic flame temperature for a given fuel over a range of unburnt temperatures and equivalence ratios.
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -debug-switch -doc -doc-source -fileHandler -help -help-compat -help-full -help-man -help-notes -info-switch -lib -no-libs -opt-switch</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/adiabaticflamet.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: adiabaticFlameT
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/thermophysical/adiabaticFlameT/adiabaticFlameT.C


Usage: adiabaticFlameT [OPTIONS] &lt;controlFile&gt;
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
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Calculate the adiabatic flame temperature for a given fuel over a  range of
unburnt temperatures and equivalence ratios.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/thermophysical/adiabaticFlameT/adiabaticFlameT.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/thermophysical/adiabaticFlameT/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
