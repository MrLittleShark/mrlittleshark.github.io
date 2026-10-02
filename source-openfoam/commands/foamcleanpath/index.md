---
title: "foamCleanPath · 删除重复项或指定条目后输出路径文本，当前 shell 的 PATH 保持不变"
layout: reference
description: "删除重复项或指定条目后输出路径文本，当前 shell 的 PATH 保持不变。"
cms_slug: "command-foamcleanpath"
---

<p>删除重复项或指定条目后输出路径文本，当前 shell 的 PATH 保持不变。</p><h2>用法</h2><pre><code class="language-bash">foamCleanPath &quot;$PATH&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-env=NAME</td><td>Evaluate NAME to obtain initial content, Accepts &quot;-env=-path&quot;, &quot;-env=-lib&quot; shortcuts for PATH and LD_LIBRARY_PATH (FOAM_LD_LIBRARY_PATH on Darwin)</td></tr><tr><td>-sh=NAME</td><td>Produce &#x27;NAME=...&#x27; output for sh eval</td></tr><tr><td>-csh=NAME</td><td>Produce &#x27;setenv NAME ...&#x27; output for csh eval</td></tr><tr><td>-sh-env=NAME</td><td>Same as -sh=NAME -env=NAME</td></tr><tr><td>-csh-env=NAME</td><td>Same as -csh=NAME -env=NAME</td></tr><tr><td>-sh-path | -csh-path</td><td>Same as -[c]sh-env=PATH</td></tr><tr><td>-sh-lib</td><td>| -csh-lib   Same as -[c]sh-env=LD_LIBRARY_PATH (FOAM_LD_LIBRARY_PATH on Darwin)</td></tr><tr><td>-debug</td><td>Print debug information to stderr</td></tr><tr><td>-strip</td><td>Remove inaccessible directories</td></tr><tr><td>-verbose</td><td>Report some progress (input, output, ...)</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamCleanPath [OPTION] ENVNAME [filter] .. [filter]
       foamCleanPath [OPTION] -env=name [filter] .. [filter]
options:
  -env=NAME         Evaluate NAME to obtain initial content,
                    Accepts &quot;-env=-path&quot;, &quot;-env=-lib&quot; shortcuts for PATH
                    and LD_LIBRARY_PATH (FOAM_LD_LIBRARY_PATH on Darwin)
  -sh=NAME          Produce &#x27;NAME=...&#x27; output for sh eval
  -csh=NAME         Produce &#x27;setenv NAME ...&#x27; output for csh eval
  -sh-env=NAME      Same as -sh=NAME -env=NAME
  -csh-env=NAME     Same as -csh=NAME -env=NAME
  -sh-path | -csh-path  Same as -[c]sh-env=PATH
  -sh-lib  | -csh-lib   Same as -[c]sh-env=LD_LIBRARY_PATH
                        (FOAM_LD_LIBRARY_PATH on Darwin)
  -debug            Print debug information to stderr
  -strip            Remove inaccessible directories
  -verbose          Report some progress (input, output, ...)
  -help             Print the usage

Prints its argument (which should be a &#x27;:&#x27; separated list) cleansed from
  * duplicate elements
  * elements whose start matches one of the filters
  * inaccessible directories (the -strip option)

Exit status
    0  on success
    1  general error
    2  initial value of ENVNAME is empty</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCleanPath">源码与说明</a> · <a href="/assets/command-help/foamcleanpath.txt">帮助文本</a></p>
