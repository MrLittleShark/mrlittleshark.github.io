---
title: "wrap-bison · 封装 Bison，调整生成文件的名称和位置"
layout: reference
description: "封装 Bison，调整生成文件的名称和位置。"
cms_slug: "command-wrap-bison"
---

<p>封装 Bison，调整生成文件的名称和位置。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 需要 Bison；带 m4 后缀的输入还需 m4。第一例创建最小 C++ 语法和 Make 目录，演示代码生成；词法函数和应用入口需另行实现。</p>
<h2>示例 1：直接调用 Bison</h2>
<pre><code class="language-bash">mkdir -p Make lnInclude generated
touch Make/options
cat &gt; parser.yy &lt;&lt;'EOF'
%language "c++"
%defines
%token NUMBER
%%
input: NUMBER;
%%
EOF
"$WM_PROJECT_DIR/wmake/scripts/wrap-bison" parser.yy
</code></pre>
<p>不指定 output 且不使用 m4 时直接转交 Bison，生成 parser.tab.cc/.hh。</p>
<h2>示例 2：指定实现文件位置</h2>
<pre><code class="language-bash">cp parser.yy parser.yy-m4
"$WM_PROJECT_DIR/wmake/scripts/wrap-bison" -output=generated/parser.tab.cc parser.yy-m4
</code></pre>
<p>采用 m4 输入后在临时目录运行 Bison，再把实现与头文件放到 generated 和 lnInclude。此写法避开 v2512 非 m4 重命名分支重复传入文件名的问题。</p>
<h2>示例 3：生成并保留语法报告</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/wrap-bison" -v parser.yy
</code></pre>
<p>未使用 output 或 m4 时直接调用 Bison，-v 生成 parser.output，列出语法状态和冲突诊断。</p>
<h2>示例 4：展开 m4 输入</h2>
<pre><code class="language-bash">cp parser.yy parser.yy-m4
"$WM_PROJECT_DIR/wmake/scripts/wrap-bison" -dry-run parser.yy-m4 &gt; parser-expanded.yy
</code></pre>
<p>先仅展开宏，检查语法模板的最终内容。</p>
<h2>示例 5：处理 m4 后生成代码</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/wrap-bison" -no-tmp -output=generated/parser.tab.cc parser.yy-m4
</code></pre>
<p>生成代码并移除展开后的临时 .yy 文件，输出文件保留。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-dry-run</code></td><td>仅处理 m4，并将结果输出到终端。</td></tr><tr><td><code>-grammar</code></td><td>语法表输出兼容选项，当前会被忽略。</td></tr><tr><td><code>-no-tmp</code></td><td>清理经过 m4 处理的临时文件。</td></tr><tr><td><code>-output=NAME</code></td><td>指定生成文件的目标名称，并执行相应重命名。</td></tr><tr><td><code>-h, -help</code></td><td>显示用法。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wrap-bison">源码与说明</a> · <a href="/assets/command-help/wrap-bison.txt">帮助文本</a></p>
