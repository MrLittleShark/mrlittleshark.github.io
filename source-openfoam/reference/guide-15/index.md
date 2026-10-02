---
title: "第 15 章　system/blockMeshDict"
layout: reference
description: "system/blockMeshDict：用法与配置实例。"
cms_slug: "reference-guide-15"
---

<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy" src="/assets/diagrams/reference-workflow.svg"/><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><h2>15.1 完整结构与一个可运行的例子</h2>
<p>下面是标准方腔算例（cavity）的字典，每一行都加了注释：</p>
<pre><code class="language-openfoam">FoamFile { version 2.0; format ascii; class dictionary; object blockMeshDict; }

scale   0.1;              // 所有坐标乘这个系数（旧版叫 convertToMeters）

vertices                  // ① 顶点表，编号从 0 开始，顺序很重要
(
    (0 0 0)      // 0
    (1 0 0)      // 1
    (1 1 0)      // 2
    (0 1 0)      // 3
    (0 0 0.1)    // 4
    (1 0 0.1)    // 5
    (1 1 0.1)    // 6
    (0 1 0.1)    // 7
);

blocks                    // ② 块定义
(
    hex (0 1 2 3 4 5 6 7)   // 8 个顶点，顺序见下文
    (20 20 1)               // x、y、z 三个方向的网格数
    simpleGrading (1 1 1)   // 三个方向的加密比
);

edges ( );                // ③ 曲边（不写就是直线）

boundary                  // ④ 边界定义
(
    movingWall
    {
        type            wall;
        faces           ( (3 7 6 2) );
    }
    fixedWalls
    {
        type            wall;
        faces           ( (0 4 7 3) (2 6 5 1) (1 5 4 0) );
    }
    frontAndBack
    {
        type            empty;          // 二维算例的前后面
        faces           ( (0 3 2 1) (4 5 6 7) );
    }
);

mergePatchPairs ( );      // ⑤ 需要缝合的 patch 对</code></pre>
<h2>15.2 顶点顺序的规则（最容易错的地方）</h2>
<p>hex (v0 v1 v2 v3 v4 v5 v6 v7) 的顺序不是随便写的：</p>
<p>先给块建立一个局部坐标系 \((x_{1}, x_{2}, x_{3})\)；</p>
<p>前四个点（v0–v3）构成 \(x_{3} = 0\) 的那个面，按逆时针（从 \(x_{3}\) 正方向往回看）排列；</p>
<p>后四个点（v4–v7）是把前四个点沿 \(x_{3}\) 正方向平移得到的，顺序一一对应。</p>
<p>写反了会得到”负体积”网格，blockMesh 会直接报错：</p>
<pre><code class="language-plaintext">--&gt; FOAM FATAL ERROR: Block ... has negative volume</code></pre>
<p>看到这个报错，回去检查顶点顺序，不要怀疑别的。</p>
<p>(20 20 1) 对应的是局部 \(x_{1}\)、\(x_{2}\)、\(x_{3}\) 三个方向的单元数（不是节点数）。二维算例在厚度方向写 1，同时把前后两个面设为 empty。</p>
<h2>15.3 网格加密 grading</h2>
<p>均匀</p>
<pre><code class="language-plaintext">simpleGrading (1 1 1)</code></pre>
<p>单方向加密：数字表示”最后一个单元长度 ÷ 第一个单元长度”</p>
<pre><code class="language-plaintext">simpleGrading (1 10 1)      // y 方向：最后一个单元是第一个的 10 倍（往下密）
simpleGrading (1 0.1 1)     // 反过来（往上密）</code></pre>
<p>多段加密（一个方向分几段，各段单独控制）——边界层网格常用：</p>
<pre><code class="language-plaintext">simpleGrading
(
    1                                  // x 方向均匀
    (                                  // y 方向分三段：
        (0.2  0.3  4)                  // 占长度 20%，占单元 30%，段内比例 4
        (0.6  0.4  1)                  // 中间均匀
        (0.2  0.3  0.25)               // 对称加密
    )
    1
);</code></pre>
<p>三个数依次是 长度占比、单元数占比、段内首末比。三段的长度占比之和、单元数占比之和都应为 1。</p>
<p>edgeGrading：给 12 条边分别指定比例，用于更精细的控制（很少手写）。</p>
<p>怎么定第一层厚度：想让 \(y^{+} \approx  1\)，先估算第一层厚度 \(\Delta y\)，再由总高 H、单元数 N 和 \(\Delta y\) 反解加密比。实际做法通常是先猜一个比例算一遍，用 simpleFoam -postProcess -func yPlus 看实际 \(y^{+}\)，再调整——这是标准的迭代过程，一次猜中反而不正常。</p>
<h2>15.4 曲边 edges</h2>
<pre><code class="language-plaintext">edges
(
    arc     1 5 (1.1 0.0 0.5)        // 过点 (1.1,0,0.5) 的圆弧
    arc     1 5 origin (0 0 0)       // 或指定圆心
    spline  0 3 ( (0.2 0.1 0) (0.4 0.3 0) )   // 样条
    polyLine 2 6 ( (…) (…) )          // 折线
    line    0 1                       // 直线（默认，可省）
);</code></pre>
<p>用途：圆柱绕流、弯管这类含圆弧的几何。不写 arc 的话，圆会被画成折线，网格贴不上真实几何。</p>
<h2>15.5 boundary 里的 type</h2>
<div class="table-scroll"><table>
<tr><th>type</th><th>含义</th><th>场文件里怎么配</th></tr>
<tr><td>patch</td><td>普通边界（进出口）</td><td>场里给 fixedValue、zeroGradient 等</td></tr>
<tr><td>wall</td><td>壁面</td><td>必须用它，否则壁面函数、\(y^{+}\) 计算都不对</td></tr>
<tr><td>empty</td><td>二维算例的前后面</td><td>场里必须写 empty</td></tr>
<tr><td>symmetryPlane</td><td>对称面（平面）</td><td>场里写 symmetryPlane</td></tr>
<tr><td>symmetry</td><td>对称（不要求平面）</td><td>场里写 symmetry</td></tr>
<tr><td>wedge</td><td>轴对称楔形（张角一般 5°，一层单元）</td><td>场里写 wedge</td></tr>
<tr><td>cyclic</td><td>周期性边界，需 neighbourPatch</td><td>场里写 cyclic</td></tr>
<tr><td>cyclicAMI</td><td>非匹配周期（旋转机械）</td><td></td></tr>
<tr><td>processor</td><td>并行内部边界</td><td>由 decomposePar 自动生成</td></tr>
</table></div>
<pre><code class="language-openfoam">inlet
{
    type            patch;
    faces           ( (0 4 7 3) );
}
left
{
    type            cyclic;
    neighbourPatch  right;         // 成对出现，互相指认
    faces           ( ... );
}</code></pre>
<p>网格边界类型与场边界条件承担不同职责。壁面距离计算和许多壁面函数需要网格 patch 为 wall，某些错误组合会直接报错。forces 按配置的 patches 选择积分边界，不应笼统描述为所有后处理都只按 wall 自动识别。</p>
<h2>15.6 多块与 mergePatchPairs</h2>
<p>多个块之间如果顶点完全共用，blockMesh 会自动连成一体（推荐做法）。如果两块的接触面网格不匹配，就要用 mergePatchPairs 缝合：</p>
<pre><code class="language-plaintext">mergePatchPairs
(
    ( masterPatch slavePatch )
);</code></pre>
<h2>15.7 调试 blockMesh 的方法</h2>
<pre><code class="language-bash">blockMesh                    # 看报错
paraFoam -block              # ★ 直接可视化块结构与顶点编号，找错最快
checkMesh -allGeometry</code></pre>
<p>配置了相容的 blockReader 插件时，paraFoam -block 可用于检查块结构。若插件缺失，可先运行 blockMesh，再用 paraFoam -vtk 查看生成的网格；这两种显示对象不同。</p>
