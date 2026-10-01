---
title: "constant/dynamicMeshDict"
layout: "reference"
description: "下例采用位移拉普拉斯方法平滑网格运动，并通过 0/pointDisplacement 指定位移。求解器需支持该运动模型。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>constant/dynamicMeshDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>dynamicFvMesh</code> · <code>dynamicRefineFvMesh</code> · <code>dynamicMotionSolverFvMesh</code> · <code>motionSolver</code> · <code>field</code> · <code>lowerRefineLevel</code> · <code>upperRefineLevel</code> · <code>refineInterval</code> · <code>maxRefinement</code> · <code>maxCells</code></p><h2>关联命令</h2><p><a href="/commands/?q=interFoam">interFoam</a> · <a href="/commands/?q=pimpleFoam">pimpleFoam</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary constant/dynamicMeshDict -keywords
interFoam -help</code></pre><h2>9.11 constant/dynamicMeshDict</h2><p>下例采用位移拉普拉斯方法平滑网格运动，并通过 0/pointDisplacement 指定位移。求解器需支持该运动模型。</p>
<pre><code>dynamicFvMesh dynamicMotionSolverFvMesh;
motionSolverLibs (&quot;libfvMotionSolvers.so&quot;);
solver displacementLaplacian;
displacementLaplacianCoeffs
{
    diffusivity uniform;
}</code></pre>
<p>pointDisplacement 为 pointVectorField，采用长度量纲。运动壁面指定相应位移，固定壁面指定零位移。motionSolver 或兼容键 solver 按 v2512 对应模型的接口设置。</p>
<div class="table-scroll"><table>
<tr><th>模型或功能</th><th>配置项</th><th>相关参数</th></tr>
<tr><td>规定刚体运动</td><td>solidBodyMotionFvMesh、solidBodyMotionFunction 及相应系数</td><td>旋转中心、轴、速度或时间函数</td></tr>
<tr><td>六自由度</td><td>sixDoFRigidBodyMotion 运动求解器</td><td>mass、momentOfInertia、centreOfMass、力矩参考与约束</td></tr>
<tr><td>自适应细化</td><td>dynamicRefineFvMesh</td><td>field、refineInterval、lowerRefineLevel、upperRefineLevel、unrefineLevel</td></tr>
<tr><td>细化限制</td><td>maxRefinement、maxCells、nBufferLayers</td><td>内存估计和细化一致性</td></tr>
<tr><td>拓扑改变通量修正</td><td>correctFluxes</td><td>通量和关联速度字段的配对，依求解器设置</td></tr>
<tr><td>重叠网格</td><td>dynamicOversetFvMesh 等、oversetInterpolation</td><td>zoneID、overset patch、孔切割和插值层</td></tr>
</table></div>
<p>先运行 moveDynamicMesh 检查网格运动，重点检查运动过程中质量最差的时刻，再进行流场求解。运动和拓扑变化类型应处于求解器的支持范围内。</p>
<h2>18.5 dynamicMeshDict（动网格）</h2><p>刚体运动（最简单）</p>
<pre><code>dynamicFvMesh   dynamicMotionSolverFvMesh;
motionSolver    solidBody;
solidBodyMotionFunction  rotatingMotion;
rotatingMotionCoeffs
{
    origin  (0 0 0);
    axis    (0 0 1);
    omega   6.28;                 // rad/s
}
cellZone        rotor;            // 只让这个 zone 动</code></pre>
<p>其他运动函数：oscillatingLinearMotion、linearMotion、SDA、tabulated6DoFMotion、multiMotion。</p>
<p>六自由度耦合（自由运动物体）</p>
<pre><code>motionSolver    sixDoFRigidBodyMotion;
sixDoFRigidBodyMotionCoeffs
{
    patches         (floatingObject);
    innerDistance   0.05;
    outerDistance   0.35;
    mass            9.6;
    centreOfMass    (0.5 0.45 0.4);
    momentOfInertia (0.08 0.08 0.06);
    accelerationRelaxation 0.7;
    solver          { type Newmark; }
    constraints     { zAxis { sixDoFRigidBodyMotionConstraint line; direction (0 0 1);} }
}</code></pre>
<p>动态加密（AMR）</p>
<pre><code>dynamicFvMesh   dynamicRefineFvMesh;
refineInterval  10;
field           alpha.water;      // 按哪个场判断
lowerRefineLevel 0.001;
upperRefineLevel 0.999;
maxRefinement   2;
maxCells        2000000;
nBufferLayers   1;</code></pre>
<p>用途：VOF 里只在界面附近加密，单元数可以省一个量级。</p>
{% endraw %}