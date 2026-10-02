---
title: "foamEtcFile · 按用户、站点和安装目录搜索并输出文件路径"
layout: reference
description: "按用户、站点和安装目录搜索并输出文件路径。-all 列出全部匹配项，-list 列出搜索目录。"
cms_slug: "command-foametcfile"
---

<p>按用户、站点和安装目录搜索并输出文件路径。-all 列出全部匹配项，-list 列出搜索目录。</p><h2>用法</h2><pre><code class="language-bash">foamEtcFile caseDicts/meshQualityDict</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-all (-a)</td><td>Return all files (otherwise stop after the first match)</td></tr><tr><td>-list (-l)</td><td>列出可用的预配置函数。</td></tr><tr><td>-list-test</td><td>List (existing) directories or files to be checked</td></tr><tr><td>-mode=MODE</td><td>Any combination of u(user), g(group), o(other)</td></tr><tr><td>-csh</td><td>Produce &#x27;source FILE&#x27; output for a csh eval</td></tr><tr><td>-sh</td><td>Produce &#x27;. FILE&#x27; output for a sh eval</td></tr><tr><td>-csh-verbose</td><td>As per -csh, with additional verbosity</td></tr><tr><td>-sh-verbose</td><td>As per -sh,  with additional verbosity</td></tr><tr><td>-config</td><td>Add config directory prefix for shell type: with -csh* for a config.csh/ prefix with -sh*  for a config.sh/ prefix</td></tr><tr><td>-etc=[DIR]</td><td>set/unset FOAM_CONFIG_ETC for alternative etc directory</td></tr><tr><td>-show-api</td><td>Print META-INFO api value and exit</td></tr><tr><td>-show-patch</td><td>Print META-INFO patch value and exit</td></tr><tr><td>-show-build</td><td>Print META-INFO build value and exit</td></tr><tr><td>-with-api=NUM</td><td>Specify alternative api value to search with</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamEtcFile [OPTION] fileName [-- args]
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
    FOAM_CONFIG_ETC  : ${FOAM_CONFIG_ETC:-[]}
    FOAM_CONFIG_MODE : ${FOAM_CONFIG_MODE:-[]}
    WM_PROJECT_SITE  : ${WM_PROJECT_SITE:-[PROJECT/site]}


Exit status
    0  when the file is found. Print resolved path to stdout.
    1  for miscellaneous errors.
    2  when the file is not found.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamEtcFile">源码与说明</a> · <a href="/assets/command-help/foametcfile.txt">帮助文本</a></p>
