---
title: "foamSequenceVTKFiles · 为 VTK 文件建立连续编号的链接，便于 ParaView 按时间序列读取"
layout: reference
description: "为 VTK 文件建立连续编号的链接，便于 ParaView 按时间序列读取。"
cms_slug: "command-foamsequencevtkfiles"
---

<p>为 VTK 文件建立连续编号的链接，便于 ParaView 按时间序列读取。</p><h2>开始前</h2>
<p>准备按时间目录存放的 VTK 采样结果。此脚本创建符号链接序列，不重写网格数据；示例在支持符号链接的 Linux 文件系统中运行。 输入目录中相邻时间的文件需保持相同文件名。-out 分支在 v2512 中会多消耗一个参数，下例将其置于末尾并附加 --，用于吸收该次参数移动；输出目录中原有内容会被清理。</p>
<h2>示例 1：整理默认 VTK 结果</h2>
<pre><code class="language-bash">foamSequenceVTKFiles -case caseA
</code></pre>
<p>搜索 postProcessing 下的 .vtk 文件，在默认 sequencedVTK 输出连续编号链接。</p>
<h2>示例 2：指定采样目录</h2>
<pre><code class="language-bash">foamSequenceVTKFiles -case caseA -dir postProcessing/surfaces
</code></pre>
<p>-dir 限定数据目录，避免合并无关采样。</p>
<h2>示例 3：处理 VTP 表面</h2>
<pre><code class="language-bash">foamSequenceVTKFiles -case caseA -vtp
</code></pre>
<p>选择 XML PolyData 扩展名 .vtp。</p>
<h2>示例 4：处理 VTU 网格</h2>
<pre><code class="language-bash">foamSequenceVTKFiles -case caseA -vtu
</code></pre>
<p>选择 XML UnstructuredGrid 扩展名 .vtu。</p>
<h2>示例 5：分开保存两组序列</h2>
<pre><code class="language-bash">foamSequenceVTKFiles -case caseA -dir postProcessing/planeA -out sequence-planeA --
foamSequenceVTKFiles -case caseA -dir postProcessing/planeB -out sequence-planeB --
</code></pre>
<p>分别生成两组独立链接序列。末尾 -- 用于兼容此版本 -out 分支的额外 shift；各输出目录专门用于本工具，原有内容会先被清理。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-c | -case &lt;dir&gt;</code></td><td>指定算例目录，默认使用当前目录。</td></tr><tr><td><code>-d | -dir &lt;dir&gt;</code></td><td>指定后处理目录，默认为 postProcessing。</td></tr><tr><td><code>-o | -out &lt;dir&gt;</code></td><td>指定输出链接目录，默认为 sequencedVTK。</td></tr><tr><td><code>-vtk</code></td><td>生成 VTK 文件序列，此项为默认设置。</td></tr><tr><td><code>-vtp</code></td><td>生成 VTP 文件序列。</td></tr><tr><td><code>-vtu</code></td><td>生成 VTU 文件序列。</td></tr><tr><td><code>-h | -help</code></td><td>显示帮助。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamSequenceVTKFiles">源码与说明</a> · <a href="/assets/command-help/foamsequencevtkfiles.txt">帮助文本</a></p>
