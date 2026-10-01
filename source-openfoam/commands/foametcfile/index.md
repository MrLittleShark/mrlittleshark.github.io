---
title: "foamEtcFile  按配置层级查找 etc 文件"
layout: reference
description: "按用户、站点和安装目录搜索并输出文件路径。-all 列出全部匹配项，-list 列出搜索目录。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>按用户、站点和安装目录搜索并输出文件路径。-all 列出全部匹配项，-list 列出搜索目录。</p><h2>v2512 源码中的用途</h2><p>Locate user/group/other file as per &#x27;#includeEtc&#x27;. The -mode option is used within etc/{bashrc,cshrc} to ensure that system prefs are respected: \code eval &#36;(foamEtcFile -sh -mode=o prefs.sh) eval &#36;(foamEtcFile -sh -mode=ug prefs.sh) \endcode The -mode option can also be used when chaining settings. For example, in the user ~/.OpenFOAM/config.sh/compiler \code eval &#36;(foamEtcFile -sh -mode=go config.sh/compiler) \endcode</p><h2>使用入口</h2><pre><code class="language-bash">foamEtcFile caseDicts/meshQualityDict</code></pre><h2>使用条件与核对</h2><p>按用户、站点和安装目录搜索并输出文件路径。-all 列出全部匹配项，-list 列出搜索目录。 用法：foamEtcFile [选项] 相对文件 示例：foamEtcFile caseDicts/meshQualityDict
Locate user/group/other file as per &#x27;#includeEtc&#x27;. The -mode option is used within etc/{bashrc,cshrc} to ensure that system prefs are respected: \code eval &#36;(foamEtcFile -sh -mode=o prefs.sh) eval &#36;(foamEtcFile -sh -mode=ug prefs.sh) \endcode The -mode option can also be used when chaining settings. For example, in the user ~/.OpenFOAM/config.sh/compiler \code eval &#36;(foamEtcFile -sh -mode=go config.sh/compiler) \endcode
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-all -config -csh -csh-verbose -etc -help -help-full -list -list-test -mode -quiet -sh -sh-verbose -show-api -show-build -show-patch -silent -version -with-api</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foametcfile.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamEtcFile
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamEtcFile

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamEtcFile [OPTION] fileName [-- args]
       foamEtcFile [OPTION] [-list|-list-test] [fileName]

options:
  -all (-a)         Return all files (otherwise stop after the first match)
  -list (-l)        List directories or files to be checked
  -list-test        List (existing) directories or files to be checked
  -mode=MODE        Any combination of u(user), g(group), o(other)
  -csh              Produce &#x27;source FILE&#x27; output for a csh eval
  -sh               Produce &#x27;. FILE&#x27; output for a sh eval
  -csh-verbose      As per -csh, with additional verbosity
  -sh-verbose       As per -sh,  with additional verbosity
  -config           Add config directory prefix for shell type:
                        with -csh* for a config.csh/ prefix
                        with -sh*  for a config.sh/ prefix
  -etc=[DIR]        set/unset FOAM_CONFIG_ETC for alternative etc directory
  -show-api         Print META-INFO api value and exit
  -show-patch       Print META-INFO patch value and exit
  -show-build       Print META-INFO build value and exit
  -with-api=NUM     Specify alternative api value to search with
  -quiet (-q)       Suppress all normal output
  -silent (-s)      Suppress stderr, except -csh-verbose, -sh-verbose output
  -version | --version  Print version (same as -show-api)
  -help             Display short help and exit
  -help-full        Display full help and exit

Locate user/group/other file as per &#x27;#includeEtc&#x27;
Do not group single character options.


Equivalent options:
  |  -mode=MODE     | -mode MODE  | -m MODE
  |  -prefix=DIR    [obsolete 1812]
  |  -version=VER   [obsolete 1812]

Environment
    FOAM_CONFIG_ETC  : &#36;{FOAM_CONFIG_ETC:-[]}
    FOAM_CONFIG_MODE : &#36;{FOAM_CONFIG_MODE:-[]}
    WM_PROJECT_SITE  : &#36;{WM_PROJECT_SITE:-[PROJECT/site]}


Exit status
    0  when the file is found. Print resolved path to stdout.
    1  for miscellaneous errors.
    2  when the file is not found.</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamEtcFile">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
