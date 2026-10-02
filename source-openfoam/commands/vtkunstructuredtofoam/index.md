---
title: "vtkUnstructuredToFoam · 输入采用旧式 ASCII VTK 格式"
layout: reference
description: "输入采用旧式 ASCII VTK 格式。"
cms_slug: "command-vtkunstructuredtofoam"
---

<p>输入采用旧式 ASCII VTK 格式。</p><h2>开始前</h2>
<p>准备旧式 ASCII VTK UNSTRUCTURED_GRID 文件；转换器读取体网格，物理边界分组需后续建立。</p>
<h2>示例 1：导入 VTK 体网格</h2>
<pre><code class="language-bash">vtkUnstructuredToFoam mesh.vtk
</code></pre>
<p>读取点坐标和支持的单元连接，生成 OpenFOAM 网格。查看转换日志中的单元类型及数量。</p>
<h2>示例 2：检查混合单元网格</h2>
<pre><code class="language-bash">vtkUnstructuredToFoam mixed.vtk
checkMesh -constant -allTopology -allGeometry
</code></pre>
<p>输入包含多种受支持的体单元时，检查转换后的连接和单元质量。关注未识别单元以及异常体积报告。</p>
<h2>示例 3：换算毫米坐标</h2>
<pre><code class="language-bash">vtkUnstructuredToFoam mesh-mm.vtk
transformPoints -scale '(0.001 0.001 0.001)'
</code></pre>
<p>转换后缩放全网格到米制，便于与其他 OpenFOAM 案例的物性和边界条件一致。</p>
<h2>示例 4：按外形建立边界分区</h2>
<pre><code class="language-bash">vtkUnstructuredToFoam mesh.vtk
autoPatch 45 -overwrite
</code></pre>
<p>转换器没有物理边界信息，第二步按特征角划分外表面。根据实际位置进一步命名和配置场边界。</p>
<h2>示例 5：在独立案例提取表面核对</h2>
<pre><code class="language-bash">vtkUnstructuredToFoam /data/mesh.vtk -case ../vtkCase
foamToSurface vtk-boundary.obj -case ../vtkCase -constant
</code></pre>
<p>将转换结果放入 vtkCase，并导出外表面。与原 VTK 数据叠加查看，检查几何位置、尺度和边界是否完整。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: vtkUnstructuredToFoam [OPTIONS] &lt;vtk-file&gt;
Arguments:
  &lt;vtk-file&gt;        The input legacy ascii vtk file
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
  -noFunctionObjects
                    Do not execute function objects
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Convert legacy VTK file (ascii) containing an unstructured grid to an OpenFOAM
mesh without boundary information

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/vtkUnstructuredToFoam/vtkUnstructuredToFoam.C">源码与说明</a> · <a href="/assets/command-help/vtkunstructuredtofoam.txt">帮助文本</a></p>
