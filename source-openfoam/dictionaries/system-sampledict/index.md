---
title: "sampleDict"
layout: reference
description: "采样点、线或面的配置。"
dictionary: true
cms_slug: "dictionary-sampledict"
---

<p>采样点、线或面的配置。</p><p>位置：<code>system/sampleDict</code></p><h2>配置实例</h2><p>incompressible/pimpleFoam/LES/NACA4412 中的 sampleDict：</p><pre><code class="language-foam">sample.lines
{
    type                sets;
    libs                (sampling);
    writeControl        writeTime;
    timeStart           $tStartAvg;

    interpolationScheme cellPoint;
    setFormat           raw;

    sets
    (
        xbyc0.68
        {
            type            face;
            axis            z;
            start           (6.753000021E-01 0.0001 7.061254978E-02);
            end             (7.216045260E-01 0.0001 3.526125550E-01);
        }
        xbyc0.73
        {
            type            face;
            axis            z;
            start           (7.307999730E-01 0.0001 6.140028313E-02);
            end             (7.803474069E-01 0.0001 3.434002697E-01);
        }
        xbyc0.79
        {
            type            face;
            axis            z;
            start           (7.863000035E-01 0.0001 5.103440955E-02);
            end             (8.403753638E-01 0.0001 3.330343962E-01);
        }
        xbyc0.84
        {
            type            face;
            axis            z;
            start           (8.417999744E-01 0.0001 3.950987384E-02);
            end             (8.998869658E-01 0.0001 3.215098679E-01);
        }
        xbyc0.90
        {
            type            face;
            axis            z;
            start           (8.973000050E-01 0.0001 2.680198476E-02);
            end             (9.618465304E-01 0.0001 3.088019788E-01);
        }
        xbyc0.95
        {
            type            face;
            axis            z;
            start           (9.527999759E-01 0.0001 1.286614314E-02);
            end             (1.022162795E+00 0.0001 2.928661406E-01);
        }
    );

    fields
    (
        columnAverage(UMean)
        columnAverage(UPrime2Mean)
    );
}

sample.aerofoil
{
    type                surfaces;
    libs                (sampling);
    writeControl        writeTime;
    timeStart           $tStartAvg;

    interpolationScheme cell;
    surfaceFormat       raw;

    fields
    (
        pMean
        wallShearStressMean
    );

    surfaces
    (
        aerofoil
        {
            type            patch;
            patches         ( &quot;aerofoil&quot; );
        }
    );
}</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>libs</td><td>额外加载的共享库。函数对象或自定义边界未注册时，应检查库名与编译版本。</td></tr><tr><td>writeControl</td><td>输出触发方式，其值决定 writeInterval 表示步数、物理时间或时钟时间。</td></tr><tr><td>interpolationScheme</td><td>把离散场插值到采样位置的方式；不同插值可能影响局部峰值。</td></tr><tr><td>axis</td><td>旋转轴或方向向量；需明确是否要求单位向量。</td></tr><tr><td>fields</td><td>目标场列表。场名、数据类型和计算时刻必须满足相应函数对象的要求。</td></tr><tr><td>patches</td><td>参与该操作的边界列表，必须对应网格中的实际 patch 名称。</td></tr><tr><td>T</td><td>温度值或温度场引用，通常采用热力学温度 K。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/pimpleFoam/LES/NACA4412</summary><p>NACA4412 的 sampleDict 从时间平均结果中提取边界层剖面和翼面分布，便于分析尾缘附近的湍流结构。</p>
<ul>
<li>sample.lines 使用 sets，字段为 <code>columnAverage(UMean)</code> 与 <code>columnAverage(UPrime2Mean)</code>，需要先产生相应时间平均和列平均结果。</li>
<li>六条线位于名称标示的 x/c≈0.68～0.95 位置，<code>type face</code> 在采样线与网格面的交点取样。</li>
<li><code>interpolationScheme cellPoint</code> 在单元与节点数据之间插值，<code>setFormat raw</code> 生成便于绘图的文本。</li>
<li><code>timeStart $tStartAvg</code> 复用统一的平均开始时间；sample.aerofoil 还在翼面导出 pMean 与 wallShearStressMean。</li>
</ul>
<p>比较不同工况时保持采样位置与平均时长一致，再由这些剖面计算速度亏损或摩阻分布。</p>
<p><a href="/assets/examples/v2512/sampledict/1-sampleDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/NACA4412/system/sampleDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/NACA4412">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/

sample.lines
{
    type                sets;
    libs                (sampling);
    writeControl        writeTime;
    timeStart           $tStartAvg;

    interpolationScheme cellPoint;
    setFormat           raw;

    sets
    (
        xbyc0.68
        {
            type            face;
            axis            z;
            start           (6.753000021E-01 0.0001 7.061254978E-02);
            end             (7.216045260E-01 0.0001 3.526125550E-01);
        }
        xbyc0.73
        {
            type            face;
            axis            z;
            start           (7.307999730E-01 0.0001 6.140028313E-02);
            end             (7.803474069E-01 0.0001 3.434002697E-01);
        }
        xbyc0.79
        {
            type            face;
            axis            z;
            start           (7.863000035E-01 0.0001 5.103440955E-02);
            end             (8.403753638E-01 0.0001 3.330343962E-01);
        }
        xbyc0.84
        {
            type            face;
            axis            z;
            start           (8.417999744E-01 0.0001 3.950987384E-02);
            end             (8.998869658E-01 0.0001 3.215098679E-01);
        }
        xbyc0.90
        {
            type            face;
            axis            z;
            start           (8.973000050E-01 0.0001 2.680198476E-02);
            end             (9.618465304E-01 0.0001 3.088019788E-01);
        }
        xbyc0.95
        {
            type            face;
            axis            z;
            start           (9.527999759E-01 0.0001 1.286614314E-02);
            end             (1.022162795E+00 0.0001 2.928661406E-01);
        }
    );

    fields
    (
        columnAverage(UMean)
        columnAverage(UPrime2Mean)
    );
}

sample.aerofoil
{
    type                surfaces;
    libs                (sampling);
    writeControl        writeTime;
    timeStart           $tStartAvg;

    interpolationScheme cell;
    surfaceFormat       raw;

    fields
    (
        pMean
        wallShearStressMean
    );

    surfaces
    (
        aerofoil
        {
            type            patch;
            patches         ( &quot;aerofoil&quot; );
        }
    );
}

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/pimpleFoam/LES/wallMountedHump/setups.orig/common</summary><p>wallMountedHump 在隆起及其下游抽取平均速度和脉动统计剖面，用于分析分离与再附着。</p>
<ul>
<li>八条采样线的 x/c 从 0.65 到 1.3，各线沿 y 方向延伸，z 坐标固定为 0.0001。</li>
<li><code>type face</code> 使采样点落在穿过的网格面上，<code>axis y</code> 用法向坐标整理输出。</li>
<li>字段 <code>columnAverage(UMean)</code>、<code>columnAverage(UPrime2Mean)</code> 来自预先得到的统计平均，raw 格式适合外部绘图。</li>
<li>bottomWall 表面还输出 pMean 与 wallShearStressMean，可从壁面剪应力变号位置分析分离和再附着。</li>
</ul>
<p>若要比较瞬时结构，可另设 U 采样；进行统计对照时保持平均区间和剖面位置一致。</p>
<p><a href="/assets/examples/v2512/sampledict/2-sampleDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/wallMountedHump/setups.orig/common/system/sampleDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/wallMountedHump/setups.orig/common">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/

sample.lines
{
    type                sets;
    libs                (sampling);
    writeControl        writeTime;
    timeStart           $tStartAvg;

    interpolationScheme cellPoint;
    setFormat           raw;

    sets
    (
        xbyc0.65
        {
            type            face;
            axis            y;
            start           (0.65 0 0.0001);
            end             (0.65 1 0.0001);
        }
        xbyc0.66
        {
            type            face;
            axis            y;
            start           (0.66 0 0.0001);
            end             (0.66 1 0.0001);
        }
        xbyc0.80
        {
            type            face;
            axis            y;
            start           (0.80 0 0.0001);
            end             (0.80 1 0.0001);
        }
        xbyc0.90
        {
            type            face;
            axis            y;
            start           (0.90 0 0.0001);
            end             (0.90 1 0.0001);
        }
        xbyc1.00
        {
            type            face;
            axis            y;
            start           (1.00 0 0.0001);
            end             (1.00 1 0.0001);
        }
        xbyc1.10
        {
            type            face;
            axis            y;
            start           (1.10 0 0.0001);
            end             (1.10 1 0.0001);
        }
        xbyc1.20
        {
            type            face;
            axis            y;
            start           (1.20 0 0.0001);
            end             (1.20 1 0.0001);
        }
        xbyc1.30
        {
            type            face;
            axis            y;
            start           (1.30 0 0.0001);
            end             (1.30 1 0.0001);
        }
    );

    fields
    (
        columnAverage(UMean)
        columnAverage(UPrime2Mean)
    );
}

sample.bottomWall
{
    type                surfaces;
    libs                (sampling);
    writeControl        writeTime;
    timeStart           $tStartAvg;

    interpolationScheme cell;
    surfaceFormat       raw;

    fields
    (
        pMean
        wallShearStressMean
    );

    surfaces
    (
        bottomWall
        {
            type            patch;
            patches         ( &quot;bottomWall&quot; );
        }
    );
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · combustion/reactingFoam/RAS/SandiaD_LTS</summary><p>Sandia D 火焰在轴向中心线和多个径向截面输出温度、燃料、氧化剂及主要产物的分布。</p>
<ul>
<li><code>fields</code> 包含 T、CO、CO2、H2、H2O、N2、O2、OH、CH4，组分字段名与反应机理中的物种一致。</li>
<li>Centerline 从 z=0 延伸到 0.5 m，以 <code>nPoints 500</code> 均匀采样；x=0.00001 m 的小偏移使采样线靠近轴线。</li>
<li>各 Radial_* 在指定 z 截面沿半径取 100 点，<code>cellPoint</code> 提供插值，<code>setFormat raw</code> 输出文本数据。</li>
<li>原示例的 Radial_15 中 <code>end (0.024 0.108)</code> 缺少 y 分量。使用时改为 <code>end (0.024 0 0.108);</code>，与同一截面的 start 坐标对应。</li>
</ul>
<p>截面名称用于识别测量位置，实际位置由 start/end 决定；对照实验时按坐标和喷口直径核对无量纲距离。</p>
<p><a href="/assets/examples/v2512/sampledict/3-sampleDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/reactingFoam/RAS/SandiaD_LTS/system/sampleDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/reactingFoam/RAS/SandiaD_LTS">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version         2.0;
    format          ascii;
    class           dictionary;
    location        system;
    object          sampleDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Set output format : choice of
//      raw
//      gnuplot
//      xmgr
setFormat raw;

// Surface output format. Choice of
//      none        : suppress output
//      foam        : separate points, faces and values file
//      vtk         : VTK ascii format
//      raw         : x y z value format for use with e.g. gnuplot &#x27;splot&#x27;.
//
// Note:
// other formats such as obj, stl, etc can also be written (by proxy)
// but without any values!
surfaceFormat vtk;

// interpolationScheme. choice of
//      cell          : use cell-centre value only; constant over cells (default)
//      cellPoint     : use cell-centre and vertex values
//      cellPointFace : use cell-centre, vertex and face values.
// 1] vertex values determined from neighbouring cell-centre values
// 2] face values determined using the current face interpolation scheme
//    for the field (linear, gamma, etc.)
interpolationScheme cellPoint;

// Fields to sample.
fields
(
    T
    CO
    CO2
    H2
    H2O
    N2
    O2
    OH
    CH4
);


// Set sampling definition: choice of
//      uniform             evenly distributed points on line
//      face                one point per face intersection
//      midPoint            one point per cell, inbetween two face intersections
//      midPointAndFace     combination of face and midPoint
//
//      curve               specified points, not necessary on line, uses
//                          tracking
//      cloud               specified points, uses findCell
//
// axis: how to write point coordinate. Choice of
// - x/y/z: x/y/z coordinate only
// - xyz: three columns
//  (probably does not make sense for anything but raw)
// - distance: distance from start of sampling line (if uses line) or
//             distance from first specified sampling point
//
// type specific:
//      uniform, face, midPoint, midPointAndFace : start and end coordinate
//      uniform: extra number of sampling points
//      curve, cloud: list of coordinates
sets
{
    Centerline
    {
        type        uniform;
        axis        distance;

        start       (0.00001 0. 0. );
        end         (0.00001 0. 0.500);
        nPoints     500;
    }

    Radial_075
    {
        type        uniform;
        axis        distance;

        start       (0 0 0.054);
        end         (0.020 0 0.054);
        nPoints     100;
    }
    Radial_15
    {
        type        uniform;
        axis        distance;

        start       (0 0 0.108);
        end         (0.024 0.108);
        nPoints     100;
    }
    Radial_30
    {
        type        uniform;
        axis        distance;

        start       (0 0 0.216);
        end         (0.042 0 0.216);
        nPoints     100;
    }
    Radial_45
    {
        type        uniform;
        axis        distance;

        start       (0 0 0.324);
        end         (0.056 0 0.324);
        nPoints     100;
    }
    Radial_60
    {
        type        uniform;
        axis        distance;

        start       (0 0 0.432);
        end         (0.070 0 0.432);
        nPoints     100;
    }
    Radial_75
    {
        type        uniform;
        axis        distance;

        start       (0 0 0.54);
        end         (0.080 0 0.54);
        nPoints     100;
    }
}


// Surface sampling definition: choice of
//      plane : values on plane defined by point, normal.
//      patch : values on patch.
//
// 1] patches are not triangulated by default
// 2] planes are always triangulated
// 3] iso-surfaces are always triangulated
surfaces {}


// *********************************************************************** //</code></pre></details><h2>相关命令</h2><p><a href="/commands/postprocess/">postProcess</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>No field / No functionObject</td><td>确认场已写出、当前时刻正确且所需库已加载；派生量可能必须先生成。</td></tr><tr><td>结果坐标或单位错误</td><td>记录采样坐标、截面法向和物理单位，尤其注意压力定义与法向通量符号。</td></tr><tr><td>峰值随采样方式改变</td><td>比较插值方案与网格分辨率；点值、面平均和体平均不是同一个量。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
