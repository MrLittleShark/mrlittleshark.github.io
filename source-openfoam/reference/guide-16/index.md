---
title: "第 16 章　system/snappyHexMeshDict"
layout: reference
description: "OpenCFD v2512 system/snappyHexMeshDict；包含原理、示例与版本核对。"
---
{% raw %}
<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img src="/assets/diagrams/reference-workflow.svg" alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy"><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><h2>16.1 三阶段开关与总体结构</h2>
<pre><code class="language-openfoam">castellatedMesh true;      // ① 按几何切割背景网格 + 局部加密
snap            true;      // ② 把切割后的网格贴合到几何表面
addLayers       true;      // ③ 在壁面上长边界层

geometry { ... }                 // 几何来源
castellatedMeshControls { ... }
snapControls { ... }
addLayersControls { ... }
meshQualityControls { ... }

mergeTolerance 1e-6;</code></pre>
<h2>16.2 geometry</h2>
<pre><code class="language-openfoam">geometry
{
    body.stl                              // 文件放在 constant/triSurface/
    {
        type triSurfaceMesh;
        name body;                        // 后面用这个名字引用
    }

    refineBox                             // 也可以用解析形状定义加密区
    {
        type searchableBox;
        min  (-1 -1 -1);
        max  ( 3  1  1);
    }

    refineSphere
    {
        type searchableSphere;
        origin (0 0 0);
        radius 0.5;
    }
};</code></pre>
<h2>16.3 castellatedMeshControls</h2>
<pre><code class="language-openfoam">castellatedMeshControls
{
    maxLocalCells        1000000;    // 单进程最大单元数
    maxGlobalCells       20000000;   // 全局最大单元数（超了会自动降级加密）
    minRefinementCells   10;
    nCellsBetweenLevels  3;          // ★ 相邻加密等级之间的缓冲层数，2–4 合适

    features                          // 特征边捕捉（先跑 surfaceFeatureExtract）
    (
        { file "body.eMesh"; level 3; }
    );

    refinementSurfaces               // 表面加密
    {
        body
        {
            level (2 3);             // (最小 最大) 加密等级
            patchInfo { type wall; } // ★ 生成的 patch 类型，壁面一定写 wall
        }
    }

    resolveFeatureAngle  30;         // 夹角大于此值的地方自动加密

    refinementRegions                // 区域加密
    {
        refineBox
        {
            mode   inside;           // inside / outside / distance
            levels ((1e15 2));       // (距离 等级)；inside 模式下距离随便填大数
        }
    }

    locationInMesh (2.5 0.5 0.5);    // ★★ 保留哪一侧：必须落在"流体区域"内
    allowFreeStandingZoneFaces true;
}</code></pre>
<p>locationInMesh 指定待保留流体区域内部的一个点。该点应位于目标连通区域内，并避开几何表面和网格面。坐标选择应依据几何尺寸和区域拓扑，不宜使用与模型尺度无关的固定偏移。</p>
<p>加密等级的含义：level n 表示单元边长被二分 n 次，即尺寸变成背景网格的 1/2ⁿ。level 3 就是 1/8。每加一级，该区域单元数变 8 倍——因此应逐级增加加密等级，并记录单元数与计算成本。</p>
<h2>16.4 snapControls</h2>
<pre><code class="language-plaintext">snapControls
{
    nSmoothPatch    3;
    tolerance       2.0;
    nSolveIter      30;        // 贴合迭代次数，质量不好时加大到 50–100
    nRelaxIter      5;
    nFeatureSnapIter 10;       // 特征边贴合迭代
    implicitFeatureSnap false;
    explicitFeatureSnap  true; // 用 surfaceFeatureExtract 提取的特征
    multiRegionFeatureSnap false;
}</code></pre>
<h2>16.5 addLayersControls</h2>
<pre><code class="language-plaintext">addLayersControls
{
    relativeSizes    true;       // 厚度相对于邻近单元尺寸（true 更好控制）

    layers
    {
        body                     // patch 名（支持正则 "body.*"）
        {
            nSurfaceLayers 5;    // 层数
        }
    }

    expansionRatio      1.2;     // 层间增长比，1.1–1.3
    finalLayerThickness 0.5;     // 最外层厚度 / 邻近单元尺寸
    minThickness        0.1;     // 低于此值就不加层
    nGrow               0;

    featureAngle        130;     // 大于此角度的地方不加层（凹角处易失败）
    maxFaceThicknessRatio 0.5;
    maxThicknessToMedialRatio 0.3;
    minMedianAxisAngle  90;
    nBufferCellsNoExtrude 0;

    nLayerIter          50;      // 加层迭代次数
    nRelaxIter          5;
    nSmoothSurfaceNormals 1;
    nSmoothNormals      3;
    nSmoothThickness    10;
}</code></pre>
<p>加层失败怎么看：日志最后会打印每个 patch 的 Layer thickness ratio（实际层数/期望层数）。低于 0.7 就说明加层大面积失败，常见原因是 featureAngle 太小、几何有尖角、或者 minThickness 设得太大。先降 nSurfaceLayers，确认能加上，再逐步加回去。</p>
<h2>16.6 meshQualityControls</h2>
<pre><code class="language-plaintext">meshQualityControls
{
    maxNonOrtho         65;
    maxBoundarySkewness 20;
    maxInternalSkewness  4;
    maxConcave          80;
    minVol              1e-13;
    minTetQuality       1e-15;   // 常见做法：设为 -1e30 放宽（否则加层容易全失败）
    minArea             -1;
    minTwist            0.02;
    minDeterminant      0.001;
    minFaceWeight       0.02;
    minVolRatio         0.01;
    minTriangleTwist    -1;
    nSmoothScale        4;
    errorReduction      0.75;
}</code></pre>
<p>这些是 snappy 内部的接受阈值：任何一步操作若使网格质量突破这些限制，该操作就被撤销。所以质量控制太严 = 贴不上、加不了层；太松 = 网格能生成但 checkMesh 不过。常见折中是把 minTetQuality 放宽到 -1e30，其余保持默认。</p>
<h2>16.7 一份可用的操作顺序</h2>
<pre><code class="language-bash">cp geometry.stl constant/triSurface/
surfaceCheck constant/triSurface/geometry.stl      # 查封闭性和尺寸
blockMesh                                          # 造背景网格
surfaceFeatureExtract                              # 提特征边
snappyHexMesh -overwrite                           # 生成
checkMesh -allGeometry -allTopology                # 验收</code></pre>
{% endraw %}
