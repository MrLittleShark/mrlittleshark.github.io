---
title: "yPlus"
layout: reference
description: "根据流场和近壁模型计算壁面的无量纲距离 y+，用于检查近壁网格。"
dictionary: true
cms_slug: "dictionary-yplus"
---

<p>根据流场和近壁模型计算壁面的无量纲距离 y+，用于检查近壁网格。</p><p>位置：<code>system/controlDict → functions → yPlus</code></p><p><code>yPlus</code> 计算壁面附近的无量纲距离，用于判断第一层单元与近壁模型的配合情况：</p>
<p>\[
y^+=\frac{u_\tau y}{\nu},\qquad u_\tau=\sqrt{|\tau_w|/\rho}.
\]</p>
<p>这里 \(y\) 是壁面到第一层单元中心的距离。具体计算路径会使用所选湍流模型及壁面函数提供的信息。</p>
<h3>示例：求解时写出 y⁺</h3>
<p>在已有湍流模型的 <code>system/controlDict/functions</code> 中加入：</p>
<pre><code class="language-foam">wallResolution
{
    type yPlus;
    libs (fieldFunctionObjects);
    writeControl writeTime;
    log true;
}
</code></pre>
<p><code>writeTime</code> 随整场结果保存 <code>yPlus</code> 字段，<code>log true</code> 打印各壁面的统计。可以在 ParaView 中只显示目标壁面，用 <code>yPlus</code> 着色，定位分离、再附着和局部加速附近的变化。</p>
<p>对已完成的 <code>simpleFoam</code> 案例也可执行：</p>
<pre><code class="language-bash">simpleFoam -postProcess -func yPlus -latestTime
</code></pre>
<p>求解器的后处理模式会构造所需模型，<code>-latestTime</code> 指定最新结果。若提示模型或字段缺失，先检查 <code>turbulenceProperties</code> 和对应 <code>k</code>、<code>omega</code>、<code>epsilon</code> 等场。</p>
<p>解析近壁区常从 \(y^+\approx1\) 设计；传统高雷诺数壁面函数通常安排在适合壁面律的区域。查看分布时同时记录首层厚度、总层厚和覆盖情况，便于解释壁面剪切与热流的网格敏感性。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/simpleFoam/turbulentFlatPlate/setups.orig/common</summary><p>湍流平板算例输出各壁面的 y⁺，检查近壁分辨率与壁面处理是否匹配。</p>
<ul>
<li><code>type yPlus</code>、<code>libs (fieldFunctionObjects)</code> 启用计算。</li>
<li><code>writeFields yes</code> 保存空间分布。v2512 的 yPlus 遍历所有壁面；文件中的 <code>patches (fixedWall)</code> 不限制该对象的计算范围，可在结果中单独查看 fixedWall。</li>
<li><code>writeControl writeTime</code> 跟随每 100 步的主场写出。</li>
<li>配置还输出速度极值、单元中心和壁面剪应力，便于联合分析。</li>
</ul>
<p>调整首层高度后比较沿壁 y⁺ 分布和摩阻系数，目标范围应由选定湍流模型与壁面处理确定。</p>
<p><a href="/assets/examples/v2512/yplus/1-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/turbulentFlatPlate/setups.orig/common/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/turbulentFlatPlate/setups.orig/common">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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

application     simpleFoam;

startFrom       startTime;

startTime       0;

stopAt          endTime;

endTime         5000;

deltaT          1;

writeControl    timeStep;

writeInterval   100;

purgeWrite      1;

writeFormat     ascii;

writePrecision  8;

writeCompression off;

timeFormat      general;

timePrecision   8;

runTimeModifiable true;

functions
{
    minMax
    {
        type          fieldMinMax;
        libs          (fieldFunctionObjects);
        writeControl  timeStep;
        fields        (U);
    }

    yPlus
    {
        type            yPlus;
        libs            (fieldFunctionObjects);
        patches         (fixedWall);
        writeFields     yes;
        writeControl    writeTime;
    }

    #includeFunc &quot;writeCellCentres&quot;
    #includeFunc &quot;wallShearStress&quot;
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/simpleFoam/bump2D/setups.orig/common</summary><p>bump2D 用 y⁺、壁面剪应力、压力系数与总载荷共同检查凸起壁面附近流动。</p>
<ul>
<li>yPlus 开启 <code>writeFields yes</code> 并在 writeTime 保存。</li>
<li>wallShearStress 对 <code>bump</code> patch 输出壁面剪切。</li>
<li>pressure 函数对象以 <code>UInf (69.44 0 0)</code>、<code>rhoInf 1</code> 等参考量计算 Cp。</li>
<li>主场每 100 次迭代写出，最多保留最近 3 份结果。</li>
</ul>
<p>改变近壁网格后同时比较 y⁺、Cp 和分离位置，保留同一参考速度与几何尺度。</p>
<p><a href="/assets/examples/v2512/yplus/2-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/bump2D/setups.orig/common/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/bump2D/setups.orig/common">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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

application     simpleFoam;

startFrom       startTime;

startTime       0;

stopAt          endTime;

endTime         10000;

deltaT          1;

writeControl    timeStep;

writeInterval   100;

purgeWrite      3;

writeFormat     ascii;

writePrecision  8;

writeCompression off;

timeFormat      general;

timePrecision   8;

runTimeModifiable true;

functions
{
    pressure
    {
        type            pressure;
        libs            (fieldFunctionObjects);
        writeControl    writeTime;
        result          Cp;
        mode            staticCoeff;
        rho             rhoInf;
        rhoInf          1;
        U               UInf;
        UInf            (69.44 0 0);
        pInf            0;
    }

    forceCoeffs
    {
        type            forceCoeffs;
        libs            (forces);
        writeControl    writeTime;
        rho             rhoInf;
        rhoInf          1;
        liftDir         (0 1 0);
        dragDir         (1 0 0);
        CofR            (0.75 0 0); // bump midpoint
        pitchAxis       (0 0 1);
        magUInf         69.44;
        lRef            0.9; // length of bump
        Aref            0.1; // mesh span = 2, bump height = 0.05; 2*0.05=0.1
        patches         (bump);
    }

    wallShearStress
    {
        type            wallShearStress;
        libs            (fieldFunctionObjects);
        writeFields     yes;
        writeControl    writeTime;
        patches         (bump);
    }

    yPlus
    {
        type            yPlus;
        libs            (fieldFunctionObjects);
        writeFields     yes;
        writeControl    writeTime;
    }

    cellCentres
    {
        type            writeCellCentres;
        libs            (fieldFunctionObjects);
        writeControl    writeTime;
    }

    residuals
    {
        type            solverInfo;
        libs            (utilityFunctionObjects);
        fields          (&quot;.*&quot;);
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · incompressible/pimpleFoam/LES/surfaceMountedCube/fullCase</summary><p>绕立方体的 LES 完整算例把近壁分辨率、涡结构和时间统计一并输出。</p>
<ul>
<li>yPlus 使用 <code>fieldFunctionObjects</code>，<code>writeFields yes</code> 保存场。</li>
<li><code>writeControl writeTime</code> 跟随主场，每 100 步写出；固定 <code>deltaT 0.002</code> 时对应 0.2 s。</li>
<li>fieldAverage 从 <code>timeStart 10</code> 开始，对 U、p 计算均值和二阶脉动量。</li>
<li>Q、vorticity 与 DESField 提供流动结构和模型区域信息。</li>
</ul>
<p>比较壁面模型或网格时固定统计时段，再看 y⁺、平均流动与波动强度是否共同变化。</p>
<p><a href="/assets/examples/v2512/yplus/3-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/surfaceMountedCube/fullCase/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/surfaceMountedCube/fullCase">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/simplefoam/">simpleFoam</a> · <a href="/commands/postprocess/">postProcess</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>函数对象未执行</td><td>核对 libs、type、enabled、executeControl 与选定时间；求解器创建的模型对象可能是必要依赖。</td></tr><tr><td>输出路径找不到</td><td>检查 postProcessing/实例名/起始时刻，部分函数对象把场写入常规时间目录。</td></tr><tr><td>统计量定义不一致</td><td>明确面积/体积/时间加权，检查 fields、operation 与 base 的含义。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
