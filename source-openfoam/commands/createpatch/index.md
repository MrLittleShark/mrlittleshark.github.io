---
title: "createPatch · 把已有边界面或 faceSet 重组为指定 patch"
layout: reference
description: "把已有边界面或 faceSet 重组为指定 patch。"
cms_slug: "command-createpatch"
---

<p>把已有边界面或 faceSet 重组为指定 patch。</p><h2>开始前</h2>
<p>已有网格和 system/createPatchDict；字典中的 patches/source 对应实际边界或 faceSet。</p>
<h2>示例 1：按默认字典重组边界</h2>
<pre><code class="language-bash">createPatch
</code></pre>
<p>读取 createPatchDict，把选定面归入新 patch，输出新网格时间目录；检查日志中的新 patch 名称和面数。</p>
<h2>示例 2：将入口拆分方案写回网格</h2>
<pre><code class="language-bash">createPatch -dict system/createPatch-inletDict -overwrite
</code></pre>
<p>替代字典描述入口面分组；-overwrite 更新当前 boundary 与相关网格文件，便于后续按新名称填写 0/ 下边界条件。</p>
<h2>示例 3：检查周期面配对</h2>
<pre><code class="language-bash">createPatch -writeObj
</code></pre>
<p>字典已经定义 cyclic 配对时，额外写 OBJ 匹配几何，供可视化检查两侧位置与对应关系。</p>
<h2>示例 4：为指定区域整理边界</h2>
<pre><code class="language-bash">createPatch -region fluid -overwrite
</code></pre>
<p>只重组 fluid 区域的边界，适合多区域案例中单独修正流体入口、出口和壁面名称。</p>
<h2>示例 5：依次处理所有区域</h2>
<pre><code class="language-bash">createPatch -allRegions -overwrite
checkMesh -allRegions
</code></pre>
<p>regionProperties 已列出各区域且相应字典已准备好；-allRegions 对所有区域执行重组，再逐区域检查结果。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-allRegions</code></td><td>处理 regionProperties 中列出的所有区域。</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-parallel</code></td><td>启用并行运行；由 mpirun 启动相应进程数。</td></tr><tr><td><code>-region &lt;name&gt;</code></td><td>指定网格区域名称。</td></tr><tr><td><code>-writeObj</code></td><td>Write obj files showing the cyclic matching process</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-createpatchdict/">createPatchDict</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: createPatch [OPTIONS]
Options:
  -allRegions       Use all regions in regionProperties
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -decomposeParDict &lt;file&gt;
                    Alternative decomposePar dictionary file
  -dict &lt;file&gt;      Alternative createPatchDict
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
  -region &lt;name&gt;    Use specified mesh region. Eg, -region gas
  -regions &lt;wordRes&gt;
                    Use specified mesh region. Eg, -regions gas
                    Or from regionProperties.  Eg, -regions &#x27;(gas &quot;solid.*&quot;)&#x27;
  -roots &lt;(dir1 .. dirN)&gt;
                    Subprocess root directories for distributed running
  -world &lt;name&gt;     Name of the local world for parallel communication
  -writeObj         Write obj files showing the cyclic matching process
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Create patches out of selected boundary faces, which are either from existing
patches or from a faceSet

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/createPatch/createPatch.C">源码与说明</a> · <a href="/assets/command-help/createpatch.txt">帮助文本</a></p>
