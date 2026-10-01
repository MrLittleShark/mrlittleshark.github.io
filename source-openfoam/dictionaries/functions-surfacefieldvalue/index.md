---
title: "system/controlDict → functions → surfaceFieldValue · surfaceFieldValue"
layout: reference
description: "表中名称包括函数对象类型和预配置函数。postProcess -list 列出可直接通过 -func 调用的预配置名称；其余类型按 functions 子字典配置。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>表中名称包括函数对象类型和预配置函数。postProcess -list 列出可直接通过 -func 调用的预配置名称；其余类型按 functions 子字典配置。</p><figure><img src="/assets/diagrams/reference-7.svg" alt="函数对象配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/controlDict → functions → surfaceFieldValue</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>type</code> · <code>surfaceFieldValue</code> · <code>regionType</code> · <code>name</code> · <code>operation</code> · <code>fields</code></p><h2>关联命令</h2><p><a href="/commands/?q=postProcess">postProcess</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
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
}</code></pre><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>application</td><td>供运行脚本查询的求解器名称；直接在终端执行程序时，以执行的命令为准。</td></tr><tr><td>writeControl</td><td>输出触发方式，其值决定 writeInterval 表示步数、物理时间或时钟时间。</td></tr><tr><td>writeInterval</td><td>输出间隔，需要结合 writeControl 理解单位与触发时刻。</td></tr><tr><td>functions</td><td>函数对象实例集合，可以记录残差、采样、积分或计算派生量。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>libs</td><td>额外加载的共享库。函数对象或自定义边界未注册时，应检查库名与编译版本。</td></tr><tr><td>fields</td><td>目标场列表。场名、数据类型和计算时刻必须满足相应函数对象的要求。</td></tr><tr><td>T</td><td>温度值或温度场引用，通常采用热力学温度 K。</td></tr><tr><td>region</td><td>目标网格区域名称；多区域场与网格路径中应保持一致。</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · lagrangian/simpleReactingParcelFoam/verticalChannel</h3><p>原始路径：<code>tutorials/lagrangian/simpleReactingParcelFoam/verticalChannel/system/controlDict</code>；求解器：<code>simpleReactingParcelFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/simpleReactingParcelFoam/verticalChannel/system/controlDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/surfacefieldvalue/1-controlDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/simpleReactingParcelFoam/verticalChannel">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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

application     simpleReactingParcelFoam;

startFrom       latestTime;

startTime       0;

stopAt          endTime;

endTime         500;

deltaT          1;

writeControl    timeStep;

writeInterval   20;

purgeWrite      10;

writeFormat     ascii;

writePrecision  10;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable yes;


functions
{
    avgOutlets
    {
        type            surfaceFieldValue;
        libs            (fieldFunctionObjects);
        enabled         yes;
        writeControl    writeTime;
        log             yes;
        writeFields     no;
        regionType      patch;
        name            outlet;
        operation       weightedAverage;
        weightField     phi;
        fields
        (
            H2O
            T
        );
    }
}


// ************************************************************************* //</code></pre><h3>示例 2 · lagrangian/reactingParcelFoam/verticalChannelLTS</h3><p>原始路径：<code>tutorials/lagrangian/reactingParcelFoam/verticalChannelLTS/system/controlDict</code>；求解器：<code>reactingParcelFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/verticalChannelLTS/system/controlDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/surfacefieldvalue/2-controlDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/verticalChannelLTS">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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

application     reactingParcelFoam;

startFrom       latestTime;

startTime       0;

stopAt          endTime;

endTime         300;

deltaT          1;

writeControl    timeStep;

writeInterval   10;

purgeWrite      20;

writeFormat     ascii;

writePrecision  10;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable yes;

profiling
{
    memInfo     true;
}

functions
{
    surfaceFieldValue1
    {
        type            surfaceFieldValue;
        libs            (fieldFunctionObjects);
        writeControl    writeTime;
        log             yes;
        writeFields     no;
        regionType      patch;
        name            outlet;
        operation       weightedAverage;
        weightField     phi;
        fields
        (
            H2O
            T
        );
    }
}


// ************************************************************************* //</code></pre><h3>示例 3 · heatTransfer/chtMultiRegionFoam/windshieldDefrost</h3><p>原始路径：<code>tutorials/heatTransfer/chtMultiRegionFoam/windshieldDefrost/system/controlDict</code>；求解器：<code>chtMultiRegionFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/windshieldDefrost/system/controlDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/surfacefieldvalue/3-controlDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionFoam/windshieldDefrost">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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

application     chtMultiRegionFoam;

startFrom       startTime;

startTime       0;

stopAt          endTime;

endTime         400;

deltaT          0.0001;

writeControl    adjustable;

writeInterval   1;

purgeWrite      0;

writeFormat     binary;

writePrecision  10;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable true;

adjustTimeStep  yes;

maxCo           5;

maxDeltaT       1;

functions
{
    massFlux
    {
        type            surfaceFieldValue;
        libs            (fieldFunctionObjects);
        enabled         yes;
        writeControl    timeStep;
        writeInterval   1;
        log             yes;
        writeFields     no;
        regionType      patch;
        name            inlet;
        operation       sum;
        fields          (phi);
        region          cabin;
    }
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/postprocess/">postProcess</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/controlDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/controlDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>函数对象未执行</td><td>核对 libs、type、enabled、executeControl 与选定时间；求解器创建的模型对象可能是必要依赖。</td></tr><tr><td>输出路径找不到</td><td>检查 postProcessing/实例名/起始时刻，部分函数对象把场写入常规时间目录。</td></tr><tr><td>统计量定义不一致</td><td>明确面积/体积/时间加权，检查 fields、operation 与 base 的含义。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
