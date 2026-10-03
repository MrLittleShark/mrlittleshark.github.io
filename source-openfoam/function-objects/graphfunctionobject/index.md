---
title: "graphFunctionObject"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-graphfunctionobject"
description: "报告汇总与监测量曲线输出"
---
{% raw %}
<p>报告汇总与监测量曲线输出</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    forceCoeffsGraph1
    {
        type            graphFunctionObject;
        libs            (utilityFunctionObjects);
        writeControl    writeTime;
        logScaleX       no;
        logScaleY       no;
        xLabel          &quot;Iteration&quot;;
        yLabel          &quot;Coefficient&quot;;
        yMin            -1;
        yMax            1;
        functions
        {
            Cd
            {
                object      forceCoeffs1;
                entry       Cd;
            }
            Cd(f)
            {
                object      forceCoeffs1;
                entry       Cd(f);
            }
            Cd(r)
            {
                object      forceCoeffs1;
                entry       Cd(r);
            }
            Cl
            {
                object      forceCoeffs1;
                entry       Cl;
            }
            Cl(f)
            {
                object      forceCoeffs1;
                entry       Cl(f);
                title       Cl(f);
            }
            Cl(r)
            {
                object      forceCoeffs1;
                entry       Cl(r);
                title       Cl(r);
            }
        }
    }
}</code></pre><p>将其他功能对象的数值结果绘制为 SVG 曲线。本例从 forceCoeffs1 读取 Cd、Cl 等系数，functions 中每个子字典定义一条曲线。</p><p>配套教程配置：<code>incompressible/simpleFoam/motorBike/system/graphFunctionObject</code>。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>graphFunctionObject</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(utilityFunctionObjects)</code></td></tr><tr><td><code>functions</code></td><td>子功能对象或曲线的定义子字典。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>width</code></td><td>SVG 图像宽度，单位像素。</td><td>可选</td><td><code>800</code></td></tr><tr><td><code>height</code></td><td>SVG 图像高度，单位像素。</td><td>可选</td><td><code>600</code></td></tr><tr><td><code>xMin</code></td><td>横坐标下限。</td><td>可选</td><td><code>自动计算</code></td></tr><tr><td><code>xMax</code></td><td>横坐标上限。</td><td>可选</td><td><code>自动计算</code></td></tr><tr><td><code>yMin</code></td><td>纵坐标下限。</td><td>可选</td><td><code>自动计算</code></td></tr><tr><td><code>yMax</code></td><td>纵坐标上限。</td><td>可选</td><td><code>自动计算</code></td></tr><tr><td><code>xLabel</code></td><td>横坐标标签。</td><td>可选</td><td><code>Iteration/Time</code></td></tr><tr><td><code>yLabel</code></td><td>纵坐标标签。</td><td>可选</td><td><code>Property</code></td></tr><tr><td><code>strokeWidth</code></td><td>曲线线宽，单位像素。</td><td>可选</td><td><code>2</code></td></tr><tr><td><code>logScaleX</code></td><td>是否使用对数横坐标。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>logScaleY</code></td><td>是否使用对数纵坐标。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>drawGrid</code></td><td>是否绘制图中网格线。</td><td>可选</td><td><code>true</code></td></tr><tr><td><code>functions.&lt;曲线名&gt;.object</code></td><td>提供曲线数据的功能对象名称。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>functions.&lt;曲线名&gt;.entry</code></td><td>上游功能对象中需要绘制的结果条目名称。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>functions.&lt;曲线名&gt;.colour</code></td><td>曲线的 RGB 颜色。</td><td>可选</td><td><code>auto</code></td></tr><tr><td><code>functions.&lt;曲线名&gt;.dashes</code></td><td>虚线的实线段与间隔长度。</td><td>可选</td><td><code>auto</code></td></tr><tr><td><code>functions.&lt;曲线名&gt;.title</code></td><td>曲线标题。</td><td>可选</td><td><code>子字典名称</code></td></tr><tr><td><code>writeToFile</code></td><td>是否保存统计文本文件</td><td>可选</td><td><code>true</code></td></tr><tr><td><code>writePrecision</code></td><td>文本数值的有效位数</td><td>可选</td><td><code>全局写出精度</code></td></tr><tr><td><code>useUserTime</code></td><td>是否采用用户时间单位</td><td>可选</td><td><code>true</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>将其他功能对象的数值结果绘制为 SVG 曲线。本例从 forceCoeffs1 读取 Cd、Cl 等系数，functions 中每个子字典定义一条曲线。</p><pre><code class="language-foam">forceCoeffsGraph1
{
    type            graphFunctionObject;
    libs            (utilityFunctionObjects);
    writeControl    writeTime;
    logScaleX       no;
    logScaleY       no;
    xLabel          &quot;Iteration&quot;;
    yLabel          &quot;Coefficient&quot;;
    yMin            -1;
    yMax            1;
    functions
    {
        Cd
        {
            object      forceCoeffs1;
            entry       Cd;
        }
        Cd(f)
        {
            object      forceCoeffs1;
            entry       Cd(f);
        }
        Cd(r)
        {
            object      forceCoeffs1;
            entry       Cd(r);
        }
        Cl
        {
            object      forceCoeffs1;
            entry       Cl;
        }
        Cl(f)
        {
            object      forceCoeffs1;
            entry       Cl(f);
            title       Cl(f);
        }
        Cl(r)
        {
            object      forceCoeffs1;
            entry       Cl(r);
            title       Cl(r);
        }
    }
}</code></pre><h3 id="example-2">示例 2 · 扩大图像尺寸</h3><p>为多条曲线和图例提供更多像素。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">width 1200;
height 800;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">forceCoeffsGraph1
{
    type            graphFunctionObject;
    libs            (utilityFunctionObjects);
    writeControl    writeTime;
    logScaleX       no;
    logScaleY       no;
    xLabel          &quot;Iteration&quot;;
    yLabel          &quot;Coefficient&quot;;
    yMin            -1;
    yMax            1;
    functions
    {
        Cd
        {
            object      forceCoeffs1;
            entry       Cd;
        }
        Cd(f)
        {
            object      forceCoeffs1;
            entry       Cd(f);
        }
        Cd(r)
        {
            object      forceCoeffs1;
            entry       Cd(r);
        }
        Cl
        {
            object      forceCoeffs1;
            entry       Cl;
        }
        Cl(f)
        {
            object      forceCoeffs1;
            entry       Cl(f);
            title       Cl(f);
        }
        Cl(r)
        {
            object      forceCoeffs1;
            entry       Cl(r);
            title       Cl(r);
        }
    }
    width 1200;
    height 800;
}</code></pre></details><h3 id="example-3">示例 3 · 限定系数显示范围</h3><p>聚焦较小的系数变化，并使用网格辅助读数。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">yMin -0.5;
yMax 0.5;
drawGrid true;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">forceCoeffsGraph1
{
    type            graphFunctionObject;
    libs            (utilityFunctionObjects);
    writeControl    writeTime;
    logScaleX       no;
    logScaleY       no;
    xLabel          &quot;Iteration&quot;;
    yLabel          &quot;Coefficient&quot;;
    yMin -0.5;
    yMax 0.5;
    functions
    {
        Cd
        {
            object      forceCoeffs1;
            entry       Cd;
        }
        Cd(f)
        {
            object      forceCoeffs1;
            entry       Cd(f);
        }
        Cd(r)
        {
            object      forceCoeffs1;
            entry       Cd(r);
        }
        Cl
        {
            object      forceCoeffs1;
            entry       Cl;
        }
        Cl(f)
        {
            object      forceCoeffs1;
            entry       Cl(f);
            title       Cl(f);
        }
        Cl(r)
        {
            object      forceCoeffs1;
            entry       Cl(r);
            title       Cl(r);
        }
    }
    drawGrid true;
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">forceCoeffsGraph1
{
    type            graphFunctionObject;
    libs            (utilityFunctionObjects);
    writeControl timeStep;
    logScaleX       no;
    logScaleY       no;
    xLabel          &quot;Iteration&quot;;
    yLabel          &quot;Coefficient&quot;;
    yMin            -1;
    yMax            1;
    functions
    {
        Cd
        {
            object      forceCoeffs1;
            entry       Cd;
        }
        Cd(f)
        {
            object      forceCoeffs1;
            entry       Cd(f);
        }
        Cd(r)
        {
            object      forceCoeffs1;
            entry       Cd(r);
        }
        Cl
        {
            object      forceCoeffs1;
            entry       Cl;
        }
        Cl(f)
        {
            object      forceCoeffs1;
            entry       Cl(f);
            title       Cl(f);
        }
        Cl(r)
        {
            object      forceCoeffs1;
            entry       Cl(r);
            title       Cl(r);
        }
    }
    writeInterval 10;
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">forceCoeffsGraph1
{
    type            graphFunctionObject;
    libs            (utilityFunctionObjects);
    writeControl    writeTime;
    logScaleX       no;
    logScaleY       no;
    xLabel          &quot;Iteration&quot;;
    yLabel          &quot;Coefficient&quot;;
    yMin            -1;
    yMax            1;
    functions
    {
        Cd
        {
            object      forceCoeffs1;
            entry       Cd;
        }
        Cd(f)
        {
            object      forceCoeffs1;
            entry       Cd(f);
        }
        Cd(r)
        {
            object      forceCoeffs1;
            entry       Cd(r);
        }
        Cl
        {
            object      forceCoeffs1;
            entry       Cl;
        }
        Cl(f)
        {
            object      forceCoeffs1;
            entry       Cl(f);
            title       Cl(f);
        }
        Cl(r)
        {
            object      forceCoeffs1;
            entry       Cl(r);
            title       Cl(r);
        }
    }
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E6%96%87%E4%BB%B6%E4%B8%8E%E6%8E%A7%E5%88%B6">文件与控制速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-16">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/utilities/graphFunctionObject/graphFunctionObject.H">OpenFOAM v2512 · graphFunctionObject 接口</a>。</p>
{% endraw %}
