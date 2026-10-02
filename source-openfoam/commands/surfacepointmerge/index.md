---
title: "surfacePointMerge · 距离阈值采用表面坐标的长度单位"
layout: reference
description: "距离阈值采用表面坐标的长度单位。"
cms_slug: "command-surfacepointmerge"
---

<p>距离阈值采用表面坐标的长度单位。</p><h2>开始前</h2>
<p>准备三角表面；距离使用当前表面坐标单位。先查看最小真实几何间隙，再选择明显小于该间隙的合并距离。</p>
<h2>示例 1：合并近重合点</h2>
<pre><code class="language-bash">surfacePointMerge body.stl 1e-8 body-merged.stl
</code></pre>
<p>将距离小于 10⁻⁸ 的点合并，处理导出造成的近重合坐标。比较输出点数，并检查开放边是否减少。</p>
<h2>示例 2：处理更大的接缝误差</h2>
<pre><code class="language-bash">surfacePointMerge body.stl 1e-5 body-merged-10um.stl
</code></pre>
<p>米制模型使用 10 μm 容差。适合已确认接缝误差在该量级的输入；合并后核对窄缝和薄壁是否仍存在。</p>
<h2>示例 3：合并前换算单位</h2>
<pre><code class="language-bash">surfacePointMerge body-mm.stl 1e-5 body-m.stl -scale 0.001
</code></pre>
<p>先把毫米坐标缩放为米，再以 10⁻⁵ m 的距离合并。输出可以直接与米制背景网格组合。</p>
<h2>示例 4：比较两档容差</h2>
<pre><code class="language-bash">surfacePointMerge body.stl 1e-7 merged-a.stl
surfacePointMerge body.stl 1e-6 merged-b.stl
surfaceCheck merged-a.stl
surfaceCheck merged-b.stl
</code></pre>
<p>从同一输入分别生成结果，比较非流形边、开放边和点数，选取能修复接缝且保留结构的较小容差。</p>
<h2>示例 5：为特征提取准备表面</h2>
<pre><code class="language-bash">surfacePointMerge body.stl 1e-8 body-joined.stl
surfaceCheck body-joined.stl
</code></pre>
<p>检查合并结果的连通性后，将 body-joined.stl 放到 constant/triSurface，并在 surfaceFeatureExtractDict 指向该文件。这样特征提取使用的是修复后的接缝。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-scale &lt;factor&gt;</code></td><td>Input geometry scaling factor</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfacePointMerge [OPTIONS] &lt;input&gt; &lt;distance&gt; &lt;output&gt;
Arguments:
  &lt;input&gt;           The input surface file
  &lt;distance&gt;        The merge distance
  &lt;output&gt;          The output surface file
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
  -scale &lt;factor&gt;   Input geometry scaling factor
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Merge points on surface if they are within absolute distance [m].

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfacePointMerge/surfacePointMerge.C">源码与说明</a> · <a href="/assets/command-help/surfacepointmerge.txt">帮助文本</a></p>
