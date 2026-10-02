---
title: "kivaToFoam · 输入为 KIVA3v 发动机网格"
layout: reference
description: "输入为 KIVA3v 发动机网格。"
cms_slug: "command-kivatofoam"
---

<p>输入为 KIVA3v 发动机网格。</p><h2>开始前</h2>
<p>准备 KIVA3 或 KIVA3v 网格文件；目标案例是独立副本，转换后需核对缸体、活塞及缸盖边界。</p>
<h2>示例 1：导入默认文件</h2>
<pre><code class="language-bash">kivaToFoam
</code></pre>
<p>从当前目录读取 otape17，默认采用 KIVA3v 处理方式。日志显示各类边界和单元数量。</p>
<h2>示例 2：指定输入文件</h2>
<pre><code class="language-bash">kivaToFoam -file engine.otape17
</code></pre>
<p>读取明确命名的网格，便于同时保存不同曲轴位置或不同几何版本的输入。</p>
<h2>示例 3：导入 KIVA3 格式</h2>
<pre><code class="language-bash">kivaToFoam -file engine3.otape17 -version kiva3
</code></pre>
<p>选择 KIVA3 解析路径。版本参数应与输入文件格式一致，转换后核对活塞和缸套相关边界。</p>
<h2>示例 4：显式选择 KIVA3v</h2>
<pre><code class="language-bash">kivaToFoam -file engine3v.otape17 -version kiva3v -case ../engineCase
</code></pre>
<p>把 KIVA3v 网格转换到 engineCase。适合在多个发动机案例之间明确输入版本与目标目录。</p>
<h2>示例 5：调整缸盖边界识别高度</h2>
<pre><code class="language-bash">kivaToFoam -file engine.otape17 -zHeadMin 0.1
checkMesh -constant
</code></pre>
<p>按 z 高度阈值把相应缸套面转入缸盖分组；0.1 应按输入几何坐标确定。检查转换后的缸盖范围和网格质量。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-file &lt;name&gt;</code></td><td>Specify alternative input file name - default is otape17 Override the file handler type Set named InfoSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: kivaToFoam [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -file &lt;name&gt;      Specify alternative input file name - default is otape17
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
  -version &lt;version&gt;
                    Specify kiva version [kiva3|kiva3v] - default is &#x27;3v&#x27;
  -zHeadMin &lt;scalar&gt;
                    Minimum z-height for transferring liner faces to
                    cylinder-head
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Convert a KIVA3v grid to OpenFOAM

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/kivaToFoam/kivaToFoam.C">源码与说明</a> · <a href="/assets/command-help/kivatofoam.txt">帮助文本</a></p>
