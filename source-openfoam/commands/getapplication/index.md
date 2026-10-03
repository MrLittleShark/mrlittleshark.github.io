---
title: "getApplication · 读取 controlDict 中指定的求解器或应用程序名称"
layout: reference
description: "读取 controlDict 中指定的求解器或应用程序名称。"
cms_slug: "command-getapplication"
---

<p>读取 controlDict 中指定的求解器或应用程序名称。</p><h2>开始前</h2>
<p>先在单独一行执行 source "$WM_PROJECT_DIR/bin/tools/RunFunctions"。示例在个人算例工作区操作，caseA、caseB 均为可修改的副本。</p>
<h2>示例 1：读取求解器名称</h2>
<pre><code class="language-bash">cd caseA
getApplication
</code></pre>
<p>读取 system/controlDict 中 application 的单值并输出。</p>
<h2>示例 2：把名称存为变量</h2>
<pre><code class="language-bash">cd caseA
solver=$(getApplication) || exit 1
printf 'Solver: %s\n' "$solver"
</code></pre>
<p>脚本中读取成功后继续，失败会停止脚本，避免使用错误名称。</p>
<h2>示例 3：运行字典指定程序</h2>
<pre><code class="language-bash">cd caseA
runApplication "$(getApplication)"
</code></pre>
<p>函数读取求解器名，runApplication 写入 log.&lt;求解器名&gt;。</p>
<h2>示例 4：批量检查求解器</h2>
<pre><code class="language-bash">for c in caseA caseB; do (cd "$c" &amp;&amp; printf '%s: ' "$c" &amp;&amp; getApplication); done
</code></pre>
<p>每个子 shell 从自己的 system/controlDict 读取，输出目录与求解器映射。</p>
<h2>示例 5：修改后重新读取</h2>
<pre><code class="language-bash">cd caseA
foamDictionary system/controlDict -entry application -set icoFoam
getApplication
</code></pre>
<p>仅对为 icoFoam 准备的算例执行；输出应变为 icoFoam，其他物性和场仍需匹配该求解器。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
