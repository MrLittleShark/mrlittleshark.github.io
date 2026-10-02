---
title: "foamExec · 使用安装目录中提供的环境包装脚本运行应用"
layout: reference
description: "使用安装目录中提供的环境包装脚本运行应用。"
cms_slug: "command-foamexec"
---

<p>使用安装目录中提供的环境包装脚本运行应用。</p><h2>开始前</h2>
<p>安装目录中需要存在 bin/tools/foamExec；以下无环境示例采用 /usr/lib/openfoam/openfoam2512，按本机安装位置替换。其余示例在已加载 v2512 环境的终端中运行。准备个人算例 caseA；生成网格时需有 system/blockMeshDict，检查网格时需已生成 constant/polyMesh。</p>
<h2>示例 1：从无 OpenFOAM 环境的终端生成网格</h2>
<pre><code class="language-bash">/usr/lib/openfoam/openfoam2512/bin/tools/foamExec blockMesh -case caseA
</code></pre>
<p>使用安装脚本的完整路径即可启动。包装器定位同一安装中的 etc/bashrc，加载程序与库路径，再运行 blockMesh；网格写入 caseA/constant/polyMesh。</p>
<h2>示例 2：执行网格检查</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamExec" checkMesh -case caseA -allTopology
</code></pre>
<p>其余参数原样传给程序，输出拓扑检查结果。</p>
<h2>示例 3：读取字典条目</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamExec" foamDictionary caseA/system/controlDict -entry application -value
</code></pre>
<p>程序可找到 OpenFOAM 动态库，并输出求解器名。</p>
<h2>示例 4：运行自己的脚本</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamExec" bash ./run-study.sh
</code></pre>
<p>先准备 run-study.sh；它继承已加载的计算环境，适合非交互批处理。</p>
<h2>示例 5：查看环境选择</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/foamExec" bash -c 'printf "%s\n" "$WM_OPTIONS" "$FOAM_APPBIN"'
</code></pre>
<p>单引号让变量在加载环境后的子 shell 展开。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-help</code></td><td>显示用法。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/foamExec">源码与说明</a> · <a href="/assets/command-help/foamexec.txt">帮助文本</a></p>
