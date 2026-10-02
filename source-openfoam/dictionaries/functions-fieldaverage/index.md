---
title: "fieldAverage"
layout: reference
description: "计算场的时间平均或迭代平均，可同时输出脉动二阶矩。"
dictionary: true
cms_slug: "dictionary-fieldaverage"
---

<p>计算场的时间平均或迭代平均，可同时输出脉动二阶矩。</p><p>位置：<code>system/controlDict → functions → fieldAverage</code></p><p><code>fieldAverage</code> 在计算过程中累计均值和脉动二阶矩。它可以输出速度平均场 <code>UMean</code>、压力平均场 <code>pMean</code>，以及速度脉动的二阶矩 <code>UPrime2Mean</code>。</p>
<h3>示例：2 s 后开始平均</h3>
<p>加入 <code>system/controlDict/functions</code>：</p>
<pre><code class="language-foam">meanFlow
{
    type fieldAverage;
    libs (fieldFunctionObjects);
    timeStart 2;
    executeControl timeStep;
    executeInterval 1;
    writeControl writeTime;
    restartOnRestart false;
    fields
    (
        U
        {
            mean on;
            prime2Mean on;
            base time;
        }
        p
        {
            mean on;
            prime2Mean off;
            base time;
        }
    );
}
</code></pre>
<p><code>timeStart</code> 决定统计起点，通常根据启动过程选择。<code>executeInterval 1</code> 每步更新，<code>writeTime</code> 随全场写出保存结果。<code>base time</code> 按时间加权，适用于变化的时间步；<code>base iteration</code> 则按累计次数平均。</p>
<p>速度的 <code>prime2Mean</code> 是对称张量，包含 \(\overline{u_i'u_j'}\)；压力的此开关关闭，因此只输出均值。统计累计信息保存在时间目录的 <code>uniform</code> 中，<code>restartOnRestart false</code> 配合这些记录支持续算时继续平均。</p>
<p>需要分段平均时，可研究 <code>periodicRestart</code> 和 <code>restartPeriod</code>。需要固定窗口时，可查看各字段的 <code>window</code> 设置。比较两段平均或逐步增加统计时长，可以观察统计结果是否已趋于稳定。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/simpleFoam/simpleCar</summary><p>simpleCar 在迭代后期对速度做平均，减小稳态迭代波动对展示结果的影响。</p>
<ul>
<li><code>type fieldAverage</code> 启用统计，<code>fields</code> 只选择 U。</li>
<li><code>base iteration</code> 以迭代为统计基准，<code>mean on</code> 输出平均，<code>prime2Mean off</code> 不计算二阶脉动量。</li>
<li><code>timeStart 500</code>、<code>triggerStart 1</code> 与 <code>controlMode timeOrTrigger</code> 通过时间或触发器条件控制启动。</li>
<li><code>writeControl writeTime</code> 让统计字段随主结果保存。</li>
</ul>
<p>用于非定常湍流统计时应按物理时间设计平均窗口，并在启动瞬态结束后开始累计。</p>
<p><a href="/assets/examples/v2512/fieldaverage/1-fieldAverage.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/simpleCar/system/fieldAverage">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/simpleCar">案例目录</a></p><pre><code class="language-foam">fieldAverage1
{
    type            fieldAverage;
    libs            (fieldFunctionObjects);
    triggerStart    1;
    timeStart       500;
    controlMode     timeOrTrigger;
    writeControl    writeTime;
    fields
    (
        U
        {
            base        iteration;
            mean        on;
            prime2Mean  off;
        }
    );
}</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/pimpleFoam/LES/NACA4412</summary><p>NACA4412 的 LES 统计在指定开始时刻后累计均值与速度脉动二阶矩。</p>
<ul>
<li><code>timeStart $tStartAvg</code> 从外部定义读取起始时刻，需在包含环境中找到其数值。</li>
<li>所有字段 <code>base time</code> 按时间累计，适合不等时间步统计。</li>
<li>U 同时启用 <code>mean</code> 和 <code>prime2Mean</code>；p、nut、nuTilda、wallShearStress 只启用均值。</li>
<li><code>writeControl writeTime</code> 输出当前累计统计字段。</li>
</ul>
<p>延长统计时长后比较均值与脉动量是否稳定，改变重启策略时同时检查已有统计累计状态。</p>
<p><a href="/assets/examples/v2512/fieldaverage/2-fieldAverage.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/NACA4412/system/fieldAverage">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/NACA4412">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/

fieldAverage
{
    type            fieldAverage;
    libs            (fieldFunctionObjects);

    enabled         true;
    writeControl    writeTime;

    timeStart       $tStartAvg;

    fields
    (
        U
        {
            mean            on;
            prime2Mean      on;
            base            time;
        }
        p
        {
            mean            on;
            prime2Mean      off;
            base            time;
        }
        nut
        {
            mean            on;
            prime2Mean      off;
            base            time;
        }
        nuTilda
        {
            mean            on;
            prime2Mean      off;
            base            time;
        }
        wallShearStress
        {
            mean            on;
            prime2Mean      off;
            base            time;
        }
    );
}

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · verificationAndValidation/atmosphericModels/atmFlatTerrain/successor/setups.orig/common</summary><p>大气边界层 successor 在这里累计 U 的平均字段，便于检查稳态结果的变化。</p>
<ul>
<li><code>type fieldAverage</code>、<code>fields (U ...)</code> 选择速度统计。</li>
<li><code>mean on</code>、<code>prime2Mean off</code> 仅计算平均。</li>
<li><code>base time</code> 按求解器时间权重累计；本例为稳态应用、<code>deltaT 1</code>，应按其迭代过程解释。</li>
<li>主场每 500 步写出，文本 <code>writePrecision 16</code> 提高保存有效位数，统计也在 writeTime 输出。</li>
</ul>
<p>转为非定常边界层时需重新选择采样开始时刻和足够长的物理平均时间。</p>
<p><a href="/assets/examples/v2512/fieldaverage/3-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/verificationAndValidation/atmosphericModels/atmFlatTerrain/successor/setups.orig/common/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/verificationAndValidation/atmosphericModels/atmFlatTerrain/successor/setups.orig/common">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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

// Make sure all utilities know specialised models
libs            (atmosphericModels);

application     buoyantBoussinesqSimpleFoam;

startFrom       latestTime;

startTime       0;

stopAt          endTime;

endTime         1000;

deltaT          1;

writeControl    timeStep;

writeInterval   500;

purgeWrite      0;

writeFormat     ascii;

writePrecision  16;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable false;

functions
{
    fieldAverage1
    {
        type            fieldAverage;
        libs            (fieldFunctionObjects);
        writeControl    writeTime;

        fields
        (
            U
            {
                mean        on;
                prime2Mean  off;
                base        time;
            }
        );
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/postprocess/">postProcess</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>函数对象未执行</td><td>核对 libs、type、enabled、executeControl 与选定时间；求解器创建的模型对象可能是必要依赖。</td></tr><tr><td>输出路径找不到</td><td>检查 postProcessing/实例名/起始时刻，部分函数对象把场写入常规时间目录。</td></tr><tr><td>统计量定义不一致</td><td>明确面积/体积/时间加权，检查 fields、operation 与 base 的含义。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
