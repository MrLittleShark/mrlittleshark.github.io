---
title: "constant/turbulenceProperties"
layout: "reference"
description: "v2512 常见流体求解器通过 turbulenceProperties 配置湍流，RASModel 和 LESModel 分别指定 RAS 与 LES 模型。Foundation 分支采用的 momentumTransport 属于另一套配置接口。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>constant/turbulenceProperties</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>simulationType</code> · <code>laminar</code> · <code>RAS</code> · <code>LES</code> · <code>RASModel</code> · <code>turbulence</code> · <code>printCoeffs</code></p><h2>关联命令</h2><p><a href="/commands/?q=simpleFoam">simpleFoam</a> · <a href="/commands/?q=pimpleFoam">pimpleFoam</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary constant/turbulenceProperties -keywords
simpleFoam -help</code></pre><h2>9.6 constant/turbulenceProperties</h2><p>v2512 常见流体求解器通过 turbulenceProperties 配置湍流，RASModel 和 LESModel 分别指定 RAS 与 LES 模型。Foundation 分支采用的 momentumTransport 属于另一套配置接口。</p>
<pre><code>FoamFile
{
    version 2.0; format ascii;
    class dictionary; object turbulenceProperties;
}
simulationType RAS;
RAS
{
    RASModel kOmegaSST;
    turbulence on;
    printCoeffs on;
}</code></pre>
<p>层流采用 simulationType laminar;。LES 可采用 simulationType LES; LES { LESModel WALE; turbulence on; printCoeffs on; delta cubeRootVol; }。</p>
<p>LES 配置还需确定滤波宽度、近壁处理、入口脉动和时间分辨率，并与网格及边界条件配合。</p>
<h2>18.2 turbulenceProperties（湍流模型）</h2><pre><code>simulationType  RAS;          // laminar / RAS / LES

RAS
{
    RASModel        kOmegaSST;
    turbulence      on;
    printCoeffs     on;        // 启动时把模型系数打印到日志，便于确认
}
simulationType  LES;

LES
{
    LESModel        WALE;              // 或 Smagorinsky / kEqn / dynamicKEqn
    delta           cubeRootVol;       // 滤波尺度：cubeRootVol / vanDriest / smooth
    turbulence      on;
    printCoeffs     on;

    cubeRootVolCoeffs { deltaCoeff 1; }
}</code></pre>
<p>常用 RANS 模型怎么挑</p>
<div class="table-scroll"><table>
<tr><th>模型</th><th>特点</th><th>场合</th></tr>
<tr><td>kEpsilon</td><td>最经典，壁面靠壁函数</td><td>内流、自由剪切流</td></tr>
<tr><td>realizableKE</td><td>对旋转/分离更好</td><td>旋流</td></tr>
<tr><td>kOmegaSST</td><td>近壁用 \(k-\omega\)、远场用 \(k-\varepsilon\)，逆压梯度和分离预测好</td><td>外流绕流、翼型，最常用</td></tr>
<tr><td>SpalartAllmaras</td><td>单方程，便宜</td><td>航空外流</td></tr>
<tr><td>LaunderSharmaKE</td><td>低雷诺数版本，需要 \(y^{+}\approx 1\)</td><td>不用壁函数时</td></tr>
</table></div>
<p>v2512 的 kEpsilon 新增 twoLayerTreatment 开关，可以在近壁内层用代数关系式，降低对第一层网格的要求：</p>
<pre><code>RAS
{
    RASModel        kEpsilon;
    turbulence      on;
    kEpsilonCoeffs  { twoLayerTreatment true; }
}</code></pre>
<p>层流就写 simulationType laminar;，此时 0/ 里不需要 k、epsilon、nut 等文件。</p>
{% endraw %}