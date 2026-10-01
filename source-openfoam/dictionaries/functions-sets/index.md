---
title: "system/controlDict → functions → sets · sets"
layout: reference
description: "转换面集合时需处理面方向信息。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>转换面集合时需处理面方向信息。</p><figure><img src="/assets/diagrams/reference-7.svg" alt="函数对象配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/controlDict → functions → sets</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>type</code> · <code>sets</code> · <code>interpolationScheme</code> · <code>setFormat</code> · <code>fields</code> · <code>sets</code> · <code>axis</code> · <code>start</code> · <code>end</code> · <code>nPoints</code></p><h2>关联命令</h2><p><a href="/commands/?q=postProcess">postProcess</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/controlDict -entry functions -value
postProcess -help</code></pre><h2>setsToZones  将集合转换为同名网格区域  源码</h2><p>转换面集合时需处理面方向信息。</p>
<p>用法：setsToZones [选项]</p>
<pre><code class="language-openfoam">示例：setsToZones</code></pre>
<h2>10.3 沿线采样</h2><pre><code class="language-openfoam">lineSample
{
    type sets;
    libs (&quot;libsampling.so&quot;);
    writeControl writeTime;
    setFormat raw;
    interpolationScheme cellPoint;
    fields (U p);
    sets
    {
        centreline
        {
            type uniform;
            axis x;
            start (0.01 0.05 0.005);
            end (0.99 0.05 0.005);
            nPoints 100;
        }
    }
}</code></pre>
<p>axis 指定输出横坐标类型，nPoints 指定采样点数，interpolationScheme 指定单元或点插值方法。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>application</td><td>供运行脚本查询的求解器名称；直接在终端执行程序时，以执行的命令为准。</td></tr><tr><td>writeControl</td><td>输出触发方式，其值决定 writeInterval 表示步数、物理时间或时钟时间。</td></tr><tr><td>writeInterval</td><td>输出间隔，需要结合 writeControl 理解单位与触发时刻。</td></tr><tr><td>functions</td><td>函数对象实例集合，可以记录残差、采样、积分或计算派生量。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>libs</td><td>额外加载的共享库。函数对象或自定义边界未注册时，应检查库名与编译版本。</td></tr><tr><td>interpolationScheme</td><td>把离散场插值到采样位置的方式；不同插值可能影响局部峰值。</td></tr><tr><td>fields</td><td>目标场列表。场名、数据类型和计算时刻必须满足相应函数对象的要求。</td></tr><tr><td>axis</td><td>旋转轴或方向向量；需明确是否要求单位向量。</td></tr><tr><td>region</td><td>目标网格区域名称；多区域场与网格路径中应保持一致。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>start</td><td>Slightly perturbed so as not to align with face or edge</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · verificationAndValidation/schemes/divergenceExample</h3><p>原始路径：<code>tutorials/verificationAndValidation/schemes/divergenceExample/system/controlDict</code>；求解器：<code>scalarTransportFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/verificationAndValidation/schemes/divergenceExample/system/controlDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/sets/1-controlDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/verificationAndValidation/schemes/divergenceExample">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 2 · heatTransfer/chtMultiRegionSimpleFoam/jouleHeatingSolid</h3><p>原始路径：<code>tutorials/heatTransfer/chtMultiRegionSimpleFoam/jouleHeatingSolid/system/controlDict</code>；求解器：<code>chtMultiRegionSimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/jouleHeatingSolid/system/controlDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/sets/2-controlDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/jouleHeatingSolid">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 3 · multiphase/interFoam/laminar/waves/irregularMultiDirection</h3><p>原始路径：<code>tutorials/multiphase/interFoam/laminar/waves/irregularMultiDirection/system/controlDict</code>；求解器：<code>interFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/waves/irregularMultiDirection/system/controlDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/sets/3-controlDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/waves/irregularMultiDirection">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/postprocess/">postProcess</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/controlDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/controlDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>函数对象未执行</td><td>核对 libs、type、enabled、executeControl 与选定时间；求解器创建的模型对象可能是必要依赖。</td></tr><tr><td>输出路径找不到</td><td>检查 postProcessing/实例名/起始时刻，部分函数对象把场写入常规时间目录。</td></tr><tr><td>统计量定义不一致</td><td>明确面积/体积/时间加权，检查 fields、operation 与 base 的含义。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
