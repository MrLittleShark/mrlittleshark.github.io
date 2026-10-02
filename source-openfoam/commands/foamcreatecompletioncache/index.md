---
title: "foamCreateCompletionCache · 生成 OpenFOAM 命令补全缓存"
layout: reference
description: "生成 OpenFOAM 命令补全缓存。"
cms_slug: "command-foamcreatecompletioncache"
---

<p>生成 OpenFOAM 命令补全缓存。</p><h2>开始前</h2>
<p>加载 v2512 环境。内部脚本使用完整路径调用；在个人可写工作目录中生成输出。 已安装的 OpenFOAM 应用需支持程序帮助查询，输出路径使用个人文件。</p>
<h2>示例 1：为单个程序建缓存</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamCreateCompletionCache" -output completion-blockMesh blockMesh
</code></pre>
<p>提取 blockMesh 的补全信息，写入指定文件。</p>
<h2>示例 2：为网格工具建缓存</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamCreateCompletionCache" -output completion-mesh blockMesh checkMesh snappyHexMesh
</code></pre>
<p>合并三个程序的选项补全。</p>
<h2>示例 3：扫描默认程序目录</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamCreateCompletionCache" -output completion-all
</code></pre>
<p>未指定程序时扫描 FOAM_APPBIN。</p>
<h2>示例 4：包含个人程序</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamCreateCompletionCache" -user -output completion-with-user
</code></pre>
<p>-user 把 FOAM_USER_APPBIN 加入搜索范围。</p>
<h2>示例 5：单独处理用户目录</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamCreateCompletionCache" -dir "$FOAM_USER_APPBIN" -no-header -output completion-user
</code></pre>
<p>限定输入目录并省略文件头，便于与其他缓存拼接。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-dir DIR</code></td><td>Directory to process</td></tr><tr><td><code>-user</code></td><td>Add \$FOAM_USER_APPBIN to the search directories</td></tr><tr><td><code>-no-header</code></td><td>Suppress header generation Write to alternative output</td></tr><tr><td><code>-h | -help</code></td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamCreateCompletionCache [OPTION] [appName .. [appNameN]]
options:
  -dir DIR          Directory to process
  -user             Add \$FOAM_USER_APPBIN to the search directories
  -no-header        Suppress header generation
  -output FILE, -o FILE
                    Write to alternative output
  -h | -help        Print the usage

Create cache of bash completion values for OpenFOAM applications.
The cached values are typically used by the tcsh completion wrapper.
Default search: \$FOAM_APPBIN only.
Default output: $defaultOutputFile

Uses the search directory if applications are specified.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamCreateCompletionCache">源码与说明</a> · <a href="/assets/command-help/foamcreatecompletioncache.txt">帮助文本</a></p>
