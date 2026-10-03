---
title: "scalarTransport"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-scalartransport"
description: "额外输运方程或流龄"
---
{% raw %}
<p>额外输运方程或流龄</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    tracer0
    {
        type  scalarTransport;
        libs  (solverFunctionObjects);
        log   off;
        resetOnStartUp  false;
        writeControl    writeTime;
        field           tracer0;
        D               0.001;
    }
}</code></pre><p>在已有速度或通量场中额外求解被动标量。本例对 tracer0 使用 0.001 的扩散系数；算例需要 tracer0 的初始与边界条件，以及离散和求解设置。</p><p>配套教程配置：<code>compressible/rhoSimpleFoam/gasMixing/injectorPipe/system/scalarTransport</code>。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>scalarTransport</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(solverFunctionObjects)</code></td></tr><tr><td><code>field</code></td><td>输入场的名称。</td><td>可选</td><td><code>s</code></td></tr><tr><td><code>phi</code></td><td>面通量场名称。</td><td>可选</td><td><code>phi</code></td></tr><tr><td><code>rho</code></td><td>密度场名称；使用常密度时按示例选择 rhoInf。</td><td>可选</td><td><code>rho</code></td></tr><tr><td><code>nut</code></td><td>湍流运动黏度场名称。</td><td>可选</td><td><code>none</code></td></tr><tr><td><code>phase</code></td><td>处理的相名称。</td><td>可选</td><td><code>none</code></td></tr><tr><td><code>phasePhiCompressed</code></td><td>VOF 压缩输运使用的相通量场名称。</td><td>可选</td><td><code>alphaPhiUn</code></td></tr><tr><td><code>schemesField</code></td><td>从 fvSchemes 和 fvSolution 中读取离散与求解设置时使用的场名。</td><td>可选</td><td><code>field</code></td></tr><tr><td><code>bounded01</code></td><td>多相标量输运时将标量限制在 0 到 1。</td><td>可选</td><td><code>true</code></td></tr><tr><td><code>D</code></td><td>扩散系数。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>alphaD</code></td><td>层流扩散项的比例系数。</td><td>可选</td><td><code>1</code></td></tr><tr><td><code>alphaDt</code></td><td>湍流扩散项的比例系数。</td><td>可选</td><td><code>1</code></td></tr><tr><td><code>tolerance</code></td><td>迭代或判定所用的容差，具体含义见本页说明。</td><td>可选</td><td><code>1</code></td></tr><tr><td><code>nCorr</code></td><td>外层校正迭代次数。</td><td>可选</td><td><code>0</code></td></tr><tr><td><code>resetOnStartUp</code></td><td>启动时是否将输运标量重新设为零。</td><td>可选</td><td><code>no</code></td></tr><tr><td><code>fvOptions</code></td><td>额外源项、约束和校正的设置。</td><td>可选</td><td><code>—</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>在已有速度或通量场中额外求解被动标量。本例对 tracer0 使用 0.001 的扩散系数；算例需要 tracer0 的初始与边界条件，以及离散和求解设置。</p><pre><code class="language-foam">tracer0
{
    type  scalarTransport;
    libs  (solverFunctionObjects);
    log   off;
    resetOnStartUp  false;
    writeControl    writeTime;
    field           tracer0;
    D               0.001;
}</code></pre><h3 id="example-2">示例 2 · 减小分子扩散</h3><p>降低扩散后，标量分布更受对流支配；应同时检查网格和对流格式。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">D 0.0001;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">tracer0
{
    type  scalarTransport;
    libs  (solverFunctionObjects);
    log   off;
    resetOnStartUp  false;
    writeControl    writeTime;
    field           tracer0;
    D 0.0001;
}</code></pre></details><h3 id="example-3">示例 3 · 启动时清零标量</h3><p>以新的零初始分布开始标量输运，入口注入条件仍由场边界决定。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">resetOnStartUp true;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">tracer0
{
    type  scalarTransport;
    libs  (solverFunctionObjects);
    log   off;
    resetOnStartUp true;
    writeControl    writeTime;
    field           tracer0;
    D               0.001;
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">tracer0
{
    type  scalarTransport;
    libs  (solverFunctionObjects);
    log   off;
    resetOnStartUp  false;
    writeControl timeStep;
    field           tracer0;
    D               0.001;
    writeInterval 10;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">tracer0
{
    type  scalarTransport;
    libs  (solverFunctionObjects);
    log   off;
    resetOnStartUp  false;
    writeControl    writeTime;
    field           tracer0;
    D               0.001;
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E5%8A%9B%E4%B8%8E%E7%89%A9%E7%90%86%E9%87%8F">力与物理量速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-16">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/solvers/scalarTransport/scalarTransport.H">OpenFOAM v2512 · scalarTransport 接口</a>。</p>
{% endraw %}
