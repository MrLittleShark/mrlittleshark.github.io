---
title: "system/controlDict → functions → solverInfo · solverInfo"
layout: reference
description: "记录线性求解器类型、初始/最终残差、迭代次数与收敛标记。v2512 使用 solverInfo；旧资料中的 type residuals 不能作为本版本的默认配置照抄。"
dictionary: true
---
{% raw %}
<div class="source-note">适用版本：OpenCFD OpenFOAM v2512。示例逐字提取自固定版本源码，未宣称本页每个算例均已完整运行。配置文件是算例的一部分，不能脱离网格、模型、初始场与依赖文件单独使用。</div><p>记录线性求解器类型、初始/最终残差、迭代次数与收敛标记。v2512 使用 solverInfo；旧资料中的 type residuals 不能作为本版本的默认配置照抄。</p><figure><img src="/assets/diagrams/reference-7.svg" alt="函数对象配置的数据依赖关系" loading="lazy"><figcaption>配置关系示意图。箭头表示准备与检查顺序，不表示求解器对所有文件采用固定读取顺序。</figcaption></figure><h2>配置原理与基础示例</h2><h3>残差记录属于求解过程</h3><p>solverInfo 读取 mesh 中的 solverPerformance 数据，必须在实际方程求解时执行。对已经写出的 U 和 p 单独运行后处理，不能重建过去每一步的线性求解历史。初始残差、最终残差与连续性误差是不同指标，需要分别监测。</p><pre><code class="language-openfoam">functions
{
    linearSolverHistory
    {
        type solverInfo;
        libs (utilityFunctionObjects);
        fields (p U);
        writeResidualFields false;
        executeControl timeStep;
        executeInterval 1;
        writeControl timeStep;
        writeInterval 1;
    }
}</code></pre><p>上例为依据 v2512 solverInfo.H 整理的教学配置。writeResidualFields 控制是否额外写出初始残差场，会增加输出开销。向量各分量与总体守恒需要结合检查。</p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/utilities/solverInfo/solverInfo.H">查看类型注册、必需参数与默认值</a></p><h2>从真实配置理解关键条目</h2><div class="table-scroll"><table><thead><tr><th>条目</th><th>含义与使用条件</th></tr></thead><tbody><tr><td>fields</td><td>目标场列表。场名、数据类型和计算时刻必须满足相应函数对象的要求。</td></tr><tr><td>writeControl</td><td>输出触发方式，其值决定 writeInterval 表示步数、物理时间或时钟时间。</td></tr></tbody></table></div><h2>v2512 完整示例与对照</h2><p>共选取 3 份不同配置，保留文件头、注释和 include 指令。相对路径引用的文件仍需从对应教程目录取得。对照时先比较 application、模型名称和字段，再比较数值参数。</p><h3>示例 1 · incompressible/pimpleFoam/laminar/planarPoiseuille/setups.orig/common</h3><p>原始路径：<code>tutorials/incompressible/pimpleFoam/laminar/planarPoiseuille/setups.orig/common/system/solverInfo</code>；求解器：<code>pimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/planarPoiseuille/setups.orig/common/system/solverInfo">查看固定版本源码</a> · <a href="/assets/examples/v2512/solverinfo/1-solverInfo.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/incompressible/pimpleFoam/laminar/planarPoiseuille/setups.orig/common">查看配套目录</a></p><pre><code class="language-openfoam">// -*- C++ -*-

#includeEtc &quot;caseDicts/postProcessing/numerical/solverInfo.cfg&quot;

fields      ( p );


// ************************************************************************* //</code></pre><p>本例包含外部引用：&quot;caseDicts/postProcessing/numerical/solverInfo.cfg&quot;。下载单个文件不会自动取得这些依赖。</p><h3>示例 2 · compressible/rhoSimpleFoam/aerofoilNACA0012</h3><p>原始路径：<code>tutorials/compressible/rhoSimpleFoam/aerofoilNACA0012/system/solverInfo</code>；求解器：<code>rhoSimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/compressible/rhoSimpleFoam/aerofoilNACA0012/system/solverInfo">查看固定版本源码</a> · <a href="/assets/examples/v2512/solverinfo/2-solverInfo.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/compressible/rhoSimpleFoam/aerofoilNACA0012">查看配套目录</a></p><pre><code class="language-openfoam">// -*- C++ -*-

#includeEtc &quot;caseDicts/postProcessing/numerical/solverInfo.cfg&quot;

fields      ( p U e k omega );


// ************************************************************************* //</code></pre><p>本例包含外部引用：&quot;caseDicts/postProcessing/numerical/solverInfo.cfg&quot;。下载单个文件不会自动取得这些依赖。</p><h3>示例 3 · heatTransfer/buoyantBoussinesqPimpleFoam/BenardCells</h3><p>原始路径：<code>tutorials/heatTransfer/buoyantBoussinesqPimpleFoam/BenardCells/system/solverInfo</code>；求解器：<code>buoyantBoussinesqPimpleFoam</code></p><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/tutorials/heatTransfer/buoyantBoussinesqPimpleFoam/BenardCells/system/solverInfo">查看固定版本源码</a> · <a href="/assets/examples/v2512/solverinfo/3-solverInfo.txt">下载完整配置</a> · <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/tutorials/heatTransfer/buoyantBoussinesqPimpleFoam/BenardCells">查看配套目录</a></p><pre><code class="language-openfoam">// -*- C++ -*-

#includeEtc &quot;caseDicts/postProcessing/numerical/solverInfo.cfg&quot;

writeControl writeTime;

fields      (p_rgh);

writeFields yes;


// ************************************************************************* //</code></pre><p>本例包含外部引用：&quot;caseDicts/postProcessing/numerical/solverInfo.cfg&quot;。下载单个文件不会自动取得这些依赖。</p><h2>配套命令与验证次序</h2><p><a href="/commands/icofoam/">icoFoam</a> · <a href="/commands/simplefoam/">simpleFoam</a></p><pre><code class="language-bash"># 在完整算例目录中检查；解析成功不等于模型和物理设置正确
printf &#x27;%s\n&#x27; &quot;&#36;WM_PROJECT_VERSION&quot;
foamDictionary &quot;system/solverInfo&quot; -keywords
# 如包含 #codeStream / #calc，展开时可能编译或执行算例代码；先阅读其内容
# foamDictionary &quot;system/solverInfo&quot; -expand</code></pre><div class="table-scroll"><table><thead><tr><th>现象</th><th>检查方法</th></tr></thead><tbody><tr><td>函数对象未执行</td><td>核对 libs、type、enabled、executeControl 与选定时间；求解器创建的模型对象可能是必要依赖。</td></tr><tr><td>输出路径找不到</td><td>检查 postProcessing/实例名/起始时刻，部分函数对象把场写入常规时间目录。</td></tr><tr><td>统计量定义不一致</td><td>明确面积/体积/时间加权，检查 fields、operation 与 base 的含义。</td></tr></tbody></table></div><h2>来源与许可</h2><p>本页完整源码示例来自 <a href="https://gitlab.com/openfoam/core/openfoam/-/tree/OpenFOAM-v2512/">OpenFOAM-v2512 官方标签</a>，保留原文件版权头，适用 <a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/COPYING">GPL-3.0 或更新版本许可</a>。图示为本站绘制，配置解释由本站整理。安装缺失的模块、模型或库需单独核对。</p>
{% endraw %}
