---
title: "PDRblockMesh · 读取 PDRblockMeshDict"
layout: reference
description: "读取 PDRblockMeshDict。"
cms_slug: "command-pdrblockmesh"
---

<p>读取 PDRblockMeshDict。</p><h2>用法</h2><pre><code class="language-bash">PDRblockMesh</code></pre><h2>指定算例目录</h2><pre><code class="language-bash">PDRblockMesh -case ../myCase</code></pre><p>把 ../myCase 换成已有算例目录，其余输入参数保持相应含义。</p><h2>常用参数</h2><table><thead><tr><th>参数</th><th>作用</th></tr></thead><tbody><tr><td>-case &lt;dir&gt;</td><td>指定算例目录；省略时使用当前目录。</td></tr><tr><td>-dict &lt;file&gt;</td><td>改用指定字典文件。</td></tr><tr><td>-no-clean</td><td>保留已有 polyMesh 文件；默认行为见完整帮助。</td></tr><tr><td>-no-outer</td><td>Create without any other region Set named OptimisationSwitch (default value: 1). [Can be used multiple times]</td></tr><tr><td>-print-dict</td><td>Print blockMeshDict equivalent and exit</td></tr><tr><td>-time &lt;time&gt;</td><td>选择时刻或时间范围，如 0.1:0.5。</td></tr><tr><td>-write-dict</td><td>Write system/blockMeshDict.PDRblockMesh and exit</td></tr><tr><td>-help</td><td>显示常用参数。</td></tr><tr><td>-help-full</td><td>显示完整参数。</td></tr></tbody></table><h2>配套算例</h2><ul><li><a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/PDRblockMesh/box0">mesh/PDRblockMesh/box0</a></li></ul><details><summary>完整命令帮助</summary><pre><code class="language-text">Usage: PDRblockMesh [OPTIONS]
Options:
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -debug-switch &lt;name=val&gt;
                    Set named DebugSwitch (default value: 1).
                    [Can be used multiple times]
  -dict &lt;file&gt;      Alternative PDRblockMeshDict
  -fileHandler &lt;handler&gt;
                    Override the file handler type
  -info-switch &lt;name=val&gt;
                    Set named InfoSwitch (default value: 1).
                    [Can be used multiple times]
  -lib &lt;name&gt;       Additional library or library list to load.
                    [Can be used multiple times]
  -no-clean         Do not remove polyMesh/ directory or files
  -no-libs          Disable use of the controlDict &#x27;libs&#x27; entry
  -no-outer         Create without any other region
  -opt-switch &lt;name=val&gt;
                    Set named OptimisationSwitch (default value: 1).
                    [Can be used multiple times]
  -print-dict       Print blockMeshDict equivalent and exit
  -time &lt;time&gt;      Specify a time to write mesh to (default: constant)
  -write-dict       Write system/blockMeshDict.PDRblockMesh and exit
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

A block mesh generator for a rectilinear mesh in x-y-z.
  The ordering of vertex and face labels within a block as shown below.
  For the local vertex numbering in the sequence 0 to 7:
    Faces 0, 1  ==  x-min, x-max.
    Faces 2, 3  ==  y-min, y-max.
    Faces 4, 5  ==  z-min, z-max.

                        7 ---- 6
                 f5     |\     |\     f3
                 |      | 4 ---- 5     \
                 |      3 |--- 2 |      \
                 |       \|     \|      f2
                 f4       0 ---- 1
    Y  Z
     \ |                f0 ------ f1
      \|
       O--- X

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/generation/PDRblockMesh/PDRblockMesh.C">源码与说明</a> · <a href="/assets/command-help/pdrblockmesh.txt">帮助文本</a></p>
