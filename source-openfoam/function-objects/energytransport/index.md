---
title: "energyTransport"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-energytransport"
description: "额外输运方程或流龄"
---
{% raw %}
<p>额外输运方程或流龄</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    sTransport
    {
        type            energyTransport;
        libs            (solverFunctionObjects);
        enabled         true;
        writeControl    writeTime;
        writeInterval   1;
        write           true;
        field           T;
        rho             rho;
        phi             rhoPhi;
        phaseThermos
        {
            alpha.air
            {
                Cp          1e3;
                kappa       0.0243;
            }
            alpha.mercury
            {
                Cp          140;
                kappa       8.2;
            }
            alpha.oil
            {
                Cp          2e3;
                kappa       0.2;
            }
            alpha.water
            {
                Cp          4e3;
                kappa       0.6;
            }
        }
        fvOptions
        {
            viscousDissipation
            {
                type            viscousDissipation;
                enabled         true;
                viscousDissipationCoeffs
                {
                    fields      (T);
                    rho         rho;
                }
            }
        }
    }
}</code></pre><p>在现有流动上求解附加能量输运。本例对 T 使用质量通量 rhoPhi，各相的 Cp 和 kappa 决定热容与导热，并可通过 fvOptions 加入热源。</p><p>配套教程配置：<code>multiphase/multiphaseInterFoam/laminar/mixerVessel2D/system/controlDict</code>。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>energyTransport</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(solverFunctionObjects)</code></td></tr><tr><td><code>field</code></td><td>输入场的名称。</td><td>可选</td><td><code>s</code></td></tr><tr><td><code>phi</code></td><td>面通量场名称。</td><td>可选</td><td><code>phi</code></td></tr><tr><td><code>rho</code></td><td>密度场名称；使用常密度时按示例选择 rhoInf。</td><td>可选</td><td><code>rho</code></td></tr><tr><td><code>Cp</code></td><td>定压比热容。</td><td>可选</td><td><code>0</code></td></tr><tr><td><code>kappa</code></td><td>导热系数。</td><td>可选</td><td><code>0</code></td></tr><tr><td><code>rhoInf</code></td><td>不可压缩计算使用的参考密度。</td><td>可选</td><td><code>0</code></td></tr><tr><td><code>Prt</code></td><td>湍流普朗特数。</td><td>可选</td><td><code>1</code></td></tr><tr><td><code>schemesField</code></td><td>从 fvSchemes 和 fvSolution 中读取离散与求解设置时使用的场名。</td><td>可选</td><td><code>field</code></td></tr><tr><td><code>tolerance</code></td><td>迭代或判定所用的容差，具体含义见本页说明。</td><td>可选</td><td><code>1</code></td></tr><tr><td><code>nCorr</code></td><td>外层校正迭代次数。</td><td>可选</td><td><code>0</code></td></tr><tr><td><code>fvOptions</code></td><td>额外源项、约束和校正的设置。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>phaseThermos</code></td><td>各相热物性的设置子字典。</td><td>可选</td><td><code>null</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>在现有流动上求解附加能量输运。本例对 T 使用质量通量 rhoPhi，各相的 Cp 和 kappa 决定热容与导热，并可通过 fvOptions 加入热源。</p><pre><code class="language-foam">sTransport
{
    type            energyTransport;
    libs            (solverFunctionObjects);
    enabled         true;
    writeControl    writeTime;
    writeInterval   1;
    write           true;
    field           T;
    rho             rho;
    phi             rhoPhi;
    phaseThermos
    {
        alpha.air
        {
            Cp          1e3;
            kappa       0.0243;
        }
        alpha.mercury
        {
            Cp          140;
            kappa       8.2;
        }
        alpha.oil
        {
            Cp          2e3;
            kappa       0.2;
        }
        alpha.water
        {
            Cp          4e3;
            kappa       0.6;
        }
    }
    fvOptions
    {
        viscousDissipation
        {
            type            viscousDissipation;
            enabled         true;
            viscousDissipationCoeffs
            {
                fields      (T);
                rho         rho;
            }
        }
    }
}</code></pre><h3 id="example-2">示例 2 · 增加温度校正</h3><p>对相同流场多执行校正，改善附加能量方程的代数求解。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">nCorr 2;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">sTransport
{
    type            energyTransport;
    libs            (solverFunctionObjects);
    enabled         true;
    writeControl    writeTime;
    writeInterval   1;
    write           true;
    field           T;
    rho             rho;
    phi             rhoPhi;
    phaseThermos
    {
        alpha.air
        {
            Cp          1e3;
            kappa       0.0243;
        }
        alpha.mercury
        {
            Cp          140;
            kappa       8.2;
        }
        alpha.oil
        {
            Cp          2e3;
            kappa       0.2;
        }
        alpha.water
        {
            Cp          4e3;
            kappa       0.6;
        }
    }
    fvOptions
    {
        viscousDissipation
        {
            type            viscousDissipation;
            enabled         true;
            viscousDissipationCoeffs
            {
                fields      (T);
                rho         rho;
            }
        }
    }
    nCorr 2;
}</code></pre></details><h3 id="example-3">示例 3 · 设置明确的停止容差</h3><p>根据温度方程的初始残差控制校正过程。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">tolerance 1e-6;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">sTransport
{
    type            energyTransport;
    libs            (solverFunctionObjects);
    enabled         true;
    writeControl    writeTime;
    writeInterval   1;
    write           true;
    field           T;
    rho             rho;
    phi             rhoPhi;
    phaseThermos
    {
        alpha.air
        {
            Cp          1e3;
            kappa       0.0243;
        }
        alpha.mercury
        {
            Cp          140;
            kappa       8.2;
        }
        alpha.oil
        {
            Cp          2e3;
            kappa       0.2;
        }
        alpha.water
        {
            Cp          4e3;
            kappa       0.6;
        }
    }
    fvOptions
    {
        viscousDissipation
        {
            type            viscousDissipation;
            enabled         true;
            viscousDissipationCoeffs
            {
                fields      (T);
                rho         rho;
            }
        }
    }
    tolerance 1e-6;
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">sTransport
{
    type            energyTransport;
    libs            (solverFunctionObjects);
    enabled         true;
    writeControl timeStep;
    writeInterval 10;
    write           true;
    field           T;
    rho             rho;
    phi             rhoPhi;
    phaseThermos
    {
        alpha.air
        {
            Cp          1e3;
            kappa       0.0243;
        }
        alpha.mercury
        {
            Cp          140;
            kappa       8.2;
        }
        alpha.oil
        {
            Cp          2e3;
            kappa       0.2;
        }
        alpha.water
        {
            Cp          4e3;
            kappa       0.6;
        }
    }
    fvOptions
    {
        viscousDissipation
        {
            type            viscousDissipation;
            enabled         true;
            viscousDissipationCoeffs
            {
                fields      (T);
                rho         rho;
            }
        }
    }
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">sTransport
{
    type            energyTransport;
    libs            (solverFunctionObjects);
    enabled         true;
    writeControl    writeTime;
    writeInterval   1;
    write           true;
    field           T;
    rho             rho;
    phi             rhoPhi;
    phaseThermos
    {
        alpha.air
        {
            Cp          1e3;
            kappa       0.0243;
        }
        alpha.mercury
        {
            Cp          140;
            kappa       8.2;
        }
        alpha.oil
        {
            Cp          2e3;
            kappa       0.2;
        }
        alpha.water
        {
            Cp          4e3;
            kappa       0.6;
        }
    }
    fvOptions
    {
        viscousDissipation
        {
            type            viscousDissipation;
            enabled         true;
            viscousDissipationCoeffs
            {
                fields      (T);
                rho         rho;
            }
        }
    }
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E5%8A%9B%E4%B8%8E%E7%89%A9%E7%90%86%E9%87%8F">力与物理量速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-16">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/solvers/energyTransport/energyTransport.H">OpenFOAM v2512 · energyTransport 接口</a>。</p>
{% endraw %}
