---
title: "polyDualMesh · 把体网格转成保留几何特征的对偶多面体网格"
layout: reference
description: "把体网格转成保留几何特征的对偶多面体网格。"
cms_slug: "command-polydualmesh"
---

<p>把体网格转成保留几何特征的对偶多面体网格。</p><h2>开始前</h2>
<p>已有可转换的 polyMesh；featureAngle 以度表示。各比较案例使用相同原始网格副本。</p>
<h2>示例 1：按30度特征角生成对偶网格</h2>
<pre><code class="language-bash">polyDualMesh 30
</code></pre>
<p>位置参数30控制边界特征识别；程序沿特征边与patch边界构造对偶单元，输出新网格时间。</p>
<h2>示例 2：保留更细的几何转折</h2>
<pre><code class="language-bash">polyDualMesh 15
</code></pre>
<p>较小特征角把更多法向变化识别为特征，适合比较对偶网格对较缓转折的保留程度。</p>
<h2>示例 3：处理凹边附近的单元</h2>
<pre><code class="language-bash">polyDualMesh 30 -concaveMultiCells
</code></pre>
<p>在凹边界边附近允许生成多个单元，改善该位置的对偶拓扑表达，随后检查凹角网格。</p>
<h2>示例 4：让相邻单元之间保留多个面</h2>
<pre><code class="language-bash">polyDualMesh 30 -splitAllFaces
</code></pre>
<p>-splitAllFaces 允许相邻对偶单元之间存在多个面，适合研究对偶拓扑及面拆分方式。</p>
<h2>示例 5：忽略原 faceZone 保留并更新</h2>
<pre><code class="language-bash">polyDualMesh 30 -doNotPreserveFaceZones -overwrite
checkMesh
</code></pre>
<p>关闭默认的 faceZone 特殊保留策略，写回当前网格；用于不需要原面区约束的转换流程，随后检查网格。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-splitAllFaces</code></td><td>Have multiple faces in between cells</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: polyDualMesh [OPTIONS] &lt;featureAngle&gt;
Arguments:
  &lt;featureAngle&gt;    in degrees [0-180]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -concaveMultiCells
                    Split cells on concave boundary edges into multiple cells
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -doNotPreserveFaceZones
                    Disable the default behaviour of preserving faceZones by
                    having multiple faces in between cells
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
  -overwrite        Overwrite existing mesh/results files
  -splitAllFaces    Have multiple faces in between cells
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Creates the dual of a polyMesh, adhering to all the feature and patch edges.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/polyDualMesh/meshDualiser.C">源码与说明</a> · <a href="/assets/command-help/polydualmesh.txt">帮助文本</a></p>
