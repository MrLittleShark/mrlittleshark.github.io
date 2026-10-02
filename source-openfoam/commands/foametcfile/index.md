---
title: "foamEtcFile · 按用户、站点和安装目录搜索并输出文件路径"
layout: reference
description: "按用户、站点和安装目录搜索并输出文件路径。-all 列出全部匹配项，-list 列出搜索目录。"
cms_slug: "command-foametcfile"
---

<p>按用户、站点和安装目录搜索并输出文件路径。-all 列出全部匹配项，-list 列出搜索目录。</p><h2>开始前</h2>
<p>已加载环境。搜索优先级由用户、站点和安装的 etc 配置组成，-mode 可限定来源。</p>
<h2>示例 1：定位全局控制字典</h2>
<pre><code class="language-bash">foamEtcFile controlDict
</code></pre>
<p>输出搜索到的首个 etc/controlDict 路径。</p>
<h2>示例 2：列出全部同名配置</h2>
<pre><code class="language-bash">foamEtcFile -all controlDict
</code></pre>
<p>显示所有匹配路径，用于检查个人配置是否覆盖安装默认值。</p>
<h2>示例 3：仅查安装配置</h2>
<pre><code class="language-bash">foamEtcFile -mode=o controlDict
</code></pre>
<p>o 选择安装级目录，排除用户和站点级覆盖。</p>
<h2>示例 4：查看有效搜索目录</h2>
<pre><code class="language-bash">foamEtcFile -list-test
</code></pre>
<p>打印实际存在的搜索目录，用于定位可放置自定义配置的位置。</p>
<h2>示例 5：读取配置内容</h2>
<pre><code class="language-bash">configFile=$(foamEtcFile controlDict) &amp;&amp; less "$configFile"
</code></pre>
<p>将找到的路径传给 less，适合检查 optimisation/debug 开关。</p>
<h2>示例 6：查询安装 API</h2>
<pre><code class="language-bash">foamEtcFile -show-api
</code></pre>
<p>从 META-INFO 获取 API 数字，v2512 对应 2512。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-all (-a)</code></td><td>Return all files (otherwise stop after the first match)</td></tr><tr><td><code>-list (-l)</code></td><td>列出可用的预配置函数。</td></tr><tr><td><code>-list-test</code></td><td>List (existing) directories or files to be checked</td></tr><tr><td><code>-mode=MODE</code></td><td>Any combination of u(user), g(group), o(other)</td></tr><tr><td><code>-csh</code></td><td>Produce &#x27;source FILE&#x27; output for a csh eval</td></tr><tr><td><code>-sh</code></td><td>Produce &#x27;. FILE&#x27; output for a sh eval</td></tr><tr><td><code>-csh-verbose</code></td><td>As per -csh, with additional verbosity</td></tr><tr><td><code>-sh-verbose</code></td><td>As per -sh,  with additional verbosity</td></tr><tr><td><code>-config</code></td><td>Add config directory prefix for shell type: with -csh* for a config.csh/ prefix with -sh*  for a config.sh/ prefix</td></tr><tr><td><code>-etc=[DIR]</code></td><td>set/unset FOAM_CONFIG_ETC for alternative etc directory</td></tr><tr><td><code>-show-api</code></td><td>Print META-INFO api value and exit</td></tr><tr><td><code>-show-patch</code></td><td>Print META-INFO patch value and exit</td></tr><tr><td><code>-show-build</code></td><td>Print META-INFO build value and exit</td></tr><tr><td><code>-with-api=NUM</code></td><td>Specify alternative api value to search with</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamEtcFile [OPTION] fileName [-- args]
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
