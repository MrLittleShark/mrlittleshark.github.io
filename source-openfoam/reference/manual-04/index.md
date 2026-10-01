---
title: "04 求解器与并行计算"
layout: "reference"
description: "OpenFOAM v2512 命令、文件与配置参考"
manual: 1
---
{% raw %}
<p class="source-note">资料来源：OpenFOAM_v2512命令与配置参考手册（GPT整理）.docx。网页版已对部分表述作技术性修订，原文可在资料页下载。命令选项以本机 v2512 的 <code>-help</code> 为准。核心模板工具使用 <code>foamGetDict</code>；版本差异与安装步骤需结合官方说明核对。</p><p>求解前完成初始场设置；并行计算还需进行网格分区。随后启动与物理模型对应的求解器，并通过日志监测迭代过程。controlDict 中的 application 供运行脚本选择程序，终端直接调用时执行指定的求解器。</p>
<h3>4.1 作业启动与并行工具</h3>
<h4>foamJob  启动后台计算并记录日志  源码</h4>
<p>默认日志名为 log。-parallel 启用 MPI，-screen 同时输出至终端，-wait 等待计算结束。</p>
<p>用法：foamJob [选项] 应用 [应用参数]</p>
<pre><code>示例：foamJob -log-app simpleFoam</code></pre>
<h4>foamEndJob  通过 stopAt 结束算例计算  源码</h4>
<p>需启用 runTimeModifiable。默认在下一写出时刻结束，-now 请求立即写出并结束；PID 使用实际进程号。</p>
<p>用法：foamEndJob [-case 目录] [-now] PID</p>
<pre><code>示例：foamEndJob -case . -now 12345</code></pre>
<h4>foamCheckJobs  检查作业记录及运行锁状态  源码</h4>
<p>通过 FOAM_JOB_DIR 中的作业记录检查状态，访问远程主机时使用 SSH。</p>
<p>用法：foamCheckJobs [状态输出文件]</p>
<pre><code>示例：foamCheckJobs jobState</code></pre>
<h4>foamPrintJobs  输出 OpenFOAM 作业记录  源码</h4>
<p>与 foamCheckJobs 配合使用。</p>
<p>用法：foamPrintJobs [状态文件]</p>
<pre><code>示例：foamPrintJobs jobState</code></pre>
<h4>mpirunDebug  记录 MPI 分进程日志或启动调试  源码</h4>
<p>计算前完成分区。图形调试模式需配置 xterm 及对应调试器。</p>
<p>用法：mpirunDebug [选项] -np N 程序 参数</p>
<pre><code>示例：mpirunDebug -log -np 4 simpleFoam -parallel</code></pre>
<h4>decomposePar  将网格和场分解为并行子域  源码</h4>
<p>读取 decomposeParDict，-force 替换已有 processor 目录。</p>
<p>用法：decomposePar [选项]</p>
<pre><code>示例：decomposePar</code></pre>
<h4>reconstructPar  将并行场重构为串行结果  源码</h4>
<p>-fields 指定场。动网格结果按需先重构网格。</p>
<p>用法：reconstructPar [选项]</p>
<pre><code>示例：reconstructPar -latestTime</code></pre>
<h4>reconstructParMesh  重构分区网格及处理器寻址  源码</h4>
<p>用于并行网格生成后的主网格及寻址重构。</p>
<p>用法：reconstructParMesh [选项]</p>
<pre><code>示例：reconstructParMesh -constant</code></pre>
<h4>redistributePar  并行重分区或重构网格和场  源码</h4>
<p>修改 decomposeParDict 后执行重分配，MPI 进程数取源分区数与目标分区数的较大值。</p>
<p>用法：redistributePar [选项]</p>
<pre><code>示例：mpirun -np 8 redistributePar -parallel -overwrite</code></pre>
<p>MPI 程序采用 mpirun -np N 应用 -parallel 启动，其中 N 为进程数。例如，执行 mpirun -np 4 pimpleFoam -parallel 前，将 numberOfSubdomains 设为 4，并运行 decomposePar。</p>
<h3>4.2 求解器功能与调用方法</h3>
<p>v2512 的 applications/solvers 目录包含以下 108 个求解器目标。示例均在已配置的对应算例目录中执行。支持 -postProcess 的求解器可加载物理模型后执行相关后处理。</p>
<h4>直接数值模拟</h4>
<p>dnsFoam  各向同性湍流盒直接数值模拟  源码</p>
<pre><code>用法：dnsFoam [-case 目录] [该程序支持的选项]
示例：dnsFoam &gt; log.dnsFoam 2&gt;&amp;1</code></pre>
<h4>声学</h4>
<p>acousticFoam  声压波动方程  源码</p>
<pre><code>用法：acousticFoam [-case 目录] [该程序支持的选项]
示例：acousticFoam &gt; log.acousticFoam 2&gt;&amp;1</code></pre>
<h4>基础方程</h4>
<p>laplacianFoam  标量扩散方程，例如固体热扩散  源码</p>
<pre><code>用法：laplacianFoam [-case 目录] [该程序支持的选项]
示例：laplacianFoam &gt; log.laplacianFoam 2&gt;&amp;1</code></pre>
<p>overLaplacianDyMFoam  支持重叠动网格的标量扩散  源码</p>
<pre><code>用法：overLaplacianDyMFoam [-case 目录] [该程序支持的选项]
示例：overLaplacianDyMFoam &gt; log.overLaplacianDyMFoam 2&gt;&amp;1</code></pre>
<p>potentialFoam  势流初始化，通过势函数构建通量和速度  源码</p>
<pre><code>用法：potentialFoam [-case 目录] [该程序支持的选项]
示例：potentialFoam &gt; log.potentialFoam 2&gt;&amp;1</code></pre>
<p>overPotentialFoam  重叠网格势流初始化  源码</p>
<pre><code>用法：overPotentialFoam [-case 目录] [该程序支持的选项]
示例：overPotentialFoam &gt; log.overPotentialFoam 2&gt;&amp;1</code></pre>
<p>scalarTransportFoam  给定速度场上的被动标量输运  源码</p>
<pre><code>用法：scalarTransportFoam [-case 目录] [该程序支持的选项]
示例：scalarTransportFoam &gt; log.scalarTransportFoam 2&gt;&amp;1</code></pre>
<h4>燃烧与反应</h4>
<p>PDRFoam  带亚网格阻塞处理的可压缩预混或部分预混燃烧  源码</p>
<pre><code>用法：PDRFoam [-case 目录] [该程序支持的选项]
示例：PDRFoam &gt; log.PDRFoam 2&gt;&amp;1</code></pre>
<p>XiFoam  采用 b Xi 模型的可压缩预混或部分预混燃烧  源码</p>
<pre><code>用法：XiFoam [-case 目录] [该程序支持的选项]
示例：XiFoam &gt; log.XiFoam 2&gt;&amp;1</code></pre>
<p>XiDyMFoam  支持动网格的 Xi 燃烧求解  源码</p>
<pre><code>用法：XiDyMFoam [-case 目录] [该程序支持的选项]
示例：XiDyMFoam &gt; log.XiDyMFoam 2&gt;&amp;1</code></pre>
<p>XiEngineFoam  内燃机预混燃烧  源码</p>
<pre><code>用法：XiEngineFoam [-case 目录] [该程序支持的选项]
示例：XiEngineFoam &gt; log.XiEngineFoam 2&gt;&amp;1</code></pre>
<p>chemFoam  单单元化学反应积分与机理测试  源码</p>
<pre><code>用法：chemFoam [-case 目录] [该程序支持的选项]
示例：chemFoam &gt; log.chemFoam 2&gt;&amp;1</code></pre>
<p>coldEngineFoam  内燃机无燃烧冷流  源码</p>
<pre><code>用法：coldEngineFoam [-case 目录] [该程序支持的选项]
示例：coldEngineFoam &gt; log.coldEngineFoam 2&gt;&amp;1</code></pre>
<p>fireFoam  非稳态火灾、扩散火焰及粒子、液膜、热解耦合  源码</p>
<pre><code>用法：fireFoam [-case 目录] [该程序支持的选项]
示例：fireFoam &gt; log.fireFoam 2&gt;&amp;1</code></pre>
<p>reactingFoam  可压缩化学反应流  源码</p>
<pre><code>用法：reactingFoam [-case 目录] [该程序支持的选项]
示例：reactingFoam &gt; log.reactingFoam 2&gt;&amp;1</code></pre>
<p>rhoReactingBuoyantFoam  采用密度热物性并加强浮力处理的反应流  源码</p>
<pre><code>用法：rhoReactingBuoyantFoam [-case 目录] [该程序支持的选项]
示例：rhoReactingBuoyantFoam &gt; log.rhoReactingBuoyantFoam 2&gt;&amp;1</code></pre>
<p>rhoReactingFoam  采用密度热物性模型的反应流  源码</p>
<pre><code>用法：rhoReactingFoam [-case 目录] [该程序支持的选项]
示例：rhoReactingFoam &gt; log.rhoReactingFoam 2&gt;&amp;1</code></pre>
<h4>可压缩流</h4>
<p>rhoCentralFoam  基于中心迎风格式的密度基可压缩流  源码</p>
<pre><code>用法：rhoCentralFoam [-case 目录] [该程序支持的选项]
示例：rhoCentralFoam &gt; log.rhoCentralFoam 2&gt;&amp;1</code></pre>
<p>rhoPimpleAdiabaticFoam  低马赫数声学应用中的弱可压缩绝热流动  源码</p>
<pre><code>用法：rhoPimpleAdiabaticFoam [-case 目录] [该程序支持的选项]
示例：rhoPimpleAdiabaticFoam &gt; log.rhoPimpleAdiabaticFoam 2&gt;&amp;1</code></pre>
<p>rhoPimpleFoam  采用 PIMPLE 的非稳态可压缩流  源码</p>
<pre><code>用法：rhoPimpleFoam [-case 目录] [该程序支持的选项]
示例：rhoPimpleFoam &gt; log.rhoPimpleFoam 2&gt;&amp;1</code></pre>
<p>overRhoPimpleDyMFoam  支持重叠动网格的非稳态可压缩流  源码</p>
<pre><code>用法：overRhoPimpleDyMFoam [-case 目录] [该程序支持的选项]
示例：overRhoPimpleDyMFoam &gt; log.overRhoPimpleDyMFoam 2&gt;&amp;1</code></pre>
<p>rhoSimpleFoam  稳态可压缩湍流  源码</p>
<pre><code>用法：rhoSimpleFoam [-case 目录] [该程序支持的选项]
示例：rhoSimpleFoam &gt; log.rhoSimpleFoam 2&gt;&amp;1</code></pre>
<p>overRhoSimpleFoam  重叠网格稳态可压缩湍流  源码</p>
<pre><code>用法：overRhoSimpleFoam [-case 目录] [该程序支持的选项]
示例：overRhoSimpleFoam &gt; log.overRhoSimpleFoam 2&gt;&amp;1</code></pre>
<p>rhoPorousSimpleFoam  含多孔阻力的稳态可压缩流  源码</p>
<pre><code>用法：rhoPorousSimpleFoam [-case 目录] [该程序支持的选项]
示例：rhoPorousSimpleFoam &gt; log.rhoPorousSimpleFoam 2&gt;&amp;1</code></pre>
<p>sonicFoam  跨声速或超声速可压缩气体非稳态流动  源码</p>
<pre><code>用法：sonicFoam [-case 目录] [该程序支持的选项]
示例：sonicFoam &gt; log.sonicFoam 2&gt;&amp;1</code></pre>
<p>sonicDyMFoam  支持网格运动的跨声速或超声速气体流动  源码</p>
<pre><code>用法：sonicDyMFoam [-case 目录] [该程序支持的选项]
示例：sonicDyMFoam &gt; log.sonicDyMFoam 2&gt;&amp;1</code></pre>
<p>sonicLiquidFoam  可压缩液体跨声速或超声速层流  源码</p>
<pre><code>用法：sonicLiquidFoam [-case 目录] [该程序支持的选项]
示例：sonicLiquidFoam &gt; log.sonicLiquidFoam 2&gt;&amp;1</code></pre>
<h4>离散方法</h4>
<p>dsmcFoam  多组分稀薄气体直接模拟蒙特卡洛  源码</p>
<pre><code>用法：dsmcFoam [-case 目录] [该程序支持的选项]
示例：dsmcFoam &gt; log.dsmcFoam 2&gt;&amp;1</code></pre>
<p>mdEquilibrationFoam  分子动力学系统平衡和预处理  源码</p>
<pre><code>用法：mdEquilibrationFoam [-case 目录] [该程序支持的选项]
示例：mdEquilibrationFoam &gt; log.mdEquilibrationFoam 2&gt;&amp;1</code></pre>
<p>mdFoam  流体分子动力学  源码</p>
<pre><code>用法：mdFoam [-case 目录] [该程序支持的选项]
示例：mdFoam &gt; log.mdFoam 2&gt;&amp;1</code></pre>
<h4>电磁场</h4>
<p>electrostaticFoam  静电场  源码</p>
<pre><code>用法：electrostaticFoam [-case 目录] [该程序支持的选项]
示例：electrostaticFoam &gt; log.electrostaticFoam 2&gt;&amp;1</code></pre>
<p>magneticFoam  永磁体磁场及相关磁力场  源码</p>
<pre><code>用法：magneticFoam [-case 目录] [该程序支持的选项]
示例：magneticFoam &gt; log.magneticFoam 2&gt;&amp;1</code></pre>
<p>mhdFoam  磁场作用下导电流体的不可压缩层流  源码</p>
<pre><code>用法：mhdFoam [-case 目录] [该程序支持的选项]
示例：mhdFoam &gt; log.mhdFoam 2&gt;&amp;1</code></pre>
<h4>金融方程示例</h4>
<p>financialFoam  Black Scholes 方程金融定价示例  源码</p>
<pre><code>用法：financialFoam [-case 目录] [该程序支持的选项]
示例：financialFoam &gt; log.financialFoam 2&gt;&amp;1</code></pre>
<h4>有限面积</h4>
<p>liquidFilmFoam  有限面积液膜层流  源码</p>
<pre><code>用法：liquidFilmFoam [-case 目录] [该程序支持的选项]
示例：liquidFilmFoam &gt; log.liquidFilmFoam 2&gt;&amp;1</code></pre>
<p>sphereSurfactantFoam  球面被动标量输运  源码</p>
<pre><code>用法：sphereSurfactantFoam [-case 目录] [该程序支持的选项]
示例：sphereSurfactantFoam &gt; log.sphereSurfactantFoam 2&gt;&amp;1</code></pre>
<p>surfactantFoam  有限面积被动标量输运  源码</p>
<pre><code>用法：surfactantFoam [-case 目录] [该程序支持的选项]
示例：surfactantFoam &gt; log.surfactantFoam 2&gt;&amp;1</code></pre>
<h4>传热</h4>
<p>buoyantBoussinesqPimpleFoam  采用 Boussinesq 近似的非稳态浮力流  源码</p>
<pre><code>用法：buoyantBoussinesqPimpleFoam [-case 目录] [该程序支持的选项]
示例：buoyantBoussinesqPimpleFoam &gt; log.buoyantBoussinesqPimpleFoam 2&gt;&amp;1</code></pre>
<p>buoyantBoussinesqSimpleFoam  采用 Boussinesq 近似的稳态浮力流  源码</p>
<pre><code>用法：buoyantBoussinesqSimpleFoam [-case 目录] [该程序支持的选项]
示例：buoyantBoussinesqSimpleFoam &gt; log.buoyantBoussinesqSimpleFoam 2&gt;&amp;1</code></pre>
<p>buoyantPimpleFoam  非稳态可压缩浮力与传热  源码</p>
<pre><code>用法：buoyantPimpleFoam [-case 目录] [该程序支持的选项]
示例：buoyantPimpleFoam &gt; log.buoyantPimpleFoam 2&gt;&amp;1</code></pre>
<p>overBuoyantPimpleDyMFoam  重叠动网格浮力与传热  源码</p>
<pre><code>用法：overBuoyantPimpleDyMFoam [-case 目录] [该程序支持的选项]
示例：overBuoyantPimpleDyMFoam &gt; log.overBuoyantPimpleDyMFoam 2&gt;&amp;1</code></pre>
<p>buoyantSimpleFoam  稳态可压缩浮力与传热，可含辐射  源码</p>
<pre><code>用法：buoyantSimpleFoam [-case 目录] [该程序支持的选项]
示例：buoyantSimpleFoam &gt; log.buoyantSimpleFoam 2&gt;&amp;1</code></pre>
<p>chtMultiRegionFoam  非稳态多区域流固共轭传热  源码</p>
<pre><code>用法：chtMultiRegionFoam [-case 目录] [该程序支持的选项]
示例：chtMultiRegionFoam &gt; log.chtMultiRegionFoam 2&gt;&amp;1</code></pre>
<p>chtMultiRegionSimpleFoam  稳态多区域流固共轭传热  源码</p>
<pre><code>用法：chtMultiRegionSimpleFoam [-case 目录] [该程序支持的选项]
示例：chtMultiRegionSimpleFoam &gt; log.chtMultiRegionSimpleFoam 2&gt;&amp;1</code></pre>
<p>chtMultiRegionTwoPhaseEulerFoam  流体区采用两相 Euler 模型的共轭传热  源码</p>
<pre><code>用法：chtMultiRegionTwoPhaseEulerFoam [-case 目录] [该程序支持的选项]
示例：chtMultiRegionTwoPhaseEulerFoam &gt; log.chtMultiRegionTwoPhaseEulerFoam 2&gt;&amp;1</code></pre>
<p>solidFoam  固体能量输运与热物性  源码</p>
<pre><code>用法：solidFoam [-case 目录] [该程序支持的选项]
示例：solidFoam &gt; log.solidFoam 2&gt;&amp;1</code></pre>
<p>thermoFoam  冻结流场上的能量与热物性求解  源码</p>
<pre><code>用法：thermoFoam [-case 目录] [该程序支持的选项]
示例：thermoFoam &gt; log.thermoFoam 2&gt;&amp;1</code></pre>
<h4>不可压缩流</h4>
<p>adjointOptimisationFoam  伴随形状或拓扑优化循环  源码</p>
<pre><code>用法：adjointOptimisationFoam [-case 目录] [该程序支持的选项]
示例：adjointOptimisationFoam &gt; log.adjointOptimisationFoam 2&gt;&amp;1</code></pre>
<p>adjointShapeOptimizationFoam  基于伴随阻塞方法的稳态流道优化  源码</p>
<pre><code>用法：adjointShapeOptimizationFoam [-case 目录] [该程序支持的选项]
示例：adjointShapeOptimizationFoam &gt; log.adjointShapeOptimizationFoam 2&gt;&amp;1</code></pre>
<p>boundaryFoam  一维稳态湍流边界层与入口剖面  源码</p>
<pre><code>用法：boundaryFoam [-case 目录] [该程序支持的选项]
示例：boundaryFoam &gt; log.boundaryFoam 2&gt;&amp;1</code></pre>
<p>icoFoam  采用 PISO 的非稳态不可压缩牛顿层流  源码</p>
<pre><code>用法：icoFoam [-case 目录] [该程序支持的选项]
示例：icoFoam &gt; log.icoFoam 2&gt;&amp;1</code></pre>
<p>nonNewtonianIcoFoam  非牛顿不可压缩层流  源码</p>
<pre><code>用法：nonNewtonianIcoFoam [-case 目录] [该程序支持的选项]
示例：nonNewtonianIcoFoam &gt; log.nonNewtonianIcoFoam 2&gt;&amp;1</code></pre>
<p>pimpleFoam  采用 PIMPLE 的非稳态不可压缩流  源码</p>
<pre><code>用法：pimpleFoam [-case 目录] [该程序支持的选项]
示例：pimpleFoam &gt; log.pimpleFoam 2&gt;&amp;1</code></pre>
<p>SRFPimpleFoam  单旋转参考系非稳态不可压缩流  源码</p>
<pre><code>用法：SRFPimpleFoam [-case 目录] [该程序支持的选项]
示例：SRFPimpleFoam &gt; log.SRFPimpleFoam 2&gt;&amp;1</code></pre>
<p>overPimpleDyMFoam  重叠动网格非稳态不可压缩流  源码</p>
<pre><code>用法：overPimpleDyMFoam [-case 目录] [该程序支持的选项]
示例：overPimpleDyMFoam &gt; log.overPimpleDyMFoam 2&gt;&amp;1</code></pre>
<p>pisoFoam  采用 PISO 的非稳态不可压缩流  源码</p>
<pre><code>用法：pisoFoam [-case 目录] [该程序支持的选项]
示例：pisoFoam &gt; log.pisoFoam 2&gt;&amp;1</code></pre>
<p>shallowWaterFoam  浅水方程  源码</p>
<pre><code>用法：shallowWaterFoam [-case 目录] [该程序支持的选项]
示例：shallowWaterFoam &gt; log.shallowWaterFoam 2&gt;&amp;1</code></pre>
<p>simpleFoam  采用 SIMPLE 的稳态不可压缩流  源码</p>
<pre><code>用法：simpleFoam [-case 目录] [该程序支持的选项]
示例：simpleFoam &gt; log.simpleFoam 2&gt;&amp;1</code></pre>
<p>SRFSimpleFoam  单旋转参考系稳态不可压缩流  源码</p>
<pre><code>用法：SRFSimpleFoam [-case 目录] [该程序支持的选项]
示例：SRFSimpleFoam &gt; log.SRFSimpleFoam 2&gt;&amp;1</code></pre>
<p>overSimpleFoam  重叠网格稳态不可压缩流  源码</p>
<pre><code>用法：overSimpleFoam [-case 目录] [该程序支持的选项]
示例：overSimpleFoam &gt; log.overSimpleFoam 2&gt;&amp;1</code></pre>
<p>porousSimpleFoam  含多孔介质阻力的稳态不可压缩流  源码</p>
<pre><code>用法：porousSimpleFoam [-case 目录] [该程序支持的选项]
示例：porousSimpleFoam &gt; log.porousSimpleFoam 2&gt;&amp;1</code></pre>
<h4>粒子与喷雾</h4>
<p>MPPICDyMFoam  支持动网格的多相颗粒网格法稠密粒子流  源码</p>
<pre><code>用法：MPPICDyMFoam [-case 目录] [该程序支持的选项]
示例：MPPICDyMFoam &gt; log.MPPICDyMFoam 2&gt;&amp;1</code></pre>
<p>DPMDyMFoam  支持动网格的离散粒子与连续相耦合  源码</p>
<pre><code>用法：DPMDyMFoam [-case 目录] [该程序支持的选项]
示例：DPMDyMFoam &gt; log.DPMDyMFoam 2&gt;&amp;1</code></pre>
<p>MPPICFoam  采用 MPPIC 碰撞处理的稠密粒子流  源码</p>
<pre><code>用法：MPPICFoam [-case 目录] [该程序支持的选项]
示例：MPPICFoam &gt; log.MPPICFoam 2&gt;&amp;1</code></pre>
<p>DPMFoam  考虑颗粒体积分数影响的离散粒子耦合流  源码</p>
<pre><code>用法：DPMFoam [-case 目录] [该程序支持的选项]
示例：DPMFoam &gt; log.DPMFoam 2&gt;&amp;1</code></pre>
<p>coalChemistryFoam  煤粒反应与连续相化学反应耦合  源码</p>
<pre><code>用法：coalChemistryFoam [-case 目录] [该程序支持的选项]
示例：coalChemistryFoam &gt; log.coalChemistryFoam 2&gt;&amp;1</code></pre>
<p>icoUncoupledKinematicParcelFoam  预计算速度场上的非耦合运动学粒子输运  源码</p>
<pre><code>用法：icoUncoupledKinematicParcelFoam [-case 目录] [该程序支持的选项]
示例：icoUncoupledKinematicParcelFoam &gt; log.icoUncoupledKinematicParcelFoam 2&gt;&amp;1</code></pre>
<p>icoUncoupledKinematicParcelDyMFoam  动网格上的非耦合运动学粒子输运  源码</p>
<pre><code>用法：icoUncoupledKinematicParcelDyMFoam [-case 目录] [该程序支持的选项]
示例：icoUncoupledKinematicParcelDyMFoam &gt; log.icoUncoupledKinematicParcelDyMFoam 2&gt;&amp;1</code></pre>
<p>kinematicParcelFoam  不可压缩湍流与运动学粒子云及液膜  源码</p>
<pre><code>用法：kinematicParcelFoam [-case 目录] [该程序支持的选项]
示例：kinematicParcelFoam &gt; log.kinematicParcelFoam 2&gt;&amp;1</code></pre>
<p>reactingParcelFoam  可压缩湍流与反应多相粒子云及液膜  源码</p>
<pre><code>用法：reactingParcelFoam [-case 目录] [该程序支持的选项]
示例：reactingParcelFoam &gt; log.reactingParcelFoam 2&gt;&amp;1</code></pre>
<p>reactingHeterogenousParcelFoam  异相反应粒子云与连续相耦合  源码</p>
<pre><code>用法：reactingHeterogenousParcelFoam [-case 目录] [该程序支持的选项]
示例：reactingHeterogenousParcelFoam &gt; log.reactingHeterogenousParcelFoam 2&gt;&amp;1</code></pre>
<p>simpleReactingParcelFoam  稳态可压缩反应粒子流  源码</p>
<pre><code>用法：simpleReactingParcelFoam [-case 目录] [该程序支持的选项]
示例：simpleReactingParcelFoam &gt; log.simpleReactingParcelFoam 2&gt;&amp;1</code></pre>
<p>simpleCoalParcelFoam  稳态可压缩煤粒流  源码</p>
<pre><code>用法：simpleCoalParcelFoam [-case 目录] [该程序支持的选项]
示例：simpleCoalParcelFoam &gt; log.simpleCoalParcelFoam 2&gt;&amp;1</code></pre>
<p>sprayFoam  非稳态可压缩喷雾  源码</p>
<pre><code>用法：sprayFoam [-case 目录] [该程序支持的选项]
示例：sprayFoam &gt; log.sprayFoam 2&gt;&amp;1</code></pre>
<p>engineFoam  含喷雾的可压缩发动机流动  源码</p>
<pre><code>用法：engineFoam [-case 目录] [该程序支持的选项]
示例：engineFoam &gt; log.engineFoam 2&gt;&amp;1</code></pre>
<p>simpleSprayFoam  稳态可压缩喷雾  源码</p>
<pre><code>用法：simpleSprayFoam [-case 目录] [该程序支持的选项]
示例：simpleSprayFoam &gt; log.simpleSprayFoam 2&gt;&amp;1</code></pre>
<p>sprayDyMFoam  支持动网格的可压缩喷雾  源码</p>
<pre><code>用法：sprayDyMFoam [-case 目录] [该程序支持的选项]
示例：sprayDyMFoam &gt; log.sprayDyMFoam 2&gt;&amp;1</code></pre>
<p>uncoupledKinematicParcelFoam  给定流场上的非耦合粒子输运  源码</p>
<pre><code>用法：uncoupledKinematicParcelFoam [-case 目录] [该程序支持的选项]
示例：uncoupledKinematicParcelFoam &gt; log.uncoupledKinematicParcelFoam 2&gt;&amp;1</code></pre>
<p>uncoupledKinematicParcelDyMFoam  支持动网格的给定流场粒子输运  源码</p>
<pre><code>用法：uncoupledKinematicParcelDyMFoam [-case 目录] [该程序支持的选项]
示例：uncoupledKinematicParcelDyMFoam &gt; log.uncoupledKinematicParcelDyMFoam 2&gt;&amp;1</code></pre>
<h4>多相流</h4>
<p>MPPICInterFoam  两相 VOF 自由界面与 MPPIC 粒子耦合  源码</p>
<pre><code>用法：MPPICInterFoam [-case 目录] [该程序支持的选项]
示例：MPPICInterFoam &gt; log.MPPICInterFoam 2&gt;&amp;1</code></pre>
<p>cavitatingFoam  均相平衡可压缩混合物空化  源码</p>
<pre><code>用法：cavitatingFoam [-case 目录] [该程序支持的选项]
示例：cavitatingFoam &gt; log.cavitatingFoam 2&gt;&amp;1</code></pre>
<p>cavitatingDyMFoam  支持动网格的均相平衡空化  源码</p>
<pre><code>用法：cavitatingDyMFoam [-case 目录] [该程序支持的选项]
示例：cavitatingDyMFoam &gt; log.cavitatingDyMFoam 2&gt;&amp;1</code></pre>
<p>compressibleInterFoam  两种可压缩非等温不混溶流体 VOF  源码</p>
<pre><code>用法：compressibleInterFoam [-case 目录] [该程序支持的选项]
示例：compressibleInterFoam &gt; log.compressibleInterFoam 2&gt;&amp;1</code></pre>
<p>compressibleInterDyMFoam  支持动网格的两相可压缩 VOF  源码</p>
<pre><code>用法：compressibleInterDyMFoam [-case 目录] [该程序支持的选项]
示例：compressibleInterDyMFoam &gt; log.compressibleInterDyMFoam 2&gt;&amp;1</code></pre>
<p>compressibleInterFilmFoam  可压缩 VOF 与表面液膜耦合  源码</p>
<pre><code>用法：compressibleInterFilmFoam [-case 目录] [该程序支持的选项]
示例：compressibleInterFilmFoam &gt; log.compressibleInterFilmFoam 2&gt;&amp;1</code></pre>
<p>compressibleInterIsoFoam  采用 isoAdvector 的两相可压缩界面捕捉  源码</p>
<pre><code>用法：compressibleInterIsoFoam [-case 目录] [该程序支持的选项]
示例：compressibleInterIsoFoam &gt; log.compressibleInterIsoFoam 2&gt;&amp;1</code></pre>
<p>overCompressibleInterDyMFoam  重叠动网格可压缩两相 VOF  源码</p>
<pre><code>用法：overCompressibleInterDyMFoam [-case 目录] [该程序支持的选项]
示例：overCompressibleInterDyMFoam &gt; log.overCompressibleInterDyMFoam 2&gt;&amp;1</code></pre>
<p>compressibleMultiphaseInterFoam  多种可压缩非等温不混溶流体 VOF  源码</p>
<pre><code>用法：compressibleMultiphaseInterFoam [-case 目录] [该程序支持的选项]
示例：compressibleMultiphaseInterFoam &gt; log.compressibleMultiphaseInterFoam 2&gt;&amp;1</code></pre>
<p>driftFluxFoam  采用漂移通量近似的两相相对运动  源码</p>
<pre><code>用法：driftFluxFoam [-case 目录] [该程序支持的选项]
示例：driftFluxFoam &gt; log.driftFluxFoam 2&gt;&amp;1</code></pre>
<p>icoReactingMultiphaseInterFoam  含相变的不可压缩非等温多相 VOF  源码</p>
<pre><code>用法：icoReactingMultiphaseInterFoam [-case 目录] [该程序支持的选项]
示例：icoReactingMultiphaseInterFoam &gt; log.icoReactingMultiphaseInterFoam 2&gt;&amp;1</code></pre>
<p>interCondensatingEvaporatingFoam  蒸发冷凝两相非等温 VOF  源码</p>
<pre><code>用法：interCondensatingEvaporatingFoam [-case 目录] [该程序支持的选项]
示例：interCondensatingEvaporatingFoam &gt; log.interCondensatingEvaporatingFoam 2&gt;&amp;1</code></pre>
<p>interFoam  两种不可压缩等温不混溶流体 VOF  源码</p>
<pre><code>用法：interFoam [-case 目录] [该程序支持的选项]
示例：interFoam &gt; log.interFoam 2&gt;&amp;1</code></pre>
<p>interMixingFoam  三种不可压缩流体，其中两种可混溶的界面流  源码</p>
<pre><code>用法：interMixingFoam [-case 目录] [该程序支持的选项]
示例：interMixingFoam &gt; log.interMixingFoam 2&gt;&amp;1</code></pre>
<p>overInterDyMFoam  重叠动网格不可压缩两相 VOF  源码</p>
<pre><code>用法：overInterDyMFoam [-case 目录] [该程序支持的选项]
示例：overInterDyMFoam &gt; log.overInterDyMFoam 2&gt;&amp;1</code></pre>
<p>interIsoFoam  采用 isoAdvector 的不可压缩两相界面捕捉  源码</p>
<pre><code>用法：interIsoFoam [-case 目录] [该程序支持的选项]
示例：interIsoFoam &gt; log.interIsoFoam 2&gt;&amp;1</code></pre>
<p>interPhaseChangeFoam  含空化等相变的不可压缩两相 VOF  源码</p>
<pre><code>用法：interPhaseChangeFoam [-case 目录] [该程序支持的选项]
示例：interPhaseChangeFoam &gt; log.interPhaseChangeFoam 2&gt;&amp;1</code></pre>
<p>interPhaseChangeDyMFoam  支持动网格的相变 VOF  源码</p>
<pre><code>用法：interPhaseChangeDyMFoam [-case 目录] [该程序支持的选项]
示例：interPhaseChangeDyMFoam &gt; log.interPhaseChangeDyMFoam 2&gt;&amp;1</code></pre>
<p>overInterPhaseChangeDyMFoam  重叠动网格相变 VOF  源码</p>
<pre><code>用法：overInterPhaseChangeDyMFoam [-case 目录] [该程序支持的选项]
示例：overInterPhaseChangeDyMFoam &gt; log.overInterPhaseChangeDyMFoam 2&gt;&amp;1</code></pre>
<p>multiphaseEulerFoam  包含传热的多相 Euler 流  源码</p>
<pre><code>用法：multiphaseEulerFoam [-case 目录] [该程序支持的选项]
示例：multiphaseEulerFoam &gt; log.multiphaseEulerFoam 2&gt;&amp;1</code></pre>
<p>multiphaseInterFoam  多种不可压缩流体界面捕捉及表面张力  源码</p>
<pre><code>用法：multiphaseInterFoam [-case 目录] [该程序支持的选项]
示例：multiphaseInterFoam &gt; log.multiphaseInterFoam 2&gt;&amp;1</code></pre>
<p>potentialFreeSurfaceFoam  用波高场近似自由表面的单相流  源码</p>
<pre><code>用法：potentialFreeSurfaceFoam [-case 目录] [该程序支持的选项]
示例：potentialFreeSurfaceFoam &gt; log.potentialFreeSurfaceFoam 2&gt;&amp;1</code></pre>
<p>potentialFreeSurfaceDyMFoam  支持动网格的波高自由表面近似  源码</p>
<pre><code>用法：potentialFreeSurfaceDyMFoam [-case 目录] [该程序支持的选项]
示例：potentialFreeSurfaceDyMFoam &gt; log.potentialFreeSurfaceDyMFoam 2&gt;&amp;1</code></pre>
<p>reactingMultiphaseEulerFoam  共享压力的多相 Euler 组分和反应流  源码</p>
<pre><code>用法：reactingMultiphaseEulerFoam [-case 目录] [该程序支持的选项]
示例：reactingMultiphaseEulerFoam &gt; log.reactingMultiphaseEulerFoam 2&gt;&amp;1</code></pre>
<p>reactingTwoPhaseEulerFoam  共享压力的两相 Euler 组分和反应流  源码</p>
<pre><code>用法：reactingTwoPhaseEulerFoam [-case 目录] [该程序支持的选项]
示例：reactingTwoPhaseEulerFoam &gt; log.reactingTwoPhaseEulerFoam 2&gt;&amp;1</code></pre>
<p>twoLiquidMixingFoam  两种不可压缩流体混合  源码</p>
<pre><code>用法：twoLiquidMixingFoam [-case 目录] [该程序支持的选项]
示例：twoLiquidMixingFoam &gt; log.twoLiquidMixingFoam 2&gt;&amp;1</code></pre>
<p>twoPhaseEulerFoam  包含分散相及传热的两相 Euler 流  源码</p>
<pre><code>用法：twoPhaseEulerFoam [-case 目录] [该程序支持的选项]
示例：twoPhaseEulerFoam &gt; log.twoPhaseEulerFoam 2&gt;&amp;1</code></pre>
<h4>固体应力</h4>
<p>solidDisplacementFoam  非稳态小应变线弹性固体位移及可选热应力  源码</p>
<pre><code>用法：solidDisplacementFoam [-case 目录] [该程序支持的选项]
示例：solidDisplacementFoam &gt; log.solidDisplacementFoam 2&gt;&amp;1</code></pre>
<p>solidEquilibriumDisplacementFoam  稳态小应变线弹性固体平衡及可选热应力  源码</p>
<pre><code>用法：solidEquilibriumDisplacementFoam [-case 目录] [该程序支持的选项]
示例：solidEquilibriumDisplacementFoam &gt; log.solidEquilibriumDisplacementFoam 2&gt;&amp;1</code></pre>
{% endraw %}