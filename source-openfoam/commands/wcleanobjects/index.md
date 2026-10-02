---
title: "wcleanObjects · 清理项目 build 目录中的指定平台编译中间文件"
layout: reference
description: "清理项目 build 目录中的指定平台编译中间文件。"
cms_slug: "command-wcleanobjects"
---

<p>清理项目 build 目录中的指定平台编译中间文件。</p><h2>开始前</h2>
<p>先加载 v2512 环境。内部工具使用完整路径；所有输出放在个人可写目录。 此工具要求当前目录等于 WM_PROJECT_DIR 或 WM_THIRD_PARTY_DIR，并删除 build 下匹配的目录。下面使用新建的演示项目并仅在子 shell 中覆盖 WM_PROJECT_DIR，完全隔离正式安装。</p>
<h2>示例 1：清理当前配置</h2>
<pre><code class="language-bash">tool="$WM_PROJECT_DIR/wmake/scripts/wcleanObjects"
demoProject=$(mktemp -d "$HOME/foam-clean-build.XXXXXX")
mkdir -p "$demoProject/build/$WM_OPTIONS"
(cd "$demoProject" &amp;&amp; WM_PROJECT_DIR="$demoProject" "$tool" current)
</code></pre>
<p>删除本例 build/当前配置 目录。</p>
<h2>示例 2：指定精确平台名称</h2>
<pre><code class="language-bash">tool="$WM_PROJECT_DIR/wmake/scripts/wcleanObjects"
demoProject=$(mktemp -d "$HOME/foam-clean-build.XXXXXX")
mkdir -p "$demoProject/build/linux64GccDPInt32Opt"
(cd "$demoProject" &amp;&amp; WM_PROJECT_DIR="$demoProject" "$tool" linux64GccDPInt32Opt)
</code></pre>
<p>处理指定名称及源码规则允许的同前缀目录。</p>
<h2>示例 3：选择一个编译器系列</h2>
<pre><code class="language-bash">tool="$WM_PROJECT_DIR/wmake/scripts/wcleanObjects"
demoProject=$(mktemp -d "$HOME/foam-clean-build.XXXXXX")
mkdir -p "$demoProject/build/${WM_ARCH}GccDPInt32Opt"
(cd "$demoProject" &amp;&amp; WM_PROJECT_DIR="$demoProject" "$tool" -compiler=Gcc)
</code></pre>
<p>-compiler=Gcc 选择当前 WM_ARCH 加 Gcc 前缀的构建目录。</p>
<h2>示例 4：同时清理两个配置</h2>
<pre><code class="language-bash">tool="$WM_PROJECT_DIR/wmake/scripts/wcleanObjects"
demoProject=$(mktemp -d "$HOME/foam-clean-build.XXXXXX")
mkdir -p "$demoProject/build"/{configA,configB}
(cd "$demoProject" &amp;&amp; WM_PROJECT_DIR="$demoProject" "$tool" configA configB)
</code></pre>
<p>输入可给出多个平台目录名，分别处理。</p>
<h2>示例 5：清除整个演示构建树</h2>
<pre><code class="language-bash">tool="$WM_PROJECT_DIR/wmake/scripts/wcleanObjects"
demoProject=$(mktemp -d "$HOME/foam-clean-build.XXXXXX")
mkdir -p "$demoProject/build/configA"
(cd "$demoProject" &amp;&amp; WM_PROJECT_DIR="$demoProject" "$tool" all)
</code></pre>
<p>直接调用 wcleanObjects 默认目标是 build；all 移除整个演示 build。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-a | -all</code></td><td>等同于 all，处理全部目标。</td></tr><tr><td><code>-curr | -current</code></td><td>使用当前 WM_OPTIONS 对应的构建配置。</td></tr><tr><td><code>-comp | -compiler</code></td><td>匹配 $WM_ARCH$WM_COMPILER* 对应的构建配置。</td></tr><tr><td><code>-compiler=NAME</code></td><td>匹配 $WM_ARCH 后接指定编译器名称的构建配置。</td></tr><tr><td><code>-help</code></td><td>显示用法。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/scripts/wcleanObjects">源码与说明</a> · <a href="/assets/command-help/wcleanobjects.txt">帮助文本</a></p>
