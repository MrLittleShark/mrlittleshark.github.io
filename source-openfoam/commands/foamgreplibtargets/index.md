---
title: "foamGrepLibTargets · 列出库的编译链接目标"
layout: reference
description: "列出库的编译链接目标。"
cms_slug: "command-foamgreplibtargets"
---

<p>列出库的编译链接目标。</p><h2>开始前</h2>
<p>加载 v2512 环境。内部脚本使用完整路径调用；在个人可写工作目录中生成输出。</p>
<h2>示例 1：列出全部库编译单元</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamGrepLibTargets"
</code></pre>
<p>输出含 LIB_LIBS 条目的 Make/options 所属目录。</p>
<h2>示例 2：只扫描 src</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamGrepLibTargets" -src
</code></pre>
<p>限定核心库与模型源码目录。</p>
<h2>示例 3：扫描应用附属库</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamGrepLibTargets" -app
</code></pre>
<p>检查 solvers/utilities 下的辅助库编译单元。</p>
<h2>示例 4：扫描解压后的树</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamGrepLibTargets" -no-git -src
</code></pre>
<p>从文件系统读取 Make/options，适合没有 Git 索引的发行源码。</p>
<h2>示例 5：筛选有限体积相关库</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamGrepLibTargets" -src -no-git | grep finiteVolume
</code></pre>
<p>按路径筛选，输出可直接进入阅读的源码目录。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-no-git</code></td><td>Disable use of git for obtaining information</td></tr><tr><td><code>-app</code></td><td>Search applications/solvers/ applications/utilities/</td></tr><tr><td><code>-src</code></td><td>Search src/</td></tr><tr><td><code>-no-git</code></td><td>Disable use of git for obtaining information</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: foamGrepLibTargets
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamGrepLibTargets

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

usage: foamGrepLibTargets
  -no-git       Disable use of git for obtaining information
  -app          Search applications/solvers/ applications/utilities/
  -src          Search src/
  -no-git       Disable use of git for obtaining information
  -help         Print the usage

List library targets (contains LIB_LIBS). Uses git when possible</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamGrepLibTargets">源码与说明</a> · <a href="/assets/command-help/foamgreplibtargets.txt">帮助文本</a></p>
