---
title: "10 后处理函数对象与数据采样"
layout: reference
description: "OpenCFD v2512 后处理函数对象与数据采样；包含原理、示例与版本核对。"
---
{% raw %}
<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img src="/assets/diagrams/reference-workflow.svg" alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy"><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><h3>10.1 函数对象的通用设置</h3>
<p>函数对象配置于 system/controlDict 的 functions 子字典，或置于独立字典并由 postProcess -dict 指定。外层名称为实例名，type 指定函数对象类型。类型定义及模板见 S2 的 src/functionObjects 和 etc/caseDicts/postProcessing。</p>
<div class="table-scroll"><table>
<tr><th>参数</th><th>含义</th><th>设置示例</th></tr>
<tr><td>type</td><td>函数对象类型</td><td>probes、forces、fieldAverage 等</td></tr>
<tr><td>libs</td><td>加载相应库</td><td>("libsampling.so") 或 ("libfieldFunctionObjects.so")</td></tr>
<tr><td>enabled、log</td><td>是否启用、是否打印日志</td><td>true</td></tr>
<tr><td>region</td><td>作用区域</td><td>多区域时指定 air 等</td></tr>
<tr><td>timeStart、timeEnd</td><td>作用时间范围</td><td>例如 0.2 到 1.0</td></tr>
<tr><td>executeControl、executeInterval</td><td>计算触发方式与间隔</td><td>timeStep 与 1</td></tr>
<tr><td>writeControl、writeInterval</td><td>结果输出方式与间隔</td><td>timeStep、runTime、writeTime 等</td></tr>
<tr><td>fields 或 field</td><td>待处理字段</td><td>列表或单字段由具体类型决定</td></tr>
</table></div>
<p>executeControl 和 writeControl 分别控制计算与输出。fieldAverage 和累积积分依赖历史数据，统计区间内需连续执行相应函数对象。</p>
<h3>10.2 点探针采样</h3>
<pre><code class="language-openfoam">// 放入 functions 内
pressureProbes
{
    type probes;
    libs ("libsampling.so");
    writeControl timeStep;
    writeInterval 1;
    fields (p U);
    probeLocations
    (
        (0.25 0.05 0.005)
        (0.75 0.05 0.005)
    );
}</code></pre>
<p>探针位置应位于有效流体单元内，压力结果输出至 postProcessing/pressureProbes/起始时刻/p。冲击和快速瞬态计算需按目标时间尺度设置采样频率，以记录峰值及波形变化。</p>
<h3>10.3 沿线采样</h3>
<pre><code class="language-openfoam">lineSample
{
    type sets;
    libs ("libsampling.so");
    writeControl writeTime;
    setFormat raw;
    interpolationScheme cellPoint;
    fields (U p);
    sets
    {
        centreline
        {
            type uniform;
            axis x;
            start (0.01 0.05 0.005);
            end (0.99 0.05 0.005);
            nPoints 100;
        }
    }
}</code></pre>
<p>axis 指定输出横坐标类型，nPoints 指定采样点数，interpolationScheme 指定单元或点插值方法。</p>
<h3>10.4 面采样</h3>
<pre><code class="language-openfoam">sectionSample
{
    type surfaces;
    libs ("libsampling.so");
    writeControl writeTime;
    surfaceFormat vtk;
    fields (U p);
    interpolationScheme cellPoint;
    surfaces
    {
        midPlane
        {
            type cuttingPlane;
            planeType pointAndNormal;
            pointAndNormalDict
            {
                point (0.5 0 0);
                normal (1 0 0);
            }
            interpolate true;
        }
    }
}</code></pre>
<p>面采样还支持 patch、isoSurface 等类型。采用 isoSurface 时，通过字段、等值和采样算法定义所需相界面或涡结构。</p>
<h3>10.5 力与力系数</h3>
<pre><code class="language-openfoam">bodyForces
{
    type forces;
    libs ("libforces.so");
    patches (walls);
    p p;
    U U;
    rho rhoInf;
    rhoInf 1000;
    CofR (0 0 0);
    writeControl timeStep;
    writeInterval 1;
}</code></pre>
<p>下例使用参考密度处理不可压缩压力场。可压缩计算通常指定实际 rho 字段及对应压力形式。CofR 定义力矩参考中心，压力基准应与载荷积分采用的压力定义一致。</p>
<p>计算力系数时，将 type 设为 forceCoeffs，并指定 liftDir、dragDir、pitchAxis、magUInf、lRef 和 Aref。若阻力沿 x 方向、升力沿 y 方向，可设置 dragDir (1 0 0); liftDir (0 1 0); pitchAxis (0 0 1);。lRef 和 Aref 分别为归一化参考长度和面积，二维算例的参考面积需计入所取厚度。</p>
<h3>10.6 统计量与派生场</h3>
<div class="table-scroll"><table>
<tr><th>类型</th><th>主要参数</th><th>配置与调用示例</th></tr>
<tr><td>fieldAverage</td><td>fields 下每场的 mean、prime2Mean、base</td><td>U { mean on; prime2Mean on; base time; }；生成 UMean 等</td></tr>
<tr><td>fieldMinMax</td><td>fields、location、mode</td><td>fields (p U); location true;，输出极值及位置</td></tr>
<tr><td>volFieldValue</td><td>regionType、name、operation、fields</td><td>regionType all; operation volAverage; fields (T);</td></tr>
<tr><td>surfaceFieldValue</td><td>regionType patch、name、operation、fields</td><td>name outlet; operation sum; fields (phi);，输出带法向符号的通量</td></tr>
<tr><td>solverInfo</td><td>fields</td><td>fields (p U);，记录各方程初始残差</td></tr>
<tr><td>yPlus</td><td>湍流模型及壁面量</td><td>simpleFoam -postProcess -func yPlus -latestTime</td></tr>
<tr><td>wallShearStress</td><td>patches、writeControl</td><td>simpleFoam -postProcess -func wallShearStress -latestTime</td></tr>
<tr><td>wallHeatFlux</td><td>热模型和壁面</td><td>通过相应传热求解器 -postProcess -func wallHeatFlux</td></tr>
<tr><td>CourantNo</td><td>通量及密度条件</td><td>postProcess -func CourantNo -latestTime，读取所需通量等场</td></tr>
<tr><td>mag、grad、div</td><td>操作字段</td><td>postProcess -func 'mag(U)' -latestTime</td></tr>
<tr><td>vorticity、Q</td><td>速度梯度派生量</td><td>postProcess -func vorticity -latestTime</td></tr>
<tr><td>MachNo</td><td>速度和热物性声速</td><td>通过可压缩求解器 -postProcess -func MachNo</td></tr>
<tr><td>streamLine</td><td>seedSampleSet、direction、lifeTime、trackLength 等</td><td>foamGetDict streamlines 获取模板，随后配置种子点</td></tr>
</table></div>
<p>表中名称包括函数对象类型和预配置函数。postProcess -list 列出可直接通过 -func 调用的预配置名称；其余类型按 functions 子字典配置。</p>
<pre><code class="language-openfoam">statistics
{
    type fieldAverage;
    libs ("libfieldFunctionObjects.so");
    timeStart 0.2;
    executeControl timeStep;
    executeInterval 1;
    writeControl writeTime;
    fields
    (
        U { mean on; prime2Mean on; base time; }
        p { mean on; prime2Mean off; base time; }
    );
}</code></pre>
<h3>10.7 system/noiseDict 与粒子后处理</h3>
<p>noiseDict 通过 noiseModel 选择 pointNoise、surfaceNoise 等模型，并定义输入数据、FFT 分块和窗函数。频谱分析采用等时间间隔采样，采样时长决定频率分辨率，Nyquist 频率为采样频率的一半。</p>
<p>particleTracksDict 指定粒子云、采样频率和轨迹长度，轨迹重建使用求解阶段保存的粒子标识。steadyParticleTracksDict 用于稳态轨迹处理。字段设置采用对应粒子模型的教程结构。</p>
<h3>10.8 常用后处理流程</h3>
<pre><code class="language-bash">postProcess -list
postProcess -func 'mag(U)' -latestTime
postProcess -func 'grad(p)' -latestTime
simpleFoam -postProcess -func yPlus -latestTime
foamToVTK -latestTime -fields '(U p)'
paraFoam -builtin</code></pre>
<p>上述命令中的 simpleFoam 按算例所用求解器替换。瞬态压力载荷结果应注明压力单位、压力基准、采样频率、探针坐标及积分区间。</p><h2>v2512 的残差记录接口</h2><p>使用 <code>type solverInfo</code>，并加载 <code>utilityFunctionObjects</code>。<code>#includeFunc solverInfo</code> 的官方模板默认选择 p 和 U；如需其他字段，应复制模板并修改 fields。此功能读取求解过程中的 solverPerformance 数据，事后只读取已写出的 U、p 不能重建历史残差。</p><p><a href="/dictionaries/functions-solverinfo/">完整配置、字段解释与三个 v2512 示例</a></p>
{% endraw %}
