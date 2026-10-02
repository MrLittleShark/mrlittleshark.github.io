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
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-d | -dir &lt;dir&gt;</code></td><td>指定 PNG 图片所在目录，默认为当前目录。</td></tr><tr><td><code>-f | -fps &lt;fps&gt;</code></td><td>设置每秒帧数，默认为 10。</td></tr><tr><td><code>-i | -image &lt;name&gt;</code></td><td>设置输入图片序列的文件名前缀，默认为 image.。</td></tr><tr><td><code>-o | -out &lt;name&gt;</code></td><td>设置输出视频名称，默认为 video。</td></tr><tr><td><code>-tool=NAME</code></td><td>指定视频工具，例如 avconv、ffmpeg 或 mencoder。</td></tr><tr><td><code>-mask &lt;width&gt;</code></td><td>设置 avconv 输入文件编号的位数，默认为 4。</td></tr><tr><td><code>-start &lt;frame&gt;</code></td><td>设置 avconv 的起始帧编号。</td></tr><tr><td><code>-webm</code></td><td>输出 WebM 视频，仅适用于 avconv。</td></tr><tr><td><code>-h | -help</code></td><td>显示用法。</td></tr></tbody></table><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/foamCreateVideo">源码与说明</a> · <a href="/assets/command-help/foamcreatevideo.txt">帮助文本</a></p>
