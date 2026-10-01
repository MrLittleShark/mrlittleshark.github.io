---
title: "constant/MRFProperties · MRFProperties"
layout: reference
description: "rotor 为预先建立的 cellZone，omega 的单位为 rad/s。nonRotatingPatches 指定区域内保持静止的边界。MRF 在固定网格上采用旋转参考系近似处理。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>rotor 为预先建立的 cellZone，omega 的单位为 rad/s。nonRotatingPatches 指定区域内保持静止的边界。MRF 在固定网格上采用旋转参考系近似处理。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>constant/MRFProperties</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>cellZone</code> · <code>active</code> · <code>origin</code> · <code>axis</code> · <code>omega</code> · <code>nonRotatingPatches</code></p><h2>关联命令</h2><p><a href="/commands/?q=simpleFoam">simpleFoam</a> · <a href="/commands/?q=pimpleFoam">pimpleFoam</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary constant/MRFProperties -keywords
simpleFoam -help</code></pre><h2>9.10 constant/MRFProperties 与 SRFProperties</h2><pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object MRFProperties;
}
rotorZone
{
    active yes;
    cellZone rotor;
    nonRotatingPatches (stator);
    origin (0 0 0);
    axis (0 0 1);
    omega constant 100;
}</code></pre>
<p>rotor 为预先建立的 cellZone，omega 的单位为 rad/s。nonRotatingPatches 指定区域内保持静止的边界。MRF 在固定网格上采用旋转参考系近似处理。</p>
<p>SRFProperties 配置单参考系模型，常用 SRFModel rpm 和 rpmCoeffs/rpm，以 rpm 表示转速。使用两种模型时应分别采用对应的角速度单位。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>cellZone</td><td>源项、运动或材料区域所引用的单元区名称。</td></tr><tr><td>active</td><td>是否启用当前模型实例或操作。</td></tr><tr><td>origin</td><td>局部坐标系、旋转或几何操作的参考原点。</td></tr><tr><td>axis</td><td>旋转轴或方向向量；需明确是否要求单位向量。</td></tr><tr><td>omega</td><td>角速度参数或湍流比耗散率场名，二者物理意义与量纲不同。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>MRF1</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr><tr><td>nonRotatingPatches</td><td>Fixed patches (by default they &#x27;move&#x27; with the MRF zone)</td></tr><tr><td>VC_1</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/simpleFoam/rotatingCylinders</h3><p>原始路径：<code>tutorials/incompressible/simpleFoam/rotatingCylinders/constant/MRFProperties</code>；求解器：<code>simpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/rotatingCylinders/constant/MRFProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/mrfproperties/1-MRFProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/rotatingCylinders">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    location    &quot;constant&quot;;
    object      MRFProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

MRF1
{
    cellZone    all;
    active      yes;

    nonRotatingPatches (outerWall);

    origin    (0 0 0);
    axis      (0 0 1);
    omega     100;
}

// ************************************************************************* //</code></pre><h3>示例 2 · heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet</h3><p>原始路径：<code>tutorials/heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet/constant/domain0/MRFProperties</code>；求解器：<code>chtMultiRegionSimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet/constant/domain0/MRFProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/mrfproperties/2-MRFProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    location    &quot;constant&quot;;
    object      MRFProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

VC_1
{
    cellZone        v_MRF;
    active          true;
    nonRotatingPatches ();
    origin          (-0.01 0.04 -0.06);
    axis            (1 0 0);
    omega           209.44;
}


// ************************************************************************* //</code></pre><h3>示例 3 · incompressible/simpleFoam/mixerVessel2D</h3><p>原始路径：<code>tutorials/incompressible/simpleFoam/mixerVessel2D/constant/MRFProperties</code>；求解器：<code>simpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/mixerVessel2D/constant/MRFProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/mrfproperties/3-MRFProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/mixerVessel2D">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      MRFProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

MRF1
{
    cellZone    rotor;
    active      yes;

    // Fixed patches (by default they &#x27;move&#x27; with the MRF zone)
    nonRotatingPatches ();

    origin    (0 0 0);
    axis      (0 0 1);
    omega     104.72;
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/simplefoam/">simpleFoam</a> · <a href="/commands/pimplefoam/">pimpleFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/MRFProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/MRFProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
