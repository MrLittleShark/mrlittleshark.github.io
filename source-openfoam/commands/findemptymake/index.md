---
title: "findEmptyMake · 查找缺少 files 或 options 的 Make 目录"
layout: reference
description: "查找缺少 files 或 options 的 Make 目录。"
cms_slug: "command-findemptymake"
---

<p>查找缺少 files 或 options 的 Make 目录。</p><h2>开始前</h2>
<p>加载 v2512 环境。内部脚本使用完整路径调用；在个人可写工作目录中生成输出。</p>
<h2>示例 1：检查一个项目</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/findEmptyMake" myUtility
</code></pre>
<p>列出缺少 files 或 options 的 Make 目录。</p>
<h2>示例 2：检查用户源码树</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/findEmptyMake" "$WM_PROJECT_USER_DIR/applications"
</code></pre>
<p>递归定位移动源码后遗留的编译控制目录。</p>
<h2>示例 3：比较两个项目</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/findEmptyMake" myUtility myLibrary
</code></pre>
<p>两条路径一起检查，输出包含问题目录位置。</p>
<h2>示例 4：从当前目录检查</h2>
<pre><code class="language-bash">cd user-project
"$WM_PROJECT_DIR/bin/tools/findEmptyMake"
</code></pre>
<p>无路径参数时扫描当前目录树。</p>
<h2>示例 5：构造一个缺文件案例</h2>
<pre><code class="language-bash">mkdir -p make-demo/Make
touch make-demo/Make/files
"$WM_PROJECT_DIR/bin/tools/findEmptyMake" make-demo
</code></pre>
<p>只有 files、缺 options 的示例应被报告，便于理解检测标准。</p>
<details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: findEmptyMake [OPTION] [dir1 .. dirN]

Find Make/ directories without a &#x27;files&#x27; or &#x27;options&#x27; file.
This can occur when a directory has been moved.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/findEmptyMake">源码与说明</a> · <a href="/assets/command-help/findemptymake.txt">帮助文本</a></p>
