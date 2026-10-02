---
title: "snappyRefineMesh · 输入为待处理表面及细化字典"
layout: reference
description: "输入为待处理表面及细化字典。"
cms_slug: "command-snappyrefinemesh"
---

<p>输入为待处理表面及细化字典。</p><h2>开始前</h2>
<p>准备适用于 snappyRefineMesh 的完整 system/snappyRefineMeshDict、背景网格及三角表面。该字典使用 surface、minEdgeLen、maxEdgeLen 等条目，与 snappyHexMeshDict 分别配置。</p>
<h2>示例 1：按现有表面细化设置运行</h2>
<pre><code class="language-bash">snappyRefineMesh
</code></pre>
<p>读取表面和细化规则，在表面附近逐步细分网格。日志给出每轮选中的单元及网格规模，可查看最终表面附近的分辨率。</p>
<h2>示例 2：减小目标最小边长</h2>
<pre><code class="language-bash">foamDictionary system/snappyRefineMeshDict -entry minEdgeLen -set 0.001
snappyRefineMesh
</code></pre>
<p>在全新背景网格副本中把细化停止相关的最小边长设为 0.001。长度使用网格坐标单位；与原方案比较近表面网格密度和单元总数。</p>
<h2>示例 3：设置单元规模阈值</h2>
<pre><code class="language-bash">foamDictionary system/snappyRefineMeshDict -entry cellLimit -set 200000
snappyRefineMesh
</code></pre>
<p>将细化流程的单元数量阈值设为 20 万。程序在细化前根据当前单元数与候选数量估计新增规模，并据此决定是否继续；日志会说明因数量阈值停止的情况。</p>
<h2>示例 4：选择内部和相交区域</h2>
<pre><code class="language-bash">foamDictionary system/snappyRefineMeshDict -entry nCutLayers -set 0
foamDictionary system/snappyRefineMeshDict -entry selectInside -set true
foamDictionary system/snappyRefineMeshDict -entry selectCut -set true
foamDictionary system/snappyRefineMeshDict -entry selectOutside -set false
snappyRefineMesh
</code></pre>
<p>以闭合表面内部为目标，保留内部及相交单元。outsidePoints 应位于表面外部，随后查看 selected 集合和最终边界。</p>
<h2>示例 5：保存中间细化网格</h2>
<pre><code class="language-bash">foamDictionary system/snappyRefineMeshDict -entry writeMesh -set true
snappyRefineMesh
checkMesh -latestTime
</code></pre>
<p>把中间细化阶段的网格也写到时间目录，便于逐步观察细化区域变化。最终用 checkMesh 检查最新网格。</p>
<h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td><code>-case &lt;dir&gt;</code></td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td><code>-help</code></td><td>显示常用参数。</td></tr><tr><td><code>-help-full</code></td><td>显示完整参数。</td></tr></tbody></table><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: snappyRefineMesh [OPTIONS]
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

Refine cells near to a surface

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/advanced/snappyRefineMesh/snappyRefineMesh.C">源码与说明</a> · <a href="/assets/command-help/snappyrefinemesh.txt">帮助文本</a></p>
