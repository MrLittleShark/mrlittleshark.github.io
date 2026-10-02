---
title: "foamSequenceVTKFiles · 生成的符号链接供 ParaView 识别时间序列"
layout: reference
description: "生成的符号链接供 ParaView 识别时间序列。"
cms_slug: "command-foamsequencevtkfiles"
---

<p>生成的符号链接供 ParaView 识别时间序列。</p><h2>用法</h2><pre><code class="language-bash">foamSequenceVTKFiles -dir postProcessing -out sequencedVTK</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-c | -case &lt;dir&gt;</td><td>specify case directory (default = local dir)</td></tr><tr><td>-d | -dir &lt;dir&gt;</td><td>post-processing directory &lt;dir&gt; (default = postProcessing)</td></tr><tr><td>-o | -out &lt;dir&gt;</td><td>output links directory &lt;dir&gt; (default = sequencedVTK)</td></tr><tr><td>-vtk</td><td>create sequence of vtk files (default)</td></tr><tr><td>-vtp</td><td>create sequence of vtp files</td></tr><tr><td>-vtu</td><td>create sequence of vtu files</td></tr><tr><td>-h | -help</td><td>help</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamSequenceVTKFiles [OPTIONS] ...
options:
  -c | -case &lt;dir&gt;    specify case directory (default = local dir)
  -d | -dir &lt;dir&gt;     post-processing directory &lt;dir&gt; (default = postProcessing)
  -o | -out &lt;dir&gt;     output links directory &lt;dir&gt; (default = sequencedVTK)
  -vtk                create sequence of vtk files (default)
  -vtp                create sequence of vtp files
  -vtu                create sequence of vtu files
  -h | -help          help

Creates symbolic links to all VTK files in a post-processing directory
Links form a sequence like name.0000.vtk, name.0001.vtk, etc.
Paraview recognises the link names as a sequence which can be opened and played.
The sequence of links to images can be used to create a video from the images.
- Default directory name for VTK files is postProcessing</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamSequenceVTKFiles">源码与说明</a> · <a href="/assets/command-help/foamsequencevtkfiles.txt">帮助文本</a></p>
