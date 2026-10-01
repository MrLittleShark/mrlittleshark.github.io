---
title: "constant/regionFaIBMProperties · regionFaIBMProperties"
layout: reference
description: "风挡颗粒/液膜教程中的有限面积区域运动表面配置。示例以 IBM1、IBM2 分别指定 surface、旋转原点、轴及随时间变化的 omega，并通过 scale 与 level 设置相应函数参数。表面 OBJ 文件及区域模型必须配套。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>风挡颗粒/液膜教程中的有限面积区域运动表面配置。示例以 IBM1、IBM2 分别指定 surface、旋转原点、轴及随时间变化的 omega，并通过 scale 与 level 设置相应函数参数。表面 OBJ 文件及区域模型必须配套。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>surface</td><td>运动表面的几何路径，&lt;constant&gt; 在 OpenFOAM 文件查找机制中展开。</td></tr><tr><td>solidBodyMotionFunction</td><td>刚体运动函数，这些示例使用 rotatingMotion。</td></tr><tr><td>origin</td><td>局部坐标系、旋转或几何操作的参考原点。</td></tr><tr><td>axis</td><td>旋转轴或方向向量；需明确是否要求单位向量。</td></tr><tr><td>omega</td><td>角速度参数或湍流比耗散率场名，二者物理意义与量纲不同。</td></tr><tr><td>frequency</td><td>sine 函数的频率参数；与所定义函数的时间变量配合。</td></tr><tr><td>amplitude</td><td>sine 函数的振幅。</td></tr><tr><td>t0</td><td>时间函数参考起点，改变相位。</td></tr><tr><td>scale</td><td>此处属于对应区域对象的标量 Function1 设置，应按所用区域模型解释。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>IBM1</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr><tr><td>scale</td><td>A scalar Function1</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 1 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><p>该文件族在本次固定版本源码中仅选到一份不同的完整配置；不重复同一个文件充当多个案例。</p><h3>示例 1 · lagrangian/kinematicParcelFoam/windshield</h3><p>原始路径：<code>tutorials/lagrangian/kinematicParcelFoam/windshield/constant/regionFaIBMProperties</code>；求解器：<code>kinematicParcelFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/kinematicParcelFoam/windshield/constant/regionFaIBMProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/regionfaibmproperties/1-regionFaIBMProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/kinematicParcelFoam/windshield">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      IBMProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

IBM1
{
    surface             &quot;&lt;constant&gt;/surface.obj&quot;;

    solidBodyMotionFunction rotatingMotion;

    origin              (0.5 0 0);
    axis                (0 0 1);
    omega               sine;
    frequency           0.5;
    amplitude           1;
    t0                 -1;

    // A scalar Function1
    scale               0.8;
    level               0;
}

IBM2
{
    surface             &quot;&lt;constant&gt;/surface_offset.obj&quot;;

    solidBodyMotionFunction rotatingMotion;

    origin              (0.65 0 0);
    axis                (0 0 1);
    omega               sine;
    frequency           0.5;
    amplitude           1;
    t0                 -1;

    // A scalar Function1
    scale               0.8;
    level               0;
}

// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/kinematicparcelfoam/">kinematicParcelFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/regionFaIBMProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/regionFaIBMProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
