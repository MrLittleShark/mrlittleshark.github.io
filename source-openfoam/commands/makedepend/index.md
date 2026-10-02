---
title: "makeDepend · 封装预处理器的依赖生成命令，供构建规则使用"
layout: reference
description: "封装预处理器的依赖生成命令，供构建规则使用。"
cms_slug: "command-makedepend"
---

<p>封装预处理器的依赖生成命令，供构建规则使用。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 这是用 cpp -M 生成 C++ 依赖的测试包装器。先准备 main.C；WM_PRECISION_OPTION 和 WM_LABEL_SIZE 来自已加载环境。以下通过重定向保存依赖。</p>
<h2>示例 1：生成简单依赖</h2>
<pre><code class="language-bash">printf '#include "model.H"\nint main() { return 0; }\n' &gt; main.C
touch model.H
"$WM_PROJECT_DIR/wmake/scripts/makeDepend" main.C &gt; main.dep
</code></pre>
<p>cpp 读取 main.C 的头文件引用，输出 make 依赖规则。</p>
<h2>示例 2：增加头文件搜索目录</h2>
<pre><code class="language-bash">mkdir -p include
cp model.H include/model.H
"$WM_PROJECT_DIR/wmake/scripts/makeDepend" -Iinclude main.C &gt; main-with-include.dep
</code></pre>
<p>-Iinclude 传给预处理器，供解析该目录中的头文件。</p>
<h2>示例 3：给预处理分支定义宏</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/makeDepend" -DDEMO_FEATURE=1 -Iinclude main.C &gt; main-feature.dep
</code></pre>
<p>额外宏改变条件包含时，生成与该配置一致的依赖。</p>
<h2>示例 4：生成 OpenFOAM 源码依赖</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/wmake/scripts/makeDepend" -I"$WM_PROJECT_DIR/src/OpenFOAM/lnInclude" -I"$WM_PROJECT_DIR/src/OSspecific/POSIX/lnInclude" basicFoamTool.C &gt; basicFoamTool.dep
</code></pre>
<p>basicFoamTool.C 是只使用相应基础头文件的自编源码；所用库越多，需要追加相应 include 路径。</p>
<h2>示例 5：给两个源文件分别生成依赖</h2>
<pre><code class="language-bash">for src in main.C model.C; do "$WM_PROJECT_DIR/wmake/scripts/makeDepend" -Iinclude "$src" &gt; "${src%.C}.dep" || break; done
</code></pre>
<p>先准备 model.C；每个源文件得到独立依赖文件，失败时结束循环。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/makeDepend">源码与说明</a> · <a href="/assets/command-help/makedepend.txt">帮助文本</a></p>
