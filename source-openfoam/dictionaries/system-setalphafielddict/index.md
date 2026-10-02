---
title: "setAlphaFieldDict"
layout: reference
description: "根据几何界面和单元切割体积初始化体积分数，常用于界面输运测试。"
dictionary: true
cms_slug: "dictionary-setalphafielddict"
---

<p>根据几何界面和单元切割体积初始化体积分数，常用于界面输运测试。</p><p>位置：<code>system/setAlphaFieldDict</code></p><h2>配置实例</h2><pre><code class="language-openfoam">field       alpha.water;
type        sphere;            // sphere / plane / cylinder / sin
origin      (0.5 0.5 0);
radius      0.15;
direction   (1 0 0);</code></pre>
<p>比 setFields 精细：界面所在单元会得到精确的部分体积分数（而不是 0 或 1），用于界面收敛性验证。</p><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>origin</td><td>局部坐标系、旋转或几何操作的参考原点。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · verificationAndValidation/multiphase/StefanProblem/setups.orig/interCondensatingEvaporatingFoam</summary><p>Stefan 相变验证用一个平面划分初始液相位置。</p>
<ul>
<li>目标字段为 <code>alpha.liquid</code>，相名应与物性和求解配置一致。</li>
<li><code>type plane</code> 选择平面界面，<code>origin (0.503e-3 0 0)</code> 将平面放在 x=0.503 mm。</li>
<li><code>normal (1 0 0)</code> 规定平面方向，初始化后应查看液相位于预期一侧。</li>
</ul>
<p>改变初始界面位置时移动 origin，并与解析相变问题的初始条件保持一致。</p>
<p><a href="/assets/examples/v2512/setalphafielddict/1-setAlphaFieldDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/verificationAndValidation/multiphase/StefanProblem/setups.orig/interCondensatingEvaporatingFoam/system/setAlphaFieldDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/verificationAndValidation/multiphase/StefanProblem/setups.orig/interCondensatingEvaporatingFoam">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    location    &quot;system/fluid&quot;;
    object      setFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

field   &quot;alpha.liquid&quot;;
type    plane;
origin  (0.503e-3 0 0);
normal  (1 0 0);

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · multiphase/interIsoFoam/sphereInReversedVortexFlow</summary><p>反向涡流测试以一个球形液相作为初始几何，用于比较界面变形与恢复。</p>
<ul>
<li><code>field alpha.water</code> 指定水体积分数。</li>
<li><code>type sphere</code>、<code>radius 0.15</code> 创建半径 0.15 的球面。</li>
<li><code>origin (0.35 0.35 0.35)</code> 给出球心。</li>
</ul>
<p>加密网格时保持同一几何尺寸，比较初始体积误差与完成运动周期后的形状误差。</p>
<p><a href="/assets/examples/v2512/setalphafielddict/2-setAlphaFieldDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/sphereInReversedVortexFlow/system/setAlphaFieldDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/sphereInReversedVortexFlow">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    location    &quot;system&quot;;
    object      setAlphaFieldDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

field       &quot;alpha.water&quot;;
type        sphere;
radius      0.15;
origin      (0.35 0.35 0.35);

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · multiphase/interIsoFoam/discInConstantFlowCyclicBCs</summary><p>周期平移的圆盘算例用圆柱截面定义初始水相。</p>
<ul>
<li><code>field alpha.water</code> 指定目标体积分数。</li>
<li><code>type cylinder</code>、<code>direction (0 1 0)</code> 使圆柱轴线沿 y。</li>
<li><code>radius 0.15</code>、<code>origin (0.5 0 0.75)</code> 规定半径与中心位置。</li>
</ul>
<p>改变圆盘尺寸后检查横截面网格分辨率，并保持周期边界与平移速度相配合。</p>
<p><a href="/assets/examples/v2512/setalphafielddict/3-setAlphaFieldDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/discInConstantFlowCyclicBCs/system/setAlphaFieldDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/discInConstantFlowCyclicBCs">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    location    &quot;system&quot;;
    object      setAlphaFieldDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

field     &quot;alpha.water&quot;;
type      cylinder;
direction (0 1 0);
radius    0.15;
origin    (0.5 0 0.75);

// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/setalphafield/">setAlphaField</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
