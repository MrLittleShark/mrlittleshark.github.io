---
title: "Q"
layout: reference
description: "由速度梯度计算 Q 判据场，用于显示旋转占优的流动区域。"
dictionary: true
cms_slug: "dictionary-q"
---

<p>由速度梯度计算 Q 判据场，用于显示旋转占优的流动区域。</p><p>位置：<code>system/controlDict → functions → Q</code></p><p><code>Q</code> 计算速度梯度张量的第二不变量，常通过正值等值面显示旋转占优的流动结构。场的单位是 s⁻²，等值面阈值需要结合速度和长度尺度选择。</p>
<h3>示例：计算 Q 场</h3>
<p>在 <code>system/controlDict/functions</code> 中加入：</p>
<pre><code class="language-foam">vortexQ
{
    type Q;
    libs (fieldFunctionObjects);
    field U;
    result Q;
    writeControl writeTime;
}
</code></pre>
<p><code>field U</code> 指定速度场，<code>result Q</code> 指定输出场名，<code>writeTime</code> 随整场写出保存。用 ParaView 对 <code>Q</code> 建立 Contour，再用速度或压力着色，可以观察涡结构与周围流场的关系。</p>
<p>v2512 中该对象计算</p>
<p>\[
Q=\tfrac12\left[(\operatorname{tr}\nabla\mathbf U)^2-
\operatorname{tr}((\nabla\mathbf U)^2)\right].
\]</p>
<p>对于不可压缩流，速度散度为零，公式化为 \(Q=\tfrac12(\|\boldsymbol\Omega\|^2-\|\mathbf S\|^2)\)，其中 \(\mathbf S\) 和 \(\boldsymbol\Omega\) 是速度梯度的对称和反对称部分。可压缩流中需按完整第二不变量解释。</p>
<p>已有速度场可使用 <code>postProcess -func Q -latestTime</code>。比较不同工况时可采用 \(Q L^2/U_{ref}^2\) 这样的无量纲阈值。梯度对网格和离散敏感，细小结构随网格改变时，应结合速度场与分辨率分析。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · heatTransfer/buoyantSimpleFoam/circuitBoardCooling</summary><p>circuitBoardCooling 的这个 Q 文件是 baffle3DRegion 中的体积热源。</p>
<ul>
<li>量纲 <code>[1 -1 -3 0 0 0 0]</code> 对应 W/m³。</li>
<li><code>internalField uniform 17000</code> 给出均匀的 17000 W/m³ 发热强度，总功率由它对固体体积积分得到。</li>
<li>匹配的边界采用 <code>zeroGradient</code>。</li>
</ul>
<p>已知器件总功率时，可按有效发热体积换算 Q，并检查材料导热与界面传热设置。</p>
<p><a href="/assets/examples/v2512/q/1-Q.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/buoyantSimpleFoam/circuitBoardCooling/0.orig/baffle3DRegion/Q">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/buoyantSimpleFoam/circuitBoardCooling">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    class       volScalarField;
    object      Q;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [1 -1 -3 0 0 0 0];

internalField   uniform 17000;

boundaryField
{
    &quot;.*&quot;
    {
        type            zeroGradient;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/pimpleFoam/LES/surfaceMountedCube/fullCase</summary><p>这里的 Q1 函数对象计算速度梯度的 Q 判据，用来显示绕立方体流动的旋转结构。</p>
<ul>
<li><code>type Q</code>、<code>libs (fieldFunctionObjects)</code> 选择判据计算。</li>
<li><code>writeControl writeTime</code> 使 Q 与主场同时输出，固定步长 0.002 s、每 100 步写出对应 0.2 s。</li>
<li>同一配置还输出 vorticity，并在 10 s 后累计 U、p 的时间统计。</li>
<li>Q 由速度梯度计算，量纲为 s⁻²；显示等值面时阈值应与速度和长度尺度对应。</li>
</ul>
<p>不同工况比较可采用共同的无量纲阈值或明确给出各自参考尺度。</p>
<p><a href="/assets/examples/v2512/q/2-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/surfaceMountedCube/fullCase/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/surfaceMountedCube/fullCase">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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

libs            (turbulenceModelSchemes);

application     pimpleFoam;

startFrom       startTime;

startTime       0;

stopAt          endTime;

endTime         100;

deltaT          0.002;

writeControl    timeStep;

writeInterval   100;

purgeWrite      3;

writeFormat     binary;

writePrecision  6;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable true;

functions
{
    minMax
    {
        type            fieldMinMax;
        libs            (fieldFunctionObjects);
        fields          (U p);
    }

    DESField
    {
        // Mandatory entries
        type            DESModelRegions;
        libs            (fieldFunctionObjects);

        // Optional entries
        result          DESField;

        // Optional (inherited) entries
        writePrecision   6;
        writeToFile      true;
        useUserTime      false;

        region          region0;
        enabled         true;
        log             true;
        timeStart       0;
        timeEnd         1000;
        executeControl  timeStep;
        executeInterval 1;
        writeControl    writeTime;
        writeInterval   -1;
    }
    Q1
    {
        type            Q;
        libs            (fieldFunctionObjects);
        writeControl    writeTime;
    }
    vorticity1
    {
        type            vorticity;
        libs            (fieldFunctionObjects);
        writeControl    writeTime;
    }
    yPlus
    {
        type            yPlus;
        libs            (fieldFunctionObjects);
        writeFields     yes;
        writeControl    writeTime;
    }
    fieldAverage1
    {
        type            fieldAverage;
        libs            (fieldFunctionObjects);
        writeControl    writeTime;
        timeStart       10;

        fields
        (
            U
            {
                mean        on;
                prime2Mean  on;
                base        time;
            }

            p
            {
                mean        on;
                prime2Mean  on;
                base        time;
            }
        );
    }

    sample1
    {
        #include &quot;sample&quot;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · etc/caseDicts/postProcessing/fields</summary><p>这是 Q 判据函数对象的公共配置，可在后处理时计算旋转结构指标。</p>
<ul>
<li><code>type Q</code> 指定算法，<code>field U</code> 选择输入速度场。</li>
<li><code>libs (fieldFunctionObjects)</code> 加载实现。</li>
<li><code>executeControl writeTime</code>、<code>writeControl writeTime</code> 让计算与写出都发生在结果输出时刻。</li>
</ul>
<p>更换速度字段名时修改 field；展示等值面时同时说明阈值和单位。</p>
<p><a href="/assets/examples/v2512/q/3-Q.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/postProcessing/fields/Q">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/etc/caseDicts/postProcessing/fields">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     | Version:  v2512
    \\  /    A nd           | Website:  www.openfoam.com
     \\/     M anipulation  |
-------------------------------------------------------------------------------
Description
    Calculates the second invariant of the velocity gradient tensor.

\*---------------------------------------------------------------------------*/

type            Q;
libs            (fieldFunctionObjects);

field           U;

executeControl  writeTime;
writeControl    writeTime;

// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/postprocess/">postProcess</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>函数对象未执行</td><td>核对 libs、type、enabled、executeControl 与选定时间；求解器创建的模型对象可能是必要依赖。</td></tr><tr><td>输出路径找不到</td><td>检查 postProcessing/实例名/起始时刻，部分函数对象把场写入常规时间目录。</td></tr><tr><td>统计量定义不一致</td><td>明确面积/体积/时间加权，检查 fields、operation 与 base 的含义。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
