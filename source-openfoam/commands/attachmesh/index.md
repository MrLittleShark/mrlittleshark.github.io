---
title: "attachMesh · 用于相应的拓扑连接流程"
layout: reference
description: "用于相应的拓扑连接流程。"
cms_slug: "command-attachmesh"
---

<p>用于相应的拓扑连接流程。</p><h2>开始前</h2>
<p>已有拓扑分离的接口，以及 polyMesh/meshModifiers 中为其定义的网格修改器和对应 zone。工具按这些设置连接接口，在独立副本运行。</p>
<h2>示例 1：连接已定义的滑移接口</h2>
<pre><code class="language-bash">attachMesh
</code></pre>
<p>读取网格修改器并执行接口连接，默认把结果写到下一时间实例。检查日志中的接口处理信息和生成网格路径。</p>
<h2>示例 2：检查连接后的网格</h2>
<pre><code class="language-bash">attachMesh
checkMesh -latestTime -allTopology
</code></pre>
<p>使用新时间实例检查内部面、边界面和区域连通性。连接正确时，原先分离接口两侧应具有预期的拓扑关系。</p>
<h2>示例 3：在目标案例测试接口</h2>
<pre><code class="language-bash">attachMesh -case ../interfaceTest
checkMesh -case ../interfaceTest -latestTime
</code></pre>
<p>从独立 interfaceTest 案例读取网格及 meshModifiers。适合保留原始分离网格，同时对接口设置进行调整比较。</p>
<h2>示例 4：将已确认方案写回原位置</h2>
<pre><code class="language-bash">attachMesh -overwrite
checkMesh -constant -allTopology
</code></pre>
<p>在网格原实例为 constant 的副本中直接保存连接结果。之后继续计算时，网格读取路径与常规初始网格一致。</p>
<h2>示例 5：连接后优化单元编号</h2>
<pre><code class="language-bash">attachMesh -overwrite
renumberMesh -overwrite
checkMesh -constant
</code></pre>
<p>先形成连续的网格连接，再优化单元编号。检查连接和几何保持一致，供后续线性方程求解使用。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: attachMesh [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
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
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Attach topologically detached mesh using prescribed mesh modifiers

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/attachMesh/attachMesh.C">源码与说明</a> · <a href="/assets/command-help/attachmesh.txt">帮助文本</a></p>
