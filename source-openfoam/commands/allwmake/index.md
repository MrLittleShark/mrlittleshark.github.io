---
title: "Allwmake · 按项目脚本规定的顺序批量编译库和应用程序"
layout: reference
description: "按项目脚本规定的顺序批量编译库和应用程序。"
cms_slug: "command-allwmake"
---

<p>按项目脚本规定的顺序批量编译库和应用程序。</p><h2>开始前</h2>
<p>这里指 OpenFOAM 根目录的 Allwmake。使用可写的完整源码安装，并加载该源码树的 etc/bashrc；将依次构建 wmake 工具、依赖、库和应用，需充足时间与磁盘。</p>
<h2>示例 1：构建完整源码</h2>
<pre><code class="language-bash">cd "$WM_PROJECT_DIR"
./Allwmake
</code></pre>
<p>按源码定义的依赖顺序构建，产物进入当前平台目录。</p>
<h2>示例 2：限制并发数</h2>
<pre><code class="language-bash">cd "$WM_PROJECT_DIR"
./Allwmake -j 4
</code></pre>
<p>向构建系统传递四个并行任务，控制内存占用。</p>
<h2>示例 3：保留构建日志</h2>
<pre><code class="language-bash">cd "$WM_PROJECT_DIR"
./Allwmake -j 4 -log=log.build-v2512
</code></pre>
<p>将输出同时写入指定日志，方便查找编译错误。</p>
<h2>示例 4：遇错继续构建独立部分</h2>
<pre><code class="language-bash">cd "$WM_PROJECT_DIR"
./Allwmake -j 4 -keep-going
</code></pre>
<p>继续尝试其他目标，适合收集依赖问题；最终从日志查找失败目标。</p>
<h2>示例 5：暂不构建附加模块</h2>
<pre><code class="language-bash">cd "$WM_PROJECT_DIR"
./Allwmake -j 4 -prefix=none
</code></pre>
<p>将模块前缀设为 none，使核心库和应用构建后跳过附加 modules。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/Allwmake">源码与说明</a> · <a href="/assets/command-help/allwmake.txt">帮助文本</a></p>
