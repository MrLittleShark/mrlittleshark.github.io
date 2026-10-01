---
title: "foamCloneCase  复制算例初始场及配置"
layout: reference
description: "默认复制初始时刻、constant 和 system。-latestTime 选择最后时刻，-force 覆盖目标目录。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>默认复制初始时刻、constant 和 system。-latestTime 选择最后时刻，-force 覆盖目标目录。</p><h2>v2512 源码中的用途</h2><p>Create a new case directory that includes time, system and constant directories from a source case. The time directory is the first time directory by default Requires foamListTimes</p><h2>使用入口</h2><pre><code class="language-bash">foamCloneCase ../cavity ./cavityCopy</code></pre><h2>使用条件与核对</h2><p>默认复制初始时刻、constant 和 system。-latestTime 选择最后时刻，-force 覆盖目标目录。 用法：foamCloneCase [选项] 源算例 目标算例 示例：foamCloneCase ../cavity ./cavityCopy
Create a new case directory that includes time, system and constant directories from a source case. The time directory is the first time directory by default Requires foamListTimes
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-force -h -l</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamclonecase.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamCloneCase
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCloneCase

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamCloneCase [OPTION] &lt;sourceCase&gt; &lt;targetCase&gt;
options:
  -force              Force overwrite of existing target
  -l | -latestTime    Select the latest time directory
  -h | -help          Print the usage

Create a new &lt;targetCase&gt; case directory with a copy of time, system, constant
directories from &lt;sourceCase&gt; directory.
The time directory is the first time directory by default.</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCloneCase">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
