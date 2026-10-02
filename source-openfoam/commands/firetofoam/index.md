---
title: "fireToFoam · 转换后检查长度单位"
layout: reference
description: "转换后检查长度单位。"
cms_slug: "command-firetofoam"
---

<p>转换后检查长度单位。</p><h2>开始前</h2>
<p>准备 AVL FIRE 的多面体网格文件，目标案例包含基本 system 配置。</p>
<h2>示例 1：导入 FIRE 网格</h2>
<pre><code class="language-bash">fireToFoam mesh.fpma
</code></pre>
<p>读取 FIRE 多面体网格并写入 OpenFOAM。默认采用二进制网格输出，转换后可通过 checkMesh 查看结构。</p>
<h2>示例 2：导出为可读的网格文件</h2>
<pre><code class="language-bash">fireToFoam mesh.fpma -ascii
</code></pre>
<p>把网格写为 ASCII 格式，便于直接查看 points、faces 和 boundary。大型网格的文件体积会相应增加。</p>
<h2>示例 3：开启额外边检查</h2>
<pre><code class="language-bash">fireToFoam mesh.fpma -check
</code></pre>
<p>转换时增加边相关检查，帮助定位输入面连接问题。结合后续 checkMesh 的拓扑报告判断错误位置。</p>
<h2>示例 4：将毫米网格换算为米</h2>
<pre><code class="language-bash">fireToFoam mesh.fpma -scale 0.001
</code></pre>
<p>对顶点坐标进行单位转换。检查输出包围盒，再设置以米为长度单位的物性和边界条件。</p>
<h2>示例 5：在指定案例进行完整检查</h2>
<pre><code class="language-bash">fireToFoam /data/mesh.fpma -case ../fireCase -ascii -check
checkMesh -case ../fireCase -constant -allGeometry -allTopology
</code></pre>
<p>将转换和检查集中到 fireCase。查看负体积、面连接和边界分区，确认网格可用于后续求解。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-ascii</code></td><td>Write in ASCII format instead of binary</td></tr><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-check</code></td><td>Perform edge checking as well Set named DebugSwitch (default value: 1). [Can be used multiple times] Override the file handler type Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-scale &lt;scale&gt;</code></td><td>Geometry scaling factor - default is 1 (no scaling)</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: fireToFoam [OPTIONS] &lt;firePolyMesh&gt;
Arguments:
  &lt;firePolyMesh&gt;    The input FIRE mesh
Options:
  -ascii            Write in ASCII format instead of binary
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -check            Perform edge checking as well
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -scale &lt;scale&gt;    Geometry scaling factor - default is 1 (no scaling)
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Convert AVL/FIRE polyhedral mesh to OpenFOAM format

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/fireToFoam/fireToFoam.C">源码与说明</a> · <a href="/assets/command-help/firetofoam.txt">帮助文本</a></p>
