---
title: "solverInfo"
layout: reference
description: "记录线性求解器的初始残差、最终残差和迭代次数。"
dictionary: true
cms_slug: "dictionary-solverinfo"
---

<p>记录线性求解器的初始残差、最终残差和迭代次数。</p><p>位置：<code>system/controlDict → functions → solverInfo</code></p><p><code>solverInfo</code> 记录线性方程求解器的信息，包括场名、残差和迭代次数，便于自动绘制收敛历史。它读取求解过程中产生的 solver performance 数据。</p>
<h3>示例：记录压力和速度求解信息</h3>
<p>将以下对象加入 <code>system/controlDict/functions</code>：</p>
<pre><code class="language-foam">linearSolvers
{
    type solverInfo;
    libs (utilityFunctionObjects);
    fields (p U);
    writeControl timeStep;
    writeInterval 1;
    writeResidualFields false;
}
</code></pre>
<p><code>fields</code> 选择要跟踪的方程；VOF 算例可将 <code>p</code> 换为 <code>p_rgh</code>，湍流计算可增加 <code>k</code>、<code>epsilon</code> 或 <code>omega</code>。<code>writeInterval 1</code> 每步写出，文本保存在 <code>postProcessing/linearSolvers/</code>。先查看文件头，区分初始残差、最终残差和迭代次数。</p>
<p><code>writeResidualFields</code> 开启后可写初始残差场，适合定位空间上的残差分布，同时会增加输出量。某时间步没有求解某个场时，该场可能没有新的线性求解记录。</p>
<p>一个 PIMPLE 时间步可能多次求解压力和速度，需要结合日志中的外校正与内校正次数解释记录。<code>solverInfo</code> 提供线性求解信息，稳态计算还可以同时记录流量、压降或阻力，观察这些目标量是否稳定。</p>
<p>该对象主要在求解时使用。已经结束且只保存场文件的计算，可以从保留的求解日志提取残差；这些历史迭代数据无法由某一个最终场重新构造。</p>
<h2>完整案例配置</h2><p>以下文件保留原始注释。需要配套网格、初始场或 include 文件时，从相应案例目录一起取得。</p><details class="reference-example" open><summary>示例 1 · incompressible/pimpleFoam/laminar/planarPoiseuille/setups.orig/common</summary><p>平面 Poiseuille 算例专门记录压力线性求解信息。</p>
<ul>
<li><code>#includeEtc .../solverInfo.cfg</code> 引入公共 solverInfo 设置。</li>
<li><code>fields (p)</code> 只筛选压力方程，便于逐步查看残差和迭代情况。</li>
<li>每次线性求解的停止设置仍来自 fvSolution。</li>
</ul>
<p>增加速度或其他方程监测时扩展 fields 列表，并区分每次线性求解与外层时间推进。</p>
<p><a href="/assets/examples/v2512/solverinfo/1-solverInfo.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/planarPoiseuille/setups.orig/common/system/solverInfo">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/planarPoiseuille/setups.orig/common">案例目录</a></p><pre><code class="language-foam">// -*- C++ -*-

#includeEtc &quot;caseDicts/postProcessing/numerical/solverInfo.cfg&quot;

fields      ( p );


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 2 · compressible/rhoSimpleFoam/aerofoilNACA0012</summary><p>可压缩 NACA0012 算例监测压力、速度、能量和湍流方程的求解表现。</p>
<ul>
<li>公共 solverInfo.cfg 提供函数对象类型与输出设置。</li>
<li><code>fields (p U e k omega)</code> 选择五类字段，e 是此算例使用的能量变量。</li>
<li>输出可用于发现某个方程残差持续偏高或线性迭代成本增加。</li>
</ul>
<p>更换热力学能量变量或湍流模型后同步更新字段清单。</p>
<p><a href="/assets/examples/v2512/solverinfo/2-solverInfo.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/rhoSimpleFoam/aerofoilNACA0012/system/solverInfo">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/rhoSimpleFoam/aerofoilNACA0012">案例目录</a></p><pre><code class="language-foam">// -*- C++ -*-

#includeEtc &quot;caseDicts/postProcessing/numerical/solverInfo.cfg&quot;

fields      ( p U e k omega );


// ************************************************************************* //</code></pre></details><details class="reference-example"><summary>示例 3 · heatTransfer/buoyantBoussinesqPimpleFoam/BenardCells</summary><p>Bénard 对流算例记录 p_rgh 的求解信息，便于观察浮力流动中的压力校正。</p>
<ul>
<li><code>fields (p_rgh)</code> 只监测扣除重力势后的压力变量。</li>
<li><code>writeControl writeTime</code> 跟随主结果写出。</li>
<li><code>writeFields yes</code> 同时启用相应诊断场输出，公共 solverInfo.cfg 提供其他基础设置。</li>
</ul>
<p>出现对流结构变化时把压力求解信息与温度、速度变化放在同一时间范围比较。</p>
<p><a href="/assets/examples/v2512/solverinfo/3-solverInfo.txt">下载配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/buoyantBoussinesqPimpleFoam/BenardCells/system/solverInfo">源码</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/buoyantBoussinesqPimpleFoam/BenardCells">案例目录</a></p><pre><code class="language-foam">// -*- C++ -*-

#includeEtc &quot;caseDicts/postProcessing/numerical/solverInfo.cfg&quot;

writeControl writeTime;

fields      (p_rgh);

writeFields yes;


// ************************************************************************* //</code></pre></details><h2>相关命令</h2><p><a href="/commands/icofoam/">icoFoam</a> · <a href="/commands/simplefoam/">simpleFoam</a></p><h2>常见问题</h2><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>函数对象未执行</td><td>核对 libs、type、enabled、executeControl 与选定时间；求解器创建的模型对象可能是必要依赖。</td></tr><tr><td>输出路径找不到</td><td>检查 postProcessing/实例名/起始时刻，部分函数对象把场写入常规时间目录。</td></tr><tr><td>统计量定义不一致</td><td>明确面积/体积/时间加权，检查 fields、operation 与 base 的含义。</td></tr></tbody></table><p class="figure-source">配置来源：<a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials">OpenFOAM v2512 教程</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0-or-later</a>。</p>
