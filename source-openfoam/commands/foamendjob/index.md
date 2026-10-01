---
title: "foamEndJob  通过 stopAt 结束算例计算"
layout: reference
description: "需启用 runTimeModifiable。默认在下一写出时刻结束，-now 请求立即写出并结束；PID 使用实际进程号。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>需启用 runTimeModifiable。默认在下一写出时刻结束，-now 请求立即写出并结束；PID 使用实际进程号。</p><h2>v2512 源码中的用途</h2><p>Ends running job on current machine. Called with root,case,pid. - checks if pid exists - modifies controlDict - waits until - pid disappeared - controlDict modified to restore controlDict</p><h2>使用入口</h2><pre><code class="language-bash">foamEndJob -case . -now 12345</code></pre><h2>使用条件与核对</h2><p>需启用 runTimeModifiable。默认在下一写出时刻结束，-now 请求立即写出并结束；PID 使用实际进程号。 用法：foamEndJob [-case 目录] [-now] PID 示例：foamEndJob -case . -now 12345
Ends running job on current machine. Called with root,case,pid. - checks if pid exists - modifies controlDict - waits until - pid disappeared - controlDict modified to restore controlDict
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-case -clear -help -now</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamendjob.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamEndJob
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamEndJob

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamEndJob [OPTION] &lt;pid&gt;
Usage: foamEndJob [OPTION] -c

options:
  -clear            clear any outstanding foamEndJob for the case
  -case &lt;dir&gt;       specify alternative case directory, default is the cwd
  -now              stop at next time step
  -help             print the usage

Tries to end running OpenFOAM application at next write (or optionally
at the next time step). It needs runTimeModifiable switched on in the
controlDict. It changes stopAt in the controlDict and waits for the
job to finish. Restores original controlDict if

    - job has finished
    - controlDict gets modified (by user)
    - foamEndJob gets killed.

The -clear option clears any outstanding foamEndJob for the case.</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamEndJob">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
