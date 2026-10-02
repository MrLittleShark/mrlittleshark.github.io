---
title: "wmakeWindowsDlOpenLibs · 为 Windows 程序生成运行时加载的动态库列表"
layout: reference
description: "为 Windows 程序生成运行时加载的动态库列表。"
cms_slug: "command-wmakewindowsdlopenlibs"
---

<p>为 Windows 程序生成运行时加载的动态库列表。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 读取预处理后的单行 EXE_LIBS，检查 Windows DLL 是否存在并生成 FOAM_DLOPEN_LIBS 编译宏。以下用独立空 DLL 文件演示发现规则，不运行这些文件。</p>
<h2>示例 1：发现核心 DLL</h2>
<pre><code class="language-bash">demoLib=$(mktemp -d "$HOME/foam-dll-demo.XXXXXX")
touch "$demoLib/libOpenFOAM.dll"
printf 'EXE_LIBS = -lOpenFOAM\n' &gt; options.demo
FOAM_LIBBIN="$demoLib" "$WM_PROJECT_DIR/wmake/scripts/wmakeWindowsDlOpenLibs" options.demo
</code></pre>
<p>找到对应文件后输出 EXE_INC 附加宏，宏值包含 OpenFOAM。</p>
<h2>示例 2：发现两个库</h2>
<pre><code class="language-bash">demoLib=$(mktemp -d "$HOME/foam-dll-demo.XXXXXX")
touch "$demoLib"/lib{OpenFOAM,finiteVolume}.dll
printf 'EXE_LIBS = -lOpenFOAM -lfiniteVolume\n' &gt; options.two
FOAM_LIBBIN="$demoLib" "$WM_PROJECT_DIR/wmake/scripts/wmakeWindowsDlOpenLibs" options.two
</code></pre>
<p>两个存在的 DLL 都加入列表，供 Windows 运行时显式加载。</p>
<h2>示例 3：处理用户 DLL</h2>
<pre><code class="language-bash">demoLib=$(mktemp -d "$HOME/foam-dll-demo.XXXXXX")
touch "$demoLib/libMyModel.dll"
printf 'EXE_LIBS = -lMyModel\n' &gt; options.user
FOAM_USER_LIBBIN="$demoLib" "$WM_PROJECT_DIR/wmake/scripts/wmakeWindowsDlOpenLibs" options.user
</code></pre>
<p>也会搜索 FOAM_USER_LIBBIN，适用于个人模型库。</p>
<h2>示例 4：忽略目录和目标文件项</h2>
<pre><code class="language-bash">demoLib=$(mktemp -d "$HOME/foam-dll-demo.XXXXXX")
touch "$demoLib/libMyModel.dll"
printf 'EXE_LIBS = -L/tmp/libs helper.o -lMyModel\n' &gt; options.mixed
FOAM_USER_LIBBIN="$demoLib" "$WM_PROJECT_DIR/wmake/scripts/wmakeWindowsDlOpenLibs" options.mixed
</code></pre>
<p>只从 -l 名称中筛选可找到的 DLL，-L 与 .o 不转成库名。</p>
<h2>示例 5：查看不存在的库项</h2>
<pre><code class="language-bash">printf 'EXE_LIBS = -lFoamDemoMissingLibrary\n' &gt; options.missing
"$WM_PROJECT_DIR/wmake/scripts/wmakeWindowsDlOpenLibs" options.missing
</code></pre>
<p>找不到对应 DLL 时不输出加载宏，便于核对打包遗漏。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wmakeWindowsDlOpenLibs">源码与说明</a> · <a href="/assets/command-help/wmakewindowsdlopenlibs.txt">帮助文本</a></p>
