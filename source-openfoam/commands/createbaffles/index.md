---
title: "createBaffles · 将选定内部面改成挡板两侧的边界面"
layout: reference
description: "将选定内部面改成挡板两侧的边界面。"
cms_slug: "command-createbaffles"
---

<p>将选定内部面改成挡板两侧的边界面。</p><h2>开始前</h2>
<p>已有网格和 system/createBafflesDict；字典指定待转换面及两侧 patch。示例中的区域名、字典名应与案例一致。</p>
<h2>示例 1：生成挡板</h2>
<pre><code class="language-bash">createBaffles
</code></pre>
<p>读取默认字典，将选中内部面改成边界面，并在新的网格时间目录写入结果。日志给出选面与新边界信息。</p>
<h2>示例 2：使用另一套挡板位置</h2>
<pre><code class="language-bash">createBaffles -dict system/createBaffles-obliqueDict
</code></pre>
<p>预先准备描述斜挡板的字典；-dict 选择该文件，便于在相同基础网格上比较不同挡板位置。</p>
<h2>示例 3：直接更新预处理网格</h2>
<pre><code class="language-bash">createBaffles -overwrite
checkMesh
</code></pre>
<p>-overwrite 把改动写回当前网格。随后检查单元闭合、边界拓扑与网格质量，再继续初始化场。</p>
<h2>示例 4：只处理流体区域</h2>
<pre><code class="language-bash">createBaffles -region fluid -dict system/createBaffles-fluidDict -overwrite
</code></pre>
<p>多区域案例已有 fluid 网格；-region 限定修改对象，其他区域保持原有网格。结果是 fluid 内部新增的两侧挡板边界。</p>
<h2>示例 5：挡板生成后拆分共用顶点</h2>
<pre><code class="language-bash">createBaffles -overwrite
mergeOrSplitBaffles -split -overwrite
checkMesh
</code></pre>
<p>第一步创建面，第二步复制挡板两侧需要独立的顶点，适用于随后要让两侧独立运动的网格。最终检查拆分后的连通关系。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-createbafflesdict/">createBafflesDict</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: createBaffles [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative createBafflesDict
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
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -parallel         Run in parallel
  -region &lt;name&gt;    Specify mesh region (default: region0)
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Makes internal faces into boundary faces.
Does not duplicate points.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/createBaffles/faceSelection/faceSelection.C">源码与说明</a> · <a href="/assets/command-help/createbaffles.txt">帮助文本</a></p>
