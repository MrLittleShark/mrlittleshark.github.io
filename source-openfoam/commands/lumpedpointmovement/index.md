---
title: "lumpedPointMovement · 采用对应耦合模型配置"
layout: reference
description: "采用对应耦合模型配置。"
cms_slug: "command-lumpedpointmovement"
---

<p>采用对应耦合模型配置。</p><h2>用法</h2><pre><code class="language-bash">lumpedPointMovement response.dat</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">lumpedPointMovement response.dat -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-dry-run</td><td>Test movement without a mesh Override the file handler type Per-subprocess root directories for distributed running. The host specification can be a regex. Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-max &lt;N&gt;</td><td>Maximum number of outputs</td></tr><tr><td>-parallel</td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td>-removeLock</td><td>Remove lock-file on termination of slave Subprocess root directories for distributed running</td></tr><tr><td>-scale &lt;factor&gt;</td><td>Relaxation/scaling factor for movement (default: 1)</td></tr><tr><td>-slave</td><td>Invoke as a slave responder for testing</td></tr><tr><td>-span &lt;N&gt;</td><td>Increment each input by N (default: 1) Visualization length for planes (visualized as triangles)</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: lumpedPointMovement [OPTIONS] &lt;responseFile&gt;
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dry-run          Test movement without a mesh
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -hostRoots &lt;((host1 dir1) .. (hostN dirN))&gt;
                    Per-subprocess root directories for distributed running.
                    The host specification can be a regex.
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -max &lt;N&gt;          Maximum number of outputs
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -removeLock       Remove lock-file on termination of slave
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -scale &lt;factor&gt;   Relaxation/scaling factor for movement (default: 1)
  -slave            Invoke as a slave responder for testing
  -span &lt;N&gt;         Increment each input by N (default: 1)
  -visual-length &lt;len&gt;
                    Visualization length for planes (visualized as triangles)
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Visualize lumpedPoint movements or provide a slave responder for diagnostic
purposes.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/lumped/lumpedPointMovement/lumpedPointMovement.C">源码与说明</a> · <a href="/assets/command-help/lumpedpointmovement.txt">帮助文本</a></p>
