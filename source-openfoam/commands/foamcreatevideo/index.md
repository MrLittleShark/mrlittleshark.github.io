---
title: "foamCreateVideo · 通过 ffmpeg 等工具处理图像序列，默认名称为 image.0000.png 等"
layout: reference
description: "通过 ffmpeg 等工具处理图像序列，默认名称为 image.0000.png 等。-image 指定图像前缀。"
cms_slug: "command-foamcreatevideo"
---

<p>通过 ffmpeg 等工具处理图像序列，默认名称为 image.0000.png 等。-image 指定图像前缀。</p><h2>开始前</h2>
<p>先从 ParaView 导出同尺寸 PNG 序列，例如 frames/image.0000.png、image.0001.png；需要 ffmpeg 或脚本支持的视频工具。</p>
<h2>示例 1：用默认帧率生成视频</h2>
<pre><code class="language-bash">foamCreateVideo -tool=ffmpeg -dir frames
</code></pre>
<p>默认前缀 image.、10 fps，生成默认 video.mp4。</p>
<h2>示例 2：提高播放帧率</h2>
<pre><code class="language-bash">foamCreateVideo -tool=ffmpeg -dir frames -fps 25 -out flow25
</code></pre>
<p>相同帧数以 25 fps 播放，输出 flow25.mp4，时长随帧率变化。</p>
<h2>示例 3：选择速度图序列</h2>
<pre><code class="language-bash">foamCreateVideo -tool=ffmpeg -dir frames -image velocity. -out velocity
</code></pre>
<p>读取 velocity.0000.png 等文件，适合在同一目录存放不同变量。</p>
<h2>示例 4：处理六位编号</h2>
<pre><code class="language-bash">foamCreateVideo -tool=ffmpeg -dir frames6 -mask 6 -out flow6
</code></pre>
<p>-mask 6 对应 image.000000.png 等编号宽度。</p>
<h2>示例 5：从指定帧号开始</h2>
<pre><code class="language-bash">foamCreateVideo -tool=avconv -dir frames -start 100 -out late-stage
</code></pre>
<p>需要 avconv。v2512 脚本仅把 -start 传给 avconv 分支；从编号 100 起读取连续 PNG，生成 late-stage.mp4。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-d | -dir &lt;dir&gt;</code></td><td>input directory with png images  (default: &#x27;.&#x27;)</td></tr><tr><td><code>-f | -fps &lt;fps&gt;</code></td><td>frames per second  (default: 10)</td></tr><tr><td><code>-i | -image &lt;name&gt;</code></td><td>input image sequence prefix  (default: &#x27;image.&#x27;)</td></tr><tr><td><code>-o | -out &lt;name&gt;</code></td><td>output video name  (default: &#x27;video&#x27;)</td></tr><tr><td><code>-tool=NAME</code></td><td>Specify avconv, ffmpeg, mencoder...</td></tr><tr><td><code>-mask &lt;width&gt;</code></td><td>avconv input mask width (default: 4)</td></tr><tr><td><code>-start &lt;frame&gt;</code></td><td>avconv start frame number</td></tr><tr><td><code>-webm</code></td><td>WebM output video file format (avconv only)</td></tr><tr><td><code>-h | -help</code></td><td>Print the usage</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: foamCreateVideo [OPTIONS] ...
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
