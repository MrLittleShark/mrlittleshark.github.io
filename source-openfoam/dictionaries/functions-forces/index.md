---
title: "forces"
layout: reference
description: "对选定壁面积分压力和黏性作用，计算力与相对指定中心的力矩。"
dictionary: true
cms_slug: "dictionary-forces"
---

<p>对选定壁面积分压力和黏性作用，计算力与相对指定中心的力矩。</p><p>位置：<code>system/controlDict → functions → forces</code></p><p><code>forces</code> 对选定壁面的压力与黏性应力积分，输出力和力矩。它适合计算物体阻力、升力以及相对给定点的力矩。输出力的单位为 N，力矩为 N·m。</p>
<h3>示例：不可压缩绕流的受力</h3>
<p>在具有壁面 patch <code>body</code> 的 <code>simpleFoam</code> 案例中，将以下对象加入 <code>system/controlDict/functions</code>：</p>
<pre><code class="language-foam">bodyForces
{
    type forces;
    libs (forces);
    patches (body);
    p p;
    U U;
    rho rhoInf;
    rhoInf 1.2;
    CofR (0 0 0);
    writeControl timeStep;
    writeInterval 1;
}
</code></pre>
<p><code>patches</code> 选择参与积分的表面，可以列出多个壁面。<code>rho rhoInf</code> 表示采用指定常密度，<code>rhoInf 1.2</code> 的单位是 kg/m³，用于把运动学压力等量转换成物理力。<code>CofR</code> 是力矩参考点，改变它会改变力矩，合力保持相同。</p>
<p>压力积分与黏性积分分别输出，便于判断受力来源。数据保存在 <code>postProcessing/bodyForces/</code>，先读文件头确定列含义。可压缩案例通常读取实际 <code>rho</code> 字段，并采用相应压力单位。</p>
<p>这个对象需要求解器中的输运或湍流模型来获得应力，适合在求解时执行，或在支持的求解器后处理环境中使用。二维网格积分包含实际厚度，转换为单位展长力时除以该厚度。多个离散物体可分别创建对象，保留各自 patch 与力矩中心。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/pimpleFoam/RAS/wingMotion/wingMotion2D_simpleFoam</summary><p>二维翼型预计算对 wing 边界积分压力与黏性力。</p>
<ul>
<li><code>type forces</code>、<code>libs (forces)</code> 启用力统计，<code>patches (wing)</code> 选择受力表面。</li>
<li><code>rho rhoInf</code>、<code>rhoInf 1</code> 采用参考密度 1，把相关运动学压力转换为力所需形式。</li>
<li><code>CofR (0.4974612746 -0.01671895744 0.125)</code> 给定力矩参考中心。</li>
<li>每 10 个求解步写出，<code>log false</code> 减少终端打印。</li>
</ul>
<p>改变翼型厚度方向范围时按实际三维面积解释总力；力矩比较应使用同一个参考中心。</p>
<p><a href="/assets/examples/v2512/forces/1-forces.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/RAS/wingMotion/wingMotion2D_simpleFoam/system/forces">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/RAS/wingMotion/wingMotion2D_simpleFoam">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · multiphase/interFoam/RAS/DTCHull</summary><p>DTCHull 在每个求解步统计 hull 表面的载荷，用于观察船体阻力随迭代或时间的发展。</p>
<ul>
<li><code>patches (hull)</code> 限定船体受力表面。</li>
<li><code>type forces</code> 和 forces 库计算压力力、黏性力及力矩。</li>
<li><code>CofR (2.929541 0 0.2)</code> 指定力矩参考中心。</li>
<li><code>writeControl timeStep</code>、<code>writeInterval 1</code> 每步记录载荷，<code>log on</code> 同时打印到日志；主场则每 100 步保存。</li>
</ul>
<p>更换船体或姿态后检查 patch 和参考中心，并结合求解器当前时间处理解释载荷曲线。</p>
<p><a href="/assets/examples/v2512/forces/2-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/RAS/DTCHull/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/RAS/DTCHull">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · incompressible/overSimpleFoam/aeroFoil/aeroFoil_overset</summary><p>重叠网格翼型算例对 wing 表面输出力与力矩，便于与普通网格结果比较。</p>
<ul>
<li><code>type forces</code>、<code>patches (wing)</code> 选择积分对象。</li>
<li><code>CofR (0.4974612746 -0.01671895744 0.125)</code> 保持明确的力矩中心。</li>
<li>函数对象每 10 步写出，<code>log true</code> 在终端显示统计。</li>
<li>主求解采用 <code>overSimpleFoam</code> 与 <code>startFrom latestTime</code>，从已有结果继续稳态迭代。</li>
</ul>
<p>比较不同重叠区域或网格分辨率时，保持来流、参考密度与积分表面一致。</p>
<p><a href="/assets/examples/v2512/forces/3-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/overSimpleFoam/aeroFoil/aeroFoil_overset/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/overSimpleFoam/aeroFoil/aeroFoil_overset">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/simplefoam/">simpleFoam</a> · <a href="/commands/postprocess/">postProcess</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>函数对象未执行</td><td>核对 libs、type、enabled、executeControl 与选定时间；求解器创建的模型对象可能是必要依赖。</td></tr><tr><td>输出路径找不到</td><td>检查 postProcessing/实例名/起始时刻，部分函数对象把场写入常规时间目录。</td></tr><tr><td>统计量定义不一致</td><td>明确面积/体积/时间加权，检查 fields、operation 与 base 的含义。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
