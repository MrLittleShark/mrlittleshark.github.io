---
title: "foamLog · 从求解日志提取残差、迭代次数和其他监测量"
layout: reference
description: "从求解日志提取残差、迭代次数和其他监测量。"
cms_slug: "command-foamlog"
---

<p>从求解日志提取残差、迭代次数和其他监测量。</p><h2>提取残差</h2>
<pre><code class="language-bash">foamLog log.simpleFoam
</code></pre>
<p>在 <code>logs</code> 目录生成数据文件。通常可见 <code>p_0</code>、<code>Ux_0</code> 等名称，具体取决于日志实际包含的字段。</p>
<h2>监控提取结果</h2>
<pre><code class="language-bash">foamMonitor -l logs/p_0
</code></pre>
<p><code>-l</code> 使用对数纵轴。残差下降表示方程迭代误差减小，还可同时比较压降、流量等目标量。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-list | -l</td><td>列出可用的预配置函数。</td></tr><tr><td>-n</td><td>create single column files with extracted data only</td></tr><tr><td>-quiet | -q</td><td>quiet operation</td></tr><tr><td>-local | -localDB</td><td>only use the local database file</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamLog [OPTIONS] &lt;log&gt;
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
$(foamEtcFile -list | sed -e &#x27;s#^#      #&#x27;)
      $toolsDir

    option -quiet : suppresses the default information and only prints the
    extracted variables.
-----------------------------------------------------------------------------</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamLog">源码与说明</a> · <a href="/assets/command-help/foamlog.txt">帮助文本</a></p>
