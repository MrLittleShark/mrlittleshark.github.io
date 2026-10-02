---
title: "foamUpdateCaseFileHeader · 更新算例文件头并合并连续空行"
layout: reference
description: "更新算例文件头并合并连续空行。"
cms_slug: "command-foamupdatecasefileheader"
---

<p>更新算例文件头并合并连续空行。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/foamUpdateCaseFileHeader&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-version=VER</td><td>Specifies version for header (default: $FOAM_API)</td></tr><tr><td>-h | -help</td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamUpdateCaseFileHeader [OPTION] &lt;file1&gt; ... &lt;fileN&gt;

options:
  -version=VER      Specifies version for header (default: $FOAM_API)
  -h | -help        Print the usage

Updates the header of application files and removes consecutive blank lines.
By default, writes current OpenFOAM API number version in the header.
An alternative version can be specified with the -version option.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamUpdateCaseFileHeader">源码与说明</a> · <a href="/assets/command-help/foamupdatecasefileheader.txt">帮助文本</a></p>
