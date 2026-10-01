---
title: "system/controlDict · controlDict"
layout: reference
description: "Courant 数由局部速度、通量、单元尺寸和时间步共同决定。可压缩激波计算还需考虑声速约束，时间步上限应结合所用求解器和离散格式确定。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>Courant 数由局部速度、通量、单元尺寸和时间步共同决定。可压缩激波计算还需考虑声速约束，时间步上限应结合所用求解器和离散格式确定。</p><figure><img src="/assets/diagrams/reference-3.svg" alt="计算控制配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><p class="source-note">配置位置：<code>system/controlDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>application</code> · <code>startFrom</code> · <code>startTime</code> · <code>stopAt</code> · <code>endTime</code> · <code>deltaT</code> · <code>writeControl</code> · <code>writeInterval</code> · <code>purgeWrite</code> · <code>adjustTimeStep</code> · <code>maxCo</code> · <code>maxAlphaCo</code> · <code>functions</code> · <code>libs</code></p><h2>关联命令</h2><p><a href="/commands/?q=icoFoam">icoFoam</a> · <a href="/commands/?q=interFoam">interFoam</a> · <a href="/commands/?q=simpleFoam">simpleFoam</a></p><h2>本机核对</h2><pre><code class="language-bash">printf '%s\n' &quot;$WM_PROJECT_VERSION&quot;
foamDictionary system/controlDict -keywords
icoFoam -help</code></pre><h2>8.1 system/controlDict</h2><pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object controlDict;
}
application pimpleFoam;
startFrom startTime;
startTime 0;
stopAt endTime;
endTime 1;
deltaT 0.001;
writeControl adjustableRunTime;
writeInterval 0.05;
purgeWrite 0;
writeFormat ascii;
writePrecision 8;
writeCompression off;
timeFormat general;
timePrecision 8;
runTimeModifiable true;
adjustTimeStep true;
maxCo 0.5;
maxDeltaT 0.01;
functions {};</code></pre>
<div class="table-scroll"><table>
<tr><th>参数</th><th>含义与可选值</th><th>设置方法</th></tr>
<tr><td>application</td><td>供运行脚本选择的应用名称</td><td>脚本按此项调用程序；终端直接调用时执行指定程序</td></tr>
<tr><td>startFrom</td><td>startTime、firstTime、latestTime</td><td>续算通常用 latestTime</td></tr>
<tr><td>startTime</td><td>开始时刻</td><td>在采用相应 startFrom 模式时读取</td></tr>
<tr><td>stopAt</td><td>endTime、writeNow、noWriteNow、nextWrite</td><td>指定停止时刻及结果写出方式</td></tr>
<tr><td>endTime</td><td>结束时刻或稳态迭代终点</td><td>稳态求解中的时间可表示迭代计数</td></tr>
<tr><td>deltaT</td><td>时间步或迭代步</td><td>瞬态计算按时间精度及稳定性确定</td></tr>
<tr><td>writeControl</td><td>timeStep、runTime、adjustableRunTime、cpuTime、clockTime 等</td><td>timeStep 下 writeInterval 是步数；runTime 下是模拟时间</td></tr>
<tr><td>writeInterval</td><td>输出间隔</td><td>由 writeControl 确定单位，并按瞬态特征设置间隔</td></tr>
<tr><td>purgeWrite</td><td>仅保留最近若干常规输出时刻</td><td>0 保留全部输出；正整数指定保留的最近时刻数</td></tr>
<tr><td>writeFormat、writePrecision</td><td>格式与有效数字</td><td>ASCII 便于检查；binary 减少 IO</td></tr>
<tr><td>writeCompression</td><td>输出压缩</td><td>on 或 off，后处理软件需支持相应格式</td></tr>
<tr><td>timeFormat、timePrecision</td><td>时间目录命名格式和精度</td><td>精度应能区分相邻输出时刻</td></tr>
<tr><td>runTimeModifiable</td><td>运行中重新读取可修改字典</td><td>可修改范围由模型和求解器的读取机制确定</td></tr>
<tr><td>adjustTimeStep、maxCo、maxDeltaT</td><td>自动时间步控制</td><td>仅在实现相应时间步控制的求解器中生效</td></tr>
<tr><td>maxAlphaCo</td><td>VOF 相分数相关 Courant 限制</td><td>仅相关求解器使用</td></tr>
<tr><td>maxDi</td><td>热扩散数控制</td><td>仅相关传热求解器使用</td></tr>
<tr><td>libs</td><td>加载自定义或功能库</td><td>例如 (&quot;libMyBC.so&quot;)</td></tr>
<tr><td>functions</td><td>运行时函数对象</td><td>见第 10 章</td></tr>
</table></div>
<p>Courant 数由局部速度、通量、单元尺寸和时间步共同决定。可压缩激波计算还需考虑声速约束，时间步上限应结合所用求解器和离散格式确定。</p>
<h2>补充说明</h2><p>它管什么：算多久、多久输出一次、用什么求解器、跑哪些后处理。每个算例必需。</p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>application</td><td>供运行脚本查询的求解器名称；直接在终端执行程序时，以执行的命令为准。</td></tr><tr><td>writeControl</td><td>输出触发方式，其值决定 writeInterval 表示步数、物理时间或时钟时间。</td></tr><tr><td>writeInterval</td><td>输出间隔，需要结合 writeControl 理解单位与触发时刻。</td></tr><tr><td>functions</td><td>函数对象实例集合，可以记录残差、采样、积分或计算派生量。</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/icoFoam/cavity/cavity</h3><p>原始路径：<code>tutorials/incompressible/icoFoam/cavity/cavity/system/controlDict</code>；求解器：<code>icoFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity/system/controlDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/controldict/1-controlDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      controlDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

application     icoFoam;

startFrom       startTime;

startTime       0;

stopAt          endTime;

endTime         0.5;

deltaT          0.005;

writeControl    timeStep;

writeInterval   20;

purgeWrite      0;

writeFormat     ascii;

writePrecision  6;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable true;


// ************************************************************************* //</code></pre><h3>示例 2 · incompressible/simpleFoam/pitzDaily</h3><p>原始路径：<code>tutorials/incompressible/simpleFoam/pitzDaily/system/controlDict</code>；求解器：<code>simpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily/system/controlDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/controldict/2-controlDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      controlDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

application     simpleFoam;

startFrom       startTime;

startTime       0;

stopAt          endTime;

endTime         2000;

deltaT          1;

writeControl    timeStep;

writeInterval   100;

purgeWrite      0;

writeFormat     ascii;

writePrecision  6;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable true;

functions
{
    #includeFunc streamlines
}


// ************************************************************************* //</code></pre><p>本例包含外部引用：streamlines。下载单个文件不会自动取得这些依赖。</p><h3>示例 3 · multiphase/interFoam/laminar/damBreak/damBreak</h3><p>原始路径：<code>tutorials/multiphase/interFoam/laminar/damBreak/damBreak/system/controlDict</code>；求解器：<code>interFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreak/damBreak/system/controlDict">查看固定版本源码</a> · <a href="/assets/examples/v2512/controldict/3-controlDict.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreak/damBreak">查看配套目录</a></p><pre><code class="language-openfoam">/*--------------------------------*- C++ -*----------------------------------*\
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
    object      controlDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

application     interFoam;

startFrom       startTime;

startTime       0;

stopAt          endTime;

endTime         1;

deltaT          0.001;

writeControl    adjustable;

writeInterval   0.05;

purgeWrite      0;

writeFormat     ascii;

writePrecision  6;

writeCompression off;

timeFormat      general;

timePrecision   6;

runTimeModifiable yes;

adjustTimeStep  yes;

maxCo           1;

maxAlphaCo      1;

maxDeltaT       1;

functions
{
    #sinclude   &quot;sampling&quot;
}


// ************************************************************************* //</code></pre><h2>配套命令与验证次序</h2><p><a href="/commands/icofoam/">icoFoam</a> · <a href="/commands/interfoam/">interFoam</a> · <a href="/commands/simplefoam/">simpleFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/controlDict&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/controlDict&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>重启时刻不符合预期</td><td>核对 startFrom、startTime 与已存在的时间目录，避免旧结果影响首次运行。</td></tr><tr><td>时间目录增长过快</td><td>结合 writeControl、writeInterval、purgeWrite 与函数对象输出，先估计磁盘占用。</td></tr><tr><td>开启 adjustTimeStep 仍不生效</td><td>确认求解器确实实现对应时间步控制；字典可解析不代表每个键被使用。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
