---
title: "system/controlDict → functions → yPlus · yPlus"
layout: reference
description: "表中名称包括函数对象类型和预配置函数。postProcess -list 列出可直接通过 -func 调用的预配置名称；其余类型按 functions 子字典配置。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>表中名称包括函数对象类型和预配置函数。postProcess -list 列出可直接通过 -func 调用的预配置名称；其余类型按 functions 子字典配置。</p><figure><img src="/assets/diagrams/reference-7.svg" alt="函数对象配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/controlDict → functions → yPlus</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>type</code> · <code>yPlus</code> · <code>libs</code> · <code>executeControl</code> · <code>writeControl</code></p><h2>关联命令</h2><p><a href="/commands/?q=simpleFoam">simpleFoam</a> · <a href="/commands/?q=postProcess">postProcess</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/controlDict -entry functions -value
simpleFoam -help</code></pre><h2>10.6 统计量与派生场</h2><div class="table-scroll"><table>
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
}</code></pre><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>application</td><td>供运行脚本查询的求解器名称；直接在终端执行程序时，以执行的命令为准。</td></tr><tr><td>writeControl</td><td>输出触发方式，其值决定 writeInterval 表示步数、物理时间或时钟时间。</td></tr><tr><td>writeInterval</td><td>输出间隔，需要结合 writeControl 理解单位与触发时刻。</td></tr><tr><td>functions</td><td>函数对象实例集合，可以记录残差、采样、积分或计算派生量。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>libs</td><td>额外加载的共享库。函数对象或自定义边界未注册时，应检查库名与编译版本。</td></tr><tr><td>fields</td><td>目标场列表。场名、数据类型和计算时刻必须满足相应函数对象的要求。</td></tr><tr><td>patches</td><td>参与该操作的边界列表，必须对应网格中的实际 patch 名称。</td></tr><tr><td>rho</td><td>密度或密度场引用；是否为量纲标量、常量或场名由模型定义。</td></tr><tr><td>region</td><td>目标网格区域名称；多区域场与网格路径中应保持一致。</td></tr><tr><td>executeControl</td><td>函数对象执行触发方式，与写出频率可以不同。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>result</td><td>Optional entries</td></tr><tr><td>CofR</td><td>bump midpoint</td></tr><tr><td>lRef</td><td>length of bump</td></tr><tr><td>Aref</td><td>mesh span = 2, bump height = 0.05; 2*0.05=0.1</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/simpleFoam/turbulentFlatPlate/setups.orig/common</h3><p>原始路径：<code>tutorials/incompressible/simpleFoam/turbulentFlatPlate/setups.orig/common/system/controlDict</code>；求解器：<code>simpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/turbulentFlatPlate/setups.orig/common/system/controlDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/yplus/1-controlDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/turbulentFlatPlate/setups.orig/common">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><p>本例包含外部引用：&quot;writeCellCentres&quot;；&quot;wallShearStress&quot;。下载单个文件不会自动取得这些依赖。</p><h3>示例 2 · incompressible/simpleFoam/bump2D/setups.orig/common</h3><p>原始路径：<code>tutorials/incompressible/simpleFoam/bump2D/setups.orig/common/system/controlDict</code>；求解器：<code>simpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/bump2D/setups.orig/common/system/controlDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/yplus/2-controlDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/bump2D/setups.orig/common">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h3>示例 3 · incompressible/pimpleFoam/LES/surfaceMountedCube/fullCase</h3><p>原始路径：<code>tutorials/incompressible/pimpleFoam/LES/surfaceMountedCube/fullCase/system/controlDict</code>；求解器：<code>pimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/surfaceMountedCube/fullCase/system/controlDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/yplus/3-controlDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/surfaceMountedCube/fullCase">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><p>本例包含外部引用：&quot;sample&quot;。下载单个文件不会自动取得这些依赖。</p><h2>配套命令与验证次序</h2><p><a href="/commands/simplefoam/">simpleFoam</a> · <a href="/commands/postprocess/">postProcess</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/controlDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/controlDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>函数对象未执行</td><td>核对 libs、type、enabled、executeControl 与选定时间；求解器创建的模型对象可能是必要依赖。</td></tr><tr><td>输出路径找不到</td><td>检查 postProcessing/实例名/起始时刻，部分函数对象把场写入常规时间目录。</td></tr><tr><td>统计量定义不一致</td><td>明确面积/体积/时间加权，检查 fields、operation 与 base 的含义。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
