## 选择相的描述方法

水面、气泡群和喷雾包含不同尺度的相分布。VOF 用体积分数表示网格能分辨的界面；Euler–Euler 方法将多相都描述为连续场；Euler–Lagrange 方法跟踪颗粒或液滴的运动。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-multiphase-morphology.png" alt="分散相与分离界面的形态区别" loading="lazy"><figcaption><strong>分散相与分离界面的形态区别</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 65 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

左侧的气泡或液滴分散在连续相中，右侧的两相由连续界面分隔。选择模型时，先比较气泡、液滴或界面结构与网格的尺度，再确定是解析界面形状，还是描述相的平均分布与相间作用。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-multiphase-model-families.png" alt="多相流计算框架的对照" loading="lazy"><figcaption><strong>多相流计算框架的对照</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 71 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

## 从溃坝算例认识 VOF

水相体积分数 `alpha.water` 为 1 时，单元充满水；为 0 时，单元内为空气；中间值表示水占据了部分体积。`setFields` 根据初始水柱的几何范围写入这个场。

```bash
blockMesh
setFields
interFoam > log.interFoam 2>&1
```

这三步用于已经配置好的 damBreak 算例：建立网格、设置水柱、求解界面运动。先查看初始体积分数，确认水柱位置和高度，再比较后续水面变化。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-vof-volume-fraction.png" alt="相分数如何表示网格内的界面" loading="lazy"><figcaption><strong>相分数如何表示网格内的界面</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 78 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

## 界面与体积

液体总体积由每个单元的相分数与单元体积求和：

\[
V_\mathrm{water}=\sum_P\alpha_P V_P.
\]

封闭容器中，这个量应随时间保持稳定；开放边界中则结合相通量计算流入和流出。对比不同网格和时间步时，同时记录体积变化、水面位置和压力。

[VOF 课程与案例下载](/read/?slug=vof-interface-dambreak) · [alpha.water 配置](/dictionaries/0-alpha-water/)
