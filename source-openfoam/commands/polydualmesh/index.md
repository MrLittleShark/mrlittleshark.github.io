---
title: "polyDualMesh · 生成后检查网格拓扑及场映射"
layout: reference
description: "生成后检查网格拓扑及场映射。"
cms_slug: "command-polydualmesh"
---

<p>生成后检查网格拓扑及场映射。</p><h2>用法</h2><pre><code class="language-bash">polyDualMesh 60 -overwrite</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">polyDualMesh 60 -overwrite -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-overwrite</td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td>-splitAllFaces</td><td>Have multiple faces in between cells</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: polyDualMesh [OPTIONS] &lt;featureAngle&gt;
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
