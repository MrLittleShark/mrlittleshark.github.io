---
title: "system/sampleDict · sampleDict"
layout: reference
description: "采样点、线或面的配置。v2512 常通过 controlDict 中的 sets/surfaces 函数对象采样；独立文件是否被读取，取决于 postProcess -dict 或 #include 的调用方式。比较时应保持插值格式、坐标及采样时刻一致。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>采样点、线或面的配置。v2512 常通过 controlDict 中的 sets/surfaces 函数对象采样；独立文件是否被读取，取决于 postProcess -dict 或 #include 的调用方式。比较时应保持插值格式、坐标及采样时刻一致。</p><figure><img src="/assets/diagrams/reference-8.svg" alt="后处理配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>libs</td><td>额外加载的共享库。函数对象或自定义边界未注册时，应检查库名与编译版本。</td></tr><tr><td>writeControl</td><td>输出触发方式，其值决定 writeInterval 表示步数、物理时间或时钟时间。</td></tr><tr><td>interpolationScheme</td><td>把离散场插值到采样位置的方式；不同插值可能影响局部峰值。</td></tr><tr><td>axis</td><td>旋转轴或方向向量；需明确是否要求单位向量。</td></tr><tr><td>fields</td><td>目标场列表。场名、数据类型和计算时刻必须满足相应函数对象的要求。</td></tr><tr><td>patches</td><td>参与该操作的边界列表，必须对应网格中的实际 patch 名称。</td></tr><tr><td>T</td><td>温度值或温度场引用，通常采用热力学温度 K。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>setFormat</td><td>raw gnuplot xmgr</td></tr><tr><td>sets</td><td>uniform, face, midPoint, midPointAndFace : start and end coordinate uniform: extra number of sampling points curve, cloud: list of coordinates</td></tr><tr><td>surfaceFormat</td><td>Note: other formats such as obj, stl, etc can also be written (by proxy) but without any values!</td></tr><tr><td>surfaces</td><td>1] patches are not triangulated by default 2] planes are always triangulated 3] iso-surfaces are always triangulated</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/pimpleFoam/LES/NACA4412</h3><p>原始路径：<code>tutorials/incompressible/pimpleFoam/LES/NACA4412/system/sampleDict</code>；求解器：<code>pimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/NACA4412/system/sampleDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/sampledict/1-sampleDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/NACA4412">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    timeStart           &#36;tStartAvg;

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
    timeStart           &#36;tStartAvg;

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

// ************************************************************************* //</code></pre><h3>示例 2 · incompressible/pimpleFoam/LES/wallMountedHump/setups.orig/common</h3><p>原始路径：<code>tutorials/incompressible/pimpleFoam/LES/wallMountedHump/setups.orig/common/system/sampleDict</code>；求解器：<code>pimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/wallMountedHump/setups.orig/common/system/sampleDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/sampledict/2-sampleDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/wallMountedHump/setups.orig/common">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    timeStart           &#36;tStartAvg;

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
    timeStart           &#36;tStartAvg;

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


// ************************************************************************* //</code></pre><h3>示例 3 · combustion/reactingFoam/RAS/SandiaD_LTS</h3><p>原始路径：<code>tutorials/combustion/reactingFoam/RAS/SandiaD_LTS/system/sampleDict</code>；求解器：<code>reactingFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/reactingFoam/RAS/SandiaD_LTS/system/sampleDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/sampledict/3-sampleDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/reactingFoam/RAS/SandiaD_LTS">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// *********************************************************************** //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/postprocess/">postProcess</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/sampleDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/sampleDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>No field / No functionObject</td><td>确认场已写出、当前时刻正确且所需库已加载；派生量可能必须先生成。</td></tr><tr><td>结果坐标或单位错误</td><td>记录采样坐标、截面法向和物理单位，尤其注意压力定义与法向通量符号。</td></tr><tr><td>峰值随采样方式改变</td><td>比较插值方案与网格分辨率；点值、面平均和体平均不是同一个量。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
