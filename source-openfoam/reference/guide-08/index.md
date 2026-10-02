---
title: "第 8 章　后处理命令与 functionObject"
layout: reference
description: "后处理命令与 functionObject：用法与配置实例。"
cms_slug: "reference-guide-08"
---

<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy" src="/assets/diagrams/reference-workflow.svg"/><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><p>后处理有两条路：算完再处理（postProcess 等命令）和边算边处理（controlDict 里的 functionObject）。能用后者就用后者——因为很多量（比如受力时程、探针时间序列）需要每个时间步的数据，而你不可能把每个时间步的整场都写到硬盘上。</p>
<h2>8.1 postProcess —— 通用后处理命令</h2>
<p>用法</p>
<pre><code class="language-bash">postProcess -func &lt;功能名&gt; [-time &lt;范围&gt;] [-latestTime] [-fields '(U p)'] [-noZero] [-parallel]
postProcess -funcs '(func1 func2)'
postProcess -list                    # 列出预配置函数对象入口</code></pre>
<p>示例</p>
<pre><code class="language-bash"># ① 看有哪些功能可用
postProcess -list

# ② 计算速度大小，写成新场 mag(U)
postProcess -func "mag(U)"

# ③ 计算 Q 判据（涡识别），只处理最后一个时刻
postProcess -func Q -latestTime

# ④ 计算涡量
postProcess -func vorticity -time '1:10'

# ⑤ 沿一条线取样（需要 system/singleGraph 配置文件）
postProcess -func singleGraph -latestTime

# ⑥ 求某个边界上的面积分（不用改 controlDict）
postProcess -func "patchAverage(name=outlet, field=p)" -latestTime

# ⑦ 依赖湍流模型的量必须用求解器 + -postProcess
simpleFoam -postProcess -func yPlus -latestTime</code></pre>
<p>函数对象类型与预配置模板名称需要区分。先用 postProcess -list 查询预配置入口；mag、grad、Q、probes、forces 等功能还需要各自的字段和参数。fieldAverage 等类型通常应在 functions 中显式配置。线性求解器历史使用 solverInfo，并在求解时记录。</p>
<h2>8.2 #includeFunc —— 一行开启一个后处理功能</h2>
<p>在 controlDict 的 functions 里，官方模板可以一行引入：</p>
<pre><code class="language-openfoam">functions
{
    #includeFunc solverInfo
    #includeFunc  yPlus
    #includeFunc  Q
    #includeFunc  mag(U)
    #includeFunc  probes
    #includeFunc  patchAverage(name=outlet,fields=(p))
    #includeFunc  flowRatePatch(name=outlet)
    #includeFunc  singleGraph
}</code></pre>
<p>预配置函数来自 etc/caseDicts/postProcessing；#includeFunc 按模板或本地文件展开配置。使用 foamGetDict 复制所需模板后，应明确场名、边界名称和执行/输出频率。postProcess -list 列出预配置入口，不等于所有已编译函数对象类型的全集。</p>
<pre><code class="language-plaintext">ls $FOAM_ETC/caseDicts/postProcessing/*        # 看看有哪些现成模板</code></pre>
<h2>8.3 常用 functionObject 的写法</h2>
<p>写在 system/controlDict 的 functions {} 里（也可以单独放文件再 #include）。所有 functionObject 都有这几个公共关键字：</p>
<div class="table-scroll"><table>
<tr><th>关键字</th><th>含义</th></tr>
<tr><td>type</td><td>功能类型</td></tr>
<tr><td>libs</td><td>需要加载的库，如 ("libfieldFunctionObjects.so")</td></tr>
<tr><td>writeControl</td><td>timeStep / runTime / writeTime / onEnd</td></tr>
<tr><td>writeInterval</td><td>间隔</td></tr>
<tr><td>executeControl / executeInterval</td><td>计算频率（可以算得勤、写得少）</td></tr>
<tr><td>enabled</td><td>true/false，临时关掉某个功能</td></tr>
<tr><td>timeStart / timeEnd</td><td>只在某段时间内工作（如统计平均只从流动充分发展后开始）</td></tr>
</table></div>
<p>① 探针：监测某几个点的时间序列</p>
<pre><code class="language-openfoam">probes
{
    type            probes;
    libs            ("libsampling.so");
    writeControl    timeStep;
    writeInterval   1;
    fields          (p U);
    probeLocations  ( (0.1 0.05 0.005) (0.2 0.05 0.005) );
}</code></pre>
<p>输出在 postProcessing/probes/0/p。用途：看涡脱落频率、判断是否进入统计定常。</p>
<p>② 力与力系数：算阻力升力</p>
<pre><code class="language-openfoam">forceCoeffs
{
    type            forceCoeffs;
    libs            ("libforces.so");
    writeControl    timeStep;
    writeInterval   1;
    patches         (cylinder);       // 作用在哪个边界上
    rho             rhoInf;           // 不可压时写 rhoInf
    rhoInf          1.0;              // 参考密度
    liftDir         (0 1 0);
    dragDir         (1 0 0);
    CofR            (0 0 0);          // 力矩参考点
    pitchAxis       (0 0 1);
    magUInf         1.0;              // 参考速度
    lRef            0.1;              // 参考长度
    Aref            0.001;            // 参考面积
}</code></pre>
<p>forceCoeffs 的输出目录由函数对象实例名和起始时刻决定。使用运动学压力的不可压缩求解器时，应按 forces/forceCoeffs 的接口配置密度引用（常见为 rho rhoInf 与 rhoInf 数值）；如果使用热力学压力或可压缩密度场，则应采用相应处理。还应检查参考面积、参考长度、来流速度与力矩中心。</p>
<p>③ 场平均：LES/URANS 的统计量</p>
<pre><code class="language-openfoam">fieldAverage
{
    type            fieldAverage;
    libs            ("libfieldFunctionObjects.so");
    timeStart       5;                // ★ 等流动充分发展后再开始统计
    writeControl    writeTime;
    fields
    (
        U { mean on; prime2Mean on; base time; }
        p { mean on; prime2Mean on; base time; }
    );
}</code></pre>
<p>得到 UMean、UPrime2Mean（雷诺应力）等。timeStart 不设对，统计里会混入初始瞬态，结果没法用。</p>
<p>④ 沿线取样（画剖面图）</p>
<pre><code class="language-openfoam">singleGraph
{
    type            sets;
    libs            ("libsampling.so");
    writeControl    writeTime;
    setFormat       raw;              // csv / raw / gnuplot
    interpolationScheme cellPoint;
    fields          (U p);
    sets
    (
        line1
        {
            type    uniform;          // 均匀取 N 个点
            axis    distance;         // 横坐标用弧长；也可 x/y/z
            start   (0 -0.025 0.005);
            end     (0  0.025 0.005);
            nPoints 100;
        }
    );
}</code></pre>
<p>输出在 postProcessing/singleGraph/&lt;时间&gt;/line1_U_p.xy，可直接用 gnuplot/Python 画。</p>
<p>⑤ 切面取样（导出面数据给 ParaView 或做面积分）</p>
<pre><code class="language-openfoam">surfaces
{
    type            surfaces;
    libs            ("libsampling.so");
    writeControl    writeTime;
    surfaceFormat   vtk;
    fields          (p U);
    surfaces
    (
        zNormal
        {
            type            cuttingPlane;
            point           (0 0 0.005);
            normal          (0 0 1);
            interpolate     true;
        }
        isoQ
        {
            type            isoSurface;
            isoField        Q;
            isoValue        100;
            interpolate     true;
        }
    );
}</code></pre>
<p>在求解或后处理阶段直接输出所需截面，可减少保存的场数据量。实际节省程度取决于网格规模、输出变量和时间采样频率；仍应保存满足后续验证需要的数据。</p>
<p>⑥ 积分与极值</p>
<pre><code class="language-openfoam">outletFlux
{
    type            surfaceFieldValue;
    libs            ("libfieldFunctionObjects.so");
    regionType      patch;
    name            outlet;
    operation       sum;             // sum/areaAverage/areaIntegrate/min/max/CoV
    fields          (phi);
    writeControl    timeStep;
}
volAvgT
{
    type            volFieldValue;
    libs            ("libfieldFunctionObjects.so");
    regionType      all;             // 或 cellZone + name
    operation       volAverage;
    fields          (T);
    writeControl    timeStep;
}</code></pre>
<p>用途：检查质量守恒（进出口 phi 之和应接近 0）、监测平均温度等全局量随时间的变化。</p>
<p>⑦ 残差与求解器信息</p>
<pre><code class="language-openfoam">#includeFunc solverInfo</code></pre>
<p>或</p>
<pre><code class="language-openfoam">solverInfo
{
    type            solverInfo;
    libs            ("libutilityFunctionObjects.so");
    fields          (U p);
    writeResidualFields yes;         // 把残差也写成场，可在 ParaView 里看"哪儿不收敛"
}</code></pre>
<p>writeResidualFields 可以输出初始残差的空间分布，辅助定位离散误差或局部迭代困难，同时会增加输出量。高残差区域也可能来自启动瞬态或物理源项，需要结合网格、边界和方程分析。</p>
<h2>8.4 foamToVTK / foamToEnsight —— 导出到别的软件</h2>
<pre><code class="language-bash">foamToVTK                                   # 全部时刻导出成 VTK
foamToVTK -latestTime -fields '(U p)'       # 只导最后一个时刻的两个场
foamToVTK -ascii                            # 文本格式，可以直接用编辑器看
foamToVTK -cellSet c0                       # 只导出某个 cellSet
foamToVTK -no-boundary                      # 不导边界数据
foamToEnsight -latestTime                   # 导 EnSight 格式</code></pre>
<p>什么时候需要：给合作者（用 Tecplot/EnSight）传数据，或者自己用 Python（pyvista/vtk）做定制分析时。日常用 ParaView 直接读算例目录即可，不需要转换。</p>
<h2>8.5 ParaView：paraFoam 与 .foam 文件</h2>
<p>两种打开方式</p>
<pre><code class="language-bash">paraFoam                     # 方式一：自动生成临时文件并启动 ParaView
paraFoam -vtk -touch              # 只生成 .foam 标记文件，不启动 ParaView
touch case.foam &amp;&amp; paraview case.foam &amp;   # 方式二：手动（推荐，兼容自装的 ParaView）
paraFoam -block              # 打开 blockMeshDict 定义的块结构（调试 blockMesh 用）
paraFoam -region solid       # 打开指定区域
paraFoam -case ../run1</code></pre>
<p>v2512 的 paraFoam 最终调用 PATH 中的 paraview。-vtk（与 -builtin 等价）使用 ParaView 内置 OpenFOAM 读取器；-block 需要匹配的 blockReader 插件。可以用 command -v paraview 核对实际程序，使用 .foam 标记文件并不能保证所有版本都支持全部场与网格功能。</p>
<p>并行结果怎么看：不需要先 reconstructPar。在 ParaView 里打开 .foam 后，属性面板里把 Case Type 从 Reconstructed Case 改成 Decomposed Case 即可直接读 processor* 目录。省时间也省硬盘。</p>
<p>六个必会操作</p>
<div class="table-scroll"><table>
<tr><th>目的</th><th>操作</th></tr>
<tr><td>看内部流场</td><td>Filters → Slice（切面），法向选 z</td></tr>
<tr><td>看等值面</td><td>Filters → Contour（先 Cell Data to Point Data）</td></tr>
<tr><td>看涡结构</td><td>先 postProcess -func Q，再 Contour 取 Q 的正值</td></tr>
<tr><td>看矢量</td><td>Filters → Glyph，Scale Array 选 U，Scale Factor 调到合适</td></tr>
<tr><td>取一条线的数据</td><td>Filters → Plot Over Line，右侧直接出曲线，可 Save Data 成 csv</td></tr>
<tr><td>看流线</td><td>Filters → Stream Tracer</td></tr>
</table></div>
<p>使用 ParaView 过滤器前，应检查输入数组是单元数据还是点数据。对需要点数据的操作，可根据过滤器要求使用 Cell Data to Point Data，或检查 OpenFOAM 读取器的相关转换选项。转换会引入插值，分析结果时应明确其数据位置。</p>
<p>导出动画：View → Animation，或者 File → Save Animation 存成 png 序列，再用</p>
<pre><code class="language-bash">foamCreateVideo -dir images -image seq -out movie      # 需要 ffmpeg
# 或者直接：
ffmpeg -r 25 -i images/seq.%04d.png -pix_fmt yuv420p movie.mp4</code></pre>
<h2>8.6 其他后处理小工具</h2>
<div class="table-scroll"><table>
<tr><th>命令</th><th>作用</th></tr>
<tr><td>reconstructPar</td><td>合并并行结果（见第 9 章）</td></tr>
<tr><td>foamListTimes -rm</td><td>清时间目录</td></tr>
<tr><td>foamLog</td><td>日志转数据（见 5.10）</td></tr>
<tr><td>foamMonitor</td><td>实时画曲线（见 5.11）</td></tr>
<tr><td>postProcess -func writeCellCentres</td><td>输出单元中心坐标场，做自定义分析时常用</td></tr>
<tr><td>particleTracks</td><td>拉格朗日颗粒轨迹重建</td></tr>
<tr><td>noise</td><td>声压级/频谱分析（气动噪声）</td></tr>
</table></div><h2>v2512 的残差记录接口</h2><p>使用 <code>type solverInfo</code>，并加载 <code>utilityFunctionObjects</code>。<code>#includeFunc solverInfo</code> 的官方模板默认选择 p 和 U；如需其他字段，应复制模板并修改 fields。此功能读取求解过程中的 solverPerformance 数据，事后只读取已写出的 U、p 不能重建历史残差。</p><p><a href="/dictionaries/functions-solverinfo/">完整配置、字段解释与三个 v2512 示例</a></p>
