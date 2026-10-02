---
title: "ideasUnvToFoam · 转换后检查边界、长度单位和单元类型"
layout: reference
description: "转换后检查边界、长度单位和单元类型。"
cms_slug: "command-ideasunvtofoam"
---

<p>转换后检查边界、长度单位和单元类型。</p><h2>开始前</h2>
<p>准备 I-DEAS Universal .unv 文件；按实际导出单位核对坐标，确保所需边界分组随文件一并导出。</p>
<h2>示例 1：导入 UNV 网格</h2>
<pre><code class="language-bash">ideasUnvToFoam mesh.unv
</code></pre>
<p>读取通用格式中的网格与分组，写出 OpenFOAM polyMesh。检查单元数量和边界名称与原模型是否对应。</p>
<h2>示例 2：导出边界调试几何</h2>
<pre><code class="language-bash">ideasUnvToFoam mesh.unv -dump
</code></pre>
<p>转换时额外写出 boundaryFaces.obj，便于可视化核对读取到的边界面。适合排查分组与几何位置不对应的问题。</p>
<h2>示例 3：转换毫米坐标</h2>
<pre><code class="language-bash">ideasUnvToFoam mesh-mm.unv
transformPoints -scale '(0.001 0.001 0.001)'
</code></pre>
<p>导入完成后统一将节点坐标换算为米。后续 checkMesh 的边界框应对应模型的实际米制尺寸。</p>
<h2>示例 4：在独立案例检查全部连接</h2>
<pre><code class="language-bash">ideasUnvToFoam /data/mesh.unv -case ../unvCase
checkMesh -case ../unvCase -constant -allTopology
</code></pre>
<p>转换结果写入 unvCase，随后检查面连接和不连通区域。便于把格式转换问题与已有求解设置分开排查。</p>
<h2>示例 5：整理分组后查看外形</h2>
<pre><code class="language-bash">ideasUnvToFoam mesh.unv
createPatch -overwrite
foamToSurface unv-boundary.obj -constant
</code></pre>
<p>先依据导入名称编写 createPatchDict，再整理边界并导出外表面。对照原始几何检查入口、出口和壁面归属。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dump</code></td><td>Dump boundary faces as boundaryFaces.obj (for debugging) Override the file handler type Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: ideasUnvToFoam [OPTIONS] &lt;.unv file&gt;
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dump             Dump boundary faces as boundaryFaces.obj (for debugging)
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
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Convert I-Deas unv format to OpenFOAM

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/ideasUnvToFoam/ideasUnvToFoam.C">源码与说明</a> · <a href="/assets/command-help/ideasunvtofoam.txt">帮助文本</a></p>
