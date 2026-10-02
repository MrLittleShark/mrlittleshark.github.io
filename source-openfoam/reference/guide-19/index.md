---
title: "第 19 章　0/ 目录与边界条件参考"
layout: reference
description: "0/ 目录与边界条件参考：用法与配置实例。"
cms_slug: "reference-guide-19"
---

<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy" src="/assets/diagrams/reference-workflow.svg"/><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><h2>19.1 场文件的结构</h2>
<pre><code class="language-openfoam">FoamFile { version 2.0; format ascii; class volVectorField; object U; }

dimensions      [0 1 -1 0 0 0 0];        // 量纲
internalField   uniform (0 0 0);         // 内部场初值

boundaryField
{
    inlet
    {
        type            fixedValue;
        value           uniform (1 0 0);
    }
    outlet
    {
        type            zeroGradient;
    }
    walls
    {
        type            noSlip;
    }
    frontAndBack
    {
        type            empty;
    }
}</code></pre>
<p>三条强制规则：① boundaryField 里的 patch 名必须与 constant/polyMesh/boundary 完全对应（可用正则），漏一个就报 Cannot find patchField entry for xxx；② empty、symmetryPlane、wedge、cyclic 这类约束型边界，场里的 type 必须与网格里的 type 一致，否则报错；③ 很多边界条件即使值用不上也要写 value 一行（它是”当前值”的存储位置，重启时要用）。</p>
<h2>19.2 通用边界条件</h2>
<div class="table-scroll"><table>
<tr><th>type</th><th>数学含义</th><th>用在</th></tr>
<tr><td>fixedValue</td><td>\(\varphi\)= 给定值（Dirichlet）</td><td>进口速度、给定温度</td></tr>
<tr><td>zeroGradient</td><td>\(\partial \varphi /\partial n = 0\)（Neumann）</td><td>出口、绝热壁</td></tr>
<tr><td>fixedGradient</td><td>\(\partial \varphi /\partial n\)= 给定值</td><td>给定热流</td></tr>
<tr><td>mixed</td><td>Dirichlet 与 Neumann 的加权混合</td><td>大多数复合条件的基类</td></tr>
<tr><td>calculated</td><td>由其他场算出，不独立求解</td><td>nut、rho 等</td></tr>
<tr><td>noSlip</td><td>\(U = 0\)（等价于 fixedValue uniform (0 0 0)）</td><td>静止壁面</td></tr>
<tr><td>slip</td><td>法向为 0，切向零梯度</td><td>无摩擦壁</td></tr>
<tr><td>symmetry / symmetryPlane</td><td>对称</td><td>对称面</td></tr>
<tr><td>empty</td><td>该方向不求解</td><td>二维算例前后面</td></tr>
<tr><td>wedge</td><td>轴对称</td><td>楔形算例</td></tr>
<tr><td>cyclic</td><td>周期性</td><td>槽道流、叶栅</td></tr>
<tr><td>cyclicAMI</td><td>非匹配周期</td><td>旋转机械交界面</td></tr>
<tr><td>processor</td><td>并行内部边界</td><td>自动生成，不用手写</td></tr>
</table></div>
<h2>19.3 速度 U 的常用边界条件</h2>
<div class="table-scroll"><table>
<tr><th>type</th><th>作用</th><th>示例</th></tr>
<tr><td>fixedValue</td><td>给定速度</td><td>value uniform (10 0 0);</td></tr>
<tr><td>noSlip</td><td>无滑移壁</td><td>——</td></tr>
<tr><td>inletOutlet</td><td>流入时用 inletValue，流出时零梯度</td><td>防回流发散，出口首选</td></tr>
<tr><td>pressureInletOutletVelocity</td><td>由压力边界推速度，允许双向</td><td>配 totalPressure 用</td></tr>
<tr><td>pressureInletVelocity</td><td>由通量反推速度</td><td>只允许流入</td></tr>
<tr><td>flowRateInletVelocity</td><td>给定体积/质量流量</td><td>volumetricFlowRate 0.01;</td></tr>
<tr><td>swirlFlowRateInletVelocity</td><td>带旋流的流量入口</td><td>旋流燃烧器</td></tr>
<tr><td>movingWallVelocity</td><td>动网格壁面（自动扣除网格运动通量）</td><td>动网格里必须用它，不能用 fixedValue</td></tr>
<tr><td>rotatingWallVelocity</td><td>旋转壁</td><td>origin,axis,omega</td></tr>
<tr><td>translatingWallVelocity</td><td>平移壁</td><td>顶盖驱动腔</td></tr>
<tr><td>freestreamVelocity</td><td>远场（自动判进出）</td><td>外流远场</td></tr>
<tr><td>codedFixedValue</td><td>自定义分布（见 10.3）</td><td>抛物线入口</td></tr>
<tr><td>timeVaryingMappedFixedValue</td><td>从文件读随时间/空间变化的入口</td><td>用实测或前驱算例数据</td></tr>
<tr><td>turbulentDFSEMInlet</td><td>合成湍流入口（LES 用）</td><td>生成带脉动的入口</td></tr>
</table></div>
<pre><code class="language-openfoam">// 典型出口写法：允许流出，万一回流也不会炸
outlet
{
    type            inletOutlet;
    inletValue      uniform (0 0 0);
    value           uniform (0 0 0);
}

// 给定流量入口
inlet
{
    type            flowRateInletVelocity;
    volumetricFlowRate  0.001;      // m³/s；也可用 massFlowRate
    value           uniform (0 0 0);
}</code></pre>
<h2>19.4 压力 p / p_rgh 的常用边界条件</h2>
<div class="table-scroll"><table>
<tr><th>type</th><th>作用</th></tr>
<tr><td>zeroGradient</td><td>壁面标准做法（不可压）</td></tr>
<tr><td>fixedValue</td><td>出口给定压力（不可压时值是 \(p/\rho\)）</td></tr>
<tr><td>totalPressure</td><td>给定总压，静压随速度自动调整</td></tr>
<tr><td>fixedFluxPressure</td><td>壁面与动网格的正确做法：保证边界通量与速度边界一致</td></tr>
<tr><td>prghPressure / prghTotalPressure</td><td>多相流的 p_rgh（已扣除静水压）</td></tr>
<tr><td>freestreamPressure</td><td>远场</td></tr>
<tr><td>waveTransmissive</td><td>无反射出口（可压缩，防激波反射回来）</td></tr>
</table></div>
<pre><code class="language-openfoam">// 不可压出口
outlet { type fixedValue; value uniform 0; }

// 壁面（含浮力/动网格时必须这样写）
walls  { type fixedFluxPressure; value uniform 0; }

// 可压超声速出口，防止反射
outlet
{
    type            waveTransmissive;
    field           p;
    gamma           1.4;
    value           uniform 1e5;
}</code></pre>
<p>压力边界应与离散动量方程和法向通量约束一致。fixedFluxPressure 可在支持该更新流程的求解器中设置与通量相容的压力梯度；含重力或网格运动时尤其需要核对 p 与 p_rgh 的定义。zeroGradient 是否合理，应按具体方程和边界条件判断。</p>
<p>p 和 p_rgh 的区别：多相流和浮力问题里求解的是 \(p_{\mathrm{rgh}}=p-\rho\boldsymbol g\cdot\boldsymbol h\)（扣掉静水压），这样数值上更好解。你在 0/ 里给的是 p_rgh，p 由程序算出。边界条件要给在 p_rgh 上。</p>
<h2>19.5 湍流量的边界条件</h2>
<div class="table-scroll"><table>
<tr><th>场</th><th>入口</th><th>壁面</th><th>出口</th></tr>
<tr><td>k</td><td>turbulentIntensityKineticEnergyInlet 或 fixedValue</td><td>kqRWallFunction</td><td>inletOutlet</td></tr>
<tr><td>epsilon</td><td>turbulentMixingLengthDissipationRateInlet</td><td>epsilonWallFunction</td><td>inletOutlet</td></tr>
<tr><td>omega</td><td>turbulentMixingLengthFrequencyInlet</td><td>omegaWallFunction</td><td>inletOutlet</td></tr>
<tr><td>nut</td><td>calculated</td><td>nutkWallFunction 或 nutUSpaldingWallFunction</td><td>calculated</td></tr>
<tr><td>nuTilda</td><td>fixedValue</td><td>fixedValue uniform 0</td><td>inletOutlet</td></tr>
</table></div>
<pre><code class="language-openfoam">// 0/k
inlet
{
    type        turbulentIntensityKineticEnergyInlet;
    intensity   0.05;                 // 湍流度 5%
    value       uniform 0.375;
}
walls  { type kqRWallFunction; value uniform 0.375; }

// 0/epsilon
inlet
{
    type        turbulentMixingLengthDissipationRateInlet;
    mixingLength 0.007;               // 特征长度的 7% 是常用估计
    value       uniform 14.855;
}
walls  { type epsilonWallFunction; value uniform 14.855; }</code></pre>
<p>入口湍流量可以根据湍流强度和特征长度估算；下式依赖各向同性及所选湍流模型的常见假设，实验数据可用时应优先核对：</p>
<p>\(k = 1.5 (U\cdot I)^{2}\)，I 是湍流度（管流取 5%，风洞取 1%）</p>
<p>\(\varepsilon=\frac{C_\mu^{0.75}k^{1.5}}{l}\)，\(C_\mu = 0.09\)，\(l \approx  0.07\)× 水力直径</p>
<p>\(\omega=\frac{k^{0.5}}{C_\mu^{0.25}l}\)</p>
<p>壁面函数怎么选</p>
<div class="table-scroll"><table>
<tr><th>壁面函数</th><th>\(y^{+}\) 适用范围</th><th>说明</th></tr>
<tr><td>nutkWallFunction</td><td>30–300</td><td>标准壁函数，基于 k</td></tr>
<tr><td>nutUSpaldingWallFunction</td><td>全 \(y^{+}\)</td><td>连续壁函数，网格 \(y^{+}\) 不好控制时用它最省心</td></tr>
<tr><td>nutUWallFunction</td><td>30–300</td><td>基于速度</td></tr>
<tr><td>nutLowReWallFunction</td><td>\(y^{+} &lt; 1\)</td><td>解析近壁</td></tr>
</table></div>
<p>先看 \(y^{+}\) 再选：跑几步后 simpleFoam -postProcess -func yPlus -latestTime，看 postProcessing/yPlus/ 里的范围。\(y^{+}\) 落在 5–30 的缓冲层是最糟的情况（两种做法都不准），要么加密到 \(y^{+}&lt;1\)，要么放粗到 \(y^{+}&gt;30\)——或者直接用 nutUSpaldingWallFunction。</p>
<h2>19.6 温度与传热</h2>
<div class="table-scroll"><table>
<tr><th>type</th><th>作用</th></tr>
<tr><td>fixedValue</td><td>恒温壁</td></tr>
<tr><td>zeroGradient</td><td>绝热壁</td></tr>
<tr><td>externalWallHeatFluxTemperature</td><td>给定热流/对流换热系数/外界温度</td></tr>
<tr><td>compressible::turbulentTemperatureCoupledBaffleMixed</td><td>共轭传热的流固交界面</td></tr>
<tr><td>wallHeatTransfer</td><td>给定传热系数</td></tr>
<tr><td>inletOutlet</td><td>出口</td></tr>
</table></div>
<pre><code class="language-openfoam">// 对流边界：给外界温度和换热系数
wall
{
    type            externalWallHeatFluxTemperature;
    mode            coefficient;         // power / flux / coefficient
    h               uniform 10;          // W/(m²K)
    Ta              uniform 300;         // 环境温度
    kappaMethod     fluidThermo;
    value           uniform 300;
}</code></pre>
<h2>19.7 多相流的 alpha</h2>
<pre><code class="language-openfoam">// 0/alpha.water
inlet   { type fixedValue; value uniform 1; }
outlet  { type inletOutlet; inletValue uniform 0; value uniform 0; }
walls
{
    type            constantAlphaContactAngle;   // 接触角（毛细现象重要时）
    theta0          90;
    limit           gradient;
    value           uniform 0;
}
atmosphere { type inletOutlet; inletValue uniform 0; value uniform 0; }</code></pre>
<h2>19.8 时变与外部数据</h2>
<pre><code class="language-openfoam">// ① 用表格给随时间变化的值
inlet
{
    type            uniformFixedValue;
    uniformValue    table ((0 (0 0 0)) (1 (10 0 0)) (5 (10 0 0)));
}

// ② 从文件读随时间和空间变化的入口（前驱算例 / 实测数据）
inlet
{
    type            timeVaryingMappedFixedValue;
    offset          (0 0 0);
    setAverage      off;
}
// 数据放在 constant/boundaryData/inlet/{points, 0/U, 0.1/U, ...}

// ③ 把另一处的场映射过来（回收入口，做周期性湍流入口）
inlet
{
    type            mapped;
    field           U;
    setAverage      true;
    average         (10 0 0);
    interpolationScheme cell;
    value           uniform (10 0 0);
}</code></pre>
<h2>19.9 边界条件查询方法</h2>
<pre><code class="language-bash">foamHelp boundary -field U | less          # 本机所有可用类型
pimpleFoam -listVectorBCs                  # 同上，另一个入口
find $FOAM_SRC -name "*inletOutlet*"       # 找源码
grep -rl "inletOutlet" $FOAM_TUTORIALS/incompressible --include=U | head   # 找用例</code></pre>
<p>最后一条最实用：先找到一个用了这个边界条件的官方算例，再照抄它的完整写法，包括那些你不确定要不要写的参数。</p>
