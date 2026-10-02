---
title: "wmakeLnInclude · 将头文件和模板实现链接到 lnInclude 目录"
layout: reference
description: "将头文件和模板实现链接到 lnInclude 目录。"
cms_slug: "command-wmakelninclude"
---

<p>将头文件和模板实现链接到 lnInclude 目录。</p><h2>开始前</h2>
<p>在个人库源码目录 libraryA 中准备 Make/files 和头文件。lnInclude 是生成的头文件索引目录，依赖 Linux 符号链接。</p>
<h2>示例 1：创建头文件索引</h2>
<pre><code class="language-bash">wmakeLnInclude libraryA
</code></pre>
<p>递归查找库头文件及模板源文件，链接到 libraryA/lnInclude。</p>
<h2>示例 2：更新新增头文件</h2>
<pre><code class="language-bash">wmakeLnInclude -update libraryA
</code></pre>
<p>新增或改变头文件后更新链接，已有链接可重新指向源位置。</p>
<h2>示例 3：从库内部查找根目录</h2>
<pre><code class="language-bash">cd libraryA/subdir
wmakeLnInclude -pwd
</code></pre>
<p>向上定位含 Make 的源码根，再创建对应 lnInclude。</p>
<h2>示例 4：包含全部源码文件</h2>
<pre><code class="language-bash">wmakeLnInclude -extra libraryA
</code></pre>
<p>额外链接普通源文件，便于某些依赖源码访问的开发工具。</p>
<h2>示例 5：同时处理两个库</h2>
<pre><code class="language-bash">wmakeLnInclude -update libraryA libraryB
</code></pre>
<p>为两个独立编译单元各自更新索引。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-f | -force</code></td><td>删除已有 lnInclude/ 后重新创建。</td></tr><tr><td><code>-u | -update</code></td><td>更新已有 lnInclude 目录。</td></tr><tr><td><code>-s | -silent</code></td><td>静默运行，省略命令回显。</td></tr><tr><td><code>-extra</code></td><td>同时将所有源文件加入 lnInclude/。</td></tr><tr><td><code>-no-extra</code></td><td>仅包含默认类型的文件，省略其余源文件；此项为默认设置。</td></tr><tr><td><code>-pwd</code></td><td>查找包含 Make/ 的源码根目录。</td></tr><tr><td><code>-help</code></td><td>显示用法。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wmakeLnInclude">源码与说明</a> · <a href="/assets/command-help/wmakelninclude.txt">帮助文本</a></p>
