---
title: "mirrorMeshDict"
layout: reference
description: "关于指定平面镜像网格。"
dictionary: true
cms_slug: "dictionary-mirrormeshdict"
---

<p>关于指定平面镜像网格。</p><p>位置：<code>system/mirrorMeshDict</code></p><h2>配置实例</h2><p>incompressible/pimpleFoam/RAS/ellipsekkLOmega 中的 mirrorMeshDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      mirrorMeshDict;
}

planeType       pointAndNormal;

pointAndNormalDict
{
    point   (0 0 0);
    normal  (0 0 -1);
}

planeTolerance  1e-6;</code></pre><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/pimpleFoam/RAS/ellipsekkLOmega</summary><p>ellipsekkLOmega 将半域网格关于 z=0 平面镜像，生成完整几何。</p>
<ul>
<li><code>planeType pointAndNormal</code> 用一个点和一个法向量定义镜面。</li>
<li><code>point (0 0 0)</code> 使平面经过原点，<code>normal (0 0 -1)</code> 对应 z=0 平面。</li>
<li><code>planeTolerance 1e-6</code> 设置判断点是否位于镜面附近的容差，应与网格坐标尺度匹配。</li>
</ul>
<p>镜像后检查原镜面上的点是否正确连接，并更新完整域所需的边界条件。</p>
<p><a href="/assets/examples/v2512/mirrormeshdict/1-mirrorMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/RAS/ellipsekkLOmega/system/mirrorMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/RAS/ellipsekkLOmega">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      mirrorMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

planeType       pointAndNormal;

pointAndNormalDict
{
    point   (0 0 0);
    normal  (0 0 -1);
}

planeTolerance  1e-6;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/pimpleFoam/laminar/cylinder2D</summary><p>cylinder2D 以 y=0 为镜面对网格补全，减少原始网格构造所需的几何范围。</p>
<ul>
<li><code>point (0 0 0)</code> 与 <code>normal (0 -1 0)</code> 定义经过原点的 y=0 平面。</li>
<li><code>planeType pointAndNormal</code> 指定这种平面描述方式。</li>
<li><code>planeTolerance 1e-3</code> 将距平面足够近的点按镜面点处理；该数值对应网格使用的长度单位。</li>
</ul>
<p>若几何很小，应相应减小容差，避免把靠近镜面但本应独立的点合并。</p>
<p><a href="/assets/examples/v2512/mirrormeshdict/2-mirrorMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/cylinder2D/system/mirrorMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/cylinder2D">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      mirrorMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

planeType           pointAndNormal;

pointAndNormalDict
{
    point   (0 0 0);
    normal  (0 -1 0);
}

planeTolerance      1e-3;


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · etc/caseDicts/annotated</summary><p>mirrorMesh 的注释模板演示关于坐标平面的镜像操作。</p>
<ul>
<li><code>point (0 0 0)</code> 是镜面上的点。</li>
<li><code>normal (0 1 0)</code> 沿 y 方向，因此镜面为 y=0；法向反向后表示的是同一个几何平面。</li>
<li><code>planeTolerance 1e-3</code> 控制镜面附近点的识别距离。</li>
</ul>
<p>需要关于 x=a 镜像时，可将 point 改为 <code>(a 0 0)</code>、normal 改为 <code>(1 0 0)</code>，并按模型尺度设置容差。</p>
<p><a href="/assets/examples/v2512/mirrormeshdict/3-mirrorMeshDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/mirrorMeshDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/etc/caseDicts/annotated">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      mirrorMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

planeType           pointAndNormal;

pointAndNormalDict
{
    point   (0 0 0);
    normal  (0 1 0);
}

planeTolerance      1e-3;

// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/mirrormesh/">mirrorMesh</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
