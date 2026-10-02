---
title: "wmake · 读取 Make/files 和 Make/options，编译 OpenFOAM 应用或共享库"
layout: reference
description: "读取 Make/files 和 Make/options，编译 OpenFOAM 应用或共享库。"
cms_slug: "command-wmake"
---

<p>读取 Make/files 和 Make/options，编译 OpenFOAM 应用或共享库。</p><h2>开始前</h2>
<p>加载 v2512 编译环境。myUtility 与 myLibrary 是个人可写源码目录，各自具有 Make/files 和 Make/options；输出位置由 EXE 或 LIB 指定。</p>
<h2>示例 1：构建可执行程序</h2>
<pre><code class="language-bash">wmake myUtility
</code></pre>
<p>读取目标目录 Make 配置，生成可执行文件。</p>
<h2>示例 2：使用四个编译任务</h2>
<pre><code class="language-bash">wmake -j 4 myUtility
</code></pre>
<p>限制同时编译的任务数，减少大型项目构建耗时。</p>
<h2>示例 3：构建动态库</h2>
<pre><code class="language-bash">wmake libso myLibrary
</code></pre>
<p>按 LIB 目标生成共享库，供求解器或运行时选择机制加载。</p>
<h2>示例 4：只生成依赖</h2>
<pre><code class="language-bash">wmake dep myUtility
</code></pre>
<p>创建 lnInclude 和依赖信息，不完成最终链接。</p>
<h2>示例 5：为调试增加信息</h2>
<pre><code class="language-bash">wmake -debug-O0 myUtility
</code></pre>
<p>加调试符号、FULLDEBUG 并关闭优化，便于逐行调试当前应用。</p>
<h2>示例 6：编译整个用户项目树</h2>
<pre><code class="language-bash">wmake -all "$WM_PROJECT_USER_DIR/applications"
</code></pre>
<p>递归处理子目录；遇到 Allwmake 时按其流程构建。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-s | -silent</code></td><td>静默编译，省略命令回显。</td></tr><tr><td><code>-a | -all</code></td><td>编译所有子目录；存在 Allwmake 时执行该脚本。</td></tr><tr><td><code>-q | -queue</code></td><td>将构建任务汇总为一个 Makefile；存在 Allwmake 时执行该脚本。</td></tr><tr><td><code>-k | -keep-going</code></td><td>遇到错误后继续处理其他构建任务。</td></tr><tr><td><code>-j | -jN | -j N</code></td><td>使用全部或指定数量的处理器核心、硬件线程进行编译。</td></tr><tr><td><code>-update</code></td><td>更新 lnInclude 和依赖文件，并清理废弃文件、目录。</td></tr><tr><td><code>-all=FILE</code></td><td>执行当前目录中的指定脚本，替代 Allwmake。</td></tr><tr><td><code>-debug</code></td><td>添加 -g -DFULLDEBUG 编译选项。</td></tr><tr><td><code>-debug-O[g0123]</code></td><td>添加 -g -DFULLDEBUG，并指定优化级别。</td></tr><tr><td><code>-strict</code></td><td>启用更多废弃接口警告，对应 WM_COMPILE_CONTROL 中的 +strict。</td></tr><tr><td><code>-build-root=PATH</code></td><td>设置编译中间产物的 FOAM_BUILDROOT 目录。</td></tr><tr><td><code>-module-prefix=PATH</code></td><td>以绝对或相对路径指定 FOAM_MODULE_PREFIX。</td></tr><tr><td><code>-module-prefix=TYPE</code></td><td>按预设位置指定 FOAM_MODULE_PREFIX：u 或 user 为用户，g 或 group 为用户组，o 或 openfoam 为主安装目录。</td></tr><tr><td><code>-no-openfoam</code></td><td>关闭 OpenFOAM 库链接，对应 WM_COMPILE_CONTROL 中的 ~openfoam。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/make-files/">files</a> · <a href="/dictionaries/make-options/">options</a></p><details class="command-more-options"><summary>更多参数（20 项）</summary><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-openmp</code></td><td>编译、链接时启用 OpenMP，对应 +openmp。</td></tr><tr><td><code>-no-openmp</code></td><td>关闭 OpenMP，对应 ~openmp。</td></tr><tr><td><code>-no-scheduler</code></td><td>关闭基于调度器的并行编译。</td></tr><tr><td><code>-show-api</code></td><td>显示 Make 规则中的 API 版本值。</td></tr><tr><td><code>-show-ext-so</code></td><td>显示共享库扩展名，包含前导点号。</td></tr><tr><td><code>-show-c</code></td><td>显示所用的 C 编译器。</td></tr><tr><td><code>-show-cflags</code></td><td>显示 C 编译选项。</td></tr><tr><td><code>-show-cxx</code></td><td>显示所用的 C++ 编译器。</td></tr><tr><td><code>-show-cxxflags</code></td><td>显示 C++ 编译选项。</td></tr><tr><td><code>-show-cflags-arch</code></td><td>显示 C 编译器的架构选项，例如 -m64。</td></tr><tr><td><code>-show-cxxflags-arch</code></td><td>显示 C++ 编译器的架构选项，例如 -m64。</td></tr><tr><td><code>-show-compile-c</code></td><td>同时显示 C 编译器与编译选项，等同于 -show-c -show-cflags。</td></tr><tr><td><code>-show-path-c</code></td><td>显示 C 编译器路径。</td></tr><tr><td><code>-show-path-cxx</code></td><td>显示 C++ 编译器路径。</td></tr><tr><td><code>-show-mpi-link</code></td><td>显示链接时使用的 MPI 选项。</td></tr><tr><td><code>-show-openmp-compile</code></td><td>显示编译时使用的 OpenMP 选项。</td></tr><tr><td><code>-show-openmp-link</code></td><td>显示编译时使用的 OpenMP 选项。</td></tr><tr><td><code>-build-info</code></td><td>查询或管理 api、branch、build 构建信息。</td></tr><tr><td><code>-check-dir</code></td><td>检查两个目录是否相同。</td></tr><tr><td><code>-with-bear</code></td><td>通过 bear 调用 wmake，生成 JSON 编译数据库。</td></tr></tbody></table></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/wmake/wmake">源码与说明</a> · <a href="/assets/command-help/wmake.txt">帮助文本</a></p>
