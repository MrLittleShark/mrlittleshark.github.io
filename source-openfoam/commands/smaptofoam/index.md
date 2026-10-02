---
title: "smapToFoam · 把 STAR-CD SMAP 字段映射到已有 OpenFOAM 场"
layout: reference
description: "把 STAR-CD SMAP 字段映射到已有 OpenFOAM 场。"
cms_slug: "command-smaptofoam"
---

<p>把 STAR-CD SMAP 字段映射到已有 OpenFOAM 场。</p><h2>开始前</h2>
<p>已有与SMAP数据对应的网格、当前时间目录中的目标场文件；支持SU→U、P→p、T→T等固定名称映射。</p>
<h2>示例 1：导入已有SMAP结果</h2>
<pre><code class="language-bash">smapToFoam results.smap
</code></pre>
<p>位置参数是SMAP文件；程序根据当前目录已有字段读取对应数据并重写字段内部值。</p>
<h2>示例 2：导入到指定案例</h2>
<pre><code class="language-bash">smapToFoam -case ./convertedCase results.smap
</code></pre>
<p>convertedCase已建立相同几何对应网格和目标场；-case决定结果写入的案例。</p>
<h2>示例 3：把SMAP结果作为重启初值</h2>
<pre><code class="language-bash">foamDictionary system/controlDict -entry startFrom -set startTime
foamDictionary system/controlDict -entry startTime -set 0
smapToFoam steady.smap
</code></pre>
<p>把当前实例明确设为0，导入数据到已准备的0/U、0/p等文件，供后续求解器从此状态启动。</p>
<h2>示例 4：仅导入已有目标标量</h2>
<pre><code class="language-bash">smapToFoam -case ./temperatureImport thermal.smap
</code></pre>
<p>temperatureImport当前时间只准备需要的T等目标字段时，工具按已有文件建立名称映射；检查SMAP内相应列与目标单位。</p>
<h2>示例 5：导入后可视化核对</h2>
<pre><code class="language-bash">smapToFoam results.smap
foamToVTK -time 0 -fields '(U p T)' -name VTK-smap
</code></pre>
<p>本案例当前实例为0并已有U、p、T；导出导入后的字段，检查空间分布、速度方向和数量级。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: smapToFoam [OPTIONS] &lt;SMAP fileName&gt;
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
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Translate a STARCD SMAP data file into OpenFOAM field format

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/postProcessing/dataConversion/smapToFoam/smapToFoam.C">源码与说明</a> · <a href="/assets/command-help/smaptofoam.txt">帮助文本</a></p>
