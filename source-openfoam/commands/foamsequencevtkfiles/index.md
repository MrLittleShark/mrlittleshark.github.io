---
title: "foamSequenceVTKFiles  为 VTK 文件建立连续编号链接"
layout: reference
description: "生成的符号链接供 ParaView 识别时间序列。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>生成的符号链接供 ParaView 识别时间序列。</p><h2>v2512 源码中的用途</h2><p>Creates symbolic links to all VTK files in a post-processing directory Links form a sequence like name.0000.vtk, name.0001.vtk, etc. Paraview recognises link names as a sequence which can be animated. The sequence of links can be used to create a video from the images. - Default directory name for VTK files is postProcessing</p><h2>使用入口</h2><pre><code class="language-bash">foamSequenceVTKFiles -dir postProcessing -out sequencedVTK</code></pre><h2>使用条件与核对</h2><p>生成的符号链接供 ParaView 识别时间序列。 用法：foamSequenceVTKFiles [选项] 示例：foamSequenceVTKFiles -dir postProcessing -out sequencedVTK
Creates symbolic links to all VTK files in a post-processing directory Links form a sequence like name.0000.vtk, name.0001.vtk, etc. Paraview recognises link names as a sequence which can be animated. The sequence of links can be used to create a video from the images. - Default directory name for VTK files is postProcessing
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-c -d -h -o -vtk -vtp -vtu</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamsequencevtkfiles.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamSequenceVTKFiles
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamSequenceVTKFiles

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamSequenceVTKFiles [OPTIONS] ...
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
- Default directory name for VTK files is postProcessing</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamSequenceVTKFiles">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
