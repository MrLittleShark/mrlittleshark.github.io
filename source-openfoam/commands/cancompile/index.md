---
title: "canCompile · 检查 make、wmake 和 C++ 编译器是否可用"
layout: reference
description: "检查 make、wmake 和 C++ 编译器是否可用。"
cms_slug: "command-cancompile"
---

<p>检查 make、wmake 和 C++ 编译器是否可用。</p><h2>开始前</h2>
<p>先在单独一行执行 source "$WM_PROJECT_DIR/bin/tools/RunFunctions"。示例在个人算例工作区操作，caseA、caseB 均为可修改的副本。</p>
<h2>示例 1：检测编译条件</h2>
<pre><code class="language-bash">if canCompile; then echo "compiler available"; fi
</code></pre>
<p>依次检查 make、wmake 以及 wmake 选中的 C++ 编译器是否存在。</p>
<h2>示例 2：缺依赖时终止脚本</h2>
<pre><code class="language-bash">canCompile || exit 1
wmake myUtility
</code></pre>
<p>用于构建脚本；myUtility 应含 Make/files 与 Make/options，环境不完整时先停止。</p>
<h2>示例 3：条件编译教程</h2>
<pre><code class="language-bash">if canCompile; then compileApplication myUtility; else echo "build skipped"; fi
</code></pre>
<p>编译条件满足时执行 wmake，否则保留明确提示。</p>
<h2>示例 4：检查不同环境组合</h2>
<pre><code class="language-bash">(source "$WM_PROJECT_DIR/etc/bashrc" WM_COMPILER=Gcc; canCompile)
</code></pre>
<p>在子 shell 选 GCC 后检查，可判断该配置对应编译器是否安装。</p>
<h2>示例 5：准备多个开发项目</h2>
<pre><code class="language-bash">if canCompile; then for appDir in fieldStats meshReport; do wmake "$appDir" || break; done; fi
</code></pre>
<p>先准备两个完整源码目录，统一检查后按顺序构建；任一失败时结束循环。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
