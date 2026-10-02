---
title: "foamSearch · 键路径以点号分隔，-count 统计相同配置的出现次数"
layout: reference
description: "键路径以点号分隔，-count 统计相同配置的出现次数。"
cms_slug: "command-foamsearch"
---

<p>键路径以点号分隔，-count 统计相同配置的出现次数。</p><h2>用法</h2><pre><code class="language-bash">foamSearch &quot;$FOAM_TUTORIALS&quot; ddtSchemes.default fvSchemes</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-c | -count</td><td>prefix lines by the number of occurrences</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamSearch [OPTIONS] &lt;directory&gt; &lt;keyword&gt; &lt;fileName&gt;
       foamSearch [OPTIONS] &lt;keyword&gt; &lt;fileName&gt;

Options:
    -c | -count     prefix lines by the number of occurrences
    -help           help

* Searches the &lt;directory&gt; for files named &lt;fileName&gt; and extracts entries
  with &lt;keyword&gt;. Sorts result into a list of unique entries.
  Uses the cwd if the &lt;directory&gt; is not provided.

Examples:
* Default ddtSchemes entries in the fvSchemes files in all tutorials:
    foamSearch \$FOAM_TUTORIALS ddtSchemes.default fvSchemes

* Relaxations factors for U in fvSolutions files in all tutorials:
    foamSearch -count \$FOAM_TUTORIALS relaxationFactors.equations.U fvSolution</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamSearch">源码与说明</a> · <a href="/assets/command-help/foamsearch.txt">帮助文本</a></p>
