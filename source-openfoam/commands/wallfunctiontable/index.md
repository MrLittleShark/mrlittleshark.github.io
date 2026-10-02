---
title: "wallFunctionTable · 为查表壁面函数生成速度壁面律反查表"
layout: reference
description: "为查表壁面函数生成速度壁面律反查表。"
cms_slug: "command-wallfunctiontable"
---

<p>为查表壁面函数生成速度壁面律反查表。</p><h2>开始前</h2>
<p>已有网格和constant/wallFunctionDict；官方注释示例采用SpaldingsLaw，可配置表名、步长、区间和对数坐标。</p>
<h2>示例 1：从官方示例生成表</h2>
<pre><code class="language-bash">cp "$WM_PROJECT_DIR/etc/caseDicts/annotated/wallFunctionDict" constant/wallFunctionDict
wallFunctionTable
</code></pre>
<p>使用SpaldingsLaw默认系数生成uPlusWallFunctionData，日志给出输出路径。</p>
<h2>示例 2：提高表格分辨率</h2>
<pre><code class="language-bash">foamDictionary constant/wallFunctionDict -entry dx -set 0.1
wallFunctionTable
</code></pre>
<p>dx由默认0.2改为0.1；在相同坐标区间内增加采样密度，减小后续查表间距。</p>
<h2>示例 3：扩展表格上限</h2>
<pre><code class="language-bash">foamDictionary constant/wallFunctionDict -entry xMax -set 8
wallFunctionTable
</code></pre>
<p>保留log10设置时，xMax表示对数坐标上界；提高上限扩展可查询的Re范围。</p>
<h2>示例 4：使用另一输出表名</h2>
<pre><code class="language-bash">foamDictionary constant/wallFunctionDict -entry invertedTableName -set uPlusFine
wallFunctionTable
</code></pre>
<p>将结果保存为uPlusFine，便于同时保留不同分辨率的壁面律表。</p>
<h2>示例 5：比较壁面律常数</h2>
<pre><code class="language-bash">foamDictionary constant/wallFunctionDict -entry SpaldingsLawCoeffs/kappa -set 0.40
wallFunctionTable
</code></pre>
<p>在独立参数方案中把kappa改为0.40，比较相同Re位置的u+；其余系数与坐标设置保持一致。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: wallFunctionTable [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
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
  -mpi-no-comm-dup  Disable initial MPI_Comm_dup()
  -mpi-split-by-appnum
                    Split world communicator based on the APPNUM
  -mpi-threads      Request use of MPI threads
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -parallel         Run in parallel
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Generates a table suitable for use by tabulated wall functions

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/wallFunctionTable/wallFunctionTable.C">源码与说明</a> · <a href="/assets/command-help/wallfunctiontable.txt">帮助文本</a></p>
