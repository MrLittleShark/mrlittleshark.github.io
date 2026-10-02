---
title: "surfaces"
layout: reference
description: "在平面、边界或等值面上采样场数据，输出可视化或分析用的表面数据。"
dictionary: true
cms_slug: "dictionary-surfaces"
---

<p>在平面、边界或等值面上采样场数据，输出可视化或分析用的表面数据。</p><p>位置：<code>system/controlDict → functions → surfaces</code></p><p><code>surfaces</code> 把体积场采样到平面、等值面或其他表面，并导出 VTK 等格式。它适合保存速度截面、温度截面以及多相界面附近的场。</p>
<h3>示例：导出方腔中间截面</h3>
<p>将下列对象放入 <code>system/controlDict/functions</code>：</p>
<pre><code class="language-foam">midPlane
{
    type surfaces;
    libs (sampling);
    writeControl writeTime;
    surfaceFormat vtk;
    interpolationScheme cellPoint;
    fields (U p);
    surfaces
    {
        zMid
        {
            type plane;
            point (0 0 0.005);
            normal (0 0 1);
            interpolate true;
        }
    }
}
</code></pre>
<p><code>point</code> 给出平面经过的一点，<code>normal</code> 给出法向；这里是 z=0.005 m 的截面。<code>interpolate true</code> 将数据插值到采样表面的点，采用外层指定的 <code>cellPoint</code>；输出格式为 VTK，可直接在 ParaView 中打开。</p>
<p>结果位于 <code>postProcessing/midPlane/</code> 下的时间目录。使用同一色标比较不同时间或工况，有助于分辨实际场变化。更改法向可生成流向或横向截面，改变平面位置可比较入口发展和下游分布。</p>
<p>对于相分数或压力等值面，可选择相应的等值面采样类型。做表面积分时，需要关注表面的完整性、法向和三角面重复情况；计算出口流量通常优先使用原网格 patch 上的 <code>surfaceFieldValue</code>，可以直接利用求解器的面通量。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/pimpleFoam/RAS/propeller</summary><p>螺旋桨流动的 surfaces 同时输出剖面、涡结构等值面与桨叶表面。</p>
<ul>
<li><code>fields (p U Q)</code> 选择要带到采样表面的字段，Q 需已由相应计算生成。</li>
<li><code>zNormal/cuttingPlane</code> 经过原点、法向 <code>(0 0 1)</code>，得到 z=0 截面。</li>
<li><code>isoQ</code> 取 <code>Q=1000</code> 等值面，具体阈值应结合速度和长度尺度解释。</li>
<li><code>propeller/patches ("propeller.*")</code> 收集桨叶边界，使用 Ensight；其他表面默认 VTK。</li>
</ul>
<p>转速或尺度变化后重新评估 Q 阈值，并用相同剖面位置比较压力和速度。</p>
<p><a href="/assets/examples/v2512/surfaces/1-surfaces.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/RAS/propeller/system/surfaces">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/RAS/propeller">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/

surfaces
{
    type            surfaces;
    libs            (sampling);
    writeControl    writeTime;

    surfaceFormat   vtk;
    fields          (p U Q);

    // interpolationScheme cellPoint;  //&lt;- default

    surfaces
    {
        zNormal
        {
            type        cuttingPlane;
            point       (0 0 0);
            normal      (0 0 1);
            interpolate true;
        }

        isoQ
        {
            type            isoSurface;
            isoField        Q;
            isoValue        1000;
            interpolate     true;
        }

        propeller
        {
            type            patch;
            patches         (&quot;propeller.*&quot;);
            interpolate     true;
            invariant       true;  // Unaffected by mesh motion
            surfaceFormat   ensight;
        }
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · multiphase/compressibleInterIsoFoam/laminar/depthCharge2D</summary><p>depthCharge2D 使用几何 VOF 算法，并在每次主场写出时导出重构界面。</p>
<ul>
<li><code>surfaces</code> 加载 <code>geometricVoF sampling</code>，<code>freeSurf/type interface</code> 表示直接使用界面几何。</li>
<li><code>surfaceFormat vtp</code> 输出表面文件，<code>fields (p U)</code> 附带压力与速度。</li>
<li><code>interpolate false</code> 保留该界面采样方式，主结果按 <code>writeInterval 0.01</code> s 输出。</li>
<li>主步长自动调整，<code>maxCo 0.5</code> 与 <code>maxAlphaCo 0.5</code> 同时限制流动和界面输运。</li>
</ul>
<p>观察快速膨胀或压力波时，分别检查求解时间分辨率与表面输出频率。</p>
<p><a href="/assets/examples/v2512/surfaces/2-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/compressibleInterIsoFoam/laminar/depthCharge2D/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/compressibleInterIsoFoam/laminar/depthCharge2D">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      controlDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

application     compressibleInterIsoFoam;

startFrom       startTime;

startTime       0;

stopAt          endTime;

endTime         0.5;

deltaT          0.0001;

writeControl    adjustable;

writeInterval   0.01;

purgeWrite      0;

writeFormat     binary;

writePrecision  8;

writeCompression off;

timeFormat      general;

timePrecision   10;

runTimeModifiable yes;

adjustTimeStep  yes;

maxCo           0.5;
maxAlphaCo      0.5;
maxDeltaT       1;

functions
{
    surfaces
    {
        type            surfaces;
        libs            (geometricVoF sampling);
        writeControl    writeTime;

        surfaceFormat   vtp;
        fields          (p U);

        interpolationScheme cell;

        surfaces
        {
            freeSurf
            {
                type            interface;
                interpolate     false;
            }
        }
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · multiphase/interIsoFoam/damBreak</summary><p>这个溃坝版本使用 <code>interIsoFoam</code> 的几何界面输运，并在写出时把水气界面提取成可视化表面。与 <code>interFoam</code> 示例比较时，应同时看求解器和实际时间步设置。</p>
<ul>
<li><code>startFrom latestTime</code> 从已有最大数值时间目录继续；文件中的 <code>startTime 0</code> 不能单独决定起点。<code>endTime 1</code> 是本次要求达到的结束时刻。</li>
<li><code>deltaT 0.001</code> 是初始步长，<code>adjustTimeStep yes</code> 允许自动调整。这里 <code>maxCo 10</code>、<code>maxAlphaCo 0.5</code>，界面 Courant 限制比全流场设置更紧。</li>
<li><code>writeControl adjustable</code>、<code>writeInterval 0.02</code> 按 0.02 s 的物理间隔保存；<code>writePrecision 6</code> 控制文本输出的有效位数。</li>
<li><code>surfaces/type surfaces</code> 加载 <code>geometricVoF</code> 与 <code>sampling</code>，<code>freeSurf/type interface</code> 提取几何重构界面。</li>
<li><code>fields (p U)</code> 让界面携带压力和速度，<code>surfaceFormat vtp</code> 便于在 ParaView 中读取，<code>writeControl writeTime</code> 使表面输出随主结果写出。</li>
</ul>
<p>需要更密的界面动画时减小主写出间隔。改变 Courant 限制后，比较界面位置和体积守恒；<code>maxCo 10</code> 是本例的一项设置，合适步长还取决于实际网格、流速和界面算法。</p>
<p><a href="/assets/examples/v2512/surfaces/3-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/damBreak/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/damBreak">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    location    &quot;system&quot;;
    object      controlDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

application     interIsoFoam;

startFrom       latestTime;

startTime       0;

stopAt          endTime;

endTime         1;

deltaT          0.001;

writeControl    adjustable;

writeInterval   0.02;

purgeWrite      0;

writeFormat     ascii;

writePrecision  6;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable yes;

adjustTimeStep  yes;

maxCo           10;

maxAlphaCo      0.5;

maxDeltaT       1;


functions
{
    surfaces
    {
        type            surfaces;
        libs            (geometricVoF sampling);
        writeControl    writeTime;

        surfaceFormat   vtp;
        fields          (p U);

        interpolationScheme cell;

        surfaces
        {
            freeSurf
            {
                type            interface;
                interpolate     false;
            }
        }
    }
}

// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/postprocess/">postProcess</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>函数对象未执行</td><td>核对 libs、type、enabled、executeControl 与选定时间；求解器创建的模型对象可能是必要依赖。</td></tr><tr><td>输出路径找不到</td><td>检查 postProcessing/实例名/起始时刻，部分函数对象把场写入常规时间目录。</td></tr><tr><td>统计量定义不一致</td><td>明确面积/体积/时间加权，检查 fields、operation 与 base 的含义。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
