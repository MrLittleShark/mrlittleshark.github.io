---
title: "foamPackRelease · 生成打包 OpenFOAM 源码和子模块的脚本"
layout: reference
description: "生成打包 OpenFOAM 源码和子模块的脚本。"
cms_slug: "command-foampackrelease"
---

<p>生成打包 OpenFOAM 源码和子模块的脚本。</p><h2>开始前</h2>
<p>加载 v2512 环境。内部脚本使用完整路径调用；在个人可写工作目录中生成输出。 需要完整 Git 仓库与有效 commit-ish，例如 HEAD。脚本输出的是打包脚本；先保存并阅读，再显式执行。工作区未提交内容不属于指定提交。</p>
<h2>示例 1：生成默认打包脚本</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamPackRelease" HEAD &gt; pack-head.sh
less pack-head.sh
</code></pre>
<p>检查将归档的提交、模块及输出路径。</p>
<h2>示例 2：指定名称和输出目录</h2>
<pre><code class="language-bash">mkdir -p releases
"$WM_PROJECT_DIR/bin/tools/foamPackRelease" -name=foamlab-source -output=releases HEAD &gt; pack-named.sh
</code></pre>
<p>将包名主体和存放位置写入脚本。</p>
<h2>示例 3：只打包核心源码</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamPackRelease" -no-extras -name=core-only HEAD &gt; pack-core.sh
</code></pre>
<p>排除 modules/plugins 等附加内容。</p>
<h2>示例 4：选择压缩方式</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamPackRelease" -xz -name=source-xz HEAD &gt; pack-xz.sh
</code></pre>
<p>生成采用 xz 的打包脚本。</p>
<h2>示例 5：使用另一份仓库</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamPackRelease" -gitbase="$HOME/src/OpenFOAM-v2512" -name=source-copy HEAD &gt; pack-copy.sh
bash pack-copy.sh
</code></pre>
<p>输入目录必须是真实 Git 仓库；审核脚本后执行，生成该提交的源码包。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-name=NAME</code></td><td>指定归档文件的基本名称，默认自动生成。</td></tr><tr><td><code>-output=DIR</code></td><td>指定输出目录，默认为当前目录。</td></tr><tr><td><code>-prefix=NAME</code></td><td>指定归档内部的顶层目录名，默认自动生成。</td></tr><tr><td><code>-pkg-modules</code></td><td>仅打包 modules。</td></tr><tr><td><code>-pkg-plugins</code></td><td>仅打包 plugins。</td></tr><tr><td><code>-no-extras</code></td><td>从源码包中排除 modules、plugins 等附加内容。</td></tr><tr><td><code>-no-modules</code></td><td>从源码包中排除 modules；默认包含。</td></tr><tr><td><code>-no-plugins</code></td><td>从源码包中排除 plugins；默认排除。</td></tr><tr><td><code>-all-extras</code></td><td>将 modules、plugins 等附加内容加入源码包。</td></tr><tr><td><code>-with-modules</code></td><td>将 modules 加入源码包；默认包含。</td></tr><tr><td><code>-with-plugins</code></td><td>将 plugins 加入源码包；默认排除。</td></tr><tr><td><code>-no-patch</code></td><td>输出归档名称中省略 _patch 补丁编号。</td></tr><tr><td><code>-no-prefix</code></td><td>打包时省略顶层子目录前缀。</td></tr><tr><td><code>-no-compress</code></td><td>生成未压缩归档。</td></tr></tbody></table><details class="command-more-options"><summary>更多参数（9 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-compress=TYPE</code></td><td>指定压缩格式。</td></tr><tr><td><code>-sep=SEP</code></td><td>将版本号与补丁号之间的分隔符从下划线改为指定字符。</td></tr><tr><td><code>-gitbase=DIR</code></td><td>指定另一个仓库位置。</td></tr><tr><td><code>-with-api=NUM</code></td><td>指定打包使用的 API 版本值。</td></tr><tr><td><code>-tgz, -xz, -zstd</code></td><td>分别等同于 -compress=tgz、-compress=xz、-compress=zstd。</td></tr><tr><td><code>-debian</code></td><td>采用 Debian 自动命名，并启用 -no-prefix、-xz。</td></tr><tr><td><code>-debian=NUM</code></td><td>采用 Debian 自动命名，并指定 Debian 补丁号。</td></tr><tr><td><code>-debian=NAME</code></td><td>等同于 -name=NAME.orig、-no-prefix 和 -xz 的组合。</td></tr><tr><td><code>-help</code></td><td>显示帮助。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamPackRelease">源码与说明</a> · <a href="/assets/command-help/foampackrelease.txt">帮助文本</a></p>
