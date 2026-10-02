---
title: "surfacePatch · 读取 surfacePatchDict"
layout: reference
description: "读取 surfacePatchDict。"
cms_slug: "command-surfacepatch"
---

<p>读取 surfacePatchDict。</p><h2>开始前</h2>
<p>案例有 system/surfacePatchDict，geometry 中声明实际表面。以下字典修改针对 surfaces/body.stl；工具把变更表面另存为 body_patched.stl。</p>
<h2>示例 1：按特征角拆分表面区域</h2>
<pre><code class="language-bash">foamDictionary system/surfacePatchDict -entry 'surfaces/body.stl' -set '{ type autoPatch; featureAngle 45; }'
surfacePatch
</code></pre>
<p>为 body.stl 的整体表面指定 autoPatch，按 45° 特征角形成区域。-entry 使用斜杠分隔字典层级，保留文件名 body.stl 中的点号。检查输出表面的区域数量与位置。</p>
<h2>示例 2：保留更多棱边分区</h2>
<pre><code class="language-bash">foamDictionary system/surfacePatchDict -entry 'surfaces/body.stl/featureAngle' -set 20
surfacePatch
</code></pre>
<p>把分区角度改为 20°，较小的折角也可形成区域边界。比较输出区域数，判断是否过度分割了曲面离散带来的小折角。</p>
<h2>示例 3：合并较平滑的区域</h2>
<pre><code class="language-bash">foamDictionary system/surfacePatchDict -entry 'surfaces/body.stl/featureAngle' -set 80
surfacePatch
</code></pre>
<p>较大阈值保留更明显的几何棱边，通常形成更少的区域。检查入口、出口等需要独立边界的部分是否仍能识别。</p>
<h2>示例 4：只处理一个已有区域</h2>
<pre><code class="language-bash">surfacePatch -dict system/surfacePatch-top.dict
</code></pre>
<p>前提是在该字典 surfaces/body.stl/regions 内给 maxZ 设置 { type autoPatch; featureAngle 45; }。只重新划分目标区域，便于保留其他已命名表面。</p>
<h2>示例 5：按搜索几何切分区域</h2>
<pre><code class="language-bash">surfacePatch -dict system/surfacePatch-cut.dict
</code></pre>
<p>该字典在 geometry 声明 box，在目标 surfaces 条目设置 type cut; cutters (box);。输出表面按与 box 的几何关系形成分区，便于划定局部边界区域。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-dict &lt;file&gt;</code></td><td>改用指定字典文件。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: surfacePatch [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dict &lt;file&gt;      Alternative surfacePatchDict
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

Add patches (regions) to a surface with a user-selectable method

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfacePatch/searchableSurfaceModifier/searchableSurfaceModifier.C">源码与说明</a> · <a href="/assets/command-help/surfacepatch.txt">帮助文本</a></p>
