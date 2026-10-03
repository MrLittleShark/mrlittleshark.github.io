---
title: "foamInstallationTest · 检查运行 OpenFOAM 所需的软件组件、安装路径和环境设置"
layout: reference
description: "检查运行 OpenFOAM 所需的软件组件、安装路径和环境设置。"
cms_slug: "command-foaminstallationtest"
---

<p>检查运行 OpenFOAM 所需的软件组件、安装路径和环境设置。</p><h2>开始前</h2>
<p>先加载目标 v2512 环境。此脚本检查已安装程序、编译器和 OpenFOAM 环境。</p>
<h2>示例 1：检查当前环境</h2>
<pre><code class="language-bash">foamInstallationTest
</code></pre>
<p>终端按项目显示检测结果，重点阅读缺失组件和路径。</p>
<h2>示例 2：比较初始化前后</h2>
<pre><code class="language-bash">bash --noprofile --norc -c 'source /usr/lib/openfoam/openfoam2512/etc/bashrc; foamInstallationTest'
</code></pre>
<p>在干净子 shell 中显式加载目标安装，排查个人启动文件带来的路径影响。</p>
<h2>示例 3：为源码构建选择 GCC</h2>
<pre><code class="language-bash">(source "$WM_PROJECT_DIR/etc/bashrc" WM_COMPILER=Gcc; foamInstallationTest)
</code></pre>
<p>在子 shell 中检查 Gcc 配置依赖，外层终端保持原配置。</p>
<h2>示例 4：在计算节点检查</h2>
<pre><code class="language-bash">ssh student@compute.example.org 'bash -lc "source /usr/lib/openfoam/openfoam2512/etc/bashrc; foamInstallationTest"'
</code></pre>
<p>替换远端用户与主机；检查发生在节点自身，输出返回本地。</p>
<h2>示例 5：在不同配置间比较</h2>
<pre><code class="language-bash">(source "$WM_PROJECT_DIR/etc/bashrc" WM_COMPILE_OPTION=Debug; foamInstallationTest)
</code></pre>
<p>检查 Debug 环境对应的程序、库或工具路径，适用于准备调试构建时。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamInstallationTest">源码与说明</a> · <a href="/assets/command-help/foaminstallationtest.txt">帮助文本</a></p>
