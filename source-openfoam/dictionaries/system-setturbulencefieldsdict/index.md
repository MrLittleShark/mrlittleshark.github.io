---
title: "system/setTurbulenceFieldsDict · setTurbulenceFieldsDict"
layout: reference
description: "使用经验关系初始化速度和湍流模型场。uRef 指定参考速度，initialiseU/initialiseK/initialiseEpsilon 等开关选择要更新的场，kappa、Cmu 和 dPlusRef 参与近壁经验关系。它不是随机湍流脉动生成器。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>使用经验关系初始化速度和湍流模型场。uRef 指定参考速度，initialiseU/initialiseK/initialiseEpsilon 等开关选择要更新的场，kappa、Cmu 和 dPlusRef 参与近壁经验关系。它不是随机湍流脉动生成器。</p><figure><img src="/assets/diagrams/reference-1.svg" alt="初始化配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>uRef</td><td>经验初始化所用的参考速度。</td></tr><tr><td>initialiseU</td><td>是否初始化速度场。</td></tr><tr><td>initialiseEpsilon</td><td>是否初始化湍动能耗散率。</td></tr><tr><td>initialiseK</td><td>是否初始化湍动能场。</td></tr><tr><td>initialiseOmega</td><td>是否初始化比耗散率场。</td></tr><tr><td>initialiseR</td><td>是否初始化雷诺应力张量场。</td></tr><tr><td>writeF</td><td>是否输出初始化使用的辅助 f 场。</td></tr><tr><td>kappa</td><td>此处是近壁经验关系中的 von Karman 常数，示例为 0.41。</td></tr><tr><td>Cmu</td><td>湍流经验关系中的模型常数，示例为 0.09。</td></tr><tr><td>dPlusRef</td><td>近壁无量纲距离的参考参数，具体使用方式见 setTurbulenceFields 源码。</td></tr><tr><td>omega</td><td>角速度参数或湍流比耗散率场名，二者物理意义与量纲不同。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>uRef</td><td>* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * // Mandatory entries</td></tr><tr><td>initialiseU</td><td>Optional entries</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 1 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><p>该文件族在本次固定版本源码中仅选到一份不同的完整配置；不重复同一个文件充当多个案例。</p><h3>示例 1 · verificationAndValidation/turbulenceModels/planeChannel/setups.orig/EBRSM.setTurbulenceFields</h3><p>原始路径：<code>tutorials/verificationAndValidation/turbulenceModels/planeChannel/setups.orig/EBRSM.setTurbulenceFields/system/setTurbulenceFieldsDict</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/verificationAndValidation/turbulenceModels/planeChannel/setups.orig/EBRSM.setTurbulenceFields/system/setTurbulenceFieldsDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/setturbulencefieldsdict/1-setTurbulenceFieldsDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/verificationAndValidation/turbulenceModels/planeChannel/setups.orig/EBRSM.setTurbulenceFields">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/setturbulencefields/">setTurbulenceFields</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/setTurbulenceFieldsDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/setTurbulenceFieldsDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>场没有发生预期变化</td><td>核对写入时刻、区域和所选集合；检查工具是否读取了实际传入的字典。</td></tr><tr><td>初始化破坏守恒</td><td>统计积分质量、体积或组分和；局部赋值可能覆盖其他已经设定的区域。</td></tr><tr><td>边界值与内部值冲突</td><td>初始化工具赋值不能替代合适的边界类型；确认下一次求解器更新是否重写边界。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
