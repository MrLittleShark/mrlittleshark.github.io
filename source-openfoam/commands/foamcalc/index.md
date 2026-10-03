---
title: "foamCalc · 计算数学表达式并输出数值结果"
layout: reference
description: "计算数学表达式并输出数值结果。"
cms_slug: "command-foamcalc"
---

<p>计算数学表达式并输出数值结果。</p><h2>开始前</h2>
<p>需要当前安装包含 v2512 的 foamCalc 表达式计算器。表达式加引号，数值单位由输入者保持一致；该工具求表达式值。</p>
<h2>示例 1：计算带括号的算术表达式</h2>
<pre><code class="language-bash">foamCalc '(2 + 3)*4'
</code></pre>
<p>输出数值 20。括号指定先做加法，外层引号使表达式作为完整参数交给程序。</p>
<h2>示例 2：计算雷诺数</h2>
<pre><code class="language-bash">foamCalc '0.2*0.01/1e-6'
</code></pre>
<p>按 Re=UL/ν 输入 U=0.2 m/s、L=0.01 m、ν=10⁻⁶ m²/s，结果为 2000。数值计算使用一致单位即可得到无量纲结果。</p>
<h2>示例 3：由速度分量计算大小</h2>
<pre><code class="language-bash">foamCalc 'sqrt(3*3 + 4*4)'
</code></pre>
<p>输出 5，表示二维向量 (3,4) 的模。可把数值替换为自己的速度分量，用于估算速度尺度。</p>
<h2>示例 4：按目标 Courant 数估算时间步</h2>
<pre><code class="language-bash">foamCalc -precision 12 '0.5*0.001/0.2'
</code></pre>
<p>按 Δt≈Co·Δx/U 输入 Co=0.5、Δx=0.001 m、U=0.2 m/s，得到 0.0025 s。-precision 控制输出精度，实际网格仍需查看求解器报告的最大 Courant 数。</p>
<h2>示例 5：计算正弦入口在指定时刻的速度</h2>
<pre><code class="language-bash">foamCalc -precision 12 '0.1*(1 + 0.5*sin(6.283185307179586*0.25))'
</code></pre>
<p>对应平均速度 0.1、振幅系数 0.5、频率 1 Hz，在 t=0.25 s 时得到 0.15。sin 的参数使用弧度，可据此核对时变边界的数值。</p>
<h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/applications/tools/foamCalc/foamCalc.C">源码与说明</a> · <a href="/assets/command-help/foamcalc.txt">帮助文本</a></p>
