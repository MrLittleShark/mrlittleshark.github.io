---
title: "foamSearch  搜索各算例字典中的指定条目"
layout: reference
description: "键路径以点号分隔，-count 统计相同配置的出现次数。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>键路径以点号分隔，-count 统计相同配置的出现次数。</p><h2>v2512 源码中的用途</h2><p>Search a directory for dictionary files of a particular name and extract entries of a particular keyword, sorting into a unique list. Requires foamDictionary.</p><h2>使用入口</h2><pre><code class="language-bash">foamSearch &quot;&#36;FOAM_TUTORIALS&quot; ddtSchemes.default fvSchemes</code></pre><h2>使用条件与核对</h2><p>键路径以点号分隔，-count 统计相同配置的出现次数。 用法：foamSearch [目录] 键路径 文件名 示例：foamSearch &quot;&#36;FOAM_TUTORIALS&quot; ddtSchemes.default fvSchemes
Search a directory for dictionary files of a particular name and extract entries of a particular keyword, sorting into a unique list. Requires foamDictionary.
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-c -help</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamsearch.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamSearch
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamSearch

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamSearch [OPTIONS] &lt;directory&gt; &lt;keyword&gt; &lt;fileName&gt;
       foamSearch [OPTIONS] &lt;keyword&gt; &lt;fileName&gt;

Options:
    -c | -count     prefix lines by the number of occurrences
    -help           help

* Searches the &lt;directory&gt; for files named &lt;fileName&gt; and extracts entries
  with &lt;keyword&gt;. Sorts result into a list of unique entries.
  Uses the cwd if the &lt;directory&gt; is not provided.

Examples:
* Default ddtSchemes entries in the fvSchemes files in all tutorials:
    foamSearch \&#36;FOAM_TUTORIALS ddtSchemes.default fvSchemes

* Relaxations factors for U in fvSolutions files in all tutorials:
    foamSearch -count \&#36;FOAM_TUTORIALS relaxationFactors.equations.U fvSolution</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamSearch">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
