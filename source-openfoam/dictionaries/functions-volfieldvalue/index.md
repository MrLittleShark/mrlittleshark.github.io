---
title: "volFieldValue"
layout: reference
description: "在体区域内计算场的求和、平均、极值或体积积分。"
dictionary: true
cms_slug: "dictionary-volfieldvalue"
---

<p>在体区域内计算场的求和、平均、极值或体积积分。</p><p>位置：<code>system/controlDict → functions → volFieldValue</code></p><p><code>volFieldValue</code> 对整个网格或指定 cellZone 中的单元场求平均、极值或体积分。温度适合体积平均，体积分数适合体积积分，二者对应不同操作。</p>
<h3>示例：计算水相体积</h3>
<p>在具有 <code>alpha.water</code> 的案例中加入 <code>system/controlDict/functions</code>：</p>
<pre><code class="language-foam">waterVolume
{
    type volFieldValue;
    libs (fieldFunctionObjects);
    regionType all;
    operation volIntegrate;
    fields (alpha.water);
    writeFields false;
    writeControl timeStep;
    writeInterval 1;
}
</code></pre>
<p><code>regionType all</code> 选择全部单元，<code>volIntegrate</code> 计算 \(\sum_i\alpha_iV_i\)，结果单位是 m³。<code>writeFields false</code> 只保存统计结果，减少重复字段输出。文本位于 <code>postProcessing/waterVolume/</code>。</p>
<p>将 <code>operation</code> 改为 <code>volAverage</code>、<code>fields</code> 改为 <code>(T)</code>，可以计算 \(\sum_iT_iV_i/\sum_iV_i\)。普通 <code>average</code> 按单元数平均，在大小不一的网格上与体积平均不同。</p>
<p>局部区域使用 <code>regionType cellZone</code> 并设置 <code>name heater</code> 等实际 cellZone 名称。若希望计算水相中的平均温度，可采用 <code>weightedVolAverage</code>，并以 <code>alpha.water</code> 作为 <code>weightField</code>；这种平均对应相体积权重，质量或焓权重需按目标量另外构造。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · multiphase/icoReactingMultiphaseInterFoam/oxideFormation</summary><p>氧化形成算例对液体转为氧化物的质量源作体积积分，得到整个域的相变速率监测。</p>
<ul>
<li><code>operation volIntegrate</code> 对字段乘单元体积后求和。</li>
<li><code>fields (dmdt.liquidToOxide)</code> 指定相间质量传递率场，积分结果对应总传质速率。</li>
<li>每 10 个求解步输出，<code>log true</code> 同时打印，<code>writeFields false</code> 避免另外写完整场。</li>
<li>主计算采用自动步长，所以每 10 步的物理时间间隔可能变化。</li>
</ul>
<p>更换相名称或传质模型后核对实际生成的字段名与量纲。</p>
<p><a href="/assets/examples/v2512/volfieldvalue/1-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/icoReactingMultiphaseInterFoam/oxideFormation/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/icoReactingMultiphaseInterFoam/oxideFormation">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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

application     icoReactingMultiphaseInterFoam;

startFrom       latestTime;

startTime       0;

stopAt          endTime;

endTime         3;

deltaT          1e-3;

writeControl    adjustable;

writeInterval   0.1;

purgeWrite      0;

writeFormat     ascii;

writePrecision  6;

compression     off;

timeFormat      general;

timePrecision   6;

runTimeModifiable yes;

adjustTimeStep  yes;

maxDeltaT       1e-1;

maxCo           1;
maxAlphaCo      1;
maxAlphaDdt     1;

functions
{
    mass
    {
        type            volFieldValue;
        libs            (fieldFunctionObjects);

        writeControl    timeStep;
        writeInterval   10;
        writeFields     false;
        log             true;

        operation       volIntegrate;

        fields
        (
            dmdt.liquidToOxide
        );
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · multiphase/overInterDyMFoam/twoSquaresOutDomain</summary><p>双方块重叠网格算例统计网格内水相体积分，并在指定位置记录压力和速度。</p>
<ul>
<li><code>alphaVol/type volFieldValue</code>、<code>operation volIntegrate</code> 积分 alpha.water，结果具有体积单位。</li>
<li><code>regionType all</code> 对当前网格全域求和，<code>postOperation none</code> 保留积分值。</li>
<li>每步记录，<code>writeFields false</code> 仅输出汇总数据。</li>
<li>另一个 probes 位于 <code>(0.0009999 0.0015 0.003)</code>，采样 p、U。</li>
</ul>
<p>该项直接输出当前网格的 Σalpha.water·V。统计重叠网格的物理总体积时，应另行指定不重复覆盖的统计区域或合适权重，并处理孔洞单元。</p>
<p><a href="/assets/examples/v2512/volfieldvalue/2-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/overInterDyMFoam/twoSquaresOutDomain/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/overInterDyMFoam/twoSquaresOutDomain">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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

libs            (overset fvMotionSolvers);

application     overInterDyMFoam;

startFrom       startTime;

startTime       0.0;

stopAt          endTime;

endTime         0.08;

deltaT          0.001;

writeControl    adjustable;

writeInterval   0.01;

purgeWrite      0;

writeFormat     ascii;

writePrecision  12;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable yes;

adjustTimeStep  yes;

maxCo           1.5;

maxAlphaCo      2.0;

maxDeltaT       1;


functions
{
    probes
    {
        type            probes;
        libs            (sampling);
        name            probes;
        writeControl    timeStep;
        writeInterval   1;
        fields          (p U);
        interpolationScheme cell;
        probeLocations
        (
             (0.0009999 0.0015 0.003)
        );
    }

    alphaVol
    {
        type            volFieldValue;
        libs            (fieldFunctionObjects);
        fields          (alpha.water);
        operation       volIntegrate;
        regionType      all;
        postOperation   none;
        writeControl    timeStep;
        writeInterval   1;
        writeFields     false;
        log             true;
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · multiphase/icoReactingMultiphaseInterFoam/poolEvaporation</summary><p>poolEvaporation 同时监测总蒸发速率、底部换热系数和壁面热流。</p>
<ul>
<li>mass 对 <code>dmdt.liquidToGas</code> 作 <code>volIntegrate</code>，每 10 步输出总传质速率。</li>
<li>htc 使用 <code>multiphaseInterHtcModel</code>，目标温度场 T，底部 patch 为 <code>bottom</code>。</li>
<li><code>fixedReferenceTemperature</code>、<code>TRef 373</code> 用 373 K 作为换热系数参考温度。</li>
<li>wallHeatFlux 也作用于 bottom，并随主场写出。</li>
</ul>
<p>改变加热温度时区分壁温与参考温度，再检查热流和蒸发潜热收支。</p>
<p><a href="/assets/examples/v2512/volfieldvalue/3-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/icoReactingMultiphaseInterFoam/poolEvaporation/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/icoReactingMultiphaseInterFoam/poolEvaporation">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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

application     icoReactingMultiphaseInterFoam;

startFrom       startTime;

startTime       0;

stopAt          endTime;

endTime         100;

deltaT          1e-3;

writeControl    adjustable;

writeInterval   5;

purgeWrite      4;

writeFormat     ascii;

writePrecision  6;

compression     off;

timeFormat      general;

timePrecision   6;

runTimeModifiable yes;

adjustTimeStep  yes;

maxDeltaT       1e-1;

maxCo           3;
maxAlphaCo      2;
maxAlphaDdt     1;

functions
{
    mass
    {
        type            volFieldValue;
        libs            (fieldFunctionObjects);

        writeControl    timeStep;
        writeInterval   10;
        writeFields     false;
        log             true;

        operation       volIntegrate;

        fields
        (
            dmdt.liquidToGas
        );
    }
    htc
    {
        type            multiphaseInterHtcModel;
        libs            (fieldFunctionObjects);

        field           T;
        writeControl    writeTime;
        writeInterval   1;
        htcModel        fixedReferenceTemperature;
        patches         (bottom);
        TRef            373;
    }

    wallHeatFlux
    {
        type            wallHeatFlux;
        libs            (fieldFunctionObjects);

        patches         (bottom);
        writeControl    writeTime;
        writeInterval   1;
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/postprocess/">postProcess</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>函数对象未执行</td><td>核对 libs、type、enabled、executeControl 与选定时间；求解器创建的模型对象可能是必要依赖。</td></tr><tr><td>输出路径找不到</td><td>检查 postProcessing/实例名/起始时刻，部分函数对象把场写入常规时间目录。</td></tr><tr><td>统计量定义不一致</td><td>明确面积/体积/时间加权，检查 fields、operation 与 base 的含义。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
