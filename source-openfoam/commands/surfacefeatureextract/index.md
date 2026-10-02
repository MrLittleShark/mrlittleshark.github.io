---
title: "surfaceFeatureExtract · 从表面提取特征线，供 snappyHexMesh 控制棱边细化"
layout: reference
description: "从表面提取特征线，供 snappyHexMesh 控制棱边细化。"
cms_slug: "command-surfacefeatureextract"
---

<p>从表面提取特征线，供 snappyHexMesh 控制棱边细化。</p><h2>开始前</h2>
<p>已有constant/triSurface表面及system/surfaceFeatureExtractDict；字典中逐个指定表面、提取方法与夹角。</p>
<h2>示例 1：按默认配置提取</h2>
<pre><code class="language-bash">surfaceFeatureExtract
</code></pre>
<p>读取默认字典，生成对应eMesh等特征数据，供snappyHexMesh的features条目引用。</p>
<h2>示例 2：使用独立特征配置</h2>
<pre><code class="language-bash">surfaceFeatureExtract -dict system/surfaceFeatureExtractDict.fine
</code></pre>
<p>fine字典中已设置另一夹角或表面列表时，单独选择该方案提取。</p>
<h2>示例 3：检查另一几何算例</h2>
<pre><code class="language-bash">surfaceFeatureExtract -case ../gearCase
</code></pre>
<p>gearCase包含自身几何和提取字典；结果写入其constant/triSurface。</p>
<h2>示例 4：把特征边转为可视线</h2>
<pre><code class="language-bash">surfaceFeatureExtract
surfaceFeatureConvert constant/triSurface/body.eMesh bodyEdges.obj
</code></pre>
<p>字典中输入为body.stl时，提取后将eMesh转换为OBJ，与齿尖或棱边位置对照。</p>
<h2>示例 5：用于贴体网格流程</h2>
<pre><code class="language-bash">surfaceFeatureExtract
snappyHexMesh
</code></pre>
<p>snappyHexMeshDict已引用本次生成的eMesh及细化等级；先生成特征，再进行体网格细化与贴合。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><h2>相关配置</h2><p><a href="/dictionaries/system-surfacefeatureextractdict/">surfaceFeatureExtractDict</a></p><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfaceFeatureExtract [OPTIONS]
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
