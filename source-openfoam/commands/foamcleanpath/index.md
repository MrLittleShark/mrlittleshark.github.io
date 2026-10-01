---
title: "foamCleanPath  清理路径列表"
layout: reference
description: "删除重复项或指定条目后输出路径文本，当前 shell 的 PATH 保持不变。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>删除重复项或指定条目后输出路径文本，当前 shell 的 PATH 保持不变。</p><h2>v2512 源码中的用途</h2><p>Usage: foamCleanPath [OPTION] path [filter] .. [filter] foamCleanPath [OPTION] -env=name [filter] .. [filter] Prints its argument (which should be a &#x27;:&#x27; separated path) without the following: - duplicate elements - elements matching the specified filter(s) - inaccessible directories (with the -strip option)</p><h2>使用入口</h2><pre><code class="language-bash">foamCleanPath &quot;&#36;PATH&quot;</code></pre><h2>使用条件与核对</h2><p>删除重复项或指定条目后输出路径文本，当前 shell 的 PATH 保持不变。 用法：foamCleanPath [选项] 路径 [过滤项] 示例：foamCleanPath &quot;&#36;PATH&quot;
Usage: foamCleanPath [OPTION] path [filter] .. [filter] foamCleanPath [OPTION] -env=name [filter] .. [filter] Prints its argument (which should be a &#x27;:&#x27; separated path) without the following: - duplicate elements - elements matching the specified filter(s) - inaccessible directories (with the -strip option)
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-csh -csh-env -debug -env -help -sh -sh-env -sh-lib -sh-path -strip -verbose</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamcleanpath.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamCleanPath
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCleanPath

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamCleanPath [OPTION] ENVNAME [filter] .. [filter]
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
    2  initial value of ENVNAME is empty</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCleanPath">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
