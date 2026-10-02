---
title: "foamCreateModuleInclude · 生成供环境模块系统使用的设置草稿"
layout: reference
description: "生成供环境模块系统使用的设置草稿。"
cms_slug: "command-foamcreatemoduleinclude"
---

<p>生成供环境模块系统使用的设置草稿。</p><h2>开始前</h2>
<p>加载 v2512 环境。内部脚本使用完整路径调用；在个人可写工作目录中生成输出。 用于集群 Environment Modules 配置生成，需要能够加载目标安装。输出是模块片段，供完整 modulefile 引用。</p>
<h2>示例 1：生成 Tcl 模块片段</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamCreateModuleInclude" -output=ModuleInclude.tcl "$WM_PROJECT_DIR"
</code></pre>
<p>默认 Tcl 格式，记录加载该安装所需的环境变化。</p>
<h2>示例 2：生成 shell 设置</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamCreateModuleInclude" -sh -output=ModuleInclude.sh "$WM_PROJECT_DIR"
</code></pre>
<p>-sh 输出 shell 格式，可供脚本检查或加载。</p>
<h2>示例 3：加载指定偏好文件</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamCreateModuleInclude" -prefs="$HOME/.OpenFOAM/prefs.sh" -output=ModulePrefs.tcl "$WM_PROJECT_DIR"
</code></pre>
<p>使用已经准备好的偏好文件生成相应编译配置。</p>
<h2>示例 4：保留 ParaView 环境</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamCreateModuleInclude" -paraview -output=ModuleParaView.tcl "$WM_PROJECT_DIR"
</code></pre>
<p>让片段包含 ParaView 相关路径设置。</p>
<h2>示例 5：指定构建临时目录</h2>
<pre><code class="language-bash">mkdir -p module-tmp
"$WM_PROJECT_DIR/bin/tools/foamCreateModuleInclude" -tmpdir="$PWD/module-tmp" -debug -output=ModuleDebug.tcl "$WM_PROJECT_DIR"
</code></pre>
<p>使用独立临时目录，-debug 保留中间文件供比较环境变化。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-output=file</code></td><td>指定输出文件名，默认为 ModuleInclude.tcl。</td></tr><tr><td><code>-prefs=file</code></td><td>指定要加载的 OpenFOAM 偏好配置文件。</td></tr><tr><td><code>-preload=file</code></td><td>指定预先加载的 shell 文件；可重复使用。</td></tr><tr><td><code>-tmpdir=file</code></td><td>指定临时文件目录。</td></tr><tr><td><code>-aliases</code></td><td>同时输出命令别名；加载后会影响同名命令的调用。</td></tr><tr><td><code>-paraview</code></td><td>保留 ParaView 相关配置。</td></tr><tr><td><code>-sh | -tcl</code></td><td>指定输出格式为 sh 或 Tcl，默认为 Tcl。</td></tr><tr><td><code>-debug</code></td><td>保留中间文件，便于调试。</td></tr><tr><td><code>-reduce=NUM</code></td><td>设置环境变量精简级别，属于实验功能。</td></tr><tr><td><code>-help</code></td><td>显示用法。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamCreateModuleInclude">源码与说明</a> · <a href="/assets/command-help/foamcreatemoduleinclude.txt">帮助文本</a></p>
