---
title: "foamCleanPath · 删除重复项或指定条目后输出路径文本，当前 shell 的 PATH 保持不变"
layout: reference
description: "删除重复项或指定条目后输出路径文本，当前 shell 的 PATH 保持不变。"
cms_slug: "command-foamcleanpath"
---

<p>删除重复项或指定条目后输出路径文本，当前 shell 的 PATH 保持不变。</p><h2>开始前</h2>
<p>操作冒号分隔的路径字符串。默认打印结果，不直接修改父 shell；filter 按路径前缀匹配，并带有 sed 正则语义。</p>
<h2>示例 1：消除重复项</h2>
<pre><code class="language-bash">foamCleanPath "/usr/bin:/tmp/tools:/usr/bin"
</code></pre>
<p>输出去重后的路径串，保留第一次出现的项。</p>
<h2>示例 2：移除旧工具前缀</h2>
<pre><code class="language-bash">foamCleanPath "/tmp/oldfoam/bin:/usr/bin:/tmp/newfoam/bin" /tmp/oldfoam
</code></pre>
<p>删除匹配旧安装前缀的项，保留系统目录与新路径。</p>
<h2>示例 3：读取现有变量</h2>
<pre><code class="language-bash">foamCleanPath -env=PATH
</code></pre>
<p>从 PATH 获取输入，打印清理结果。</p>
<h2>示例 4：去除不可访问目录</h2>
<pre><code class="language-bash">foamCleanPath -strip "/usr/bin:/path/that/does/not/exist"
</code></pre>
<p>-strip 过滤不存在或不可访问的目录，输出保留项。</p>
<h2>示例 5：更新自定义路径变量</h2>
<pre><code class="language-bash">export MY_TOOL_PATH="/usr/bin:/tmp/tools:/usr/bin"
cleaned=$(foamCleanPath -env=MY_TOOL_PATH) &amp;&amp; export MY_TOOL_PATH="$cleaned"
</code></pre>
<p>先捕获成功结果再更新变量，避免清理失败时覆盖旧值。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-env=NAME</code></td><td>从指定环境变量读取初始内容；-env=-path 和 -env=-lib 分别快捷选择 PATH 与 LD_LIBRARY_PATH，Darwin 系统使用 FOAM_LD_LIBRARY_PATH。</td></tr><tr><td><code>-sh=NAME</code></td><td>输出 NAME=... 形式的赋值语句，供 sh 的 eval 执行。</td></tr><tr><td><code>-csh=NAME</code></td><td>输出 setenv NAME ... 形式的语句，供 csh 的 eval 执行。</td></tr><tr><td><code>-sh-env=NAME</code></td><td>等同于同时使用 -sh=NAME 和 -env=NAME。</td></tr><tr><td><code>-csh-env=NAME</code></td><td>等同于同时使用 -csh=NAME 和 -env=NAME。</td></tr><tr><td><code>-sh-path | -csh-path</code></td><td>等同于 -sh-env=PATH 或 -csh-env=PATH。</td></tr><tr><td><code>-sh-lib  | -csh-lib</code></td><td>等同于 -sh-env=LD_LIBRARY_PATH 或 -csh-env=LD_LIBRARY_PATH；Darwin 系统使用 FOAM_LD_LIBRARY_PATH。</td></tr><tr><td><code>-debug</code></td><td>向标准错误输出调试信息。</td></tr><tr><td><code>-strip</code></td><td>移除无法访问的目录项。</td></tr><tr><td><code>-verbose</code></td><td>显示输入、输出等处理进度。</td></tr><tr><td><code>-help</code></td><td>显示用法。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCleanPath">源码与说明</a> · <a href="/assets/command-help/foamcleanpath.txt">帮助文本</a></p>
