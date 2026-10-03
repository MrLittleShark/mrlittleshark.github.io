---
title: "forceCoeffs"
layout: "reference"
section: "function-objects"
cms_slug: "function-object-forcecoeffs"
description: "计算升力、阻力与力矩系数。"
---
{% raw %}
<p>计算升力、阻力与力矩系数。</p><h2 id="usage">配置方法</h2><p>将下面的对象放入 system/controlDict 的 functions 字典。对象名可以自定；type 选择工具，libs 加载实现它的库。</p><pre><code class="language-foam">functions
{
    wallCoefficients
    {
        type forceCoeffs;
        libs (forces);

        writeControl timeStep;
        writeInterval 10;
        patches (upperWall lowerWall);
        rho rhoInf;
        rhoInf 1;
        CofR (0 0 0);
        dragDir (1 0 0);
        liftDir (0 1 0);
        magUInf 10;
        lRef 0.0254;
        Aref 0.0000254;
    }
}</code></pre><p>把压力和黏性载荷转换为无量纲系数。力系数的分母使用 0.5×rhoInf×magUInf²×Aref；力矩系数还要乘参考长度 lRef。参考值应对应所研究物体及来流。</p><p>示例算例：后台阶湍流。</p><p>完整的配置放置与运行方法见 <a href="/function-objects/usage/">functionObject 配置说明</a>。</p><h2 id="parameters">参数说明</h2><div class="table-scroll"><table><thead><tr><th>参数</th><th>含义与设置</th><th>填写条件</th><th>默认值 / 示例</th></tr></thead><tbody><tr><td><code>type</code></td><td>功能对象的类型名，大小写与工具名称一致。</td><td>必填</td><td><code>forceCoeffs</code></td></tr><tr><td><code>libs</code></td><td>加载实现该工具的共享库。</td><td>必填</td><td><code>(forces)</code></td></tr><tr><td><code>patches</code></td><td>需要处理的边界名称列表；支持名称匹配表达式。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>coefficients</code></td><td>需要输出的力或力矩系数名称列表。</td><td>可选</td><td><code>—</code></td></tr><tr><td><code>magUInf</code></td><td>计算无量纲力系数的参考速度大小。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>lRef</code></td><td>计算力矩系数的参考长度。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>Aref</code></td><td>计算力系数的参考面积。</td><td>必填</td><td><code>—</code></td></tr><tr><td><code>directForceDensity</code></td><td>true 时直接读取体积力密度场；false 时根据压力与黏性应力计算。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>porosity</code></td><td>是否计入多孔区域的阻力贡献。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>writeFields</code></td><td>是否将计算得到的场或所选原始场写出。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>useNamePrefix</code></td><td>在输出名称前加对象名前缀，便于区分多个同类对象。</td><td>可选</td><td><code>false</code></td></tr><tr><td><code>CofR</code></td><td>计算力矩使用的参考中心坐标。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>origin</code></td><td>局部坐标系或旋转轴的原点。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>e3</code></td><td>局部坐标系的第三基向量。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>e1</code></td><td>局部坐标系的第一基向量。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>coordinateSystem</code></td><td>局部坐标系子字典，包含原点与轴向设置。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>fD</code></td><td>directForceDensity 为 true 时使用的力密度场名称。</td><td>条件必填</td><td><code>fD</code></td></tr><tr><td><code>p</code></td><td>压力场名称。</td><td>条件必填</td><td><code>p</code></td></tr><tr><td><code>U</code></td><td>速度场名称。</td><td>条件必填</td><td><code>U</code></td></tr><tr><td><code>rho</code></td><td>密度场名称；使用常密度时按示例选择 rhoInf。</td><td>条件必填</td><td><code>rho</code></td></tr><tr><td><code>rhoInf</code></td><td>不可压缩计算使用的参考密度。</td><td>条件必填</td><td><code>—</code></td></tr><tr><td><code>pRef</code></td><td>参考压力。</td><td>条件必填</td><td><code>0</code></td></tr><tr><td><code>dragDir</code></td><td>阻力方向的单位向量。</td><td>条件必填</td><td><code>(1 0 0)</code></td></tr><tr><td><code>sideDir</code></td><td>侧向力方向的单位向量。</td><td>条件必填</td><td><code>(0 1 0)</code></td></tr><tr><td><code>liftDir</code></td><td>升力方向的单位向量。</td><td>条件必填</td><td><code>(0 0 1)</code></td></tr><tr><td><code>rollAxis</code></td><td>滚转力矩的轴向。</td><td>条件必填</td><td><code>(1 0 0)</code></td></tr><tr><td><code>pitchAxis</code></td><td>俯仰力矩的轴向。</td><td>条件必填</td><td><code>(0 1 0)</code></td></tr><tr><td><code>yawAxis</code></td><td>偏航力矩的轴向。</td><td>条件必填</td><td><code>(0 0 1)</code></td></tr><tr><td><code>writeToFile</code></td><td>是否保存统计文本文件</td><td>可选</td><td><code>true</code></td></tr><tr><td><code>writePrecision</code></td><td>文本数值的有效位数</td><td>可选</td><td><code>全局写出精度</code></td></tr><tr><td><code>useUserTime</code></td><td>是否采用用户时间单位</td><td>可选</td><td><code>true</code></td></tr></tbody></table></div><h3 id="scheduling">执行与保存</h3><div class="table-scroll"><table><thead><tr><th>参数</th><th>可设置的值</th><th>默认</th><th>作用</th></tr></thead><tbody><tr><td><code>enabled</code></td><td>true / false</td><td><code>true</code></td><td>是否启用当前对象。</td></tr><tr><td><code>executeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>计算或更新数据的时机。</td></tr><tr><td><code>executeInterval</code></td><td>正数</td><td><code>1</code></td><td>执行间隔；timeStep 按步数，runTime 按模拟时间。</td></tr><tr><td><code>writeControl</code></td><td>timeStep、writeTime、runTime、onEnd、none</td><td><code>timeStep</code></td><td>保存结果的时机，与执行阶段分别控制。</td></tr><tr><td><code>writeInterval</code></td><td>正数</td><td><code>1</code></td><td>写出间隔；writeTime 下表示每几次主输出保存一次。</td></tr><tr><td><code>timeStart</code></td><td>模拟时间</td><td><code>0</code></td><td>开始执行当前对象的时间。</td></tr><tr><td><code>timeEnd</code></td><td>模拟时间</td><td><code>运行结束</code></td><td>结束执行当前对象的时间。</td></tr></tbody></table></div><h2 id="examples">配置示例</h2><p>以下各例单独使用。变更参数的示例沿用上面的输入字段、几何和模型设置。</p><h3 id="example-1">示例 1 · 基本配置</h3><p>把压力和黏性载荷转换为无量纲系数。力系数的分母使用 0.5×rhoInf×magUInf²×Aref；力矩系数还要乘参考长度 lRef。参考值应对应所研究物体及来流。</p><pre><code class="language-foam">wallCoefficients
{
    type forceCoeffs;
    libs (forces);

    writeControl timeStep;
    writeInterval 10;
    patches (upperWall lowerWall);
    rho rhoInf;
    rhoInf 1;
    CofR (0 0 0);
    dragDir (1 0 0);
    liftDir (0 1 0);
    magUInf 10;
    lRef 0.0254;
    Aref 0.0000254;
}</code></pre><h3 id="example-2">示例 2 · 只计算下壁面的系数</h3><p>保持相同参考速度、面积和长度，单独比较下壁面对载荷系数的贡献。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">patches (lowerWall);</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">wallCoefficients
{
    type forceCoeffs;
    libs (forces);

    writeControl timeStep;
    writeInterval 10;
    patches (lowerWall);
    rho rhoInf;
    rhoInf 1;
    CofR (0 0 0);
    dragDir (1 0 0);
    liftDir (0 1 0);
    magUInf 10;
    lRef 0.0254;
    Aref 0.0000254;
}</code></pre></details><h3 id="example-3">示例 3 · 保存系数对应的场</h3><p>在总体系数之外保存空间分布，便于分析压力与黏性贡献的位置。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeFields true;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">wallCoefficients
{
    type forceCoeffs;
    libs (forces);

    writeControl timeStep;
    writeInterval 10;
    patches (upperWall lowerWall);
    rho rhoInf;
    rhoInf 1;
    CofR (0 0 0);
    dragDir (1 0 0);
    liftDir (0 1 0);
    magUInf 10;
    lRef 0.0254;
    Aref 0.0000254;
    writeFields true;
}</code></pre></details><h3 id="example-4">示例 4 · 只处理指定时间段</h3><p>本例把对象的工作时间限定在 0.1 到 0.5。实际使用时将两个时刻改为算例需要分析的阶段，主求解器仍按 controlDict 推进。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">timeStart 0.1;
timeEnd 0.5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">wallCoefficients
{
    type forceCoeffs;
    libs (forces);

    writeControl timeStep;
    writeInterval 10;
    patches (upperWall lowerWall);
    rho rhoInf;
    rhoInf 1;
    CofR (0 0 0);
    dragDir (1 0 0);
    liftDir (0 1 0);
    magUInf 10;
    lRef 0.0254;
    Aref 0.0000254;
    timeStart 0.1;
    timeEnd 0.5;
}</code></pre></details><h3 id="example-5">示例 5 · 每五步保存一次</h3><p>采用五步间隔，在时间分辨率与数据量之间选择适合当前计算的输出频率。</p><p>在该对象内修改以下条目：</p><pre><code class="language-foam">writeControl timeStep;
writeInterval 5;</code></pre><details><summary>完整配置</summary><pre><code class="language-foam">wallCoefficients
{
    type forceCoeffs;
    libs (forces);

    writeControl timeStep;
    writeInterval 5;
    patches (upperWall lowerWall);
    rho rhoInf;
    rhoInf 1;
    CofR (0 0 0);
    dragDir (1 0 0);
    liftDir (0 1 0);
    magUInf 10;
    lRef 0.0254;
    Aref 0.0000254;
}</code></pre></details><h2 id="related">相关工具</h2><p><a href="/function-objects/?category=%E5%8A%9B%E4%B8%8E%E7%89%A9%E7%90%86%E9%87%8F">力与物理量速查</a> · <a href="/function-objects/">全部 functionObject</a></p><p>延伸阅读：<a href="/read/?slug=function-objects-09">专题课程</a>。</p><p class="source-note">参考：<a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/src/functionObjects/forces/forceCoeffs/forceCoeffs.H">OpenFOAM v2512 · forceCoeffs 接口</a>。</p>
{% endraw %}
