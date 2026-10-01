---
title: "foamPrintJobs  输出 OpenFOAM 作业记录"
layout: reference
description: "与 foamCheckJobs 配合使用。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>与 foamCheckJobs 配合使用。</p><h2>v2512 源码中的用途</h2><p>Uses finishedJobs/ and runningJobs/ and stateFile to print job info</p><h2>使用入口</h2><pre><code class="language-bash">foamPrintJobs jobState</code></pre><h2>使用条件与核对</h2><p>与 foamCheckJobs 配合使用。 用法：foamPrintJobs [状态文件] 示例：foamPrintJobs jobState
Uses finishedJobs/ and runningJobs/ and stateFile to print job info
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamprintjobs.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamPrintJobs
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamPrintJobs

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamPrintJobs [stateFile]

This program prints a table of all running and finished jobs.

It is normally used in conjunction with foamCheckJobs which outputs
a &quot;stateFile&quot; containing the actual process status of all jobs.

If stateFile is not supplied, the default is used:
    &#36;DEFSTATEFILE</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamPrintJobs">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
