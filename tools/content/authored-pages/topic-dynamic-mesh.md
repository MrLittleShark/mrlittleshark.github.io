## 先把运动方式说清楚

处理运动物体时，首先描述什么在运动：边界的位置是否随时间变化，整个网格区域是否刚体运动，还是局部网格需要变形或重新连接。运动方式决定了网格更新方法，也决定了边界条件和数值检查的重点。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-dynamic-floating-body.png" alt="浮体运动曲线与自由液面耦合" loading="lazy"><figcaption><strong>浮体运动曲线与自由液面耦合</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 170 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

旋转参考系、滑移接口和变形网格对应不同的建模方式。例如，MRF 在一个随区域旋转的参考系中表示相关项，常用于建立旋转机械的近似稳态模型；实际滑移网格则随时间改变区域之间的相对位置，需要处理运动接口的信息传递。选择方法时，应结合是否需要解析叶片通过等非定常过程。

<figure class="wolf-figure"><img src="/assets/wolf/wolf-dynamic-cylinder-deformation.png" alt="振荡圆柱附近的网格变形" loading="lazy"><figcaption><strong>振荡圆柱附近的网格变形</strong><small class="figure-source">来源：Joel Guerrero / <a href="https://www.wolfdynamics.com/tutorials.html?id=181&amp;layout=edit">Wolf Dynamics</a> · module8.pdf，p. 164 · <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>（裁剪）</small></figcaption></figure>

## 为什么运动设置必须和通量一起检查

固定网格中，控制体积的位置不变；当网格运动时，控制面的运动也会参与质量和动量的收支。因此，需要同时检查网格速度、相对通量和物理边界速度。物体已经移动而壁面速度仍按静止壁面处理，可能产生与预期不一致的流动。

练习时可以先让网格单独运动，查看最容易压缩、拉伸或扭曲的位置。把这一检查放在完整流动求解之前，可以更快发现运动幅度、约束或网格变形策略的问题。具体命令应按下载包中的 Allrun 和说明执行，因为不同的运动方法需要的准备步骤并不完全相同。

## 从 movingCone 到 AMI

movingCone 案例用于观察运动边界与周围网格变形。阅读时先找到 dynamicMeshDict，再对照运动对象、位移描述以及速度场的边界设置。随后进入 mixerVesselAMI2D，观察旋转区域与静止区域之间如何通过 AMI 交换信息。

AMI 允许两侧接口采用不完全一致的面划分，但接口覆盖、方向和插值质量仍要检查。时间推进中还需要关注小单元、网格质量及相关 Courant 数的变化。若只看初始网格通过检查，就可能漏掉运动到某个位置后出现的问题。

这个专题先建立运动、网格和流动三者的对应关系。配套资料会分别说明源码核对、网格检查和求解运行的范围，便于在已有证据上继续做自己的验证。
