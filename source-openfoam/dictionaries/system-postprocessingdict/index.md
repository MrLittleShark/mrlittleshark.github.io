---
title: "postProcessingDict"
layout: reference
description: "教程组织后处理配置所用的独立字典。"
dictionary: true
cms_slug: "dictionary-postprocessingdict"
---

<p>教程组织后处理配置所用的独立字典。</p><p>位置：<code>system/postProcessingDict</code></p><h2>配置实例</h2><p>incompressible/overSimpleFoam/aeroFoil/background_overset 中的 postProcessingDict：</p><pre><code class="language-foam">FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      postProcessingDict;
}

functions
{
    processorField1
    {
        // Mandatory entries
        type            processorField;
        libs            (fieldFunctionObjects);

        // Optional (inherited) entries
        result          procField;
        region          region0;
        enabled         true;
        log             true;
        timeStart       0;
        timeEnd         5000;
        executeControl  timeStep;
        executeInterval 1;
        writeControl    writeTime;
        writeInterval   -1;
    }
}</code></pre><h2>参数说明</h2><table><thead><tr><th>条目</th><th>含义</th></tr></thead><tbody><tr><td>functions</td><td>函数对象实例集合，可以记录残差、采样、积分或计算派生量。</td></tr><tr><td>type</td><td>运行时选择的模型或操作类型，同一个关键字在不同子字典中具有不同注册表。</td></tr><tr><td>libs</td><td>额外加载的共享库。函数对象或自定义边界未注册时，应检查库名与编译版本。</td></tr><tr><td>region</td><td>目标网格区域名称；多区域场与网格路径中应保持一致。</td></tr><tr><td>executeControl</td><td>函数对象执行触发方式，与写出频率可以不同。</td></tr><tr><td>writeControl</td><td>输出触发方式，其值决定 writeInterval 表示步数、物理时间或时钟时间。</td></tr><tr><td>writeInterval</td><td>输出间隔，需要结合 writeControl 理解单位与触发时刻。</td></tr></tbody></table><h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/overSimpleFoam/aeroFoil/background_overset</summary><p>这个 postProcessingDict 在重叠网格计算中输出单元所属的并行进程编号，便于观察分区位置。</p>
<ul>
<li><code>type processorField</code>、<code>libs (fieldFunctionObjects)</code> 创建分区编号场，<code>result procField</code> 指定输出名称。</li>
<li><code>region region0</code> 选择网格区域，<code>enabled true</code> 与 <code>log true</code> 开启对象和日志。</li>
<li><code>timeStart 0</code>、<code>timeEnd 5000</code> 指定执行区间，<code>executeControl timeStep</code>、间隔 1 表示每步执行。</li>
<li><code>writeControl writeTime</code> 跟随主结果写出时刻保存字段；procField 的数值代表进程编号。</li>
</ul>
<p>改变分区方法后比较 procField 分布，可以检查重叠区域、窄通道或局部细网格是否集中在少量进程上。</p>
<p><a href="/assets/examples/v2512/postprocessingdict/1-postProcessingDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/overSimpleFoam/aeroFoil/background_overset/system/postProcessingDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/overSimpleFoam/aeroFoil/background_overset">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      postProcessingDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

functions
{
    processorField1
    {
        // Mandatory entries
        type            processorField;
        libs            (fieldFunctionObjects);

        // Optional (inherited) entries
        result          procField;
        region          region0;
        enabled         true;
        log             true;
        timeStart       0;
        timeEnd         5000;
        executeControl  timeStep;
        executeInterval 1;
        writeControl    writeTime;
        writeInterval   -1;
    }
}


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/postprocess/">postProcess</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>未找到指定场或函数对象：<code>No field / No functionObject</code></td><td>确认场已写出、当前时刻正确且所需库已加载；派生量可能必须先生成。</td></tr><tr><td>结果坐标或单位错误</td><td>记录采样坐标、截面法向和物理单位，尤其注意压力定义与法向通量符号。</td></tr><tr><td>峰值随采样方式改变</td><td>比较插值方案与网格分辨率；点值、面平均和体平均不是同一个量。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
