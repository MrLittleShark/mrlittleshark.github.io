---
title: "postChannelDict"
layout: reference
description: "通道流统计后处理配置，用于定义壁面法向分层与剖面提取。"
dictionary: true
cms_slug: "dictionary-postchanneldict"
---

<p>通道流统计后处理配置，用于定义壁面法向分层与剖面提取。</p><p>位置：<code>constant/postChannelDict</code></p><h2>配置实例</h2><p>incompressible/pimpleFoam/LES/periodicPlaneChannel 中的 postChannelDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      postChannelDict;
}

// Seed patches to start layering from
patches         ( bottomWall );

// Direction in which the layers are
component       y;

// Is the mesh symmetric? If so average(symmetric fields) or
// subtract(asymmetric) contributions from both halves
symmetric       true;</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>patches</td><td>开始按网格层聚合数据的种子壁面，例如 bottomWall。</td></tr><tr><td>component</td><td>层推进的坐标方向，示例为 y。</td></tr><tr><td>symmetric</td><td>是否按对称通道将两半区域的对称或反对称分量合并。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/pimpleFoam/LES/periodicPlaneChannel</summary><p>periodicPlaneChannel 对周期通道的统计流场做横向分层平均，得到用于分析近壁湍流的剖面。</p>
<ul>
<li><code>patches (bottomWall)</code> 指定参考壁面。</li>
<li><code>component y</code> 以 y 坐标组织通道法向剖面。</li>
<li><code>symmetric true</code> 利用通道两壁的统计对称性，将对称位置的结果组合。</li>
</ul>
<p>当上下壁面粗糙度、温度或运动条件不同，改用不强制对称的统计方式，并分别检查两侧剖面。</p>
<p><a href="/assets/examples/v2512/postchanneldict/1-postChannelDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/periodicPlaneChannel/constant/postChannelDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/periodicPlaneChannel">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      postChannelDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Seed patches to start layering from
patches         ( bottomWall );

// Direction in which the layers are
component       y;

// Is the mesh symmetric? If so average(symmetric fields) or
// subtract(asymmetric) contributions from both halves
symmetric       true;


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/postchannel/">postChannel</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>未找到指定场或函数对象：<code>No field / No functionObject</code></td><td>确认场已写出、当前时刻正确且所需库已加载；派生量可能必须先生成。</td></tr><tr><td>结果坐标或单位错误</td><td>记录采样坐标、截面法向和物理单位，尤其注意压力定义与法向通量符号。</td></tr><tr><td>峰值随采样方式改变</td><td>比较插值方案与网格分辨率；点值、面平均和体平均不是同一个量。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
