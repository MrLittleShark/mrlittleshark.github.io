---
title: "foamTestTutorial  执行教程测试"
layout: reference
description: "默认在临时目录运行一个时间步。-full 执行完整教程，-output=DIR 保留输出，指定目录须预先建立。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>默认在临时目录运行一个时间步。-full 执行完整教程，-output=DIR 保留输出，指定目录须预先建立。</p><h2>v2512 源码中的用途</h2><p>Run foamRunTutorials with specified tutorial directories Creates/destroys a temporary directory for each test unless an output directory has been specified.</p><h2>使用入口</h2><pre><code class="language-bash">foamTestTutorial -1 incompressible/icoFoam/cavity/cavity</code></pre><h2>使用条件与核对</h2><p>默认在临时目录运行一个时间步。-full 执行完整教程，-output=DIR 保留输出，指定目录须预先建立。 用法：foamTestTutorial [选项] 教程相对路径 示例：foamTestTutorial -1 incompressible/icoFoam/cavity/cavity
Run foamRunTutorials with specified tutorial directories Creates/destroys a temporary directory for each test unless an output directory has been specified.
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-debian -force -full -help -output -parallel -serial</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamtesttutorial.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamTestTutorial
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamTestTutorial

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

usage: foamTestTutorial [OPTION] dir [.. dirN]

options:
  -1            Run only one time step (modifies controlDict) [default]
  -full         Run to completion (does not modify controlDict)
  -force        Force overwrite of existing output directories
  -debian       Adjust for running with autopkgtest
  -serial       Prefer Allrun-serial if available
  -parallel     Prefer Allrun-parallel if available
  -output=DIR   Output directory (default: a temporary directory)
  -help         Print the usage

Run foamRunTutorials with specified tutorial directories
Creates/destroys a temporary directory for each test unless
an output directory has been specified.</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamTestTutorial">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
