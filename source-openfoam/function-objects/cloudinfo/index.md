---
title: "cloudInfo"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-cloudinfo"
description: "颗粒云的数量、质量等概要"
---
{% raw %}
<p>颗粒云的数量、质量等概要</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    cloudInfo
    {
        type    cloudInfo;
        libs    (lagrangianFunctionObjects);
        log     true;
        timeStart 0.5;
        writeControl    writeTime;
        clouds  ( reactingCloud1 );
        selection
        {
            all
            {
                action  all;
            }
            T
            {
                action  subset;
                source  field;
                field   T;
                accept  (greater 280) and (less 300);
            }
            YH2O
            {
                action  subset;
                source  field;
                field   YH2O(l);
                accept  (greater 0.5);
            }
            diameter
            {
                action  subset;
                source  field;
                field   d;
                accept  (greater 1e-10);
            }
            Umin
            {
                action  subtract;
                source  field;
                field   U;
                accept  (less 0.1);
            }
        }
    }
}</code></pre><p>统计颗粒云的数量、质量等信息。示例选择 reactingCloud1，并按温度、组分、粒径及速度筛选颗粒；selection 各操作按顺序缩小或调整统计对象。</p><p>配套教程配置：<code>lagrangian/reactingParcelFoam/filter/system/cloudInfo</code>。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>cloudInfo</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(lagrangianFunctionObjects)</code></td></tr><tr><td><code>clouds</code></td><td>要处理的多个颗粒云名称或匹配表达式。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>selection</code></td><td>单元或颗粒的选择规则子字典。</td><td>可选</td><td><code>空字典</code></td></tr><tr><td><code>sampleOnExecute</code></td><td>在执行阶段采样并保存到内存，而不只在写出阶段采样。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>verbose</code></td><td>是否打印更详细的运行信息。</td><td>可选</td><td><code>false</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>统计颗粒云的数量、质量等信息。示例选择 reactingCloud1，并按温度、组分、粒径及速度筛选颗粒；selection 各操作按顺序缩小或调整统计对象。</p><pre><code class="language-foam">cloudInfo
{
    type    cloudInfo;
    libs    (lagrangianFunctionObjects);
    log     true;
    timeStart 0.5;
    writeControl    writeTime;
    clouds  ( reactingCloud1 );
    selection
    {
        all
        {
            action  all;
        }
        T
        {
            action  subset;
            source  field;
            field   T;
            accept  (greater 280) and (less 300);
        }
        YH2O
        {
            action  subset;
            source  field;
            field   YH2O(l);
            accept  (greater 0.5);
        }
        diameter
        {
            action  subset;
            source  field;
            field   d;
            accept  (greater 1e-10);
        }
        Umin
        {
            action  subtract;
            source  field;
            field   U;
            accept  (less 0.1);
        }
    }
}</code></pre><h3 id="example-2">示例 2 · 输出更多颗粒统计信息</h3><p>在日志中保留更详细的统计。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">verbose true;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">cloudInfo
{
    type    cloudInfo;
    libs    (lagrangianFunctionObjects);
    log     true;
    timeStart 0.5;
    writeControl    writeTime;
    clouds  ( reactingCloud1 );
    selection
    {
        all
        {
            action  all;
        }
        T
        {
            action  subset;
            source  field;
            field   T;
            accept  (greater 280) and (less 300);
        }
        YH2O
        {
            action  subset;
            source  field;
            field   YH2O(l);
            accept  (greater 0.5);
        }
        diameter
        {
            action  subset;
            source  field;
            field   d;
            accept  (greater 1e-10);
        }
        Umin
        {
            action  subtract;
            source  field;
            field   U;
            accept  (less 0.1);
        }
    }
    verbose true;
}</code></pre></details><h3 id="example-3">示例 3 · 每步更新内存统计</h3><p>让下游对象可以读取本步更新后的结果。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">sampleOnExecute true;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">cloudInfo
{
    type    cloudInfo;
    libs    (lagrangianFunctionObjects);
    log     true;
    timeStart 0.5;
    writeControl    writeTime;
    clouds  ( reactingCloud1 );
    selection
    {
        all
        {
            action  all;
        }
        T
        {
            action  subset;
            source  field;
            field   T;
            accept  (greater 280) and (less 300);
        }
        YH2O
        {
            action  subset;
            source  field;
            field   YH2O(l);
            accept  (greater 0.5);
        }
        diameter
        {
            action  subset;
            source  field;
            field   d;
            accept  (greater 1e-10);
        }
        Umin
        {
            action  subtract;
            source  field;
            field   U;
            accept  (less 0.1);
        }
    }
    sampleOnExecute true;
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">cloudInfo
{
    type    cloudInfo;
    libs    (lagrangianFunctionObjects);
    log     true;
    timeStart 0.5;
    writeControl timeStep;
    clouds  ( reactingCloud1 );
    selection
    {
        all
        {
            action  all;
        }
        T
        {
            action  subset;
            source  field;
            field   T;
            accept  (greater 280) and (less 300);
        }
        YH2O
        {
            action  subset;
            source  field;
            field   YH2O(l);
            accept  (greater 0.5);
        }
        diameter
        {
            action  subset;
            source  field;
            field   d;
            accept  (greater 1e-10);
        }
        Umin
        {
            action  subtract;
            source  field;
            field   U;
            accept  (less 0.1);
        }
    }
    writeInterval 10;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">cloudInfo
{
    type    cloudInfo;
    libs    (lagrangianFunctionObjects);
    log     true;
    timeStart 0.1;
    writeControl    writeTime;
    clouds  ( reactingCloud1 );
    selection
    {
        all
        {
            action  all;
        }
        T
        {
            action  subset;
            source  field;
            field   T;
            accept  (greater 280) and (less 300);
        }
        YH2O
        {
            action  subset;
            source  field;
            field   YH2O(l);
            accept  (greater 0.5);
        }
        diameter
        {
            action  subset;
            source  field;
            field   d;
            accept  (greater 1e-10);
        }
        Umin
        {
            action  subtract;
            source  field;
            field   U;
            accept  (less 0.1);
        }
    }
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E9%A2%97%E7%B2%92%E4%B8%8E%E4%B8%A4%E7%9B%B8">颗粒与两相速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-16">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/lagrangian/cloudInfo/cloudInfo.H">OpenFOAM v2512 · cloudInfo 接口</a>。</p>
{% endraw %}
