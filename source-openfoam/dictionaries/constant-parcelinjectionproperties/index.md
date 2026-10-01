---
title: "constant/parcelInjectionProperties · parcelInjectionProperties"
layout: reference
description: "颗粒注入位置与物性分布的配置或数据。根据调用的注入模型，它可能提供粒径、速度、温度等条目；必须与 cloudProperties 中所选注入模型的读取格式一致。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>颗粒注入位置与物性分布的配置或数据。根据调用的注入模型，它可能提供粒径、速度、温度等条目；必须与 cloudProperties 中所选注入模型的读取格式一致。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><p>该专用配置的字段由对应程序决定。阅读下面完整文件时，应把同一层的大括号块作为一个模型实例，并从 Allrun 和 #include 追踪输入关系；本页不为缺少直接证据的键杜撰默认值。</p><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · lagrangian/reactingParcelFoam/rivuletPanel</h3><p>原始路径：<code>tutorials/lagrangian/reactingParcelFoam/rivuletPanel/constant/parcelInjectionProperties</code>；求解器：<code>reactingParcelFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/rivuletPanel/constant/parcelInjectionProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/parcelinjectionproperties/1-parcelInjectionProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/rivuletPanel">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      parcelInjectionProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// (x y z) (u v w) d rho mDot T cp (Y0..Y2) (Yg0..YgN) (Yl0..YlN) (Ys0..YsN)
(
    (0.050 0.025 0.09) (0 0 -5) 0.001 1000 0.002 300 4200 (1)
);


// ************************************************************************* //</code></pre><h3>示例 2 · lagrangian/reactingParcelFoam/splashPanel</h3><p>原始路径：<code>tutorials/lagrangian/reactingParcelFoam/splashPanel/constant/parcelInjectionProperties</code>；求解器：<code>reactingParcelFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/splashPanel/constant/parcelInjectionProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/parcelinjectionproperties/2-parcelInjectionProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/splashPanel">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      parcelInjectionProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// (x y z) (u v w) d rho mDot T cp (Y0..Y2) (Yg0..YgN) (Yl0..YlN) (Ys0..YsN)
(
    (0.050 0.025 0.09) (0 0 -5) 0.001 1000 0.002 300 4200 (0 1 0) () (1) ()
);


// ************************************************************************* //</code></pre><h3>示例 3 · lagrangian/reactingParcelFoam/cylinder</h3><p>原始路径：<code>tutorials/lagrangian/reactingParcelFoam/cylinder/constant/parcelInjectionProperties</code>；求解器：<code>reactingParcelFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/cylinder/constant/parcelInjectionProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/parcelinjectionproperties/3-parcelInjectionProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/cylinder">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      parcelInjectionProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// (x y z) (u v w) d rho mDot T Cp (Y0..Y2) (Yg0..YgN) (Yl0..YlN) (Ys0..YsN)
(
    (0 1.95 -0.2) (0 -5 0) 0.001 1000 0.002 300 4200 (0 1 0) () (1) ()
    (0 1.95    0) (0 -5 0) 0.001 1000 0.002 300 4200 (0 1 0) () (1) ()
    (0 1.95  0.2) (0 -5 0) 0.001 1000 0.002 300 4200 (0 1 0) () (1) ()
);


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/reactingparcelfoam/">reactingParcelFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/parcelInjectionProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/parcelInjectionProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
