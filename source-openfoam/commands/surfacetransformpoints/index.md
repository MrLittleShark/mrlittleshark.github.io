---
title: "surfaceTransformPoints  对表面进行平移旋转和缩放"
layout: reference
description: "-read-scale 和 -write-scale 分别指定读取和写出时的缩放系数。"
---
{% raw %}
<div class="source-note">v2512 帮助命令退出码 0。帮助输出只能证明程序入口与选项，不等同于网格、求解和物理验证。</div><p>-read-scale 和 -write-scale 分别指定读取和写出时的缩放系数。</p><h2>v2512 源码中的用途</h2><p>Transform (scale/rotate) a surface. Like transformPoints but for surfaces. The rollPitchYaw and yawPitchRoll options take three angles (degrees) that describe the intrinsic Euler rotation. rollPitchYaw - roll (rotation about X) followed by - pitch (rotation about Y) followed by - yaw (rotation about Z) yawPitchRoll - yaw (rotation about Z) followed by - pitch (rotation about Y) followed by - roll (rotation about X)</p><h2>使用入口</h2><pre><code class="language-bash">surfaceTransformPoints -translate &#x27;(0 0 1)&#x27; body.stl bodyMoved.stl</code></pre><h2>使用条件与核对</h2><p>-read-scale 和 -write-scale 分别指定读取和写出时的缩放系数。 用法：surfaceTransformPoints [选项] 输入 输出 示例：surfaceTransformPoints -translate &#x27;(0 0 1)&#x27; body.stl bodyMoved.stl
源码说明：Transform (scale/rotate) a surface. Like transformPoints but for surfaces. The rollPitchYaw and yawPitchRoll options take three angles (degrees) that describe the intrinsic Euler rotation. rollPitchYaw - roll (rotation about X) followed by - pitch (rotation about Y) followed by - yaw (rotation about Z) yawPitchRoll - yaw (rotation about Z) followed by - pitch (rotation about Y) followed by - roll (rotation about X)
核验范围：v2512 帮助命令退出码 0；未据此宣称完整算例通过。
已记录的选项：-auto-centre -case -centre -cylToCart -debug-switch -doc -doc-source -fileHandler -help -help-compat -help-full -help-man -help-notes -info-switch -lib -no-libs -noFunctionObjects -opt-switch -read-format -read-scale -recentre -rollPitchYaw -rotate -rotate-angle -rotate-x -rotate-y -rotate-z -translate -write-format -write-scale -yawPitchRoll</p><h2>完整帮助与证据文件</h2><p><a href="/assets/command-help/surfacetransformpoints.txt">下载或打开帮助文本</a></p><details><summary>展开完整帮助文本</summary><pre><code class="language-plaintext">OpenFOAM v2512 command reference
Command: surfaceTransformPoints
Evidence: help-verified
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceTransformPoints/surfaceTransformPoints.C


Usage: surfaceTransformPoints [OPTIONS] &lt;input&gt; &lt;output&gt;
Arguments:
  &lt;input&gt;           The input surface file
  &lt;output&gt;          The output surface file
Options:
  -auto-centre      Use bounding box centre as centre for rotations
  -case &lt;dir&gt;       Case directory (instead of current directory)
  -centre &lt;point&gt;   Use specified &lt;point&gt; as centre for rotations
  -cylToCart &lt;(originVec axisVec directionVec)&gt;
                    Tranform cylindrical coordinates to cartesian coordinates
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
  -read-format &lt;type&gt;
                    Input format (default: use file extension)
  -read-scale &lt;scalar | vector&gt;
                    Uniform or non-uniform input scaling
  -recentre         Recentre the bounding box before other operations
  -rollPitchYaw &lt;vector&gt;
                    Rotate by &#x27;(roll pitch yaw)&#x27; degrees
  -rotate &lt;(vectorA vectorB)&gt;
                    Rotate from &lt;vectorA&gt; to &lt;vectorB&gt; - eg, &#x27;((1 0 0) (0 0 1))&#x27;
  -rotate-angle &lt;(vector angle)&gt;
                    Rotate &lt;angle&gt; degrees about &lt;vector&gt; - eg, &#x27;((1 0 0) 45)&#x27;
  -rotate-x &lt;deg&gt;   Rotate (degrees) about x-axis
  -rotate-y &lt;deg&gt;   Rotate (degrees) about y-axis
  -rotate-z &lt;deg&gt;   Rotate (degrees) about z-axis
  -translate &lt;vector&gt;
                    Translate by specified &lt;vector&gt; before rotations
  -write-format &lt;type&gt;
                    Output format (default: use file extension)
  -write-scale &lt;scalar | vector&gt;
                    Uniform or non-uniform output scaling
  -yawPitchRoll &lt;vector&gt;
                    Rotate by &#x27;(yaw pitch roll)&#x27; degrees
  -doc              Display documentation in browser
  -doc-source       Display source code in browser
  -help             Display short help and exit
  -help-compat      Display compatibility options and exit
  -help-man         Display full help (manpage format) and exit
  -help-notes       Display help notes (description) and exit
  -help-full        Display full help and exit

Transform (translate / rotate / scale) surface points.
Like transformPoints but for surfaces.
Note: roll=rotate about x, pitch=rotate about y, yaw=rotate about z

Using: OpenFOAM-2512 (2512) - visit www.openfoam.com
Build: _bd2b6720-20260127
Arch:  LSB;label=32;scalar=64</code></pre></details><h2>来源与版本边界</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceTransformPoints/surfaceTransformPoints.C">对应源码或配套工具文档</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/surface/surfaceTransformPoints/Make/files">Make/files 编译目标</a></p><p>核心范围固定为官方 OpenFOAM-v2512 仓库的 applications/solvers 与 applications/utilities。独立模块、第三方扩展、个人编译工具与 shell 配套入口分别标注，不以一个命令总数代表所有 OpenFOAM 生态工具。</p>
{% endraw %}
