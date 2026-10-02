---
title: "create-mpi-config · 生成 MPI 的打包配置，记录编译和链接设置"
layout: reference
description: "生成 MPI 的打包配置，记录编译和链接设置。"
cms_slug: "command-create-mpi-config"
---

<p>生成 MPI 的打包配置，记录编译和链接设置。</p><h2>开始前</h2>
<p>加载 v2512 环境。内部脚本使用完整路径调用；在个人可写工作目录中生成输出。 用于打包时固定 MPI 路径。以下采用 dry-run 预览，避免改写安装配置；MPI 必须已经安装。</p>
<h2>示例 1：查询系统 OpenMPI</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/create-mpi-config" -query-openmpi
</code></pre>
<p>通过系统工具或安装位置探测 MPI 根目录，输出路径。</p>
<h2>示例 2：预览配置生成</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/create-mpi-config" -dry-run -write-openmpi
</code></pre>
<p>查询系统 OpenMPI 后打印拟写入内容和位置。</p>
<h2>示例 3：跳过 mpicc 检测</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/create-mpi-config" -no-mpicc -query-openmpi
</code></pre>
<p>采用环境和常见安装目录探测，适用于运行环境不含编译包装器的安装。</p>
<h2>示例 4：按现有 MPI 环境预览</h2>
<pre><code class="language-bash">"$WM_PROJECT_DIR/bin/tools/create-mpi-config" -dry-run -write
</code></pre>
<p>使用当前 FOAM_MPI、MPI_ARCH_PATH 生成候选配置。</p>
<h2>示例 5：模拟打包前缀</h2>
<pre><code class="language-bash">FOAM_MPI=sys-openmpi MPI_ARCH_PATH=/opt/mpi "$WM_PROJECT_DIR/bin/tools/create-mpi-config" -dry-run -write
</code></pre>
<p>/opt/mpi 应替换为实际目标安装路径；输出固定前缀的候选文件内容。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-dry-run, -n</code></td><td>Report but do not write config files</td></tr><tr><td><code>-no-mpicc</code></td><td>Bypass any use of mpicc (or orte-info)</td></tr><tr><td><code>-query-openmpi</code></td><td>Report installation directory for system openmpi</td></tr><tr><td><code>-write-openmpi</code></td><td>Query system openmpi and write config files</td></tr><tr><td><code>-write</code></td><td>Write config files using FOAM_MPI, MPI_ARCH_PATH</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
Command: create-mpi-config
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/create-mpi-config

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

usage: create-mpi-config options

options:
  -dry-run, -n      Report but do not write config files
  -no-mpicc         Bypass any use of mpicc (or orte-info)
  -query-openmpi    Report installation directory for system openmpi
  -write-openmpi    Query system openmpi and write config files
  -write            Write config files using FOAM_MPI, MPI_ARCH_PATH

Define hard-coded packaging settings for MPI flavours.

Equivalent options:
  -write-system-openmpi | -write-openmpi
  -query-system-openmpi | -query-openmpi</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/create-mpi-config">源码与说明</a> · <a href="/assets/command-help/create-mpi-config.txt">帮助文本</a></p>
