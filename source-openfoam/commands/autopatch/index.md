---
title: "autoPatch · 重划边界后更新对应场边界"
layout: reference
description: "重划边界后更新对应场边界。"
cms_slug: "command-autopatch"
---

<p>重划边界后更新对应场边界。</p><h2>开始前</h2>
<p>已有体网格外边界；工具按外表面折角划分 patch。每个角度对比示例应从同一原始网格的独立副本开始。</p>
<h2>示例 1：按常见特征角分区</h2>
<pre><code class="language-bash">autoPatch 45
</code></pre>
<p>使用 45° 特征角划分外部面，默认写入新的网格实例。按 patch 着色查看入口、出口和壁面是否形成可识别区域。</p>
<h2>示例 2：识别较小折角</h2>
<pre><code class="language-bash">autoPatch 20
</code></pre>
<p>较小阈值会保留更多细微折角，通常产生更多区域。适合检查浅台阶和小倒角，同时关注曲面三角离散带来的过度分区。</p>
<h2>示例 3：只保留较明显棱边</h2>
<pre><code class="language-bash">autoPatch 80
</code></pre>
<p>较大阈值强调明显的形状转折。与 45° 方案比较 patch 数量，确认重要物理边界仍可区分。</p>
<h2>示例 4：更新案例副本并检查</h2>
<pre><code class="language-bash">autoPatch 45 -overwrite
checkMesh -constant
</code></pre>
<p>直接在副本原网格位置写入分区结果。随后更新场文件中的边界名称和条件，保持与新 boundary 文件一致。</p>
<h2>示例 5：为新分区赋予物理名称</h2>
<pre><code class="language-bash">autoPatch 45 -overwrite
createPatch -overwrite
</code></pre>
<p>先按几何分区，再根据实际结果编写 createPatchDict，把相关 patch 合并或命名为 inlet、outlet、walls。两步之间需检查自动生成的名称和空间位置。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-overwrite</code></td><td>将修改后的网格写回原位置。操作前保存需要保留的网格。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: autoPatch [OPTIONS] &lt;featureAngle&gt;
Arguments:
  &lt;featureAngle&gt;    in degrees [0-180]
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
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -overwrite        Overwrite existing mesh/results files
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Divides external faces into patches based on feature angle

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/manipulation/autoPatch/autoPatch.C">源码与说明</a> · <a href="/assets/command-help/autopatch.txt">帮助文本</a></p>
