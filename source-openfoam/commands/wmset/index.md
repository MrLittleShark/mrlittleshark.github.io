---
title: "wmSet · 按给定变量重新加载 OpenFOAM 环境"
layout: reference
description: "按给定变量重新加载 OpenFOAM 环境。"
cms_slug: "command-wmset"
---

<p>按给定变量重新加载 OpenFOAM 环境。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/etc/config.sh/aliases"
wmSet WM_LABEL_SIZE=64
</code></pre>
<p>参数传给 etc/bashrc，用于选择编译和运行配置。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type wmSet
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">alias wmSet='. ${WM_PROJECT_DIR:?}/etc/bashrc'
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">源码与说明</a></p>
