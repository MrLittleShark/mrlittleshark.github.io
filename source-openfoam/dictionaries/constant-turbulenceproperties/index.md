---
title: "constant/turbulenceProperties · turbulenceProperties"
layout: reference
description: "v2512 常见流体求解器通过 turbulenceProperties 配置湍流，RASModel 和 LESModel 分别指定 RAS 与 LES 模型。Foundation 分支采用的 momentumTransport 属于另一套配置接口。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>v2512 常见流体求解器通过 turbulenceProperties 配置湍流，RASModel 和 LESModel 分别指定 RAS 与 LES 模型。Foundation 分支采用的 momentumTransport 属于另一套配置接口。</p><figure><img src="/assets/diagrams/reference-5.svg" alt="物理模型配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>constant/turbulenceProperties</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>simulationType</code> · <code>laminar</code> · <code>RAS</code> · <code>LES</code> · <code>RASModel</code> · <code>turbulence</code> · <code>printCoeffs</code></p><h2>关联命令</h2><p><a href="/commands/?q=simpleFoam">simpleFoam</a> · <a href="/commands/?q=pimpleFoam">pimpleFoam</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary constant/turbulenceProperties -keywords
simpleFoam -help</code></pre><h2>9.6 constant/turbulenceProperties</h2><p>v2512 常见流体求解器通过 turbulenceProperties 配置湍流，RASModel 和 LESModel 分别指定 RAS 与 LES 模型。Foundation 分支采用的 momentumTransport 属于另一套配置接口。</p>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object turbulenceProperties;
}
simulationType RAS;
RAS
{
    RASModel kOmegaSST;
    turbulence on;
    printCoeffs on;
}</code></pre>
<p>层流采用 simulationType laminar;。LES 可采用 simulationType LES; LES { LESModel WALE; turbulence on; printCoeffs on; delta cubeRootVol; }。</p>
<p>LES 配置还需确定滤波宽度、近壁处理、入口脉动和时间分辨率，并与网格及边界条件配合。</p>
<h2>18.2 turbulenceProperties（湍流模型）</h2><pre><code class="language-openfoam">simulationType  RAS;          // laminar / RAS / LES

RAS
{
    RASModel        kOmegaSST;
    turbulence      on;
    printCoeffs     on;        // 启动时把模型系数打印到日志，便于确认
}
simulationType  LES;

LES
{
    LESModel        WALE;              // 或 Smagorinsky / kEqn / dynamicKEqn
    delta           cubeRootVol;       // 滤波尺度：cubeRootVol / vanDriest / smooth
    turbulence      on;
    printCoeffs     on;

    cubeRootVolCoeffs { deltaCoeff 1; }
}</code></pre>
<p>常用 RANS 模型怎么挑</p>
<div class="table-scroll"><table>
<tr><th>模型</th><th>特点</th><th>场合</th></tr>
<tr><td>kEpsilon</td><td>最经典，壁面靠壁函数</td><td>内流、自由剪切流</td></tr>
<tr><td>realizableKE</td><td>对旋转/分离更好</td><td>旋流</td></tr>
<tr><td>kOmegaSST</td><td>近壁用 \(k-\omega\)、远场用 \(k-\varepsilon\)，逆压梯度和分离预测好</td><td>外流绕流、翼型，最常用</td></tr>
<tr><td>SpalartAllmaras</td><td>单方程，便宜</td><td>航空外流</td></tr>
<tr><td>LaunderSharmaKE</td><td>低雷诺数版本，需要 \(y^{+}\approx 1\)</td><td>不用壁函数时</td></tr>
</table></div>
<p>v2512 的 kEpsilon 新增 twoLayerTreatment 开关，可以在近壁内层用代数关系式，降低对第一层网格的要求：</p>
<pre><code class="language-openfoam">RAS
{
    RASModel        kEpsilon;
    turbulence      on;
    kEpsilonCoeffs  { twoLayerTreatment true; }
}</code></pre>
<p>层流就写 simulationType laminar;，此时 0/ 里不需要 k、epsilon、nut 等文件。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>simulationType</td><td>选择 laminar、RAS 或 LES 等闭合层次；改动后需同时核对模型所需的初始场、物性和壁面条件。</td></tr><tr><td>RAS</td><td>雷诺平均模型子字典，通常包含 RASModel、turbulence 和 printCoeffs。模型名称区分大小写。</td></tr></tbody></table></div><h3>教程保留的参数注释</h3><p>下面的英文说明直接来自本页选取的 v2512 文件注释。条目含义受其所在子字典限制，不能仅凭相同键名推断为同一个参数。</p><div class="table-scroll"><table><thead><tr><th>条目</th><th>源码注释</th></tr></thead><tbody><tr><td>RASModel</td><td>Tested with kEpsilon, realizableKE, kOmega, kOmegaSST, ShihQuadraticKE, LienCubicKE.</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/simpleFoam/pitzDaily</h3><p>原始路径：<code>tutorials/incompressible/simpleFoam/pitzDaily/constant/turbulenceProperties</code>；求解器：<code>simpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily/constant/turbulenceProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/turbulenceproperties/1-turbulenceProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      turbulenceProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

simulationType      RAS;

RAS
{
    // Tested with kEpsilon, realizableKE, kOmega, kOmegaSST,
    // ShihQuadraticKE, LienCubicKE.
    RASModel        kEpsilon;

    turbulence      on;

    printCoeffs     on;
}


// ************************************************************************* //</code></pre><h3>示例 2 · incompressible/pimpleFoam/LES/surfaceMountedCube/initChannel</h3><p>原始路径：<code>tutorials/incompressible/pimpleFoam/LES/surfaceMountedCube/initChannel/constant/turbulenceProperties</code>；求解器：<code>boundaryFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/surfaceMountedCube/initChannel/constant/turbulenceProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/turbulenceproperties/2-turbulenceProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/LES/surfaceMountedCube/initChannel">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      turbulenceProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

simulationType      RAS;

RAS
{
    RASModel        LaunderSharmaKE;

    turbulence      on;

    printCoeffs     on;
}


// ************************************************************************* //</code></pre><h3>示例 3 · basic/simpleFoam/implicitAMI</h3><p>原始路径：<code>tutorials/basic/simpleFoam/implicitAMI/constant/turbulenceProperties</code>；求解器：<code>simpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/basic/simpleFoam/implicitAMI/constant/turbulenceProperties">查看固定版本源码</a> · <a href="/assets/examples/v2512/turbulenceproperties/3-turbulenceProperties.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/basic/simpleFoam/implicitAMI">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      turbulenceProperties;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

simulationType laminar;

// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/simplefoam/">simpleFoam</a> · <a href="/commands/pimplefoam/">pimpleFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;constant/turbulenceProperties&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;constant/turbulenceProperties&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>Unknown model / Unknown type</td><td>核对模型名、求解器所构建的模型类别和 libs；同名模型可能属于不同注册表。</td></tr><tr><td>量纲不一致或压力基准错误</td><td>对照场 dimensions 和模型所需单位。运动学压力与热力学压力不能直接互换。</td></tr><tr><td>计算收敛但物理结果不合理</td><td>用质量、能量、相分数范围和极限工况检查模型，残差小不能替代物理验证。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
