---
title: "foamGrepExeTargets · 列出 Make/files 中的可执行文件目标，便于检查构建结果"
layout: reference
description: "列出 Make/files 中的可执行文件目标，便于检查构建结果。"
cms_slug: "command-foamgrepexetargets"
---

<p>列出 Make/files 中的可执行文件目标，便于检查构建结果。</p><h2>开始前</h2>
<p>加载 v2512 环境。内部脚本使用完整路径调用；在个人可写工作目录中生成输出。</p>
<h2>示例 1：列出源码应用目标</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamGrepExeTargets"
</code></pre>
<p>扫描 EXE 条目并输出应用目录名，默认尽量使用 Git 索引。</p>
<h2>示例 2：列出已安装程序</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamGrepExeTargets" -bin
</code></pre>
<p>直接列出 FOAM_APPBIN，包含实际目录内容。</p>
<h2>示例 3：扫描解压源码树</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamGrepExeTargets" -no-git
</code></pre>
<p>使用文件系统查找 Make/files，适合无 .git 的源码包。</p>
<h2>示例 4：查找未构建目标</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamGrepExeTargets" -no-git &gt; targets-source
"$WM_PROJECT_DIR/bin/tools/foamGrepExeTargets" -bin &gt; targets-built
diff -u targets-source targets-built
</code></pre>
<p>比较源码目标名与已生成程序，差异供定位遗漏或额外程序。</p>
<h2>示例 5：筛选网格工具</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamGrepExeTargets" -no-git | grep -i mesh
</code></pre>
<p>按名称筛选包含 mesh 的目标，辅助查找相关源码编译单元。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-bin</code></td><td>列出 $FOAM_APPBIN 中的程序，此操作无需 Git。</td></tr><tr><td><code>-no-git</code></td><td>直接扫描文件获取信息，跳过 Git 查询。</td></tr><tr><td><code>-help</code></td><td>显示用法。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamGrepExeTargets">源码与说明</a> · <a href="/assets/command-help/foamgrepexetargets.txt">帮助文本</a></p>
