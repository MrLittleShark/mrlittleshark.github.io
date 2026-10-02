---
title: "lib · 切换到已编译的库目录"
layout: reference
description: "切换到已编译的库目录。"
cms_slug: "command-lib"
---

<p>切换到已编译的库目录。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/etc/config.sh/aliases"
lib
pwd
</code></pre>
<p>这是 cd 的别名，对应目录为 <code>$FOAM_LIBBIN</code>。先创建尚不存在的个人目录，再使用相应别名。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type lib
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">alias lib='cd ${FOAM_LIBBIN:?}'
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">源码与说明</a></p>
