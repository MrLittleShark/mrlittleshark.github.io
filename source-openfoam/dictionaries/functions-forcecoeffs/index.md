---
title: "forceCoeffs"
layout: reference
description: "用参考速度、密度、面积和长度将力与力矩无量纲化，输出升力、阻力等系数。"
dictionary: true
cms_slug: "dictionary-forcecoeffs"
---

<p>用参考速度、密度、面积和长度将力与力矩无量纲化，输出升力、阻力等系数。</p><p>位置：<code>system/controlDict → functions → forceCoeffs</code></p><p><code>forceCoeffs</code> 将表面力和力矩无量纲化，便于比较不同速度、尺度和密度的工况。常见阻力系数为：</p>
<p>\[
C_D=\frac{F_D}{\tfrac12\rho U_\infty^2 A_{ref}}.
\]</p>
<p>参考面积和方向是系数定义的一部分，同一物体采用不同参考面积会得到不同数值。</p>
<h3>示例：指定升阻方向与参考尺度</h3>
<p>在有壁面 <code>body</code> 的不可压缩绕流案例中，将此对象放入 <code>system/controlDict/functions</code>：</p>
<pre><code class="language-foam">bodyCoefficients
{
    type forceCoeffs;
    libs (forces);
    patches (body);
    rho rhoInf;
    rhoInf 1.2;
    origin (0 0 0);
    e1 (1 0 0);
    e3 (0 1 0);
    magUInf 10;
    lRef 1;
    Aref 0.2;
    writeControl timeStep;
    writeInterval 1;
}
</code></pre>
<p><code>e1</code> 为阻力方向，<code>e3</code> 为升力方向，两者正交；这里阻力沿 x、升力沿 y。<code>origin</code> 是力矩参考点，<code>magUInf</code> 是参考速度，<code>lRef</code> 是力矩归一化所用长度，<code>Aref</code> 是参考面积。</p>
<p>v2512 的不可压缩系数计算中，密度在力与动压归一化中抵消；源码按单位密度处理这一情形。若要得到有量纲力并正确应用实际密度，同时使用 <code>forces</code>。可压缩系数计算则需要与参考动压一致的参考密度。</p>
<p>结果位于 <code>postProcessing/bodyCoefficients/</code>。二维案例的 <code>Aref</code> 应包含实际网格厚度，或在一致的单位展长定义下处理。改变来流方向时同步更新坐标方向与参考速度，以免把升力投影到了错误轴上。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/pisoFoam/LES/motorBike/motorBike</summary><p>motorBike 的 forceCoeffs 将总载荷换算为无量纲升阻力系数。</p>
<ul>
<li><code>patches ("motorBike.*")</code> 收集摩托车相关表面，<code>rho rhoInf</code>、<code>rhoInf 1</code> 给参考密度。</li>
<li><code>magUInf 20</code>、<code>Aref 0.75</code> 分别给 20 m/s 来流和 0.75 m² 参考面积，力系数按动压乘面积归一化。</li>
<li><code>dragDir (1 0 0)</code>、<code>liftDir (0 0 1)</code> 分别沿 x 和 z，俯仰轴为 y。</li>
<li><code>lRef 1.42</code> 用于力矩系数，<code>CofR (0.72 0 0)</code> 给力矩中心。</li>
</ul>
<p>改动车速时同步修改 magUInf；更换参考面积后应明确系数定义，才能和其他结果比较。</p>
<p><a href="/assets/examples/v2512/forcecoeffs/1-forceCoeffs.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pisoFoam/LES/motorBike/motorBike/system/forceCoeffs">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pisoFoam/LES/motorBike/motorBike">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/

forces
{
    type            forceCoeffs;
    libs            (forces);
    writeControl    timeStep;
    writeInterval   1;

    patches         (&quot;motorBike.*&quot;);
    rho             rhoInf;      // Indicates incompressible
    log             true;
    rhoInf          1;           // Required when rho = rhoInf
    liftDir         (0 0 1);
    dragDir         (1 0 0);
    CofR            (0.72 0 0);  // Axle midpoint on ground
    pitchAxis       (0 1 0);
    magUInf         20;
    lRef            1.42;        // Wheelbase length
    Aref            0.75;        // Estimated
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/pimpleFoam/LES/NACA4412</summary><p>NACA4412 的升阻力方向根据攻角表达式计算，避免手工填写不一致的方向向量。</p>
<ul>
<li><code>AoA 13.87</code> 以角度输入，<code>degToRad</code> 转为三角函数使用的弧度。</li>
<li><code>liftDir</code>、<code>dragDir</code> 分别由正弦和余弦构造，与来流方向对应。</li>
<li><code>magUInf 1</code>、<code>lRef 1</code> 给归一化参考尺度，<code>Aref #eval{$lRef*0.004}</code> 使用弦长乘展向厚度，面积为 0.004 m²。</li>
<li><code>CofR (0.25 0 0)</code> 是四分之一弦长力矩中心，每步记录系数。</li>
</ul>
<p>改变攻角时同时核对实际入口速度方向；改变展向宽度时同步更新 Aref。</p>
<p><a href="/assets/examples/v2512/forcecoeffs/2-forceCoeffs.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/NACA4412/system/forceCoeffs">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/NACA4412">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/

forceCoeffs
{
    type            forceCoeffs;

    libs            (forces);

    writeControl    timeStep;
    writeInterval   1;

    log             no;

    AoA             13.87;       // Angle-of-attack (deg)
    magUInf         1.0;         // Freestream velocity
    lRef            1.0;         // Chord length
    Aref            #eval{ $lRef*0.004 };  // Chord length times span width

    patches         (aerofoil);
    rho             rhoInf;      // Indicates incompressible
    rhoInf          1;           // Required when rho = rhoInf
    liftDir    #eval{vector( -sin(degToRad($AoA)), 0, cos(degToRad($AoA)) )};
    dragDir    #eval{vector(  cos(degToRad($AoA)), 0, sin(degToRad($AoA)) )};
    CofR            (0.25 0 0);  // Aerodynamic center point
    pitchAxis       (0 1 0);
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · compressible/sonicFoam/RAS/nacaAirfoil</summary><p>高速翼型算例把指定壁面的载荷按自由来流尺度归一化。</p>
<ul>
<li><code>patches (wall_4)</code> 选择翼型表面。</li>
<li><code>magUInf 618.022</code>、<code>lRef 1</code>、<code>Aref 1</code> 给速度、长度与面积参考。</li>
<li><code>dragDir (0.970839 0.239733 0)</code> 与 <code>liftDir (-0.239733 0.970839 0)</code> 构成相应的阻力和升力方向。</li>
<li><code>CofR (0 0 0)</code>、<code>pitchAxis (0 0 1)</code> 定义力矩中心和轴，<code>writeControl writeTime</code> 跟随主结果写出。</li>
</ul>
<p>更换攻角或实际参考面积后更新归一化设置；可压缩压力与密度应按求解器字段单位解释。</p>
<p><a href="/assets/examples/v2512/forcecoeffs/3-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/sonicFoam/RAS/nacaAirfoil/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/sonicFoam/RAS/nacaAirfoil">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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

application     sonicFoam;

startFrom       latestTime;

startTime       0;

stopAt          endTime;

endTime         0.0027;

deltaT          4e-08;

writeControl    runTime;

writeInterval   2e-04;

purgeWrite      0;

writeFormat     ascii;

writePrecision  6;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable true;

functions
{
    forces
    {
        type            forceCoeffs;
        libs            (forces);
        writeControl    writeTime;

        patches
        (
            wall_4
        );

        rhoInf      1;

        CofR        (0 0 0);
        liftDir     (-0.239733 0.970839 0);
        dragDir     (0.970839 0.239733 0);
        pitchAxis   (0 0 1);
        magUInf     618.022;
        lRef        1;
        Aref        1;
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/simplefoam/">simpleFoam</a> · <a href="/commands/postprocess/">postProcess</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>函数对象未执行</td><td>核对 libs、type、enabled、executeControl 与选定时间；求解器创建的模型对象可能是必要依赖。</td></tr><tr><td>输出路径找不到</td><td>检查 postProcessing/实例名/起始时刻，部分函数对象把场写入常规时间目录。</td></tr><tr><td>统计量定义不一致</td><td>明确面积/体积/时间加权，检查 fields、operation 与 base 的含义。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
