---
title: "wclean · 清理当前源码目标的编译中间文件"
layout: reference
description: "清理当前源码目标的编译中间文件。"
cms_slug: "command-wclean"
---

<p>清理当前源码目标的编译中间文件。</p><h2>清理应用后重新编译</h2>
<pre><code class="language-bash">wclean
wmake
</code></pre>
<p>适合更换编译配置或排除旧中间文件影响。运行位置应为对应源码目录。</p>
<h2>清理并重编译共享库</h2>
<pre><code class="language-bash">wclean libso
wmake libso
</code></pre>
<p>用于 Make/files 中以 LIB 声明的目标。头文件搜索和链接库仍由 Make/options 控制。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-a | -all</td><td>All subdirectories, uses Allwclean, Allclean if they exist</td></tr><tr><td>-s | -silent</td><td>Silent mode (ignored - for compatibility with wmake)</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr><tr><td>-build</td><td>Remove specified build/ object directories</td></tr><tr><td>-platform</td><td>Remove specified platforms/ object directories If executed in the main project directory, it will also remove deprecated object directories and respective binaries that refer to no-longer-existing source code.</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wclean [OPTION] [dir]
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


Clean up the wmake control directory Make/\$WM_OPTIONS and remove the
lnInclude directories generated for libraries.

Special targets:
  all               Same as -all option
  exe | lib | libo | libso
  empty             Remove empty sub-directories for the requested dir.
                    If executed in the main project directory, it will also
                    remove deprecated object directories and respective binaries
                    that refer to no-longer-existing source code.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wclean">源码与说明</a> · <a href="/assets/command-help/wclean.txt">帮助文本</a></p>
