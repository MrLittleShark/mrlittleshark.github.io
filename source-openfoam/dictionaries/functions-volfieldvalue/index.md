---
title: "system/controlDict → functions → volFieldValue · volFieldValue"
layout: reference
description: "表中名称包括函数对象类型和预配置函数。postProcess -list 列出可直接通过 -func 调用的预配置名称；其余类型按 functions 子字典配置。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>表中名称包括函数对象类型和预配置函数。postProcess -list 列出可直接通过 -func 调用的预配置名称；其余类型按 functions 子字典配置。</p><figure><img src="/assets/diagrams/reference-7.svg" alt="函数对象配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/controlDict → functions → volFieldValue</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>type</code> · <code>volFieldValue</code> · <code>operation</code> · <code>regionType</code> · <code>fields</code></p><h2>关联命令</h2><p><a href="/commands/?q=postProcess">postProcess</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/controlDict -entry functions -value
postProcess -help</code></pre><h2>10.6 统计量与派生场</h2><div class="table-scroll"><table>
<tr><th>类型</th><th>主要参数</th><th>配置与调用示例</th></tr>
<tr><td>fieldAverage</td><td>fields 下每场的 mean、prime2Mean、base</td><td>U { mean on; prime2Mean on; base time; }；生成 UMean 等</td></tr>
<tr><td>fieldMinMax</td><td>fields、location、mode</td><td>fields (p U); location true;，输出极值及位置</td></tr>
<tr><td>volFieldValue</td><td>regionType、name、operation、fields</td><td>regionType all; operation volAverage; fields (T);</td></tr>
<tr><td>surfaceFieldValue</td><td>regionType patch、name、operation、fields</td><td>name outlet; operation sum; fields (phi);，输出带法向符号的通量</td></tr>
<tr><td>solverInfo</td><td>fields</td><td>fields (p U);，记录各方程初始残差</td></tr>
<tr><td>yPlus</td><td>湍流模型及壁面量</td><td>simpleFoam -postProcess -func yPlus -latestTime</td></tr>
<tr><td>wallShearStress</td><td>patches、writeControl</td><td>simpleFoam -postProcess -func wallShearStress -latestTime</td></tr>
<tr><td>wallHeatFlux</td><td>热模型和壁面</td><td>通过相应传热求解器 -postProcess -func wallHeatFlux</td></tr>
<tr><td>CourantNo</td><td>通量及密度条件</td><td>postProcess -func CourantNo -latestTime，读取所需通量等场</td></tr>
<tr><td>mag、grad、div</td><td>操作字段</td><td>postProcess -func &#x27;mag(U)&#x27; -latestTime</td></tr>
<tr><td>vorticity、Q</td><td>速度梯度派生量</td><td>postProcess -func vorticity -latestTime</td></tr>
<tr><td>MachNo</td><td>速度和热物性声速</td><td>通过可压缩求解器 -postProcess -func MachNo</td></tr>
<tr><td>streamLine</td><td>seedSampleSet、direction、lifeTime、trackLength 等</td><td>foamGetDict streamlines 获取模板，随后配置种子点</td></tr>
</table></div>
<p>表中名称包括函数对象类型和预配置函数。postProcess -list 列出可直接通过 -func 调用的预配置名称；其余类型按 functions 子字典配置。</p>
<pre><code class="language-openfoam">statistics
{
    type fieldAverage;
    libs (&quot;libfieldFunctionObjects.so&quot;);
    timeStart 0.2;
    executeControl timeStep;
    executeInterval 1;
    writeControl writeTime;
    fields
    (
        U { mean on; prime2Mean on; base time; }
        p { mean on; prime2Mean off; base time; }
    );
}</code></pre><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>application</td><td>供运行脚本查询的求解器名称；直接在终端执行程序时，以执行的命令为准。</td></tr><tr><td>writeControl</td><td>输出触发方式，其值决定 writeInterval 表示步数、物理时间或时钟时间。</td></tr><tr><td>writeInterval</td><td>输出间隔，需要结合 writeControl 理解单位与触发时刻。</td></tr><tr><td>functions</td><td>函数对象实例集合，可以记录残差、采样、积分或计算派生量。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>libs</td><td>额外加载的共享库。函数对象或自定义边界未注册时，应检查库名与编译版本。</td></tr><tr><td>fields</td><td>目标场列表。场名、数据类型和计算时刻必须满足相应函数对象的要求。</td></tr><tr><td>interpolationScheme</td><td>把离散场插值到采样位置的方式；不同插值可能影响局部峰值。</td></tr><tr><td>patches</td><td>参与该操作的边界列表，必须对应网格中的实际 patch 名称。</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · multiphase/icoReactingMultiphaseInterFoam/oxideFormation</h3><p>原始路径：<code>tutorials/multiphase/icoReactingMultiphaseInterFoam/oxideFormation/system/controlDict</code>；求解器：<code>icoReactingMultiphaseInterFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/icoReactingMultiphaseInterFoam/oxideFormation/system/controlDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/volfieldvalue/1-controlDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/icoReactingMultiphaseInterFoam/oxideFormation">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 2 · multiphase/overInterDyMFoam/twoSquaresOutDomain</h3><p>原始路径：<code>tutorials/multiphase/overInterDyMFoam/twoSquaresOutDomain/system/controlDict</code>；求解器：<code>overInterDyMFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/overInterDyMFoam/twoSquaresOutDomain/system/controlDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/volfieldvalue/2-controlDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/overInterDyMFoam/twoSquaresOutDomain">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 3 · multiphase/icoReactingMultiphaseInterFoam/poolEvaporation</h3><p>原始路径：<code>tutorials/multiphase/icoReactingMultiphaseInterFoam/poolEvaporation/system/controlDict</code>；求解器：<code>icoReactingMultiphaseInterFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/icoReactingMultiphaseInterFoam/poolEvaporation/system/controlDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/volfieldvalue/3-controlDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/icoReactingMultiphaseInterFoam/poolEvaporation">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/postprocess/">postProcess</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/controlDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/controlDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>函数对象未执行</td><td>核对 libs、type、enabled、executeControl 与选定时间；求解器创建的模型对象可能是必要依赖。</td></tr><tr><td>输出路径找不到</td><td>检查 postProcessing/实例名/起始时刻，部分函数对象把场写入常规时间目录。</td></tr><tr><td>统计量定义不一致</td><td>明确面积/体积/时间加权，检查 fields、operation 与 base 的含义。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
