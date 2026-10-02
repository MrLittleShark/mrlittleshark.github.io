---
title: "stitchMeshDict"
layout: reference
description: "stitchMesh 的网格边界拼接配置，连接指定 patch 对。"
dictionary: true
cms_slug: "dictionary-stitchmeshdict"
---

<p>stitchMesh 的网格边界拼接配置，连接指定 patch 对。</p><p>位置：<code>system/stitchMeshDict</code></p><h2>配置实例</h2><p>mesh/stitchMesh/simple-cube1 中的 stitchMeshDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      stitchMeshDict;
}

outerx
{
    match   partial;    // partial | integral | perfect
    master  outerx;
    slave   innerx;
}

outery
{
    match   partial;
    master  outery;
    slave   innery;
}

outerz
{
    match   partial;
    master  outerz;
    slave   innerz;
}</code></pre><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · mesh/stitchMesh/simple-cube1</summary><p>simple-cube1 使用 stitchMesh 将相对的两个边界拼接成内部连接，字典分别列出 x、y、z 三组面。</p>
<ul>
<li>outerx、outery、outerz 是三次拼接操作的名称。</li>
<li>每组 <code>master</code> 与 <code>slave</code> 指向要连接的实际边界，例如 outerx 与 innerx。</li>
<li><code>match partial</code> 允许仅对两个边界重合的部分进行匹配，适合非完全一一对应的面布局。</li>
</ul>
<p>拼接前显示两侧边界确认空间位置，拼接后检查内部连接、剩余边界面积及网格质量。</p>
<p><a href="/assets/examples/v2512/stitchmeshdict/1-stitchMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/mesh/stitchMesh/simple-cube1/system/stitchMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/mesh/stitchMesh/simple-cube1">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      stitchMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

outerx
{
    match   partial;    // partial | integral | perfect
    master  outerx;
    slave   innerx;
}

outery
{
    match   partial;
    master  outery;
    slave   innery;
}

outerz
{
    match   partial;
    master  outerz;
    slave   innerz;
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/stitchmesh/">stitchMesh</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
