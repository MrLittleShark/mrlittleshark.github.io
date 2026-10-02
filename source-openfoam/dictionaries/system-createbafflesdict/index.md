---
title: "createBafflesDict"
layout: reference
description: "把选定的内部面转换成两侧独立的边界面，用于挡板、薄壁或区域接口。"
dictionary: true
cms_slug: "dictionary-createbafflesdict"
---

<p>把选定的内部面转换成两侧独立的边界面，用于挡板、薄壁或区域接口。</p><p>位置：<code>system/createBafflesDict</code></p><h2>配置实例</h2><p>createBaffles 将内部面转换为成对边界面。internalFacesOnly 控制选面范围，baffles 定义各挡板的 type、zoneName 和 patches。下例采用预先建立的 interfaceZone 面区域。</p>
<pre><code class="language-openfoam">internalFacesOnly true;
baffles
{
    interface
    {
        type faceZone;
        zoneName interfaceZone;
        patches
        {
            master { name sideA; type wall; }
            slave  { name sideB; type wall; }
        }
    }
}</code></pre>
<p>运行 createBaffles -overwrite 生成挡板边界。两侧的传热和流动耦合由场边界条件及物理模型确定。</p><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>patches</td><td>参与该操作的边界列表，必须对应网格中的实际 patch 名称。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet</summary><p>cpuCabinet 的这份文件保留了创建薄挡板的配置入口，但没有定义实际挡板。</p>
<ul>
<li><code>internalFacesOnly true</code> 限定操作对象为内部面。</li>
<li><code>baffles {}</code> 为空，因此这里没有要分离的面区、主面或从面。</li>
<li>要在内部面建立挡板，需要新增选择规则和成对边界信息。</li>
</ul>
<p>添加散热片或薄壁时，先确认几何应采用实际固体区还是零厚度挡板，再选择对应建模方式。</p>
<p><a href="/assets/examples/v2512/createbafflesdict/1-createBafflesDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet/system/createBafflesDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/chtMultiRegionSimpleFoam/cpuCabinet">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      createBafflesDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

internalFacesOnly true;

baffles
{
}

// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · combustion/reactingFoam/RAS/membrane</summary><p>膜算例把同一个内部面区拆为两侧边界，便于分别指定膜两侧条件。</p>
<ul>
<li><code>internalFacesOnly true</code> 只处理内部面。</li>
<li><code>type faceZone</code>、<code>zoneName membrane</code> 选择已有膜面区。</li>
<li><code>master</code> 命名为 membranePipe，<code>slave</code> 命名为 membraneSleeve，两侧都设为 <code>wall</code>。</li>
<li>生成后两侧空间位置重合，但各自有边界面与场条件。</li>
</ul>
<p>更换膜模型时在两侧场边界中设置相应耦合或传输规律；网格分面本身只建立边界。</p>
<p><a href="/assets/examples/v2512/createbafflesdict/2-createBafflesDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/combustion/reactingFoam/RAS/membrane/system/createBafflesDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/combustion/reactingFoam/RAS/membrane">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      createBafflesDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

internalFacesOnly true;

baffles
{
    membrane
    {
        type        faceZone;
        zoneName    membrane;

        patches
        {
            master
            {
                name            membranePipe;
                type            wall;
            }
            slave
            {
                name            membraneSleeve;
                type            wall;
            }
        }
    }
}


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · compressible/rhoPimpleFoam/RAS/annularThermalMixer</summary><p>环形热混合器将 rotatingZone 面区分为 AMI1、AMI2，构造不共形网格的配对接口。</p>
<ul>
<li><code>zoneName rotatingZone</code> 给出被拆分的面区。</li>
<li>主面为 <code>cyclicAMI</code>，<code>neighbourPatch AMI2</code> 指向对面，<code>matchTolerance 0.0001</code> 指定匹配容差。</li>
<li>从面通过 <code>$master</code> 继承设置，再改名 AMI2、把邻面改为 AMI1。</li>
<li><code>internalFacesOnly true</code> 将分面限制在内部面，<code>transform noOrdering</code> 保留此接口的变换设置。</li>
</ul>
<p>改动区域名称时成对更新 neighbourPatch，并检查两侧覆盖和插值权重。</p>
<p><a href="/assets/examples/v2512/createbafflesdict/3-createBafflesDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/rhoPimpleFoam/RAS/annularThermalMixer/system/createBafflesDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/rhoPimpleFoam/RAS/annularThermalMixer">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      createBafflesDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

internalFacesOnly true;

baffles
{
    baffleFaces
    {
        type        faceZone;
        zoneName    rotatingZone;

        patches
        {
            master
            {
                name            AMI1;
                type            cyclicAMI;
                matchTolerance  0.0001;
                neighbourPatch  AMI2;
                transform       noOrdering;
            }
            slave
            {
                $master;
                name            AMI2;
                neighbourPatch  AMI1;
            }
        }
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/createbaffles/">createBaffles</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>边界名称与字段不一致</td><td>修改拓扑后重新核对 constant/polyMesh/boundary 和所有 0/ 场文件，不能只修一个场。</td></tr><tr><td>单位或坐标方向错误</td><td>比较几何包围盒与预期物理尺寸；检查 scale、挤出法向和旋转轴。</td></tr><tr><td>网格生成成功但质量不足</td><td>运行 checkMesh -allTopology -allGeometry，再评估所选离散格式对非正交和扭曲的容忍度。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
