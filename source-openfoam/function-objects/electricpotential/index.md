---
title: "electricPotential"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-electricpotential"
description: "电势方程与相关量"
---
{% raw %}
<p>电势方程与相关量</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    electricPotential
    {
        type            electricPotential;
        libs            (solverFunctionObjects);
        phases
        {
            alpha.air
            {
                epsilonr      1.12940906737;
                sigma         1e-10;
            }
            alpha.water
            {
                epsilonr      3.38822720212;
                sigma         0.14;
            }
        }
        nCorr                 1;
        writeDerivedFields    true;
        region          region0;
        enabled         true;
        log             true;
        timeStart       0;
        timeEnd         100;
        executeControl  timeStep;
        executeInterval 1;
        writeControl    writeTime;
        writeInterval 1;
    }
}</code></pre><p>在现有流场上求解电势方程，并可输出电场等派生量。示例为两相分别设置电导率和介电常数；算例还要准备电势边界及对应的线性求解配置。</p><p>配套教程配置：<code>multiphase/interFoam/RAS/electrostaticDeposition/system/FOelectricPotential</code>。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>electricPotential</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(solverFunctionObjects)</code></td></tr><tr><td><code>sigma</code></td><td>电导率。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>epsilonr</code></td><td>相对介电常数。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>nCorr</code></td><td>外层校正迭代次数。</td><td>可选</td><td><code>1</code></td></tr><tr><td><code>writeDerivedFields</code></td><td>是否写出派生物理量。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>V</code></td><td>电势场名称。</td><td>可选</td><td><code>electricPotential:V</code></td></tr><tr><td><code>electricField</code></td><td>是否计算电场。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>E</code></td><td>电场名称。</td><td>可选</td><td><code>electricPotential:E</code></td></tr><tr><td><code>fvOptions</code></td><td>额外源项、约束和校正的设置。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>tolerance</code></td><td>迭代或判定所用的容差，具体含义见本页说明。</td><td>可选</td><td><code>1</code></td></tr><tr><td><code>phases</code></td><td>多相电导率和介电常数子字典，按相分数场命名</td><td>多相时使用</td><td><code>—</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>在现有流场上求解电势方程，并可输出电场等派生量。示例为两相分别设置电导率和介电常数；算例还要准备电势边界及对应的线性求解配置。</p><pre><code class="language-foam">electricPotential
{
    type            electricPotential;
    libs            (solverFunctionObjects);
    phases
    {
        alpha.air
        {
            epsilonr      1.12940906737;
            sigma         1e-10;
        }
        alpha.water
        {
            epsilonr      3.38822720212;
            sigma         0.14;
        }
    }
    nCorr                 1;
    writeDerivedFields    true;
    region          region0;
    enabled         true;
    log             true;
    timeStart       0;
    timeEnd         100;
    executeControl  timeStep;
    executeInterval 1;
    writeControl    writeTime;
    writeInterval 1;
}</code></pre><h3 id="example-2">示例 2 · 只保存电势</h3><p>先检查电势边界与分布，减少派生字段。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeDerivedFields false;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">electricPotential
{
    type            electricPotential;
    libs            (solverFunctionObjects);
    phases
    {
        alpha.air
        {
            epsilonr      1.12940906737;
            sigma         1e-10;
        }
        alpha.water
        {
            epsilonr      3.38822720212;
            sigma         0.14;
        }
    }
    nCorr                 1;
    writeDerivedFields false;
    region          region0;
    enabled         true;
    log             true;
    timeStart       0;
    timeEnd         100;
    executeControl  timeStep;
    executeInterval 1;
    writeControl    writeTime;
    writeInterval 1;
}</code></pre></details><h3 id="example-3">示例 3 · 增加电势校正</h3><p>增加外层校正次数，观察电势方程的迭代变化。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">nCorr 3;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">electricPotential
{
    type            electricPotential;
    libs            (solverFunctionObjects);
    phases
    {
        alpha.air
        {
            epsilonr      1.12940906737;
            sigma         1e-10;
        }
        alpha.water
        {
            epsilonr      3.38822720212;
            sigma         0.14;
        }
    }
    nCorr 3;
    writeDerivedFields    true;
    region          region0;
    enabled         true;
    log             true;
    timeStart       0;
    timeEnd         100;
    executeControl  timeStep;
    executeInterval 1;
    writeControl    writeTime;
    writeInterval 1;
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">electricPotential
{
    type            electricPotential;
    libs            (solverFunctionObjects);
    phases
    {
        alpha.air
        {
            epsilonr      1.12940906737;
            sigma         1e-10;
        }
        alpha.water
        {
            epsilonr      3.38822720212;
            sigma         0.14;
        }
    }
    nCorr                 1;
    writeDerivedFields    true;
    region          region0;
    enabled         true;
    log             true;
    timeStart       0;
    timeEnd         100;
    executeControl  timeStep;
    executeInterval 1;
    writeControl timeStep;
    writeInterval 10;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">electricPotential
{
    type            electricPotential;
    libs            (solverFunctionObjects);
    phases
    {
        alpha.air
        {
            epsilonr      1.12940906737;
            sigma         1e-10;
        }
        alpha.water
        {
            epsilonr      3.38822720212;
            sigma         0.14;
        }
    }
    nCorr                 1;
    writeDerivedFields    true;
    region          region0;
    enabled         true;
    log             true;
    timeStart 0.1;
    timeEnd 0.5;
    executeControl  timeStep;
    executeInterval 1;
    writeControl    writeTime;
    writeInterval 1;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E5%8A%9B%E4%B8%8E%E7%89%A9%E7%90%86%E9%87%8F">力与物理量速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-16">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/solvers/electricPotential/electricPotential.H">OpenFOAM v2512 · electricPotential 接口</a>。</p>
{% endraw %}
