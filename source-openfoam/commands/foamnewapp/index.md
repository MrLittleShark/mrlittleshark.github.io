---
title: "foamNewApp · 创建新应用程序的源码目录、主程序和编译配置"
layout: reference
description: "创建新应用程序的源码目录、主程序和编译配置。"
cms_slug: "command-foamnewapp"
---

<p>创建新应用程序的源码目录、主程序和编译配置。</p><h2>开始前</h2>
<p>在个人可写源码目录运行。每个应用名使用未占用的 C++ 标识符；生成骨架后自行实现功能。</p>
<h2>示例 1：建立应用骨架</h2>
<pre><code class="language-bash">foamNewApp inspectCase
</code></pre>
<p>生成 inspectCase/inspectCase.C 与 Make/files、Make/options。</p>
<h2>示例 2：生成后编译</h2>
<pre><code class="language-bash">foamNewApp fieldReporter
wmake fieldReporter
</code></pre>
<p>构建骨架应用到 FOAM_USER_APPBIN，可据此开始添加场读取代码。</p>
<h2>示例 3：阅读创建的编译配置</h2>
<pre><code class="language-bash">foamNewApp meshReporter
cat meshReporter/Make/files meshReporter/Make/options
</code></pre>
<p>显示应用目标路径、头文件路径和链接库，供添加依赖时参考。</p>
<h2>示例 4：放入个人工具分类</h2>
<pre><code class="language-bash">mkdir -p "$WM_PROJECT_USER_DIR/applications/utilities"
cd "$WM_PROJECT_USER_DIR/applications/utilities"
foamNewApp volumeSummary
</code></pre>
<p>按个人工具目录组织源码，应用模板在 volumeSummary 子目录中。</p>
<h2>示例 5：建立两个独立原型</h2>
<pre><code class="language-bash">for appName in pressureSummary velocitySummary; do foamNewApp "$appName"; done
</code></pre>
<p>每个原型拥有独立 Make 配置，便于分别扩展标量与矢量处理。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamNewApp">源码与说明</a> · <a href="/assets/command-help/foamnewapp.txt">帮助文本</a></p>
