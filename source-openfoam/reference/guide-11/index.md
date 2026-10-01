---
title: "第 11 章　字典文件的通用语法"
layout: "reference"
description: "OpenFOAM v2512 命令、文件与配置参考"
manual: 2
---
{% raw %}
<p class="source-note">资料来源：OpenFOAM命令与文件大全_v2512（Claude整理）.docx。网页版已对部分表述作技术性修订，原文可在资料页下载。命令选项以本机 v2512 的 <code>-help</code> 为准。核心模板工具使用 <code>foamGetDict</code>；版本差异与安装步骤需结合官方说明核对。</p><p>OpenFOAM 的所有设置文件（叫”字典”，dictionary）用的是同一套语法。先花十分钟学会这套语法，后面所有文件都只是”填什么”的问题，而不是”怎么写”的问题。</p>
<h4>11.1 文件头 FoamFile</h4>
<p>每个字典文件开头都有这一段，缺了会直接报错：</p>
<pre><code>/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2512                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;          // ascii 或 binary
    class       dictionary;     // 这个文件装的是什么类型的数据
    object      controlDict;    // 文件名，必须与实际文件名一致
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //</code></pre>
<p>class 常见取值</p>
<div class="table-scroll"><table>
<tr><th>class</th><th>用在</th></tr>
<tr><td>dictionary</td><td>所有 system/、constant/ 下的设置文件</td></tr>
<tr><td>volScalarField</td><td>0/ 下的标量场（p、T、k…）</td></tr>
<tr><td>volVectorField</td><td>0/ 下的矢量场（U）</td></tr>
<tr><td>volSymmTensorField</td><td>对称张量场（R）</td></tr>
<tr><td>pointVectorField</td><td>点场（动网格位移）</td></tr>
<tr><td>surfaceScalarField</td><td>面场（phi）</td></tr>
</table></div>
<p>object 与文件名不一致时，多数命令会警告甚至读错。手工复制文件时记得改 object——这是初学者的高频低级错误。</p>
<h4>11.2 基本语法规则</h4>
<pre><code>关键字   值;                       // 每条以分号结尾

子字典
{
    关键字   值;
}

列表 ( a b c );                    // 括号 + 空格分隔
带长度的列表 3 ( a b c );           // 也可以显式写长度

// 单行注释
/* 多行
   注释 */</code></pre>
<p>三条容易犯的错：① 忘记分号（报错信息通常指向下一行，所以要往上找）；② 子字典 {} 后面不加分号；③ 中文全角符号混进来（从 PDF 复制时常发生），报 ill defined primitiveEntry。</p>
<h4>11.3 量纲 dimensions</h4>
<pre><code>dimensions      [0 2 -2 0 0 0 0];      // 这是不可压求解器里 p 的量纲：m²/s²</code></pre>
<p>七个数字依次是：</p>
<div class="table-scroll"><table>
<tr><th>位置</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th></tr>
<tr><td>物理量</td><td>质量</td><td>长度</td><td>时间</td><td>温度</td><td>物质的量</td><td>电流</td><td>光强</td></tr>
<tr><td>单位</td><td>kg</td><td>m</td><td>s</td><td>K</td><td>mol</td><td>A</td><td>cd</td></tr>
</table></div>
<p>常见量纲</p>
<div class="table-scroll"><table>
<tr><th>量</th><th>写法</th><th>单位</th></tr>
<tr><td>速度 U</td><td>[0 1 -1 0 0 0 0]</td><td>m/s</td></tr>
<tr><td>压力 p（不可压，已除以 \(\rho\)）</td><td>[0 2 -2 0 0 0 0]</td><td>\(m^{2}/s^{2}\)</td></tr>
<tr><td>压力 p（可压，真实压力）</td><td>[1 -1 -2 0 0 0 0]</td><td>Pa</td></tr>
<tr><td>运动粘度 \(\nu\)</td><td>[0 2 -1 0 0 0 0]</td><td>\(m^{2}/s\)</td></tr>
<tr><td>动力粘度 \(\mu\)</td><td>[1 -1 -1 0 0 0 0]</td><td>Pa·s</td></tr>
<tr><td>密度 \(\rho\)</td><td>[1 -3 0 0 0 0 0]</td><td>\(\mathrm{kg}/m^{3}\)</td></tr>
<tr><td>温度 T</td><td>[0 0 0 1 0 0 0]</td><td>K</td></tr>
<tr><td>k（湍动能）</td><td>[0 2 -2 0 0 0 0]</td><td>\(m^{2}/s^{2}\)</td></tr>
<tr><td>\(\varepsilon\)</td><td>[0 2 -3 0 0 0 0]</td><td>\(m^{2}/s^{3}\)</td></tr>
<tr><td>\(\omega\)</td><td>[0 0 -1 0 0 0 0]</td><td>1/s</td></tr>
</table></div>
<p>为什么 OpenFOAM 要检查量纲：所有方程运算都带量纲校验，一旦你把 Pa 和 \(m^{2}/s^{2}\) 混用，程序会直接报 incompatible dimensions for operation。这是个好东西——它在计算开始前就抓住了物理上的错误。看到量纲报错，先想”我这个求解器里 p 到底是什么”：不可压求解器（icoFoam/simpleFoam/pimpleFoam）里的 p 是 \(p/\rho\)。</p>
<h4>11.4 场的赋值：uniform / nonuniform</h4>
<pre><code>internalField   uniform (0 0 0);              // 全场同一个值
internalField   uniform 0;

internalField   nonuniform List&lt;vector&gt;       // 逐单元给值（一般由程序生成）
400
(
(0 0 0)
(0.1 0 0)
...
);</code></pre>
<p>为什么要知道 nonuniform：setFields、mapFields 生成的场就是这种格式。文件可能有几十万行，不要用编辑器去改它，要改就用命令。</p>
<h4>11.5 边界条件块 boundaryField 与正则匹配</h4>
<pre><code>boundaryField
{
    inlet           { type fixedValue; value uniform (1 0 0); }
    outlet          { type zeroGradient; }

    &quot;(top|bottom)&quot;  { type symmetryPlane; }        // 正则：同时匹配 top 和 bottom
    &quot;wall.*&quot;        { type noSlip; }               // 所有以 wall 开头的 patch
    &quot;.*&quot;            { type zeroGradient; }         // 兜底：其余全部
}</code></pre>
<p>正则的两条规则：① 必须用双引号包起来，不然被当作普通名字；② 精确名字优先于正则，多个正则匹配时后面的优先。兜底 &quot;.*&quot; 放最后是个好习惯，可以避免”漏了一个 patch 导致启动失败”。</p>
<h4>11.6 变量、宏与文件包含（把重复的东西提出来）</h4>
<p>① 定义与引用变量</p>
<pre><code>flowVelocity     (10 0 0);
pressure         0;

internalField    uniform $flowVelocity;      // 用 $ 引用</code></pre>
<p>② 引用嵌套条目</p>
<pre><code>$..solvers/p/tolerance      // .. 表示上一层
$:solvers.p.tolerance       // 从文件根部开始的绝对路径</code></pre>
<p>③ 包含另一个文件（最有用的技巧）</p>
<pre><code>#include        &quot;initialConditions&quot;          // 相对本文件的路径
#includeIfPresent &quot;myOverrides&quot;              // 存在才包含，不存在不报错
#includeEtc     &quot;caseDicts/setConstraintTypes&quot;   // 从 $FOAM_ETC 里包含
#includeFunc    residuals(p,U)               // 引入官方 functionObject 模板</code></pre>
<p>典型用法：在算例根目录建一个 initialConditions 文件</p>
<pre><code>// &lt;算例&gt;/initialConditions
flowVelocity        (10 0 0);
pressure            0;
turbulentKE         0.375;
turbulentEpsilon    14.855;</code></pre>
<p>然后 0/U、0/p、0/k、0/epsilon 全都 #include &quot;../initialConditions&quot; 并用 $flowVelocity 这样引用。好处：改工况只改一个文件，不会出现”U 改了 k 忘了改”的错误。做参数扫描时这更是必须的。</p>
<p>④ 表达式计算</p>
<pre><code>#include &quot;initialConditions&quot;

// 用 #calc 写一段 C++ 表达式（会动态编译）
nu              #calc &quot;1.0/$Re&quot;;
endTime         #calc &quot;10.0*$period&quot;;

// v2012 起也可以用更轻量的 #eval（不需要编译，速度快）
deltaT          #eval &quot;1e-3/2&quot;;</code></pre>
<p>⑤ 删除继承来的条目</p>
<pre><code>#remove         someKeyword;
#remove         ( key1 key2 );</code></pre>
<p>⑥ 检查展开结果</p>
<p>用了一堆 #include 和 #calc 后，怎么知道程序最终读到了什么？</p>
<pre><code>$ foamDictionary system/controlDict -expand
$ foamDictionary 0/U -expand -entry boundaryField/inlet</code></pre>
<p>这条命令能省掉大量猜测。</p>
<h4>11.7 常用”填空词”</h4>
<div class="table-scroll"><table>
<tr><th>写法</th><th>含义</th></tr>
<tr><td>uniform &lt;值&gt;</td><td>均匀场</td></tr>
<tr><td>constant &lt;值&gt;</td><td>常数（部分模型用）</td></tr>
<tr><td>table ((t1 v1) (t2 v2))</td><td>分段线性表（随时间变化）</td></tr>
<tr><td>tableFile { file &quot;...&quot;; }</td><td>从文件读表</td></tr>
<tr><td>polynomial ((c0 0)(c1 1))</td><td>多项式</td></tr>
<tr><td>expression &quot;...&quot;</td><td>表达式（v2012+ 的 exprValue 类边界条件）</td></tr>
<tr><td>$internalField</td><td>用内部场的值（边界 value 里常见）</td></tr>
<tr><td>#include &quot;...&quot;</td><td>包含文件</td></tr>
<tr><td>yes/no、true/false、on/off</td><td>开关都通用</td></tr>
</table></div>
{% endraw %}