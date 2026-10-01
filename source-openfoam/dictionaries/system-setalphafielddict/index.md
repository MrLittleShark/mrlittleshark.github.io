---
title: "system/setAlphaFieldDict · setAlphaFieldDict"
layout: reference
description: "比 setFields 精细：界面所在单元会得到精确的部分体积分数（而不是 0 或 1），用于界面收敛性验证。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>比 setFields 精细：界面所在单元会得到精确的部分体积分数（而不是 0 或 1），用于界面收敛性验证。</p><figure><img src="/assets/diagrams/reference-1.svg" alt="初始化配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/setAlphaFieldDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>field</code> · <code>surfaces</code> · <code>plane</code> · <code>sphere</code></p><h2>关联命令</h2><p><a href="/commands/?q=setAlphaField">setAlphaField</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/setAlphaFieldDict -keywords
setAlphaField -help</code></pre><h2>17.12 setAlphaFieldDict</h2><pre><code class="language-openfoam">field       alpha.water;
type        sphere;            // sphere / plane / cylinder / sin
origin      (0.5 0.5 0);
radius      0.15;
direction   (1 0 0);</code></pre>
<p>比 setFields 精细：界面所在单元会得到精确的部分体积分数（而不是 0 或 1），用于界面收敛性验证。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>origin</td><td>局部坐标系、旋转或几何操作的参考原点。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>field</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · verificationAndValidation/multiphase/StefanProblem/setups.orig/interCondensatingEvaporatingFoam</h3><p>原始路径：<code>tutorials/verificationAndValidation/multiphase/StefanProblem/setups.orig/interCondensatingEvaporatingFoam/system/setAlphaFieldDict</code>；求解器：<code>interCondensatingEvaporatingFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/verificationAndValidation/multiphase/StefanProblem/setups.orig/interCondensatingEvaporatingFoam/system/setAlphaFieldDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/setalphafielddict/1-setAlphaFieldDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/verificationAndValidation/multiphase/StefanProblem/setups.orig/interCondensatingEvaporatingFoam">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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

// ************************************************************************* //</code></pre><h3>示例 2 · multiphase/interIsoFoam/sphereInReversedVortexFlow</h3><p>原始路径：<code>tutorials/multiphase/interIsoFoam/sphereInReversedVortexFlow/system/setAlphaFieldDict</code>；求解器：<code>interIsoFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/sphereInReversedVortexFlow/system/setAlphaFieldDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/setalphafielddict/2-setAlphaFieldDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/sphereInReversedVortexFlow">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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

// ************************************************************************* //</code></pre><h3>示例 3 · multiphase/interIsoFoam/discInConstantFlowCyclicBCs</h3><p>原始路径：<code>tutorials/multiphase/interIsoFoam/discInConstantFlowCyclicBCs/system/setAlphaFieldDict</code>；求解器：<code>interIsoFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/discInConstantFlowCyclicBCs/system/setAlphaFieldDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/setalphafielddict/3-setAlphaFieldDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interIsoFoam/discInConstantFlowCyclicBCs">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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

// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/setalphafield/">setAlphaField</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/setAlphaFieldDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/setAlphaFieldDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
