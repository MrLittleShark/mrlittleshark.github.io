---
title: "addr2line · 把二进制地址解析为函数名和源文件行号"
layout: reference
description: "把二进制地址解析为函数名和源文件行号。"
cms_slug: "command-addr2line"
---

<p>把二进制地址解析为函数名和源文件行号。</p><h2>开始前</h2>
<p>此处对应Linux GNU addr2line；需要带调试符号的可执行文件或库，以及该模块内的地址/偏移。示例0x1234应替换为实际值。</p>
<h2>示例 1：定位可执行文件地址</h2>
<pre><code class="language-bash">addr2line -e "$FOAM_USER_APPBIN/mySolver" 0x1234
</code></pre>
<p>-e指定产生堆栈的可执行文件，地址替换为模块内地址；输出源文件和行号。</p>
<h2>示例 2：同时显示C++函数名</h2>
<pre><code class="language-bash">addr2line -C -f -e "$FOAM_USER_APPBIN/mySolver" 0x1234
</code></pre>
<p>-f增加函数名，-C还原C++修饰名称，便于把崩溃位置对应到类成员函数。</p>
<h2>示例 3：一次解析多个地址</h2>
<pre><code class="language-bash">addr2line -C -f -e "$FOAM_USER_APPBIN/mySolver" 0x1234 0x2345 0x3456
</code></pre>
<p>依次解析同一模块中的多个堆栈地址，输出相应调用位置。</p>
<h2>示例 4：定位共享库中的错误</h2>
<pre><code class="language-bash">addr2line -C -f -e "$FOAM_USER_LIBBIN/libmyBoundary.so" 0x1234
</code></pre>
<p>崩溃位于自定义边界库时选择该.so，并使用其模块内偏移，定位库源码而非主求解器。</p>
<h2>示例 5：展开内联调用链</h2>
<pre><code class="language-bash">addr2line -C -f -i -p -e "$FOAM_USER_APPBIN/mySolver" 0x1234
</code></pre>
<p>-i展开内联函数，-p用更紧凑的单行形式输出；适合优化编译后一个地址对应多层内联代码的情况。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-a --addresses</code></td><td>显示地址。</td></tr><tr><td><code>-b --target=&lt;bfdname&gt;</code></td><td>指定二进制文件格式。</td></tr><tr><td><code>-e --exe=&lt;executable&gt;</code></td><td>指定输入可执行文件，默认为 a.out。</td></tr><tr><td><code>-i --inlines</code></td><td>展开内联函数调用信息。</td></tr><tr><td><code>-j --section=&lt;name&gt;</code></td><td>按节内偏移量读取输入，替代绝对地址。</td></tr><tr><td><code>-p --pretty-print</code></td><td>以便于阅读的格式输出。</td></tr><tr><td><code>-s --basenames</code></td><td>仅显示文件名，省略目录路径。</td></tr><tr><td><code>-f --functions</code></td><td>显示函数名。</td></tr><tr><td><code>-C --demangle[=style]</code></td><td>将编译器修饰后的符号名还原为可读的函数名。</td></tr><tr><td><code>-R --recurse-limit</code></td><td>对符号名还原过程启用递归深度限制，此项为默认设置。</td></tr><tr><td><code>-r --no-recurse-limit</code></td><td>移除符号名还原过程的递归深度限制。</td></tr><tr><td><code>-h --help</code></td><td>显示帮助信息。</td></tr><tr><td><code>-v --version</code></td><td>显示程序版本。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/miscellaneous/OSspecific/addr2line/Make/files">源码与说明</a> · <a href="/assets/command-help/addr2line.txt">帮助文本</a></p>
