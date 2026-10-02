---
title: "foamLog · 从求解日志提取残差、迭代次数和其他监测量"
layout: reference
description: "从求解日志提取残差、迭代次数和其他监测量。"
cms_slug: "command-foamlog"
---

<p>从求解日志提取残差、迭代次数和其他监测量。</p><h2>开始前</h2>
<p>加载 v2512 环境，使用个人算例副本 caseA。并行示例先配置 decomposeParDict 并完成 decomposePar，程序和字典须匹配。 先保存求解器输出为 caseA/log.icoFoam。在副本内提取，结果默认写入 logs 目录。</p>
<h2>示例 1：提取残差曲线</h2>
<pre><code class="language-bash">cd caseA
foamLog log.icoFoam
</code></pre>
<p>生成 logs/&lt;变量&gt;_&lt;子迭代号&gt;，一般包含时间与残差两列。</p>
<h2>示例 2：先列出可提取量</h2>
<pre><code class="language-bash">cd caseA
foamLog -list log.icoFoam
</code></pre>
<p>显示可识别变量，不生成提取文件。</p>
<h2>示例 3：只保留数据列</h2>
<pre><code class="language-bash">cd caseA
foamLog -n log.icoFoam
</code></pre>
<p>-n 去掉时间列，仅输出每个量的数据值。</p>
<h2>示例 4：从外部指定算例</h2>
<pre><code class="language-bash">foamLog -case caseA log.icoFoam
</code></pre>
<p>切换到指定算例后提取其日志，输出仍在该算例 logs 中。</p>
<h2>示例 5：使用自定义提取数据库</h2>
<pre><code class="language-bash">cd caseA
cp "$WM_PROJECT_DIR/bin/tools/foamLog.db" foamLog.db
foamLog -local log.icoFoam
</code></pre>
<p>将数据库复制到当前目录，可按“名称/行匹配/取值前缀”规则增加提取项；-local 只用本地数据库。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-list | -l</code></td><td>列出可用的预配置函数。</td></tr><tr><td><code>-n</code></td><td>create single column files with extracted data only</td></tr><tr><td><code>-quiet | -q</code></td><td>quiet operation</td></tr><tr><td><code>-local | -localDB</code></td><td>only use the local database file</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamLog [OPTIONS] &lt;log&gt;
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
