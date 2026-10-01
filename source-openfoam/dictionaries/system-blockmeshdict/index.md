---
title: "system/blockMeshDict"
layout: "reference"
description: "blockMeshDict 通过 vertices 定义顶点，以 hex 后的 8 个顶点编号确定块的局部方向和体积符号。(Nx Ny Nz) 指定三个方向的单元数，scale 指定坐标缩放系数，simpleGrading 指定各方向末端与起始单元的尺寸比。"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>system/blockMeshDict</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>vertices</code> · <code>blocks</code> · <code>edges</code> · <code>boundary</code> · <code>scale</code> · <code>convertToMeters</code> · <code>simpleGrading</code></p><h2>关联命令</h2><p><a href="/commands/?q=blockMesh">blockMesh</a></p><h2>本机核对</h2><pre><code>foamVersion
foamDictionary system/blockMeshDict -keywords
blockMesh -help</code></pre><h2>7.1 system/blockMeshDict</h2><p>blockMeshDict 通过 vertices 定义顶点，以 hex 后的 8 个顶点编号确定块的局部方向和体积符号。(Nx Ny Nz) 指定三个方向的单元数，scale 指定坐标缩放系数，simpleGrading 指定各方向末端与起始单元的尺寸比。</p>
<p>下例建立长 1 m、宽 0.1 m、厚 0.01 m 的二维通道。厚度方向设置一层单元，两侧边界设为 empty。</p>
<pre><code>FoamFile
{
    version 2.0; format ascii;
    class dictionary; object blockMeshDict;
}
scale 1;
vertices
(
    (0 0 0) (1 0 0) (1 0.1 0) (0 0.1 0)
    (0 0 0.01) (1 0 0.01) (1 0.1 0.01) (0 0.1 0.01)
);
blocks
(
    hex (0 1 2 3 4 5 6 7) (100 20 1)
        simpleGrading (1 1 1)
);
edges ();
boundary
(
    inlet
    {
        type patch;
        faces ((0 4 7 3));
    }
    outlet
    {
        type patch;
        faces ((1 2 6 5));
    }
    walls
    {
        type wall;
        faces ((0 1 5 4) (3 7 6 2));
    }
    frontAndBack
    {
        type empty;
        faces ((0 3 2 1) (4 5 6 7));
    }
);
mergePatchPairs ();</code></pre>
<p>执行 blockMesh 生成网格，再执行 checkMesh -allTopology -allGeometry 检查拓扑和几何。边界面的顶点顺序按外法向排列；多块网格应统一局部坐标和顶点编号。</p>
<div class="table-scroll"><table>
<tr><th>参数或结构</th><th>设置方法</th><th>使用条件</th></tr>
<tr><td>scale</td><td>如 0.001 表示原坐标按毫米给出</td><td>采用 scale 统一设置坐标缩放</td></tr>
<tr><td>simpleGrading</td><td>例如 (1 10 1)</td><td>沿块的局部方向设置；反向时取对应倒数</td></tr>
<tr><td>多段 grading</td><td>某方向可写 ((0.2 0.3 4) (0.6 0.4 1) (0.2 0.3 0.25))</td><td>每段分别为长度比例、单元比例、扩张比</td></tr>
<tr><td>edgeGrading</td><td>对 12 条局部边分别指定扩张比</td><td>按块的局部边编号依次赋值</td></tr>
<tr><td>edges</td><td>arc 0 1 (中间点)，或 spline、polyLine</td><td>弧线端点与控制点应满足非退化条件</td></tr>
<tr><td>boundary/type</td><td>patch、wall、empty、symmetryPlane、wedge、cyclic 等</td><td>定义网格边界类型；场边界另行配置</td></tr>
<tr><td>defaultPatch</td><td>为未显式列出的面指定名称和类型</td><td>显式边界之外的面归入该边界</td></tr>
<tr><td>mergePatchPairs</td><td>((patchA patchB))</td><td>合并指定的块接口</td></tr>
</table></div>
<h2>第 15 章　system/blockMeshDict</h2>
{% endraw %}