---
title: "setTurbulenceFieldsDict"
layout: reference
description: "使用经验关系初始化速度和湍流模型场。"
dictionary: true
cms_slug: "dictionary-setturbulencefieldsdict"
---

<p>使用经验关系初始化速度和湍流模型场。</p><p>位置：<code>system/setTurbulenceFieldsDict</code></p><h2>配置实例</h2><p>verificationAndValidation/turbulenceModels/planeChannel/setups.orig/EBRSM.setTurbulenceFields 中的 setTurbulenceFieldsDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      setTurbulenceFieldsDict;
}

// Mandatory entries
uRef            17.55;

// Optional entries
initialiseU     true;
initialiseEpsilon true;
initialiseK     true;
initialiseOmega true;
initialiseR     true;
writeF          true;

kappa           0.41;
Cmu             0.09;
dPlusRef        15.0;

f               f;
U               U;
epsilon         epsilon;
k               k;
omega           omega;
R               R;</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>uRef</td><td>经验初始化所用的参考速度。</td></tr><tr><td>initialiseU</td><td>是否初始化速度场。</td></tr><tr><td>initialiseEpsilon</td><td>是否初始化湍动能耗散率。</td></tr><tr><td>initialiseK</td><td>是否初始化湍动能场。</td></tr><tr><td>initialiseOmega</td><td>是否初始化比耗散率场。</td></tr><tr><td>initialiseR</td><td>是否初始化雷诺应力张量场。</td></tr><tr><td>writeF</td><td>是否输出初始化使用的辅助 f 场。</td></tr><tr><td>kappa</td><td>此处是近壁经验关系中的 von Karman 常数，示例为 0.41。</td></tr><tr><td>Cmu</td><td>湍流经验关系中的模型常数，示例为 0.09。</td></tr><tr><td>dPlusRef</td><td>近壁无量纲距离的参考参数，具体使用方式见 setTurbulenceFields 源码。</td></tr><tr><td>omega</td><td>角速度参数或湍流比耗散率场名，二者物理意义与量纲不同。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · verificationAndValidation/turbulenceModels/planeChannel/setups.orig/EBRSM.setTurbulenceFields</summary><p>planeChannel 的 EBRSM 算例通过 setTurbulenceFields 初始化通道速度和湍流量，降低从任意初值启动的调整过程。</p>
<ul>
<li><code>uRef 17.55</code> 提供参考速度尺度，单位 m/s。</li>
<li>initialiseU、initialiseEpsilon、initialiseK、initialiseOmega、initialiseR 全部为 true，要求初始化速度、耗散率、湍动能、比耗散率和雷诺应力。</li>
<li><code>kappa 0.41</code>、<code>Cmu 0.09</code> 提供壁面标度和湍流关系中使用的常数，<code>dPlusRef 15</code> 给出近壁参考无量纲距离。</li>
<li><code>writeF true</code> 输出辅助字段 f；下方 <code>U U</code>、<code>epsilon epsilon</code> 等条目将物理量映射到实际字段名。</li>
</ul>
<p>改变参考速度或通道尺度后重新初始化，并检查 k、epsilon、omega 的正值及近壁分布，再开始流动迭代。</p>
<p><a href="/assets/examples/v2512/setturbulencefieldsdict/1-setTurbulenceFieldsDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/verificationAndValidation/turbulenceModels/planeChannel/setups.orig/EBRSM.setTurbulenceFields/system/setTurbulenceFieldsDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/verificationAndValidation/turbulenceModels/planeChannel/setups.orig/EBRSM.setTurbulenceFields">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      setTurbulenceFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

// Mandatory entries
uRef            17.55;


// Optional entries
initialiseU     true;
initialiseEpsilon true;
initialiseK     true;
initialiseOmega true;
initialiseR     true;
writeF          true;

kappa           0.41;
Cmu             0.09;
dPlusRef        15.0;

f               f;
U               U;
epsilon         epsilon;
k               k;
omega           omega;
R               R;


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/setturbulencefields/">setTurbulenceFields</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
