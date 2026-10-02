---
title: "foamCreateManpage · 根据程序的 -help-man 输出生成手册页"
layout: reference
description: "根据程序的 -help-man 输出生成手册页。"
cms_slug: "command-foamcreatemanpage"
---

<p>根据程序的 -help-man 输出生成手册页。</p><h2>开始前</h2>
<p>加载 v2512 环境。内部脚本使用完整路径调用；在个人可写工作目录中生成输出。 程序需支持 -help-man。先 mkdir -p manuals；PDF 需要 groff 和 ps2pdf。</p>
<h2>示例 1：生成一个程序手册</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamCreateManpage" -output=manuals blockMesh
</code></pre>
<p>查询程序的 man 格式帮助，写入手册输出目录。</p>
<h2>示例 2：生成网格工具手册</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamCreateManpage" -output=manuals blockMesh checkMesh snappyHexMesh
</code></pre>
<p>为多个程序分别建立手册文件。</p>
<h2>示例 3：压缩手册页</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamCreateManpage" -gzip -output=manuals-gz blockMesh
</code></pre>
<p>生成 gzip 压缩的 man 文件，适用于发行包。</p>
<h2>示例 4：给个人工具生成手册</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamCreateManpage" -dir="$FOAM_USER_APPBIN" -output=manuals-user
</code></pre>
<p>扫描用户程序目录，仅能处理实现了标准帮助接口的应用。</p>
<h2>示例 5：生成 PDF 阅读版</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamCreateManpage" -pdf -output=manuals-pdf checkMesh
</code></pre>
<p>把 man 内容经排版工具转换成 PDF，输出到独立目录。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-dir=DIR</code></td><td>指定要处理的输入目录。</td></tr><tr><td><code>-output=DIR</code></td><td>指定输出目录。</td></tr><tr><td><code>-pdf</code></td><td>按 nroff 手册格式处理，再交给 ps2pdf 生成 PDF。</td></tr><tr><td><code>-gz | -gzip</code></td><td>压缩输出的 man 手册文件。</td></tr><tr><td><code>-version=VER</code></td><td>指定版本号。</td></tr><tr><td><code>-h | -help</code></td><td>显示用法。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamCreateManpage">源码与说明</a> · <a href="/assets/command-help/foamcreatemanpage.txt">帮助文本</a></p>
