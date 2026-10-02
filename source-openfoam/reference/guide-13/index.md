---
title: "第 13 章　system/fvSchemes（离散格式）"
layout: reference
description: "system/fvSchemes（离散格式）：用法与配置实例。"
cms_slug: "reference-guide-13"
---

<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy" src="/assets/diagrams/reference-workflow.svg"/><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><p>它管什么：每一项微分算子用什么数值格式离散。这是精度与稳定性的主要旋钮，也是初学者最容易被卡住的地方。</p>
<h2>13.1 六个子字典</h2>
<pre><code class="language-openfoam">ddtSchemes          { }   // 时间导数 ∂/∂t
gradSchemes         { }   // 梯度 ∇
divSchemes          { }   // 对流项 ∇·( )   ← 最关键
laplacianSchemes    { }   // 扩散项 ∇²
interpolationSchemes{ }   // 单元中心 → 面 的插值
snGradSchemes       { }   // 面法向梯度
wallDist            { }   // 壁面距离算法（湍流模型需要）</code></pre>
<h2>13.2 ddtSchemes</h2>
<div class="table-scroll"><table>
<tr><th>写法</th><th>精度/性质</th><th>何时用</th></tr>
<tr><td>steadyState</td><td>去掉时间项</td><td>稳态求解器必须用这个</td></tr>
<tr><td>Euler</td><td>一阶隐式，无条件稳定，有数值耗散</td><td>瞬态起步、鲁棒优先</td></tr>
<tr><td>backward</td><td>二阶隐式</td><td>LES/DNS 的主力</td></tr>
<tr><td>CrankNicolson 0.9</td><td>二阶，系数 0~1（0=Euler，1=纯 CN）</td><td>精度要求高时，一般取 0.9 保稳</td></tr>
<tr><td>localEuler</td><td>伪时间步（局部时间步长加速收敛）</td><td>稳态加速</td></tr>
</table></div>
<pre><code class="language-openfoam">ddtSchemes { default backward; }</code></pre>
<p>LES 需要控制时间与空间离散的数值耗散。一阶 Euler 时间格式并非语法上禁止，但通常需要更严格的时间步敏感性检查；backward 或合适的 CrankNicolson 配置也必须结合稳定性、网格分辨率和统计量验证。</p>
<h2>13.3 gradSchemes</h2>
<div class="table-scroll"><table>
<tr><th>写法</th><th>说明</th></tr>
<tr><td>Gauss linear</td><td>标准二阶，最常用</td></tr>
<tr><td>leastSquares</td><td>最小二乘，网格差时更准</td></tr>
<tr><td>cellLimited Gauss linear 1</td><td>限制梯度不产生新极值，1 = 完全限制</td></tr>
<tr><td>cellLimited&lt;cubic&gt; 1.5 Gauss linear 1</td><td>更平滑的限制器</td></tr>
</table></div>
<pre><code class="language-plaintext">gradSchemes
{
    default         Gauss linear;
    grad(U)         cellLimited Gauss linear 1;    // 网格差或有激波时加限制
}</code></pre>
<h2>13.4 divSchemes（对流项，最关键）</h2>
<p>写法是 Gauss &lt;插值格式&gt;，Gauss 表示用高斯定理做体积分→面积分。真正起作用的是后面的插值格式：</p>
<div class="table-scroll"><table>
<tr><th>插值格式</th><th>阶数</th><th>有界性</th><th>评价</th></tr>
<tr><td>upwind</td><td>一阶</td><td>绝对有界</td><td>最稳但最耗散，只用来救急或做初场</td></tr>
<tr><td>linear</td><td>二阶中心</td><td>无界</td><td>精度最好，LES 用；RANS 上容易振荡</td></tr>
<tr><td>linearUpwind grad(U)</td><td>二阶迎风</td><td>基本有界</td><td>稳态 RANS 的常用选择</td></tr>
<tr><td>limitedLinear 1</td><td>二阶 + 限制器</td><td>有界</td><td>通用、稳健，1 最严格</td></tr>
<tr><td>vanLeer</td><td>TVD</td><td>有界</td><td>相分数 alpha 常用</td></tr>
<tr><td>interfaceCompression vanLeer 1</td><td>VOF 界面压缩</td><td></td><td>interFoam 的 alpha 方程</td></tr>
<tr><td>LUST grad(U)</td><td>75% 线性 + 25% 迎风</td><td></td><td>LES 折中方案</td></tr>
<tr><td>limitedLinear01 1</td><td>限制在 [0,1]</td><td></td><td>alpha、组分等有物理上下界的量</td></tr>
</table></div>
<pre><code class="language-plaintext">// 稳态 RANS 的典型配置
divSchemes
{
    default         none;                          // ★ 强制每一项都显式指定
    div(phi,U)      bounded Gauss linearUpwind grad(U);
    div(phi,k)      bounded Gauss limitedLinear 1;
    div(phi,omega)  bounded Gauss limitedLinear 1;
    div((nuEff*dev2(T(grad(U))))) Gauss linear;
}
// LES 的典型配置
divSchemes
{
    default         none;
    div(phi,U)      Gauss LUST grad(U);
    div(phi,k)      Gauss limitedLinear 1;
    div((nuEff*dev2(T(grad(U))))) Gauss linear;
}
// interFoam（VOF）的典型配置
divSchemes
{
    default         none;
    div(rhoPhi,U)   Gauss linearUpwind grad(U);
    div(phi,alpha)  Gauss vanLeer;
    div(phirb,alpha) Gauss linear;              // 界面压缩项
    div(((rho*nuEff)*dev2(T(grad(U))))) Gauss linear;
}</code></pre>
<p>在相应格式字典中使用 default none，可要求相关项显式指定离散格式。缺失项会在运行时报告。应先确认方程项、变量及适用格式，再补充配置，避免仅根据名称机械复制。</p>
<p>bounded 前缀是什么：稳态计算中间过程质量并不严格守恒，bounded 会减去 \((\nabla \cdot \varphi )U\) 这一项来抵消不守恒带来的虚假源。稳态加、瞬态不加。</p>
<h2>13.5 laplacianSchemes 与 snGradSchemes</h2>
<pre><code class="language-plaintext">laplacianSchemes { default Gauss linear corrected; }
snGradSchemes    { default corrected; }</code></pre>
<div class="table-scroll"><table>
<tr><th>修正方式</th><th>适用非正交角</th></tr>
<tr><td>orthogonal</td><td>完全正交网格（如标准 blockMesh 方腔）</td></tr>
<tr><td>corrected</td><td>&lt; 70°，标准选择</td></tr>
<tr><td>limited corrected 0.5</td><td>70°–80°，0.5 表示限制到一半</td></tr>
<tr><td>limited corrected 0.33</td><td>&gt; 80°，更保守</td></tr>
<tr><td>uncorrected</td><td>不修正，最稳但有误差</td></tr>
</table></div>
<p>怎么选：跑一次 checkMesh 看最大非正交角，按上表挑。这就是 6.5 节强调 checkMesh 的原因之一——它的输出直接决定这里怎么填。</p>
<h2>13.6 其余两项</h2>
<pre><code class="language-plaintext">interpolationSchemes { default linear; }
wallDist             { method meshWave; }</code></pre>
