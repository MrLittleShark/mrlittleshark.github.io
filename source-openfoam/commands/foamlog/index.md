---
title: "foamLog  提取日志中的残差等数值记录"
layout: reference
description: "结果写入 logs/。-list 列出可提取的变量。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>结果写入 logs/。-list 列出可提取的变量。</p><h2>v2512 源码中的用途</h2><p>Extract data for each time-step from a log file for graphing.</p><h2>使用入口</h2><pre><code class="language-bash">foamLog log.simpleFoam</code></pre><h2>使用条件与核对</h2><p>结果写入 logs/。-list 列出可提取的变量。 用法：foamLog [选项] 日志文件 示例：foamLog log.simpleFoam
Extract data for each time-step from a log file for graphing.
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-case -help -list -local -n -quiet</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamlog.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamLog
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamLog

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamLog [OPTIONS] &lt;log&gt;
  -case &lt;dir&gt;           specify alternate case directory, default is the cwd
  -list | -l            lists but does not extract
  -n                    create single column files with extracted data only
  -quiet | -q           quiet operation
  -local | -localDB     only use the local database file
  -help                 print the usage

foamLog - extracts xy files from OpenFOAM logs.

-----------------------------------------------------------------------------
    The default is to extract the initial residual, the final residual and
    the number of iterations for all &#x27;Solved for&#x27; variables.
    Additionally, a (user editable) database is used to extract data for
    standard non-solved for variables like Courant number, and execution time.

    option -list : lists the possible variables without extracting them.

    The program will generate and run an awk script that writes a set of files,
    logs/&lt;var&gt;_&lt;subIter&gt;, for every &lt;var&gt; specified, for every occurrence inside
    a time step.

    For variables that are &#x27;Solved for&#x27;, the initial residual name will be
    &lt;var&gt;, the final residual receive the name &lt;var&gt;FinalRes,

    The files are output in a simple xy format with the first column Time
    (default) and the second the extracted values.
    Option -n creates single column files with the extracted data only.

    The query database is a simple text format with three entries per line,
    separated by &#x27;/&#x27; :
        Column 1 is the name of the variable (cannot contain spaces).
        Column 2 is the extended regular expression (egrep) to select the line.
        Column 3 is the string (fgrep) to select the column inside the line.
    The value taken will be the first (non-space)word after this column.

    The database (foamLog.db) will taken from these locations:
      ./
&#36;(foamEtcFile -list | sed -e &#x27;s#^#      #&#x27;)
      &#36;toolsDir

    option -quiet : suppresses the default information and only prints the
    extracted variables.
-----------------------------------------------------------------------------</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamLog">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
