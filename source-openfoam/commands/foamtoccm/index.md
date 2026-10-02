---
title: "foamToCcm · 需编译 CCM 库支持"
layout: reference
description: "需编译 CCM 库支持。"
cms_slug: "command-foamtoccm"
---

<p>需编译 CCM 库支持。</p><h2>开始前</h2>
<p>安装带 CCM 支持的导出工具；案例已有网格，结果导出示例还需存在相应时间的场文件。</p>
<h2>示例 1：导出网格与结果</h2>
<pre><code class="language-bash">foamToCcm -latestTime
</code></pre>
<p>选择最新时间导出 CCM 数据。几何文件使用 .ccmg，结果文件使用 .ccmp 加时间后缀，供支持 CCM 的软件读取。</p>
<h2>示例 2：仅导出网格</h2>
<pre><code class="language-bash">foamToCcm -mesh -constant -name channelMesh
</code></pre>
<p>以 channelMesh 为输出基名，只写几何。适合把网格交给另一求解软件继续配置，而不传递当前场结果。</p>
<h2>示例 3：仅导出指定结果</h2>
<pre><code class="language-bash">foamToCcm -results -time 0.5 -name channelResult
</code></pre>
<p>选取 0.5 时间目录，只写结果数据。接收端还需要与该结果对应的网格，特别是动网格情况下的几何位置。</p>
<h2>示例 4：导出一段瞬态结果</h2>
<pre><code class="language-bash">foamToCcm -time '0.1:0.5' -name transient
</code></pre>
<p>转换选定范围内已有的时间目录。每个时间对应结果文件，网格发生变化时还会输出相应几何，便于后续动画处理。</p>
<h2>示例 5：应用区域名称映射</h2>
<pre><code class="language-bash">foamToCcm -latestTime -remap constant/remapping -name mappedCase
</code></pre>
<p>按准备好的 remapping 文件进行区域映射后导出。适合需要保持与外部软件区域命名约定一致的交换流程。</p>
<details><summary>完整命令帮助</summary><pre><code class="language-text">OpenFOAM v2512 command reference
Command: foamToCcm
Evidence: not-installed
Source: https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/ccm/foamToCcm/foamToCcm.C

未取得运行时帮助。

源码路径：applications/utilities/mesh/conversion/ccm/foamToCcm/foamToCcm.C

Translates OPENFOAM mesh and/or results to CCM format</code></pre></details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/utilities/mesh/conversion/ccm/foamToCcm/foamToCcm.C">源码与说明</a> · <a href="/assets/command-help/foamtoccm.txt">帮助文本</a></p>
