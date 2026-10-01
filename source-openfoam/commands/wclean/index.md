---
title: "wclean"
layout: reference
description: "清理当前应用的构建产物；执行前确认工作目录。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>清理当前应用的构建产物；执行前确认工作目录。</p><h2>v2512 源码中的用途</h2><p>Clean up the wmake control directory Make/\&#36;WM_OPTIONS and remove the lnInclude directories generated for libraries.</p><h2>使用入口</h2><pre><code class="language-bash">wclean</code></pre><h2>使用条件与核对</h2><p>清理当前应用的构建产物；执行前确认工作目录。 示例中的算例名、路径与主机名须按实际环境替换。
Clean up the wmake control directory Make/\&#36;WM_OPTIONS and remove the lnInclude directories generated for libraries.
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-a -build -help -help-full -platform -s</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/wclean.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: wclean
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wclean

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: wclean [OPTION] [dir]
       wclean [OPTION] target [dir [MakeDir]]
       wclean -subcommand ...

options:
  -a | -all         All subdirectories, uses Allwclean, Allclean if they exist
  -s | -silent      Silent mode (ignored - for compatibility with wmake)
  -help             Display short help and exit
  -help-full        Display full help and exit

subcommands (wclean subcommand -help for more information):

  -build           Remove specified build/ object directories
  -platform        Remove specified platforms/ object directories

  -build -platform


Clean up the wmake control directory Make/\&#36;WM_OPTIONS and remove the
lnInclude directories generated for libraries.

Special targets:
  all               Same as -all option
  exe | lib | libo | libso
  empty             Remove empty sub-directories for the requested dir.
                    If executed in the main project directory, it will also
                    remove deprecated object directories and respective binaries
                    that refer to no-longer-existing source code.</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wclean">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
