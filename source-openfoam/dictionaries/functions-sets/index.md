---
title: "sets"
layout: reference
description: "沿线或点集采样场数据，可用于提取速度、压力和温度剖面。"
dictionary: true
cms_slug: "dictionary-sets"
---

<p>沿线或点集采样场数据，可用于提取速度、压力和温度剖面。</p><p>位置：<code>system/controlDict → functions → sets</code></p><p><code>sets</code> 沿一条线或一组指定位置提取场，适合速度剖面、温度分布和不同网格间的曲线比较。采样点和网格单元中心可以位于不同位置，因此需要选择插值方法。</p>
<h3>示例：方腔竖直中心线</h3>
<p>把以下对象加入 <code>system/controlDict/functions</code>：</p>
<pre><code class="language-foam">centreline
{
    type sets;
    libs (sampling);
    writeControl writeTime;
    setFormat raw;
    interpolationScheme cellPoint;
    fields (U p);
    sets
    (
        vertical
        {
            type uniform;
            axis y;
            start (0.05 0.001 0.005);
            end (0.05 0.099 0.005);
            nPoints 99;
        }
    );
}
</code></pre>
<p><code>uniform</code> 在线段上均匀布点，<code>nPoints</code> 包含端点。<code>axis y</code> 将 y 坐标写作曲线的独立坐标；<code>cellPoint</code> 结合单元值与点值进行插值。<code>writeTime</code> 在全场写出时生成采样，输出在 <code>postProcessing/centreline/&lt;time&gt;/</code>。</p>
<p><code>U</code> 包含三个速度分量。绘制方腔主流剖面时，取 x 分量并按顶盖速度归一化，位置按腔长归一化。增加采样点数能使曲线点更密，实际空间分辨率仍由计算网格决定。</p>
<p>需要任意点集时可采用相应的 <code>cloud</code> 设置；需要沿网格交点采样时可查看 <code>lineCell</code>、<code>lineFace</code> 等类型。多网格比较保持相同物理线段、插值方案、分量和时刻。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · verificationAndValidation/schemes/divergenceExample</summary><p>标量对流格式验证沿一条对角线取样，用同一空间位置比较数值剖面。</p>
<ul>
<li><code>type sets</code>、<code>libs (sampling)</code> 启用采样线。</li>
<li><code>writeControl onEnd</code> 在计算结束时输出，<code>fields (T)</code> 选择标量。</li>
<li>线从 <code>(0 1 0.00501)</code> 到 <code>(1 0 0.00501)</code>，<code>nPoints 200</code> 均匀布置 200 点。</li>
<li><code>axis distance</code> 输出沿线距离，<code>cellPoint</code> 对场插值，<code>setFormat raw</code> 保存简单文本。</li>
</ul>
<p>加密网格时保留这条线，比较同一坐标上的阶跃位置、过冲与扩散。</p>
<p><a href="/assets/examples/v2512/sets/1-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/verificationAndValidation/schemes/divergenceExample/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/verificationAndValidation/schemes/divergenceExample">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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

application     scalarTransportFoam;

startFrom       startTime;

startTime       0;

stopAt          endTime;

endTime         100;

deltaT          0.005;

writeControl    timeStep;

writeInterval   100;

purgeWrite      1;

writeFormat     ascii;

writePrecision  6;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable true;

functions
{
    sample1
    {
        type        sets;
        libs        (sampling);
        writeControl onEnd;
        setFormat   raw;
        interpolationScheme cellPoint;

        fields          (T);

        sets
        {
            line1
            {
                type        uniform;
                axis        distance;

                // Slightly perturbed so as not to align with face or edge
                start       (0 1 0.00501);
                end         (1 0 0.00501);
                nPoints     200;
            }
        }
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · heatTransfer/chtMultiRegionSimpleFoam/jouleHeatingSolid</summary><p>焦耳加热算例在 solid 区沿中心线同时采样温度、电势与电导率。</p>
<ul>
<li><code>region solid</code> 将采样绑定到固体网格。</li>
<li>字段清单为 <code>T</code>、<code>jouleHeatingSource:V</code>、<code>jouleHeatingSource:sigma</code>，保留源项对象生成的名称。</li>
<li>中心线从 x=−2.5 到 2.5，y=z=0.05，<code>nPoints 20</code> 给出 20 个采样点。</li>
<li><code>writeControl writeTime</code> 跟随主结果写出，<code>axis x</code> 以 x 坐标组织数据。</li>
</ul>
<p>电极或材料分区改变后检查电势梯度、电导率与温升在同一位置的对应关系。</p>
<p><a href="/assets/examples/v2512/sets/2-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/jouleHeatingSolid/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/jouleHeatingSolid">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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

application     chtMultiRegionSimpleFoam;

startFrom       startTime;

startTime       0;

stopAt          endTime;

endTime         20000;

deltaT          1;

writeControl    timeStep;

writeInterval   50;

purgeWrite      2;

writeFormat     ascii;

writePrecision  6;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable true;

functions
{
    sample1
    {
        type            sets;
        libs            (sampling);
        writeControl    writeTime;
        region          solid;
        fields          (T jouleHeatingSource:V jouleHeatingSource:sigma);
        interpolationScheme cellPoint;
        setFormat       raw;

        sets
        {
            centreLine
            {
                type        uniform;
                axis        x;
                start       (-2.5 0.05 0.05);
                end         ( 2.5 0.05 0.05);
                nPoints     20;
            }
        }
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · multiphase/interFoam/laminar/waves/irregularMultiDirection</summary><p>多方向不规则波在固定水平位置沿竖直线采样速度和水体积分数。</p>
<ul>
<li><code>sets/line1</code> 从 <code>(7.9253 19.8599 0)</code> 延伸到 z=30，<code>nPoints 1001</code> 提供密集竖向采样。</li>
<li><code>fields (U alpha.water)</code> 同时保存流速和界面位置相关信息。</li>
<li><code>writeControl onEnd</code> 将此线设置为结束时输出，<code>fixedLocations false</code> 允许采样位置处理随网格情况更新。</li>
<li>主控制采用 <code>latestTime</code> 续算，自动步长受 <code>maxCo 0.65</code>、<code>maxAlphaCo 0.65</code> 和 <code>maxDeltaT 0.05</code> 限制。</li>
</ul>
<p>需要波面时间序列时，应把线采样改为所需写出频率，并保持采样高度覆盖预计波峰波谷。</p>
<p><a href="/assets/examples/v2512/sets/3-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/waves/irregularMultiDirection/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/waves/irregularMultiDirection">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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

application     interFoam;

startFrom       latestTime;

startTime       0;

stopAt          endTime;

endTime         750.0;

deltaT          0.01;

writeControl    adjustable;

writeInterval   0.033;

purgeWrite      0;

writeFormat     ascii;

writePrecision  6;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable yes;

adjustTimeStep  on;

maxCo           0.65;

maxAlphaCo      0.65;

maxDeltaT       0.05;

functions
{
    line
    {
        type            sets;
        libs            (sampling);
        enabled         true;
        writeControl    onEnd;

        interpolationScheme cellPoint;
        setFormat       raw;
        fixedLocations  false;

        fields
        (
            U alpha.water
        );

        sets
        {
            line1
            {
                type    uniform;
                axis    distance;
                start   ( 7.9253 19.8599 0.0 );
                end     ( 7.9253 19.8599 30.0 );
                nPoints 1001;
            }
        }
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/postprocess/">postProcess</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>函数对象未执行</td><td>核对 libs、type、enabled、executeControl 与选定时间；求解器创建的模型对象可能是必要依赖。</td></tr><tr><td>输出路径找不到</td><td>检查 postProcessing/实例名/起始时刻，部分函数对象把场写入常规时间目录。</td></tr><tr><td>统计量定义不一致</td><td>明确面积/体积/时间加权，检查 fields、operation 与 base 的含义。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
