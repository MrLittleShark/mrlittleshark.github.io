---
title: "constant/particleTrackProperties · particleTrackProperties"
layout: reference
description: "粒子轨迹重建或轨迹输出的控制。核对云名称、采样时间、轨迹截断与采样频率；输出稀疏不一定代表颗粒消失，也可能由写出间隔造成。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>粒子轨迹重建或轨迹输出的控制。核对云名称、采样时间、轨迹截断与采样频率；输出稀疏不一定代表颗粒消失，也可能由写出间隔造成。</p><figure><img src="/assets/diagrams/reference-8.svg" alt="后处理配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>cloud</td><td>输入颗粒云名称。</td></tr><tr><td>sampleFrequency</td><td>轨迹取样频率；改变它会影响每条输出轨迹的稠密程度。</td></tr><tr><td>maxPositions</td><td>单条轨迹保留位置数量的上限，较大的值增加内存或输出需求。</td></tr><tr><td>fields</td><td>目标场列表。场名、数据类型和计算时刻必须满足相应函数对象的要求。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>cloud</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr><tr><td>setFormat</td><td>maxTracks       5;</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 2 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · lagrangian/reactingParcelFoam/airRecirculationRoom/transient</h3><p>原始路径：<code>tutorials/lagrangian/reactingParcelFoam/airRecirculationRoom/transient/constant/particleTrackProperties</code>；求解器：<code>reactingParcelFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/airRecirculationRoom/transient/constant/particleTrackProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/particletrackproperties/1-particleTrackProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/airRecirculationRoom/transient">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      particleTrackProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

cloud           reactingCloud1;

sampleFrequency 1;

maxPositions    1000000;


// ************************************************************************* //</code></pre><h3>示例 2 · lagrangian/reactingParcelFoam/filter</h3><p>原始路径：<code>tutorials/lagrangian/reactingParcelFoam/filter/constant/particleTrackProperties</code>；求解器：<code>reactingParcelFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/filter/constant/particleTrackProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/particletrackproperties/2-particleTrackProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/lagrangian/reactingParcelFoam/filter">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      particleTrackProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

cloud           reactingCloud1;

sampleFrequency 1;

maxPositions    1000000;

//maxTracks       5;

setFormat       gltf;

formatOptions
{
    animate         yes;
    colour          yes;

    animationInfo
    {
        colour          field;
        colourField     d;
        //min             0;
        //max             0.002;
        //alpha           1.0;
    }
}

fields          (d);


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/particletracks/">particleTracks</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/particleTrackProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/particleTrackProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>No field / No functionObject</td><td>确认场已写出、当前时刻正确且所需库已加载；派生量可能必须先生成。</td></tr><tr><td>结果坐标或单位错误</td><td>记录采样坐标、截面法向和物理单位，尤其注意压力定义与法向通量符号。</td></tr><tr><td>峰值随采样方式改变</td><td>比较插值方案与网格分辨率；点值、面平均和体平均不是同一个量。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
