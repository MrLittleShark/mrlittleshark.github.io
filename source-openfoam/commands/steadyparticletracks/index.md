---
title: "steadyParticleTracks  导出稳态粒子轨迹为旧式 VTK"
layout: reference
description: "并行结果通常先重构，再导出轨迹。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>并行结果通常先重构，再导出轨迹。</p><h2>v2512 源码中的用途</h2><p>Generate a legacy VTK file of particle tracks for cases that were computed using a steady-state cloud Note: - Case must be re-constructed (if running in parallel) before use</p><h2>使用入口</h2><pre><code class="language-bash">steadyParticleTracks</code></pre><h2>使用条件与核对</h2><p>并行结果通常先重构，再导出轨迹。 用法：steadyParticleTracks [-dict 文件] 示例：steadyParticleTracks
源码说明：Generate a legacy VTK file of particle tracks for cases that were computed using a steady-state cloud Note: - Case must be re-constructed (if running in parallel) before use
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-case -constant -debug-switch -dict -doc -doc-source -fileHandler -help -help-full -help-man -help-notes -info-switch -latestTime -lib -no-libs -noFunctionObjects -noZero -opt-switch -region -time -verbose</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/steadyparticletracks.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: steadyParticleTracks
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/lagrangian/steadyParticleTracks/steadyParticleTracks.C


Usage: steadyParticleTracks [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -constant         Include &#x27;constant/&#x27; dir in the times list
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dict &lt;file&gt;      Alternative particleTrackDict dictionary
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -latestTime       Select the latest time
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -noZero           Exclude &#x27;0/&#x27; dir from the times list
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -time &lt;ranges&gt;    List of ranges. Eg, &#x27;:10,20 40:70 1000:&#x27;, &#x27;none&#x27;, etc
  -verbose          Additional verbosity (can be used multiple times)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Generate a legacy VTK file of particle tracks for cases that were computed
using a steady-state cloud

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/lagrangian/steadyParticleTracks/steadyParticleTracks.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/lagrangian/steadyParticleTracks/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
