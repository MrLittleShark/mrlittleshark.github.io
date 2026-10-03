---
title: "fieldAverage"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-fieldaverage"
description: "计算场的时间平均值与脉动二阶矩。"
---
{% raw %}
<p>计算场的时间平均值与脉动二阶矩。</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    averages
    {
        type fieldAverage;
        libs (fieldFunctionObjects);

        writeControl writeTime;
        writeInterval 1;
        timeStart 0.1;
        executeControl timeStep;
        executeInterval 1;
        restartOnRestart false;
        fields
        (
            U { mean yes; prime2Mean yes; base time; }
            p { mean yes; prime2Mean no; base time; }
        );
    }
}</code></pre><p>按字段分别累积时间平均和二阶脉动矩。本例从 0.1 s 开始统计，U 同时生成 UMean 和 UPrime2Mean，p 只生成 pMean。base time 使可变时间步按实际时长加权。</p><p>示例算例：顶盖驱动方腔。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>fieldAverage</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(fieldFunctionObjects)</code></td></tr><tr><td><code>fields</code></td><td>每个字段的平均设置列表；内部填写 mean、prime2Mean 和 base。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>restartOnRestart</code></td><td>重新启动计算时重新开始累积平均值。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>restartOnOutput</code></td><td>每次保存后重新开始累积平均值。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>periodicRestart</code></td><td>是否按固定周期重新开始平均。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>restartPeriod</code></td><td>周期性重置平均的时间间隔。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>restartTime</code></td><td>到指定时间时执行一次平均重置。</td><td>可选</td><td><code>GREAT</code></td></tr><tr><td><code>subRegion</code></td><td>存放采样表面等数据的子对象数据库名称。</td><td>可选</td><td><code>&quot;&quot;</code></td></tr><tr><td><code>fields.&lt;场名&gt;.mean</code></td><td>是否计算平均场</td><td>必填</td><td><code>true / false</code></td></tr><tr><td><code>fields.&lt;场名&gt;.prime2Mean</code></td><td>是否计算二阶脉动矩</td><td>必填</td><td><code>true / false</code></td></tr><tr><td><code>fields.&lt;场名&gt;.base</code></td><td>time 按时间加权，iteration 按样本数统计</td><td>必填</td><td><code>time / iteration</code></td></tr><tr><td><code>fields.&lt;场名&gt;.window</code></td><td>该字段的平均窗口长度</td><td>可选</td><td><code>累计整个统计时段</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>按字段分别累积时间平均和二阶脉动矩。本例从 0.1 s 开始统计，U 同时生成 UMean 和 UPrime2Mean，p 只生成 pMean。base time 使可变时间步按实际时长加权。</p><pre><code class="language-foam">averages
{
    type fieldAverage;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
    timeStart 0.1;
    executeControl timeStep;
    executeInterval 1;
    restartOnRestart false;
    fields
    (
        U { mean yes; prime2Mean yes; base time; }
        p { mean yes; prime2Mean no; base time; }
    );
}</code></pre><h3 id="example-2">示例 2 · 重启时重新开始平均</h3><p>适合把本次重启后的计算当成新的统计阶段；此前保存的累计时间不会继续合并到新平均中。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">restartOnRestart true;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">averages
{
    type fieldAverage;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
    timeStart 0.1;
    executeControl timeStep;
    executeInterval 1;
    restartOnRestart true;
    fields
    (
        U { mean yes; prime2Mean yes; base time; }
        p { mean yes; prime2Mean no; base time; }
    );
}</code></pre></details><h3 id="example-3">示例 3 · 每次输出后重新统计</h3><p>按相邻两次输出之间的时间段分别求平均，可比较不同时段的流动。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">restartOnOutput true;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">averages
{
    type fieldAverage;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
    timeStart 0.1;
    executeControl timeStep;
    executeInterval 1;
    restartOnRestart false;
    fields
    (
        U { mean yes; prime2Mean yes; base time; }
        p { mean yes; prime2Mean no; base time; }
    );
    restartOnOutput true;
}</code></pre></details><h3 id="example-4">示例 4 · 每十步保存一次</h3><p>执行与保存分别设置：本段只降低保存频率。瞬态计算中对应十个时间步，稳态计算中通常对应十次迭代。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 10;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">averages
{
    type fieldAverage;
    libs (fieldFunctionObjects);

    writeControl timeStep;
    writeInterval 10;
    timeStart 0.1;
    executeControl timeStep;
    executeInterval 1;
    restartOnRestart false;
    fields
    (
        U { mean yes; prime2Mean yes; base time; }
        p { mean yes; prime2Mean no; base time; }
    );
}</code></pre></details><h3 id="example-5">示例 5 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">averages
{
    type fieldAverage;
    libs (fieldFunctionObjects);

    writeControl writeTime;
    writeInterval 1;
    timeStart 0.1;
    executeControl timeStep;
    executeInterval 1;
    restartOnRestart false;
    fields
    (
        U { mean yes; prime2Mean yes; base time; }
        p { mean yes; prime2Mean no; base time; }
    );
    timeEnd 0.5;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E9%87%87%E6%A0%B7%E4%B8%8E%E7%BB%9F%E8%AE%A1">采样与统计速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-08">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/field/fieldAverage/fieldAverage.H">OpenFOAM v2512 · fieldAverage 接口</a>。</p>
{% endraw %}
