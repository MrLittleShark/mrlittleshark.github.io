---
title: "foamCreateVideo · 通过 ffmpeg 等工具处理图像序列，默认名称为 image.0000.png 等"
layout: reference
description: "通过 ffmpeg 等工具处理图像序列，默认名称为 image.0000.png 等。-image 指定图像前缀。"
cms_slug: "command-foamcreatevideo"
---

<p>通过 ffmpeg 等工具处理图像序列，默认名称为 image.0000.png 等。-image 指定图像前缀。</p><h2>用法</h2><pre><code class="language-bash">foamCreateVideo -dir frames -fps 20 -out flow</code></pre><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-d | -dir &lt;dir&gt;</td><td>input directory with png images  (default: &#x27;.&#x27;)</td></tr><tr><td>-f | -fps &lt;fps&gt;</td><td>frames per second  (default: 10)</td></tr><tr><td>-i | -image &lt;name&gt;</td><td>input image sequence prefix  (default: &#x27;image.&#x27;)</td></tr><tr><td>-o | -out &lt;name&gt;</td><td>output video name  (default: &#x27;video&#x27;)</td></tr><tr><td>-tool=NAME</td><td>Specify avconv, ffmpeg, mencoder...</td></tr><tr><td>-mask &lt;width&gt;</td><td>avconv input mask width (default: 4)</td></tr><tr><td>-start &lt;frame&gt;</td><td>avconv start frame number</td></tr><tr><td>-webm</td><td>WebM output video file format (avconv only)</td></tr><tr><td>-h | -help</td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamCreateVideo [OPTIONS] ...
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
Use the -tool option to specify a particular converter.</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCreateVideo">源码与说明</a> · <a href="/assets/command-help/foamcreatevideo.txt">帮助文本</a></p>
