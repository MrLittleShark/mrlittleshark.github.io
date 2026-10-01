---
title: "system/controlDict → functions → forces · forces"
layout: reference
description: "下例使用参考密度处理不可压缩压力场。可压缩计算通常指定实际 rho 字段及对应压力形式。CofR 定义力矩参考中心，压力基准应与载荷积分采用的压力定义一致。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>下例使用参考密度处理不可压缩压力场。可压缩计算通常指定实际 rho 字段及对应压力形式。CofR 定义力矩参考中心，压力基准应与载荷积分采用的压力定义一致。</p><figure><img src="/assets/diagrams/reference-7.svg" alt="函数对象配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/controlDict → functions → forces</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>type</code> · <code>forces</code> · <code>patches</code> · <code>rho</code> · <code>rhoInf</code> · <code>CofR</code></p><h2>关联命令</h2><p><a href="/commands/?q=simpleFoam">simpleFoam</a> · <a href="/commands/?q=postProcess">postProcess</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/controlDict -entry functions -value
simpleFoam -help</code></pre><h2>10.5 力与力系数</h2><pre><code class="language-openfoam">bodyForces
{
    type forces;
    libs (&quot;libforces.so&quot;);
    patches (walls);
    p p;
    U U;
    rho rhoInf;
    rhoInf 1000;
    CofR (0 0 0);
    writeControl timeStep;
    writeInterval 1;
}</code></pre>
<p>下例使用参考密度处理不可压缩压力场。可压缩计算通常指定实际 rho 字段及对应压力形式。CofR 定义力矩参考中心，压力基准应与载荷积分采用的压力定义一致。</p>
<p>计算力系数时，将 type 设为 forceCoeffs，并指定 liftDir、dragDir、pitchAxis、magUInf、lRef 和 Aref。若阻力沿 x 方向、升力沿 y 方向，可设置 dragDir (1 0 0); liftDir (0 1 0); pitchAxis (0 0 1);。lRef 和 Aref 分别为归一化参考长度和面积，二维算例的参考面积需计入所取厚度。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>libs</td><td>额外加载的共享库。函数对象或自定义边界未注册时，应检查库名与编译版本。</td></tr><tr><td>writeControl</td><td>输出触发方式，其值决定 writeInterval 表示步数、物理时间或时钟时间。</td></tr><tr><td>writeInterval</td><td>输出间隔，需要结合 writeControl 理解单位与触发时刻。</td></tr><tr><td>patches</td><td>参与该操作的边界列表，必须对应网格中的实际 patch 名称。</td></tr><tr><td>rho</td><td>密度或密度场引用；是否为量纲标量、常量或场名由模型定义。</td></tr><tr><td>application</td><td>供运行脚本查询的求解器名称；直接在终端执行程序时，以执行的命令为准。</td></tr><tr><td>functions</td><td>函数对象实例集合，可以记录残差、采样、积分或计算派生量。</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/pimpleFoam/RAS/wingMotion/wingMotion2D_simpleFoam</h3><p>原始路径：<code>tutorials/incompressible/pimpleFoam/RAS/wingMotion/wingMotion2D_simpleFoam/system/forces</code>；求解器：<code>simpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/RAS/wingMotion/wingMotion2D_simpleFoam/system/forces">查看固定版本源码</a> · <a href="/assets/examples/v2512/forces/1-forces.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/RAS/wingMotion/wingMotion2D_simpleFoam">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/

forces
{
    type            forces;
    libs            (forces);

    writeControl    timeStep;
    writeInterval   10;
    log             false;

    patches         (wing);
    rho             rhoInf;
    rhoInf          1;
    CofR            (0.4974612746 -0.01671895744 0.125);
}


// ************************************************************************* //</code></pre><h3>示例 2 · multiphase/interFoam/RAS/DTCHull</h3><p>原始路径：<code>tutorials/multiphase/interFoam/RAS/DTCHull/system/controlDict</code>；求解器：<code>interFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/RAS/DTCHull/system/controlDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/forces/2-controlDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/RAS/DTCHull">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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

startFrom       startTime;

startTime       0;

stopAt          endTime;

endTime         4000;

deltaT          1;

writeControl    timeStep;

writeInterval   100;

purgeWrite      0;

writeFormat     binary;

writePrecision  6;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable yes;

functions
{
    forces
    {
        type            forces;
        libs            (forces);
        patches         (hull);
        rhoInf          998.8;
        log             on;
        writeControl    timeStep;
        writeInterval   1;
        CofR            (2.929541 0 0.2);
    }
}


// ************************************************************************* //</code></pre><h3>示例 3 · incompressible/overSimpleFoam/aeroFoil/aeroFoil_overset</h3><p>原始路径：<code>tutorials/incompressible/overSimpleFoam/aeroFoil/aeroFoil_overset/system/controlDict</code>；求解器：<code>overSimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/overSimpleFoam/aeroFoil/aeroFoil_overset/system/controlDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/forces/3-controlDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/overSimpleFoam/aeroFoil/aeroFoil_overset">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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

application     overSimpleFoam;

startFrom       latestTime;

startTime       0;

stopAt          endTime;

endTime         3000;

deltaT          1;

writeControl    runTime;

writeInterval   100;

purgeWrite      0;

writeFormat     binary;

writePrecision  6;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable true;

functions
{
    forces
    {
        type                forces;
        libs                (forces);
        writeControl        timeStep;
        writeInterval       10;
        patches             (wing);
        pName               p;
        UName               U;
        rhoName             rhoInf;
        log                 true;
        rhoInf              1;
        CofR                (0.4974612746 -0.01671895744 0.125);
    }
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/simplefoam/">simpleFoam</a> · <a href="/commands/postprocess/">postProcess</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/forces&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/forces&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>函数对象未执行</td><td>核对 libs、type、enabled、executeControl 与选定时间；求解器创建的模型对象可能是必要依赖。</td></tr><tr><td>输出路径找不到</td><td>检查 postProcessing/实例名/起始时刻，部分函数对象把场写入常规时间目录。</td></tr><tr><td>统计量定义不一致</td><td>明确面积/体积/时间加权，检查 fields、operation 与 base 的含义。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
