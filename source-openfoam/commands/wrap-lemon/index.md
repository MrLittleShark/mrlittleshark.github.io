---
title: "wrap-lemon · 使用 OpenFOAM 的解析器模板封装 Lemon"
layout: reference
description: "使用 OpenFOAM 的解析器模板封装 Lemon。"
cms_slug: "command-wrap-lemon"
---

<p>使用 OpenFOAM 的解析器模板封装 Lemon。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 需要已构建的 OpenFOAM Lemon 及 wmake/etc/lempar.c。第一例创建最小语法；后续在同一练习目录执行。</p>
<h2>示例 1：生成一个简单解析器</h2>
<pre><code class="language-bash">cat &gt; toy.lyy &lt;&lt;'EOF'
%token_type {double}
%default_type {double}
input ::= NUMBER.
EOF
"$WM_PROJECT_DIR/wmake/scripts/wrap-lemon" -ecc toy.lyy
</code></pre>
<p>-ecc 选择 .cc 输出扩展名，NUMBER 是终结符，input 是起始规则。生成代码还需接入词法扫描和应用。</p>
<h2>示例 2：只生成 token 头文件</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/wrap-lemon" -header toy.lyy
</code></pre>
<p>临时生成后只保留 toy.h，适合提前建立 token 编号。</p>
<h2>示例 3：输出语法规则表</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/wrap-lemon" -grammar toy.lyy
</code></pre>
<p>将 Lemon 的语法表打印到标准输出，便于检查规则。</p>
<h2>示例 4：指定生成目录</h2>
<pre><code class="language-bash">mkdir -p generated
"$WM_PROJECT_DIR/wmake/scripts/wrap-lemon" -dgenerated -ecc toy.lyy
</code></pre>
<p>-d&lt;目录&gt; 是 Lemon 参数，输出写入 generated。</p>
<h2>示例 5：预览 m4 展开结果</h2>
<pre><code class="language-bash">cp toy.lyy toy.lyy-m4
"$WM_PROJECT_DIR/wmake/scripts/wrap-lemon" -dry-run toy.lyy-m4 &gt; toy-expanded.lyy
</code></pre>
<p>文件名以 m4 结尾触发预处理，dry-run 只输出展开后的语法文本。</p>
<h2>示例 6：生成后移除 m4 中间文件</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/wrap-lemon" -no-tmp -ecc toy.lyy-m4
</code></pre>
<p>使用 m4 语法生成解析器，并移除该步骤的临时展开文件。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-header</code></td><td>仅生成头文件。</td></tr><tr><td><code>-dry-run</code></td><td>仅处理 m4，并将结果输出到终端。</td></tr><tr><td><code>-grammar</code></td><td>将语法表输出到终端。</td></tr><tr><td><code>-no-tmp</code></td><td>清理经过 m4 处理的临时文件。</td></tr><tr><td><code>-h, -help</code></td><td>显示用法。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wrap-lemon">源码与说明</a> · <a href="/assets/command-help/wrap-lemon.txt">帮助文本</a></p>
