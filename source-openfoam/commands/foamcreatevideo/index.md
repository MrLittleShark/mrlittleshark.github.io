---
title: "foamCreateVideo  将 PNG 图像序列合成为视频"
layout: reference
description: "通过 ffmpeg 等工具处理图像序列，默认名称为 image.0000.png 等。-image 指定图像前缀。"
---
{% raw %}
<div class="source-note">v2512 脚本源码已收录；未执行脚本。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>通过 ffmpeg 等工具处理图像序列，默认名称为 image.0000.png 等。-image 指定图像前缀。</p><h2>v2512 源码中的用途</h2><p>Creates a video file from PNG images - requires one of avconv, ffmpeg, mencoder</p><h2>使用入口</h2><pre><code class="language-bash">foamCreateVideo -dir frames -fps 20 -out flow</code></pre><h2>使用条件与核对</h2><p>通过 ffmpeg 等工具处理图像序列，默认名称为 image.0000.png 等。-image 指定图像前缀。 用法：foamCreateVideo [选项] 示例：foamCreateVideo -dir frames -fps 20 -out flow
Creates a video file from PNG images - requires one of avconv, ffmpeg, mencoder
本条基于固定版本脚本源码，运行前检查帮助与依赖。
源码帮助选项：-d -f -h -i -mask -o -start -tool -webm</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/foamcreatevideo.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 script source evidence
Command: foamCreateVideo
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCreateVideo

以下为源码中的帮助文本（保留 shell 占位符），并非本机运行输出。

Usage: foamCreateVideo [OPTIONS] ...
options:
  -d | -dir &lt;dir&gt;       input directory with png images  (default: &#x27;.&#x27;)
  -f | -fps &lt;fps&gt;       frames per second  (default: 10)
  -i | -image &lt;name&gt;    input image sequence prefix  (default: &#x27;image.&#x27;)
  -o | -out &lt;name&gt;      output video name  (default: &#x27;video&#x27;)
  -tool=NAME            Specify avconv, ffmpeg, mencoder...
  -mask &lt;width&gt;         avconv input mask width (default: 4)
  -start &lt;frame&gt;        avconv start frame number
  -webm                 WebM output video file format (avconv only)
  -h | -help            Print the usage

Creates a video file from a sequence of PNG images.
With the default prefix (&#x27;image.&#x27;), from image.0000.png, image.0001.png, ...
- The output format is MPEG4
- The output name (with mp4 format), is &quot;video.mp4&quot;
- By default the video codec is high resolution

MPEG4 output requires avconv, mencoder, ffmpeg, ...
WebM  output requires avconv.

By default will attempt avconv, ffmpeg, mencoder.
Use the -tool option to specify a particular converter.</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCreateVideo">对应源码或配套工具文档</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
