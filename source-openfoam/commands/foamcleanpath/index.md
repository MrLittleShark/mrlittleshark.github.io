---
title: "foamCleanPath · 删除重复项或指定条目后输出路径文本，当前 shell 的 PATH 保持不变"
layout: reference
description: "删除重复项或指定条目后输出路径文本，当前 shell 的 PATH 保持不变。"
cms_slug: "command-foamcleanpath"
---

<p>删除重复项或指定条目后输出路径文本，当前 shell 的 PATH 保持不变。</p><h2>开始前</h2>
<p>操作冒号分隔的路径字符串。默认打印结果，不直接修改父 shell；filter 按路径前缀匹配，并带有 sed 正则语义。</p>
<h2>示例 1：消除重复项</h2>
<pre><code class="language-bash">foamCleanPath "/usr/bin:/tmp/tools:/usr/bin"
</code></pre>
<p>输出去重后的路径串，保留第一次出现的项。</p>
<h2>示例 2：移除旧工具前缀</h2>
<pre><code class="language-bash">foamCleanPath "/tmp/oldfoam/bin:/usr/bin:/tmp/newfoam/bin" /tmp/oldfoam
</code></pre>
<p>删除匹配旧安装前缀的项，保留系统目录与新路径。</p>
<h2>示例 3：读取现有变量</h2>
<pre><code class="language-bash">foamCleanPath -env=PATH
</code></pre>
<p>从 PATH 获取输入，打印清理结果。</p>
<h2>示例 4：去除不可访问目录</h2>
<pre><code class="language-bash">foamCleanPath -strip "/usr/bin:/path/that/does/not/exist"
</code></pre>
<p>-strip 过滤不存在或不可访问的目录，输出保留项。</p>
<h2>示例 5：更新自定义路径变量</h2>
<pre><code class="language-bash">export MY_TOOL_PATH="/usr/bin:/tmp/tools:/usr/bin"
cleaned=$(foamCleanPath -env=MY_TOOL_PATH) &amp;&amp; export MY_TOOL_PATH="$cleaned"
</code></pre>
<p>先捕获成功结果再更新变量，避免清理失败时覆盖旧值。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-env=NAME</code></td><td>Evaluate NAME to obtain initial content, Accepts &quot;-env=-path&quot;, &quot;-env=-lib&quot; shortcuts for PATH and LD_LIBRARY_PATH (FOAM_LD_LIBRARY_PATH on Darwin)</td></tr><tr><td><code>-sh=NAME</code></td><td>Produce &#x27;NAME=...&#x27; output for sh eval</td></tr><tr><td><code>-csh=NAME</code></td><td>Produce &#x27;setenv NAME ...&#x27; output for csh eval</td></tr><tr><td><code>-sh-env=NAME</code></td><td>Same as -sh=NAME -env=NAME</td></tr><tr><td><code>-csh-env=NAME</code></td><td>Same as -csh=NAME -env=NAME</td></tr><tr><td><code>-sh-path | -csh-path</code></td><td>Same as -[c]sh-env=PATH</td></tr><tr><td><code>-sh-lib</code></td><td>| -csh-lib   Same as -[c]sh-env=LD_LIBRARY_PATH (FOAM_LD_LIBRARY_PATH on Darwin)</td></tr><tr><td><code>-debug</code></td><td>Print debug information to stderr</td></tr><tr><td><code>-strip</code></td><td>Remove inaccessible directories</td></tr><tr><td><code>-verbose</code></td><td>Report some progress (input, output, ...)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamCleanPath [OPTION] ENVNAME [filter] .. [filter]
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
