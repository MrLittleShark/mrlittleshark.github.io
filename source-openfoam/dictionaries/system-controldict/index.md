---
title: "controlDict"
layout: reference
description: "控制计算起止时间、时间步、结果写出和函数对象。文件位于 system 目录。"
dictionary: true
cms_slug: "dictionary-controldict"
---

<p>控制计算起止时间、时间步、结果写出和函数对象。文件位于 system 目录。</p><p>位置：<code>system/controlDict</code></p><h2>controlDict 控制计算时间和输出</h2>
<p><code>system/controlDict</code> 指定从哪个时刻开始、何时结束、每步推进多久，以及多长时间保存一次结果。网格和物理模型确定后，通常先调整这个文件。</p>
<p>以下内容放在标准 <code>FoamFile</code> 文件头之后，适用于方腔 <code>icoFoam</code> 的固定时间步计算：</p>
<pre><code class="language-foam">application     icoFoam;
startFrom       startTime;
startTime       0;
stopAt          endTime;
endTime         0.5;
deltaT          0.001;
writeControl    timeStep;
writeInterval   50;
purgeWrite      0;
writeFormat     ascii;
writePrecision  8;
writeCompression off;
timeFormat      general;
timePrecision   8;
runTimeModifiable true;
</code></pre>
<p>计算从 0 s 推进到 0.5 s，步长为 0.001 s，共 500 步。<code>writeInterval 50</code> 表示每 50 步保存一次，即每 0.05 s 生成一个时间目录。<code>purgeWrite 0</code> 保留所有输出目录，方便查看启动过程；设置为正整数时，只保留相应数量的近期写出结果。</p>
<table>
<thead>
<tr>
<th>条目</th>
<th>作用</th>
<th>修改示例</th>
</tr>
</thead>
<tbody><tr>
<td><code>application</code></td>
<td>供运行脚本识别求解器</td>
<td>直接执行命令时仍由命令名决定程序</td>
</tr>
<tr>
<td><code>startFrom</code></td>
<td>选择起始数据</td>
<td><code>latestTime</code> 从最新时间目录续算</td>
</tr>
<tr>
<td><code>endTime</code></td>
<td>结束位置</td>
<td>增大它以延长运行</td>
</tr>
<tr>
<td><code>deltaT</code></td>
<td>固定时间步长</td>
<td>减半后时间分辨率提高、步数增加</td>
</tr>
<tr>
<td><code>writeControl</code></td>
<td>输出调度方式</td>
<td><code>runTime</code> 按物理时间间隔输出</td>
</tr>
<tr>
<td><code>writePrecision</code></td>
<td>ASCII 场数据精度</td>
<td>梯度和误差分析时可适当提高</td>
</tr>
<tr>
<td><code>timePrecision</code></td>
<td>时间目录名称精度</td>
<td>较小步长时应能区分相邻输出时刻</td>
</tr>
</tbody></table>
<p><code>writeFormat ascii</code> 方便直接查看字段；<code>binary</code> 通常减少大规模数据的读写成本。<code>writeCompression on</code> 可以压缩输出，但会增加压缩和解压开销。</p>
<h3>续算与安全停止</h3>
<p>保留已有时间目录，将 <code>startFrom</code> 改为 <code>latestTime</code>，再设置更大的 <code>endTime</code>，即可从最新结果继续。若希望从头重算，使用独立算例副本并设回 <code>startTime</code>。</p>
<p><code>runTimeModifiable true</code> 允许运行期间重读支持动态修改的配置。把 <code>stopAt</code> 改为 <code>writeNow</code>，可请求程序在写出当前状态后结束；改为 <code>nextWrite</code> 则在下一次计划写出后结束。最终以日志中的结束和写出记录为准。</p>
<h3>自动时间步</h3>
<p>对支持自动步长的 <code>pimpleFoam</code>，可替换或补充以下条目：</p>
<pre><code class="language-foam">adjustTimeStep yes;
maxCo          0.5;
maxDeltaT      0.001;
writeControl   adjustableRunTime;
writeInterval  0.02;
</code></pre>
<p><code>maxCo</code> 随当前流速限制步长，<code>maxDeltaT</code> 规定步长上限，输出目标间隔为 0.02 s。<code>icoFoam</code> 使用给定步长，因此方腔中的时间步直接通过 <code>deltaT</code> 调整。</p>
<h3>添加运行时监测</h3>
<p>在文件末尾添加 <code>functions</code> 子字典；已有该字典时，将新对象合并进去：</p>
<pre><code class="language-foam">functions
{
    solverHistory
    {
        type solverInfo;
        libs (utilityFunctionObjects);
        fields (p U);
        executeControl timeStep;
        executeInterval 1;
        writeResidualFields false;
    }
}
</code></pre>
<p>这个对象每步记录压力和速度的求解信息，结果位于 <code>postProcessing/solverHistory</code>。完整场可以低频输出，探针和残差则高频记录，兼顾分析需要与磁盘占用。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/icoFoam/cavity/cavity</summary><p>这个方腔算例使用 <code>icoFoam</code> 求解不可压缩、层流、非定常流动：顶盖运动带动腔内流体，初始速度为零。这里控制计算持续多久、每步多长，以及何时保存结果。</p>
<ul>
<li><code>application icoFoam</code> 指明配套应用；在终端运行 <code>icoFoam</code> 启动求解。<code>startFrom startTime</code> 配合 <code>startTime 0</code>，从目录 <code>0</code> 读取初始场。</li>
<li><code>endTime 0.5</code> 表示算到物理时间 0.5 s，<code>deltaT 0.005</code> 表示每步推进 0.005 s；从零开始共 100 个时间步。</li>
<li><code>writeControl timeStep</code>、<code>writeInterval 20</code> 表示每 20 步保存一次，即每 0.1 s 保存一次。新结果目录依次为 <code>0.1</code>、<code>0.2</code>、<code>0.3</code>、<code>0.4</code>、<code>0.5</code>。</li>
<li><code>writeFormat ascii</code> 用文本保存字段，<code>writePrecision 6</code> 控制保存数值的有效位数。<code>fvSolution</code> 中压力 <code>1e-6</code>、速度 <code>1e-5</code> 的容差控制线性方程迭代终止；网格与时间步误差通过细化对比评估。</li>
<li><code>purgeWrite 0</code> 保留各次结果，<code>runTimeModifiable true</code> 允许运行时重新读取支持动态修改的设置。</li>
</ul>
<p>要每 0.05 s 保存一次，可把 <code>writeInterval</code> 改为 10。改变 <code>deltaT</code> 后，这种按步保存的物理间隔也会变化。续算时可使用 <code>startFrom latestTime</code>，程序从已有最大数值时间目录启动，实际起点由磁盘结果决定。</p>
<p><a href="/assets/examples/v2512/controldict/1-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/icoFoam/cavity/cavity">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · incompressible/simpleFoam/pitzDaily</summary><p><code>pitzDaily</code> 使用 <code>simpleFoam</code> 计算后台阶附近的稳态不可压缩湍流。<code>controlDict</code> 中的时间编号在这里用来计数稳态外迭代，流动状态通过迭代逐渐收敛。</p>
<ul>
<li><code>startFrom startTime</code>、<code>startTime 0</code> 从 <code>0</code> 目录的初场开始；<code>deltaT 1</code> 使迭代编号每次增加 1。</li>
<li><code>endTime 2000</code> 给出最多推进到的编号。<code>fvSolution/SIMPLE/residualControl</code> 还设置了收敛停止条件，满足时可以提前结束。</li>
<li><code>writeControl timeStep</code>、<code>writeInterval 100</code> 每 100 次迭代保存一次。目录 <code>100</code>、<code>200</code> 等表示计算进度，不应当作真实流动经历了相同秒数。</li>
<li><code>writeFormat ascii</code>、<code>writePrecision 6</code> 控制文件表示方式与输出有效位数；压力方程容差、SIMPLE 收敛阈值分别在 <code>fvSolution</code> 中设置。</li>
<li><code>purgeWrite 0</code> 保留写出的各次结果；<code>functions</code> 引入 <code>streamlines</code>，随配套函数对象设置输出流线。</li>
</ul>
<p>观察回流区长度、压降和残差是否稳定，再确定所需迭代数。只需保存较少中间结果时增大 <code>writeInterval</code>；从已收敛或部分收敛的结果继续计算时，可选择 <code>latestTime</code> 并设置更大的结束编号。</p>
<p><a href="/assets/examples/v2512/controldict/2-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/simpleFoam/pitzDaily">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · multiphase/interFoam/laminar/damBreak/damBreak</summary><p>这个溃坝算例使用 <code>interFoam</code> 计算水和空气两种不可压缩流体，水柱在重力作用下塌落并形成运动界面。快速变化的局部流速使自动时间步比固定步长更方便。</p>
<ul>
<li><code>startFrom startTime</code>、<code>startTime 0</code> 从初始化后的 <code>0</code> 目录开始，<code>endTime 1</code> 计算到 1 s。运行前按算例脚本完成网格和水体积分数初始化。</li>
<li><code>deltaT 0.001</code> 给出初始步长 0.001 s。<code>adjustTimeStep yes</code> 开启调整，此后步长会随 Courant 数变化。</li>
<li><code>maxCo 1</code> 控制流动 Courant 数，<code>maxAlphaCo 1</code> 控制界面输运对应的 Courant 数。两项同时参与时间步选择；界面附近变化较快时，后者也可能成为限制。</li>
<li><code>maxDeltaT 1</code> 将自动步长上限设为 1 s；实际步长通常还受上述两个 Courant 数和写出时刻约束，不能据此推断求解器每次走 1 s。</li>
<li><code>writeControl adjustable</code>、<code>writeInterval 0.05</code> 按物理时间每 0.05 s 保存，并允许调整步长以到达写出时刻。自适应步长下，每次写出之间的计算步数可以不同。</li>
<li><code>writeFormat ascii</code>、<code>writePrecision 6</code> 保存六位有效数字左右的文本结果；<code>fvSolution</code> 另外控制压力、速度和相分数方程的求解容差。</li>
</ul>
<p>需要更细的界面时间分辨率时，可同时减小 <code>maxCo</code>、<code>maxAlphaCo</code>，比较水前沿位置随步长的变化。把输出间隔改为 0.01 s 会增加结果文件数量；它改善观察频率，但不会自动提高每个求解步的精度。</p>
<p><a href="/assets/examples/v2512/controldict/3-controlDict.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreak/damBreak/system/controlDict">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/multiphase/interFoam/laminar/damBreak/damBreak">案例目录</a></p><pre><code class="language-foam">/*--------------------------------*- C++ -*----------------------------------*\
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


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/icofoam/">icoFoam</a> · <a href="/commands/interfoam/">interFoam</a> · <a href="/commands/simplefoam/">simpleFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>重启时刻不符合预期</td><td>核对 startFrom、startTime 与已存在的时间目录，避免旧结果影响首次运行。</td></tr><tr><td>时间目录增长过快</td><td>结合 writeControl、writeInterval、purgeWrite 与函数对象输出，先估计磁盘占用。</td></tr><tr><td>开启 adjustTimeStep 仍不生效</td><td>确认求解器确实实现对应时间步控制；检查当前求解器是否读取该参数。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
