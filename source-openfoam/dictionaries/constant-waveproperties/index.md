---
title: "constant/waveProperties · waveProperties"
layout: reference
description: "定义造波或吸波边界使用的波浪模型、周期、波高、水深和方向。这里的波速、周期与波长必须满足所选波理论的色散关系；以静水、线性小振幅波和反射率评估逐级验证。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>定义造波或吸波边界使用的波浪模型、周期、波高、水深和方向。这里的波速、周期与波长必须满足所选波理论的色散关系；以静水、线性小振幅波和反射率评估逐级验证。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>waveModel</td><td>采用的波浪理论或造波模型，决定色散关系和所需波参数。</td></tr><tr><td>waveHeight</td><td>波峰到波谷的高度，一般为振幅的两倍。</td></tr><tr><td>waveAngle</td><td>波浪传播方向角，其单位与参考方向由模型定义。</td></tr><tr><td>rampTime</td><td>造波信号逐渐增长到目标幅值的时间，用于减小启动瞬态。</td></tr><tr><td>wavePeriod</td><td>波浪周期。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>outlet</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr><tr><td>inlet</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr><tr><td>rightwall</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · multiphase/interFoam/laminar/waves/waveMakerSolitary</h3><p>原始路径：<code>tutorials/multiphase/interFoam/laminar/waves/waveMakerSolitary/constant/waveProperties</code>；求解器：<code>interFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/waves/waveMakerSolitary/constant/waveProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/waveproperties/1-waveProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/waves/waveMakerSolitary">查看配套目录</a></p><pre><code class="language-openfoam">/*---------------------------------------------------------------------------*\
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
    object      wavesProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

outlet
{
    alpha           alpha.water;

    waveModel       shallowWaterAbsorption;

    nPaddle         1;
}


// ************************************************************************* //</code></pre><h3>示例 2 · multiphase/interIsoFoam/waveExampleStreamFunction</h3><p>原始路径：<code>tutorials/multiphase/interIsoFoam/waveExampleStreamFunction/constant/waveProperties</code>；求解器：<code>interIsoFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/waveExampleStreamFunction/constant/waveProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/waveproperties/2-waveProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/waveExampleStreamFunction">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      waveProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

inlet
{
    alpha           alpha.water;

    waveModel       streamFunction;

    nPaddle         1;

    waveHeight      0.1517;

    waveAngle       0.0;

    rampTime        3.017;

    activeAbsorption yes;

    wavePeriod      3.017;

    uMean           2.0825;

    waveLength      6.2832;

    Bjs
    (
        8.6669014e-002
        2.4849799e-002
        7.7446850e-003
        2.3355420e-003
        6.4497731e-004
        1.5205114e-004
        2.5433769e-005
       -2.2045436e-007
       -2.8711504e-006
       -1.2287334e-006
    );

    Ejs
    (
        5.6009609e-002
        3.1638171e-002
        1.5375952e-002
        7.1743178e-003
        3.3737077e-003
        1.6324880e-003
        8.2331980e-004
        4.4403497e-004
        2.7580059e-004
        2.2810557e-004
    );
}

outlet
{
    alpha           alpha.water;

    waveModel       shallowWaterAbsorption;

    nPaddle         1;
}


// ************************************************************************* //</code></pre><h3>示例 3 · multiphase/interFoam/laminar/waves/waveMakerFlap</h3><p>原始路径：<code>tutorials/multiphase/interFoam/laminar/waves/waveMakerFlap/constant/waveProperties</code>；求解器：<code>interFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/waves/waveMakerFlap/constant/waveProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/waveproperties/3-waveProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/waves/waveMakerFlap">查看配套目录</a></p><pre><code class="language-openfoam">/*---------------------------------------------------------------------------*\
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
    object      wavesProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

rightwall
{
    alpha           alpha.water;

    waveModel       shallowWaterAbsorption;

    nPaddle         1;
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/interfoam/">interFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/waveProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/waveProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
