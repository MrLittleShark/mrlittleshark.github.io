---
title: "fvOptions"
layout: reference
description: "为方程添加源项、约束或求解后修正，例如动量源、多孔阻力和固定温度区。"
dictionary: true
cms_slug: "dictionary-fvoptions"
---

<p>为方程添加源项、约束或求解后修正，例如动量源、多孔阻力和固定温度区。</p><p>位置：<code>constant/fvOptions</code></p><h2>fvOptions 添加源项、约束和场修正</h2>
<p><code>fvOptions</code> 让支持该接口的求解器增加体积力、热源、多孔阻力或区域约束。它既描述采用什么模型，也描述模型作用于哪些单元。文件常位于 <code>constant/fvOptions</code>，也有教程放在 <code>system/fvOptions</code>；沿用所选完整算例的位置即可。</p>
<h3>周期通道中维持平均速度</h3>
<p>在周期通道中，可以通过动量源驱动流动。以下是 <code>meanVelocityForce</code> 的最小配置主体，放在标准文件头之后：</p>
<pre><code class="language-foam">momentumSource
{
    type          meanVelocityForce;
    active        yes;
    selectionMode all;
    fields        (U);
    Ubar          (1 0 0);
}
</code></pre>
<p><code>momentumSource</code> 是用户自定名称。<code>type</code> 选择模型；<code>selectionMode all</code> 作用于全部单元；<code>fields (U)</code> 指定速度场；<code>Ubar</code> 给出目标平均速度及方向，单位为 m/s。</p>
<p>程序根据当前区域平均速度与目标值之间的差别，调整驱动力。它适合周期流动中控制整体流速，局部速度仍由流动方程和壁面条件决定。若通道有明确入口和出口，通常先按边界条件确定流量，再判断是否确实需要额外驱动力。</p>
<p>若只选定一组单元，可替换选择部分：</p>
<pre><code class="language-foam">selectionMode cellZone;
cellZone      inletCellZone;
</code></pre>
<p><code>inletCellZone</code> 必须是网格中已有的单元区域，可由 <code>topoSet</code>、网格生成或导入步骤建立。它是一个体积单元集合，与边界面的 patch 名称不同。</p>
<h3>多孔介质阻力</h3>
<p>以下是另一个独立对象，可加入同一文件，用于已有的 <code>porosity</code> 单元区：</p>
<pre><code class="language-foam">porousResistance
{
    type explicitPorositySource;
    explicitPorositySourceCoeffs
    {
        selectionMode cellZone;
        cellZone porosity;
        type DarcyForchheimer;
        d (1e7 1e7 1e7);
        f (100 100 100);
        coordinateSystem
        {
            origin (0 0 0);
            e1 (1 0 0);
            e3 (0 0 1);
        }
    }
}
</code></pre>
<p><code>d</code> 表示黏性阻力系数，单位为 \(\mathrm{m^{-2}}\)；<code>f</code> 表示惯性阻力系数，单位为 \(\mathrm{m^{-1}}\)。三个分量对应局部坐标轴方向；此处设置相同值表示各向同性。<code>e1</code> 和 <code>e3</code> 定义局部第一、第三方向，程序据此构造正交坐标系。</p>
<p>典型阻力项可写成 \(\mathbf S=-\left(\mu\mathbf D+\rho|\mathbf U|\mathbf F/2\right)\mathbf U\)。增大 <code>d</code> 主要加强线性黏性阻力，增大 <code>f</code> 加强随流速增长的非线性阻力。参数应由材料渗透率或压降—流量关系确定。</p>
<h3>求解器中的调用位置</h3>
<p><code>simpleFoam</code>、<code>pimpleFoam</code> 等在方程组装中调用源项，并在求解前后调用约束和修正。使用基础 <code>icoFoam</code> 扩展源项时，需要在自定义程序中加入对应接口；也可以直接选用已经支持该模型的求解器。</p>
<p>启用后检查日志中选中的单元数、区域体积和模型名称。对于热源，再计算体积积分对应的总功率；对于阻力，比较源区两侧压降。这样可以直接确认源项的位置、方向和量级。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/pimpleFoam/LES/periodicHill/steadyState</summary><p>周期丘陵的 steadyState 阶段用体积动量源维持目标平均流速，避免在周期方向人为设置入口出口压差。</p>
<ul>
<li><code>type meanVelocityForce</code> 根据平均速度误差调节驱动力。</li>
<li><code>selectionMode cellZone</code>、<code>cellZone inletCellZone</code> 指定统计与作用的单元区。</li>
<li><code>fields (U)</code> 表示作用于速度方程，<code>Ubar (1 0 0)</code> 给定沿 x 的目标平均速度 1 m/s。</li>
</ul>
<p>改变目标流量时修改 Ubar；更改统计区域时同步检查 cellZone 的几何范围与场平均方式。</p>
<p><a href="/assets/examples/v2512/fvoptions/authored-periodicHill-meanVelocityForce-fvOptions.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/periodicHill/steadyState/system/fvOptions">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/periodicHill/steadyState">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      fvOptions;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

momentumSource
{
    type            meanVelocityForce;

    selectionMode   cellZone;
    cellZone        inletCellZone;

    fields          (U);
    Ubar            (1 0 0);
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/pisoFoam/laminar/porousBlockage</summary><p>porousBlockage 在选定区域添加多孔阻力，以等效连续介质代替逐个解析细孔。</p>
<ul>
<li><code>explicitPorositySource</code> 把阻力加入动量方程，<code>cellZone porousBlockage</code> 限定作用区域。</li>
<li><code>DarcyForchheimer</code> 包含线性黏性阻力和二次惯性阻力。</li>
<li><code>D 1000</code> 经 <code>$D</code> 展开为各向同性 <code>d (1000 1000 1000)</code>，Darcy 系数的单位为 m⁻²。</li>
<li><code>f (0 0 0)</code> 关闭本例的二次阻力，<code>rotation none</code> 使系数方向与给定坐标系保持一致。</li>
</ul>
<p>更换多孔材料时根据压降与流速关系拟合 d、f；各向异性材料还需设置正确的主方向。</p>
<p><a href="/assets/examples/v2512/fvoptions/authored-porousBlockage-DarcyForchheimer-fvOptions.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pisoFoam/laminar/porousBlockage/constant/fvOptions">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pisoFoam/laminar/porousBlockage">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      fvOptions;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

porosity1
{
    type            explicitPorositySource;

    explicitPorositySourceCoeffs
    {
        selectionMode   cellZone;

        cellZone        porousBlockage;

        type            DarcyForchheimer;

        // D 100;  // Very little blockage
        // D 200;  // Some blockage but steady flow
        // D 500;  // Slight waviness in the far wake
        D 1000; // Fully shedding behavior

        d   ($D $D $D);
        f   (0 0 0);

        coordinateSystem
        {
            origin  (0 0 0);
            rotation none;
        }
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/3DBox/losses</summary><p>三维拓扑优化把设计变量转化为动量阻力，用来逐步区分流体与受阻区域。</p>
<ul>
<li><code>type topOSource</code> 选择拓扑优化源项，<code>names (U Ua)</code> 指向原始速度与伴随速度变量。</li>
<li><code>function BorrvallPetersson</code> 指定设计量到源项的插值关系。</li>
<li><code>interpolationField beta</code> 使用 beta 设计场，<code>b 100</code> 是该插值函数的参数。</li>
</ul>
<p>改变惩罚程度时观察中间密度区、压降和优化目标的变化，并保证原始与伴随设置一致。</p>
<p><a href="/assets/examples/v2512/fvoptions/1-fvOptions.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/3DBox/losses/system/fvOptions">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/adjointOptimisationFoam/topologyOptimisation/monoFluidAero/laminar/3DBox/losses">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      fvOptions;
}
momSource
{
    type topOSource;
    names (U Ua);
    function BorrvallPetersson;
    b 100;
    interpolationField beta;
}</code></pre></details><details class="reference-example"><summary>示例 4 · combustion/reactingFoam/RAS/SandiaD_LTS</summary><p>SandiaD_LTS 的能量方程通过 fvOptions 接入辐射源项。</p>
<ul>
<li><code>type radiation</code> 创建辐射选项。</li>
<li><code>libs (radiationModels)</code> 加载实现所需的库。</li>
<li>本字典负责把辐射作用接到方程，辐射模型和介质参数由配套 radiationProperties 定义。</li>
</ul>
<p>更改燃烧或辐射条件时同时检查这两个文件及温度、组分字段。</p>
<p><a href="/assets/examples/v2512/fvoptions/2-fvOptions.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/reactingFoam/RAS/SandiaD_LTS/constant/fvOptions">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/reactingFoam/RAS/SandiaD_LTS">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      fvOptions;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

radiation
{
    type            radiation;
    libs (radiationModels);
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 5 · compressible/rhoPimpleFoam/RAS/TJunction</summary><p>T 形管可压缩热流动启用黏性耗散，将黏性作用产生的能量变化加入相应能量方程。</p>
<ul>
<li><code>type viscousDissipation</code> 选择该源项。</li>
<li>这个 fvOption 的开关是 <code>active</code>，省略时默认为 true。需要关闭时设置 <code>active false</code>；文件中的 <code>enabled true</code> 是保留条目，当前接口读取 active。</li>
<li>它使用已有流场及输运性质，重要程度取决于速度梯度、黏度和热量尺度。</li>
</ul>
<p>比较有无耗散时保持其他设置相同，并观察温升与整体能量收支。</p>
<p><a href="/assets/examples/v2512/fvoptions/3-fvOptions.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/rhoPimpleFoam/RAS/TJunction/constant/fvOptions">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/rhoPimpleFoam/RAS/TJunction">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      fvOptions;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

viscousDissipation
{
    type            viscousDissipation;
    enabled         true;
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/simplefoam/">simpleFoam</a> · <a href="/commands/pimplefoam/">pimpleFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，同时比较流量、压降等目标量与参考数据。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
