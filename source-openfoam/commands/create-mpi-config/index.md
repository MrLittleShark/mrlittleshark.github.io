---
title: "create-mpi-config · 生成 MPI 的打包配置，记录编译和链接设置"
layout: reference
description: "生成 MPI 的打包配置，记录编译和链接设置。"
cms_slug: "command-create-mpi-config"
---

<p>生成 MPI 的打包配置，记录编译和链接设置。</p><h2>用法</h2><pre><code class="language-bash"># 查看安装中的脚本；这条命令不会执行脚本
sed -n &#x27;1,180p&#x27; &quot;$WM_PROJECT_DIR/bin/tools/create-mpi-config&quot;</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-dry-run, -n</td><td>Report but do not write config files</td></tr><tr><td>-no-mpicc</td><td>Bypass any use of mpicc (or orte-info)</td></tr><tr><td>-query-openmpi</td><td>Report installation directory for system openmpi</td></tr><tr><td>-write-openmpi</td><td>Query system openmpi and write config files</td></tr><tr><td>-write</td><td>Write config files using FOAM_MPI, MPI_ARCH_PATH</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 script source evidence
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
