---
title: "第 8 章　后处理命令与 functionObject"
layout: "reference"
description: "OpenFOAM v2512 命令、文件与配置参考"
manual: 2
---
{% raw %}
<p class="source-note">资料来源：OpenFOAM命令与文件大全_v2512（Claude整理）.docx。网页版已对部分表述作技术性修订，原文可在资料页下载。命令选项以本机 v2512 的 <code>-help</code> 为准。核心模板工具使用 <code>foamGetDict</code>；版本差异与安装步骤需结合官方说明核对。</p><p>后处理有两条路：算完再处理（postProcess 等命令）和边算边处理（controlDict 里的 functionObject）。能用后者就用后者——因为很多量（比如受力时程、探针时间序列）需要每个时间步的数据，而你不可能把每个时间步的整场都写到硬盘上。</p>
<h4>8.1 postProcess —— 通用后处理命令</h4>
<p>用法</p>
<pre><code>postProcess -func &lt;功能名&gt; [-time &lt;范围&gt;] [-latestTime] [-fields &#x27;(U p)&#x27;] [-noZero] [-parallel]
postProcess -funcs &#x27;(func1 func2)&#x27;
postProcess -list                    # 列出所有可用功能</code></pre>
<p>示例</p>
<pre><code># ① 看有哪些功能可用
$ postProcess -list

# ② 计算速度大小，写成新场 mag(U)
$ postProcess -func &quot;mag(U)&quot;

# ③ 计算 Q 判据（涡识别），只处理最后一个时刻
$ postProcess -func Q -latestTime

# ④ 计算涡量
$ postProcess -func vorticity -time &#x27;1:10&#x27;

# ⑤ 沿一条线取样（需要 system/singleGraph 配置文件）
$ postProcess -func singleGraph -latestTime

# ⑥ 求某个边界上的面积分（不用改 controlDict）
$ postProcess -func &quot;patchAverage(patch=outlet, field=p)&quot; -latestTime

# ⑦ 依赖湍流模型的量必须用求解器 + -postProcess
$ simpleFoam -postProcess -func yPlus -latestTime</code></pre>
<p>常用 -func 名字：mag(U)、magSqr(U)、grad(p)、div(phi)、Q、vorticity、Lambda2、CourantNo、yPlus、wallShearStress、turbulenceFields(R)、enstrophy、flowType、components(U)、writeCellCentres、writeCellVolumes、streamlines、surfaces、sets、probes、forces、forceCoeffs、fieldAverage、residuals、solverInfo。</p>
<h4>8.2 #includeFunc —— 一行开启一个后处理功能</h4>
<p>在 controlDict 的 functions 里，官方模板可以一行引入：</p>
<pre><code>functions
{
    #includeFunc  residuals(p,U)
    #includeFunc  yPlus
    #includeFunc  Q
    #includeFunc  mag(U)
    #includeFunc  probes
    #includeFunc  patchAverage(patch=outlet, field=p)
    #includeFunc  flowRatePatch(name=outlet)
    #includeFunc  singleGraph
}</code></pre>
<p>为什么这么方便：这些名字对应 $FOAM_ETC/caseDicts/postProcessing/ 下的模板文件，#includeFunc 就是把模板内容读进来。想改参数时，用 foamGet 把模板拷到 system/ 再改，本地文件优先级更高。</p>
<pre><code>$ ls $FOAM_ETC/caseDicts/postProcessing/*        # 看看有哪些现成模板</code></pre>
<h4>8.3 常用 functionObject 的写法</h4>
<p>写在 system/controlDict 的 functions {} 里（也可以单独放文件再 #include）。所有 functionObject 都有这几个公共关键字：</p>
<div class="table-scroll"><table>
<tr><th>关键字</th><th>含义</th></tr>
<tr><td>type</td><td>功能类型</td></tr>
<tr><td>libs</td><td>需要加载的库，如 (&quot;libfieldFunctionObjects.so&quot;)</td></tr>
<tr><td>writeControl</td><td>timeStep / runTime / writeTime / onEnd</td></tr>
<tr><td>writeInterval</td><td>间隔</td></tr>
<tr><td>executeControl / executeInterval</td><td>计算频率（可以算得勤、写得少）</td></tr>
<tr><td>enabled</td><td>true/false，临时关掉某个功能</td></tr>
<tr><td>timeStart / timeEnd</td><td>只在某段时间内工作（如统计平均只从流动充分发展后开始）</td></tr>
</table></div>
<p>① 探针：监测某几个点的时间序列</p>
<pre><code>probes
{
    type            probes;
    libs            (&quot;libsampling.so&quot;);
    writeControl    timeStep;
    writeInterval   1;
    fields          (p U);
    probeLocations  ( (0.1 0.05 0.005) (0.2 0.05 0.005) );
}</code></pre>
<p>输出在 postProcessing/probes/0/p。用途：看涡脱落频率、判断是否进入统计定常。</p>
<p>② 力与力系数：算阻力升力</p>
<pre><code>forceCoeffs
{
    type            forceCoeffs;
    libs            (&quot;libforces.so&quot;);
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
<p>输出在 postProcessing/forceCoeffs/0/coefficient.dat。注意：不可压求解器里 p 的单位是 \(m^{2}/s^{2}\)（已除以密度），所以必须给 rhoInf，否则力小了 \(\rho\) 倍——这是最常见的错误之一。</p>
<p>③ 场平均：LES/URANS 的统计量</p>
<pre><code>fieldAverage
{
    type            fieldAverage;
    libs            (&quot;libfieldFunctionObjects.so&quot;);
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
<pre><code>singleGraph
{
    type            sets;
    libs            (&quot;libsampling.so&quot;);
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
<pre><code>surfaces
{
    type            surfaces;
    libs            (&quot;libsampling.so&quot;);
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
<pre><code>outletFlux
{
    type            surfaceFieldValue;
    libs            (&quot;libfieldFunctionObjects.so&quot;);
    regionType      patch;
    name            outlet;
    operation       sum;             // sum/areaAverage/areaIntegrate/min/max/CoV
    fields          (phi);
    writeControl    timeStep;
}
volAvgT
{
    type            volFieldValue;
    libs            (&quot;libfieldFunctionObjects.so&quot;);
    regionType      all;             // 或 cellZone + name
    operation       volAverage;
    fields          (T);
    writeControl    timeStep;
}</code></pre>
<p>用途：检查质量守恒（进出口 phi 之和应接近 0）、监测平均温度等全局量随时间的变化。</p>
<p>⑦ 残差与求解器信息</p>
<pre><code>#includeFunc residuals(p,U,k,epsilon)</code></pre>
<p>或</p>
<pre><code>solverInfo
{
    type            solverInfo;
    libs            (&quot;libutilityFunctionObjects.so&quot;);
    fields          (U p);
    writeResidualFields yes;         // 把残差也写成场，可在 ParaView 里看&quot;哪儿不收敛&quot;
}</code></pre>
<p>writeResidualFields 很值得开：残差高的区域往往就是网格差或边界条件不合理的区域，一眼定位问题在哪。</p>
<h4>8.4 foamToVTK / foamToEnsight —— 导出到别的软件</h4>
<pre><code>$ foamToVTK                                   # 全部时刻导出成 VTK
$ foamToVTK -latestTime -fields &#x27;(U p)&#x27;       # 只导最后一个时刻的两个场
$ foamToVTK -ascii                            # 文本格式，可以直接用编辑器看
$ foamToVTK -cellSet c0                       # 只导出某个 cellSet
$ foamToVTK -no-boundary                      # 不导边界数据
$ foamToEnsight -latestTime                   # 导 EnSight 格式</code></pre>
<p>什么时候需要：给合作者（用 Tecplot/EnSight）传数据，或者自己用 Python（pyvista/vtk）做定制分析时。日常用 ParaView 直接读算例目录即可，不需要转换。</p>
<h4>8.5 ParaView：paraFoam 与 .foam 文件</h4>
<p>两种打开方式</p>
<pre><code>$ paraFoam                     # 方式一：自动生成临时文件并启动 ParaView
$ paraFoam -touch              # 只生成 &lt;算例名&gt;.foam 文件，不启动
$ touch case.foam &amp;&amp; paraview case.foam &amp;   # 方式二：手动（推荐，兼容自装的 ParaView）
$ paraFoam -block              # 打开 blockMeshDict 定义的块结构（调试 blockMesh 用）
$ paraFoam -region solid       # 打开指定区域
$ paraFoam -case ../run1</code></pre>
<p>推荐方式二的原因：paraFoam 会去调用与 OpenFOAM 配套的那个 ParaView。如果你自己装了新版 ParaView，用 .foam 文件的方式可以随便挑版本，也方便远程拷回本地打开。</p>
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
<pre><code>$ foamCreateVideo -dir images -image seq -out movie      # 需要 ffmpeg
# 或者直接：
$ ffmpeg -r 25 -i images/seq.%04d.png -pix_fmt yuv420p movie.mp4</code></pre>
<h4>8.6 其他后处理小工具</h4>
<div class="table-scroll"><table>
<tr><th>命令</th><th>作用</th></tr>
<tr><td>reconstructPar</td><td>合并并行结果（见第 9 章）</td></tr>
<tr><td>foamListTimes -rm</td><td>清时间目录</td></tr>
<tr><td>foamLog</td><td>日志转数据（见 5.10）</td></tr>
<tr><td>foamMonitor</td><td>实时画曲线（见 5.11）</td></tr>
<tr><td>postProcess -func writeCellCentres</td><td>输出单元中心坐标场，做自定义分析时常用</td></tr>
<tr><td>particleTracks</td><td>拉格朗日颗粒轨迹重建</td></tr>
<tr><td>noise</td><td>声压级/频谱分析（气动噪声）</td></tr>
</table></div>
{% endraw %}