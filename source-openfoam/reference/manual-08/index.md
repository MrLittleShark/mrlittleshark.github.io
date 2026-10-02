---
title: "08 时间控制与数值求解设置"
layout: reference
description: "时间控制与数值求解设置：用法与配置实例。"
cms_slug: "reference-manual-08"
---

<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy" src="/assets/diagrams/reference-workflow.svg"/><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><h3>8.1 system/controlDict</h3>
<pre><code class="language-openfoam">FoamFile
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
<tr><td>libs</td><td>加载自定义或功能库</td><td>例如 ("libMyBC.so")</td></tr>
<tr><td>functions</td><td>运行时函数对象</td><td>见第 10 章</td></tr>
</table></div>
<p>Courant 数由局部速度、通量、单元尺寸和时间步共同决定。可压缩激波计算还需考虑声速约束，时间步上限应结合所用求解器和离散格式确定。</p>
<h3>8.2 system/fvSchemes</h3>
<p>下例给出不可压缩非稳态层流的离散设置。采用湍流模型或求解能量方程时，应补充相应方程的对流项。</p>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object fvSchemes;
}
ddtSchemes { default Euler; }
gradSchemes { default Gauss linear; }
divSchemes
{
    default none;
    div(phi,U) Gauss linearUpwind grad(U);
    div((nuEff*dev2(T(grad(U))))) Gauss linear;
}
laplacianSchemes { default Gauss linear corrected; }
interpolationSchemes { default linear; }
snGradSchemes { default corrected; }
wallDist { method meshWave; }</code></pre>
<div class="table-scroll"><table>
<tr><th>字典</th><th>控制对象</th><th>常用设置</th></tr>
<tr><td>ddtSchemes</td><td>时间导数</td><td>Euler 为一阶；backward 为二阶；CrankNicolson 0.9 为混合格式；steadyState 用于稳态</td></tr>
<tr><td>gradSchemes</td><td>梯度</td><td>Gauss linear、leastSquares、cellLimited Gauss linear 1</td></tr>
<tr><td>divSchemes</td><td>对流及显式散度</td><td>Gauss upwind 耗散较强；linearUpwind 阶数较高；limitedLinear 等限制格式按字段类型选择</td></tr>
<tr><td>laplacianSchemes</td><td>扩散项</td><td>常用 Gauss linear corrected；非正交程度较高时可采用 limited 修正</td></tr>
<tr><td>interpolationSchemes</td><td>面插值</td><td>linear 等</td></tr>
<tr><td>snGradSchemes</td><td>面法向梯度</td><td>corrected、uncorrected、limited 0.5 等</td></tr>
<tr><td>fluxRequired</td><td>指定需保留通量的场</td><td>按求解器要求标记 p 等场</td></tr>
<tr><td>wallDist</td><td>壁距算法</td><td>meshWave 等</td></tr>
<tr><td>default none</td><td>无默认格式</td><td>所需离散项必须显式配置，缺失时报告错误</td></tr>
</table></div>
<p>湍流方程可采用 div(phi,k) Gauss upwind; 和 div(phi,omega) Gauss upwind;，字段名称随模型确定。VOF 求解器的 div(phi,alpha)、div(phirb,alpha) 等条目采用其配套教程的定义。rhoCentralFoam 还需设置 fluxScheme 及变量重构格式。</p>
<h3>8.3 system/fvSolution</h3>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object fvSolution;
}
solvers
{
    p
    {
        solver GAMG;
        tolerance 1e-7;
        relTol 0.05;
        smoother GaussSeidel;
    }
    pFinal { $p; relTol 0; }
    U
    {
        solver smoothSolver;
        smoother symGaussSeidel;
        tolerance 1e-8;
        relTol 0;
    }
}
PIMPLE
{
    nOuterCorrectors 2;
    nCorrectors 2;
    nNonOrthogonalCorrectors 0;
    momentumPredictor yes;
    pRefCell 0;
    pRefValue 0;
}
relaxationFactors
{
    equations { U 1; }
}</code></pre>
<div class="table-scroll"><table>
<tr><th>条目</th><th>含义</th><th>设置原则</th></tr>
<tr><td>solver</td><td>线性代数求解器</td><td>PCG 适于相容的对称矩阵；PBiCGStab 可处理非对称矩阵；GAMG 为多重网格</td></tr>
<tr><td>preconditioner</td><td>预条件器</td><td>DIC、DILU 等须与矩阵和 solver 相容</td></tr>
<tr><td>smoother</td><td>平滑器</td><td>如 GaussSeidel、symGaussSeidel、DICGaussSeidel</td></tr>
<tr><td>tolerance</td><td>绝对残差停止阈值</td><td>控制线性方程残差的停止条件</td></tr>
<tr><td>relTol</td><td>相对本次求解初始残差的停止阈值</td><td>0 表示关闭相对阈值，常用于最终校正</td></tr>
<tr><td>minIter、maxIter</td><td>线性迭代上下限</td><td>达到 maxIter 时结合残差判断收敛状态</td></tr>
<tr><td>nSweeps</td><td>每组平滑扫描次数</td><td>仅适用求解器使用</td></tr>
<tr><td>cacheAgglomeration</td><td>缓存 GAMG 聚合</td><td>静态网格可复用聚合结果</td></tr>
<tr><td>nCellsInCoarsestLevel</td><td>GAMG 最粗层目标单元数</td><td>结合并行分区和收敛情况调整</td></tr>
<tr><td>pFinal、UFinal 等</td><td>最后一次校正的专用设置</td><td>是否使用由求解器控制</td></tr>
<tr><td>正则字段名</td><td>共享线性求解配置</td><td>如 "(U|k|omega)"，采用引号包围正则表达式</td></tr>
<tr><td>relaxationFactors/fields</td><td>场松弛</td><td>如稳态 p 0.3</td></tr>
<tr><td>relaxationFactors/equations</td><td>方程松弛</td><td>如稳态 U 0.7；较小因子降低更新幅度</td></tr>
</table></div>
<p>SIMPLE、PISO 和 PIMPLE 分别采用对应的算法子字典。SIMPLE 常用 nNonOrthogonalCorrectors、consistent、residualControl 和 pRefCell/pRefValue；PISO 通过 nCorrectors 控制校正次数；PIMPLE 另设 nOuterCorrectors 控制外迭代。压力方程需要参考值且求解器采用该机制时，设置 pRefCell 和 pRefValue。</p>
<pre><code class="language-plaintext">// SIMPLE 片段：稳态算例
SIMPLE
{
    nNonOrthogonalCorrectors 0;
    residualControl
    {
        p 1e-5;
        U 1e-6;
        "(k|omega)" 1e-6;
    }
}
relaxationFactors
{
    fields { p 0.3; }
    equations { U 0.7; k 0.7; omega 0.7; }
}</code></pre>
<p>residualControl 的结构由算法接口确定，部分 PIMPLE 控制采用 tolerance/relTol 子字典。收敛判定应同时考察残差、质量守恒及力、流量、温度等目标量的稳定性。</p>
<h3>8.4 system/decomposeParDict</h3>
<pre><code class="language-openfoam">FoamFile
{
    version 2.0; format ascii;
    class dictionary; object decomposeParDict;
}
numberOfSubdomains 4;
method scotch;</code></pre>
<p>numberOfSubdomains 指定分区数，与求解阶段 mpirun -np 的进程数一致。scotch 采用图分割，simple 按坐标规则划分，hierarchical 按指定方向依次划分，manual 使用给定的处理器映射，multiLevel 组合多级分解方法。</p>
<pre><code class="language-plaintext">// 用 simple 替换上面的 method 时，加入以下系数
method simple;
simpleCoeffs
{
    n (2 2 1);
    delta 0.001;
}</code></pre>
<p>示例中 n 的三个分量乘积为 4。hierarchicalCoeffs 还通过 order 指定划分顺序，如 xyz。多区域算例可在 regions 子字典中分别设置方法和子域数。constraints 用于保持挡板、面区域及指定连接关系，约束范围同时影响负载均衡。</p>
<h3>8.5 system/renumberMeshDict 与文件处理器</h3>
<p>renumberMethod 指定网格编号算法，如 CuthillMcKee；算法参数置于对应系数字典。运行 renumberMesh -list-renumber 可查询可用方法。重新编号用于调整稀疏矩阵带宽，网格几何分辨率保持不变。</p>
<p>FOAM_FILEHANDLER 设置默认文件处理器，常用值为 uncollated 和 collated；命令行 -fileHandler 可覆盖该设置。collated 通过合并并行 I/O 减少文件数量，其性能取决于文件系统、MPI 和缓冲策略。结果读取及重分配应使用支持该格式的工具。</p>
