---
title: "lib · 切换到已编译的库目录"
layout: reference
description: "切换到已编译的库目录。"
cms_slug: "command-lib"
---

<p>切换到已编译的库目录。</p><h2>开始前</h2>
<p>先加载 v2512 环境，在交互式 Bash 中逐行执行。lib 展开为 cd "$FOAM_LIBBIN"。</p>
<h2>示例 1：查看核心库</h2>
<pre><code class="language-bash">lib
ls libOpenFOAM*
</code></pre>
<p>进入当前编译配置的库目录，显示核心库文件。</p>
<h2>示例 2：查找有限体积库</h2>
<pre><code class="language-bash">lib
ls libfiniteVolume*
</code></pre>
<p>库名供 Make/options 的 -lfiniteVolume 和运行时加载参考。</p>
<h2>示例 3：检查 MPI 相关子目录</h2>
<pre><code class="language-bash">lib
find . -maxdepth 2 -name "*Pstream*"
</code></pre>
<p>显示并行通信库实际路径，区分不同 MPI 配置。</p>
<h2>示例 4：检查 Linux 动态依赖</h2>
<pre><code class="language-bash">lib
ldd libfiniteVolume.so
</code></pre>
<p>Linux 共享库安装中，ldd 展示依赖库及解析路径，找不到时显示 not found。</p>
<h2>示例 5：比较库文件后回算例</h2>
<pre><code class="language-bash">lib
ls -lh libOpenFOAM.so libfiniteVolume.so
cd -
</code></pre>
<p>显示当前配置下库的大小与时间，然后返回原目录。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/config.sh/aliases">源码与说明</a></p>
