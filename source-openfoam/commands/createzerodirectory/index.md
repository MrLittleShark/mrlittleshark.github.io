---
title: "createZeroDirectory · 按求解器模板、湍流模型和 caseProperties 生成初始场"
layout: reference
description: "按求解器模板、湍流模型和 caseProperties 生成初始场。"
cms_slug: "command-createzerodirectory"
---

<p>按求解器模板、湍流模型和 caseProperties 生成初始场。</p><h2>开始前</h2>
<p>已有网格、system/controlDict、system/caseProperties及模型设置；每个实体边界在caseProperties中有对应条件。</p>
<h2>示例 1：生成所需初始字段</h2>
<pre><code class="language-bash">createZeroDirectory
</code></pre>
<p>根据controlDict的application和模型类型选择模板，在0目录生成匹配的场及边界条目。</p>
<h2>示例 2：使用个人模板库</h2>
<pre><code class="language-bash">createZeroDirectory -templateDir ./fieldTemplates
</code></pre>
<p>fieldTemplates具有与官方模板相同的solvers、models和边界模板结构；按自定义模板生成字段。</p>
<h2>示例 3：复制模板后定制</h2>
<pre><code class="language-bash">cp -r "$WM_PROJECT_DIR/etc/caseDicts/createZeroDirectoryTemplates" myTemplates
createZeroDirectory -templateDir ./myTemplates
</code></pre>
<p>先把官方模板复制为可编辑的个人版本，再用它生成场；后续可在该目录调整常用初值或边界模板。</p>
<h2>示例 4：湍流模型切换后重新配场</h2>
<pre><code class="language-bash">createZeroDirectory -case ./case-kOmegaSST
patchSummary -case ./case-kOmegaSST -time 0 -expand
</code></pre>
<p>独立案例已配置kOmegaSST及相应caseProperties；生成所需湍流场，并逐patch检查场类型。</p>
<h2>示例 5：多区域案例生成初值</h2>
<pre><code class="language-bash">createZeroDirectory -case ./heatExchanger
</code></pre>
<p>heatExchanger的求解器模板支持多区域，regionProperties及各区域caseProperties已配置；程序按区域分别生成流体和固体初始场。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: createZeroDirectory [OPTIONS]
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
  -templateDir &lt;dir&gt;
                    Read case set-up templates from specified location
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Create a 0/ directory with fields appropriate for the chosen solver and
turbulence model.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/preProcessing/createZeroDirectory/boundaryInfo.C">源码与说明</a> · <a href="/assets/command-help/createzerodirectory.txt">帮助文本</a></p>
