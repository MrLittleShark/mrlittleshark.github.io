---
title: "wmake-with-bear · 通过 Bear 调用 wmake，生成编译命令数据库"
layout: reference
description: "通过 Bear 调用 wmake，生成编译命令数据库。"
cms_slug: "command-wmake-with-bear"
---

<p>通过 Bear 调用 wmake，生成编译命令数据库。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 需要安装 Bear，以及带 Make 配置的个人项目 myUtility/myLibrary。Bear 捕获实际编译命令，已无需重编的项目可能产生空数据库；必要时先在自己的项目内 wclean。</p>
<h2>示例 1：记录一次应用编译</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/wmake-with-bear" myUtility
</code></pre>
<p>包装 wmake，默认向选定 build/WM_OPTIONS 位置输出 compile_commands.json。</p>
<h2>示例 2：指定数据库目录</h2>
<pre><code class="language-bash">mkdir -p compile-db
"$WM_PROJECT_DIR/wmake/scripts/wmake-with-bear" -bear-output-dir="$PWD/compile-db" myUtility
</code></pre>
<p>让编辑器从固定个人目录读取数据库。</p>
<h2>示例 3：捕获并行构建</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/wmake-with-bear" -bear-output-dir="$PWD/db-parallel" -j 4 myUtility
</code></pre>
<p>-j 4 传给 wmake，数据库包含本次实际执行的编译项。</p>
<h2>示例 4：捕获共享库编译</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/wmake-with-bear" -bear-output-dir="$PWD/db-library" libso myLibrary
</code></pre>
<p>数据库记录库源码的 include 与宏设置，供源码导航使用。</p>
<h2>示例 5：重新获取完整命令集</h2>
<pre><code class="language-bash">wclean myUtility
"$WM_PROJECT_DIR/wmake/scripts/wmake-with-bear" -bear-output-dir="$PWD/db-fresh" myUtility
</code></pre>
<p>在个人副本中清理后重编，使所有编译单元被 Bear 捕获。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-bear-output-dir=DIR</code></td><td>指定输出目录。</td></tr><tr><td><code>-version</code></td><td>显示 bear 版本。</td></tr><tr><td><code>-h | -help</code></td><td>显示简要帮助并退出。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wmake-with-bear">源码与说明</a> · <a href="/assets/command-help/wmake-with-bear.txt">帮助文本</a></p>
