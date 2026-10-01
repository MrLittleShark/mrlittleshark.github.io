---
title: "constant/createBoxTurbDict · createBoxTurbDict"
layout: reference
description: "特定湍流盒教程用于生成初始谱场的配置。将文件名与调用脚本一起阅读，并通过最终速度能谱和散度检查初始化是否达到目标。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>特定湍流盒教程用于生成初始谱场的配置。将文件名与调用脚本一起阅读，并通过最终速度能谱和散度检查初始化是否达到目标。</p><figure><img src="/assets/diagrams/reference-1.svg" alt="初始化配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>N</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr><tr><td>L</td><td>N           (128 128 128); N           (256 256 256); Suggested box size of 9*2*pi [cm]</td></tr><tr><td>Ek</td><td>Energy as a function of wave number Here using Comte-Bellot and Corrsin data at t.U_0/M = 42 (see Ref. table 3)</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 2 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/pimpleFoam/LES/decayIsoTurb</h3><p>原始路径：<code>tutorials/incompressible/pimpleFoam/LES/decayIsoTurb/constant/createBoxTurbDict</code>；求解器：<code>pimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/decayIsoTurb/constant/createBoxTurbDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/createboxturbdict/1-createBoxTurbDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/decayIsoTurb">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      createBoxTurbDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

N           (64 64 64);
//N           (128 128 128);
//N           (256 256 256);

// Suggested box size of 9*2*pi [cm]
L           (0.56548667765 0.56548667765 0.56548667765);

nModes      5000;

// Energy as a function of wave number
// Here using Comte-Bellot and Corrsin data at t.U_0/M = 42 (see Ref. table 3)
Ek          table
(
    (15 0)
    (20 0.000129)
    (25 0.00023)
    (30 0.000322)
    (40 0.000435)
    (50 0.000457)
    (70 0.00038)
    (100 0.00027)
    (150 0.000168)
    (200 0.00012)
    (250 8.9e-05)
    (300 7.03e-05)
    (400 4.7e-05)
    (600 2.47e-05)
    (800 1.26e-05)
    (1000 7.42e-06)
    (1250 3.96e-06)
    (1500 2.33e-06)
    (1750 1.34e-06)
    (2000 8e-07)
);


// ************************************************************************* //</code></pre><h3>示例 2 · etc/caseDicts/annotated</h3><p>原始路径：<code>etc/caseDicts/annotated/createBoxTurbDict</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/etc/caseDicts/annotated/createBoxTurbDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/createboxturbdict/2-createBoxTurbDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/etc/caseDicts/annotated">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      createBoxTurbDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

N           (64 64 64);

// Suggested box size of 9*2*pi [cm]
L           (0.56548667765 0.56548667765 0.56548667765);

nModes      5000;

// Energy as a function of wave number
// Here using Comte-Bellot and Corrsin data at t.U_0/M = 42 (see Ref. table 3)
Ek          table
(
    (15 0)
    (20 0.000129)
    (25 0.00023)
    (30 0.000322)
    (40 0.000435)
    (50 0.000457)
    (70 0.00038)
    (100 0.00027)
    (150 0.000168)
    (200 0.00012)
    (250 8.9e-05)
    (300 7.03e-05)
    (400 4.7e-05)
    (600 2.47e-05)
    (800 1.26e-05)
    (1000 7.42e-06)
    (1250 3.96e-06)
    (1500 2.33e-06)
    (1750 1.34e-06)
    (2000 8e-07)
);


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/boxturb/">boxTurb</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/createBoxTurbDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/createBoxTurbDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
