---
title: "surfaceFeatureExtract · 从表面提取特征线，供 snappyHexMesh 控制棱边细化"
layout: reference
description: "从表面提取特征线，供 snappyHexMesh 控制棱边细化。"
cms_slug: "command-surfacefeatureextract"
---

<p>从表面提取特征线，供 snappyHexMesh 控制棱边细化。</p><h2>提取特征线</h2>
<pre><code class="language-bash">surfaceFeatureExtract
</code></pre>
<p>读取 <code>system/surfaceFeatureExtractDict</code>。表面通常位于 <code>constant/triSurface</code>，生成的 eMesh 由 <code>snappyHexMeshDict/features</code> 引用。</p>
<h2>使用另一份提取配置</h2>
<pre><code class="language-bash">surfaceFeatureExtract -dict system/features-fineDict
</code></pre>
<p>配置文件应包含待处理表面名称和提取角度。比较不同 <code>includedAngle</code> 下的特征线数量和位置，再选择能保留关键棱边的设置。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-dict &lt;file&gt;</td><td>改用指定字典文件。</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-surfacefeatureextractdict/">surfaceFeatureExtractDict</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceFeatureExtract [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dict &lt;file&gt;      Read surfaceFeatureExtractDict from specified location
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
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

Extract and write surface feature lines to file.
Feature line extraction only valid on closed manifold surfaces.

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceFeatureExtract/surfaceFeatureExtract.C">源码与说明</a> · <a href="/assets/command-help/surfacefeatureextract.txt">帮助文本</a></p>
