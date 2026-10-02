---
title: "remove0DirFields · 删除 0 目录中指定名称的场文件"
layout: reference
description: "删除 0 目录中指定名称的场文件。"
cms_slug: "command-remove0dirfields"
---

<p>删除 0 目录中指定名称的场文件。</p><h2>开始前</h2>
<p>先在单独一行执行 source "$WM_PROJECT_DIR/bin/tools/RunFunctions"。示例在个人算例工作区操作，caseA、caseB 均为可修改的副本。 函数只移除 0 和 processor*/0 中指定的普通文件；region 可改变这些路径。先在独立副本中操作。</p>
<h2>示例 1：移除旧派生压力场</h2>
<pre><code class="language-bash">remove0DirFields p
</code></pre>
<p>删除顶层和分区初始目录中的 p；适用于下一步将重新生成 p 的流程。</p>
<h2>示例 2：切换模型前移除多项</h2>
<pre><code class="language-bash">remove0DirFields k epsilon
</code></pre>
<p>移除旧湍流初始字段，之后用目标模型的初始场模板补齐。</p>
<h2>示例 3：指定流体区域</h2>
<pre><code class="language-bash">remove0DirFields -region fluid p
</code></pre>
<p>只处理 0/fluid/p 与各子域对应位置。</p>
<h2>示例 4：指定固体区域字段</h2>
<pre><code class="language-bash">remove0DirFields -region solid T
</code></pre>
<p>移除固体区域温度初值，随后从新模板或映射结果恢复。</p>
<h2>示例 5：为区域循环处理字段</h2>
<pre><code class="language-bash">for region in fluid1 fluid2; do remove0DirFields -region "$region" k omega; done
</code></pre>
<p>两个流体区域分别处理相同字段，其他区域与文件保留。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
