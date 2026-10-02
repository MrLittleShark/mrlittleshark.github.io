---
title: "help-filter · 过滤 -help-full 的输出，供文档生成使用"
layout: reference
description: "过滤 -help-full 的输出，供文档生成使用。"
cms_slug: "command-help-filter"
---

<p>过滤 -help-full 的输出，供文档生成使用。</p><h2>开始前</h2>
<p>加载 v2512 环境。内部脚本使用完整路径调用；在个人可写工作目录中生成输出。 输入从标准输入接收，预期为 OpenFOAM 程序 -help-full 输出；结果是用于补全或索引的简化选项列表。</p>
<h2>示例 1：提取网格生成选项</h2>
<pre><code class="language-bash">blockMesh -help-full | "$WM_PROJECT_DIR/bin/tools/help-filter"
</code></pre>
<p>保留选项名并用 &lt; 标记需要值的选项。</p>
<h2>示例 2：提取网格检查选项</h2>
<pre><code class="language-bash">checkMesh -help-full | "$WM_PROJECT_DIR/bin/tools/help-filter"
</code></pre>
<p>生成 checkMesh 的可检索选项列表。</p>
<h2>示例 3：保存后处理选项</h2>
<pre><code class="language-bash">postProcess -help-full | "$WM_PROJECT_DIR/bin/tools/help-filter" &gt; postProcess-options.txt
</code></pre>
<p>将过滤后的列表保存为索引输入。</p>
<h2>示例 4：比较两个工具的选项</h2>
<pre><code class="language-bash">blockMesh -help-full | "$WM_PROJECT_DIR/bin/tools/help-filter" &gt; options-blockMesh
checkMesh -help-full | "$WM_PROJECT_DIR/bin/tools/help-filter" &gt; options-checkMesh
diff -u options-blockMesh options-checkMesh
</code></pre>
<p>统一过滤格式后查看两工具特有选项。</p>
<h2>示例 5：读取离线帮助文本</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/help-filter" &lt; saved-help-full.txt
</code></pre>
<p>saved-help-full.txt 须为此前完整帮助输出，适合构建离线命令索引。</p>
<details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: help-filter
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/help-filter

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Feed with output from -help-full. For example, blockMesh -help-full | ./help-filter</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/help-filter">源码与说明</a> · <a href="/assets/command-help/help-filter.txt">帮助文本</a></p>
