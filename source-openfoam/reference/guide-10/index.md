---
title: "第 10 章　编译与二次开发命令"
layout: reference
description: "OpenCFD v2512 编译与二次开发命令；包含原理、示例与版本核对。"
---
{% raw %}
<div class="source-note">本章由用户提供的两份 v2512 参考文档整理，并结合 OpenFOAM-v2512 源码修订。它提供主题说明；具体程序选项、安装缺失状态与完整配置示例请交叉查看 <a href="/commands/">命令库</a>和 <a href="/dictionaries/">配置库</a>。</div><figure><img src="/assets/diagrams/reference-workflow.svg" alt="算例准备、网格检查、求解监测与后处理验证的关系" loading="lazy"><figcaption>通用算例工作流示意。检查步骤围绕版本、网格、守恒和可复现性展开。</figcaption></figure><h2>10.1 wmake 系列</h2>
<p>wmake 是 OpenFOAM 自己的编译系统（对 make 的封装），你自己写的求解器、边界条件、functionObject 都用它编译。</p>
<div class="table-scroll"><table>
<tr><th>命令</th><th>作用</th></tr>
<tr><td>wmake</td><td>编译当前目录的程序或库</td></tr>
<tr><td>wmake -j8</td><td>用 8 核并行编译</td></tr>
<tr><td>wmake libso</td><td>编译成动态库（写边界条件/模型时用）</td></tr>
<tr><td>wmake all</td><td>递归编译子目录</td></tr>
<tr><td>wclean</td><td>清理当前目录的编译产物</td></tr>
<tr><td>wclean all</td><td>递归清理</td></tr>
<tr><td>wmakeLnInclude &lt;目录&gt;</td><td>生成 lnInclude 符号链接目录（头文件索引）</td></tr>
<tr><td>wmakeFilesAndOptions</td><td>生成 Make/files 与 Make/options 模板</td></tr>
<tr><td>wmakeCollect</td><td>批量编译加速（编译整个 OpenFOAM 时用）</td></tr>
</table></div>
<h2>10.2 一个自定义求解器的最小流程</h2>
<pre><code class="language-bash"># ① 到你的私有开发目录（不要污染安装目录！）
mkdir -p &#36;WM_PROJECT_USER_DIR/applications/solvers
cd &#36;WM_PROJECT_USER_DIR/applications/solvers

# ② 复制官方求解器做起点
cp -r &#36;FOAM_SOLVERS/incompressible/icoFoam myIcoFoam
cd myIcoFoam
mv icoFoam.C myIcoFoam.C
wclean                       # 清掉复制过来的旧编译产物

# ③ 改 Make/files
cat Make/files
myIcoFoam.C
EXE = &#36;(FOAM_USER_APPBIN)/myIcoFoam      # ★ 指向 USER 目录，不是 FOAM_APPBIN

# ④ 编译
wmake
which myIcoFoam
/home/chen/OpenFOAM/chen-v2512/platforms/linux64GccDPInt32Opt/bin/myIcoFoam</code></pre>
<p>建议将自定义源码放在独立的用户工作目录，并通过版本控制管理。代码不必限定在一个固定目录，但编译输出与运行时库路径应按 FOAM_USER_APPBIN、FOAM_USER_LIBBIN 等配置，避免把个人修改混入安装源码。</p>
<p>Make/files 与 Make/options 是什么</p>
<pre><code class="language-makefile"># Make/files —— 编译哪些源文件、产物叫什么、放哪
myIcoFoam.C
EXE = &#36;(FOAM_USER_APPBIN)/myIcoFoam

# Make/options —— 去哪找头文件（-I）、链接哪些库（-l）
EXE_INC = \
    -I&#36;(LIB_SRC)/finiteVolume/lnInclude \
    -I&#36;(LIB_SRC)/meshTools/lnInclude
EXE_LIBS = \
    -lfiniteVolume \
    -lmeshTools</code></pre>
<p>找不到头文件可能来自包含路径、文件名大小写、缺失依赖或尚未生成的 lnInclude。undefined reference 还可能来自源文件未参与编译、库依赖、链接顺序或 ABI 不匹配，应结合完整编译/链接命令定位。</p>
<h2>10.3 codeStream 与 codedFixedValue：不编译也能写代码</h2>
<p>是什么：直接在字典里嵌 C++ 代码，OpenFOAM 运行时自动编译成库并加载。</p>
<p>codedFixedValue 可以在字典中嵌入 C++ 实现定制边界，并在运行时编译相关代码。使用时仍需正确设置 name、code、包含项和库依赖，并确认代码在当前 v2512 API 下能够编译。</p>
<pre><code class="language-cpp">// 0/U 里给一个抛物线入口
inlet
{
    type            codedFixedValue;
    value           uniform (0 0 0);
    name            parabolicInlet;          // 生成的类名，必须唯一
    code
    #{
        const fvPatch&amp; p = patch();
        const vectorField&amp; c = p.Cf();       // 面心坐标
        scalarField y = c.component(1);
        operator==(vector(1,0,0)*1.5*(1.0 - sqr(y/0.05)));
    #};
}
// system/controlDict 里用 #codeStream 动态算一个值
endTime  #codeStream
{
    code #{ os &lt;&lt; 10.0*2; #};
};</code></pre>
<p>改了代码不生效？ 动态编译的产物缓存在算例的 dynamicCode/ 目录里。改完 code 块必须清缓存：</p>
<pre><code class="language-bash">rm -rf dynamicCode
# 或
. &#36;WM_PROJECT_DIR/bin/tools/CleanFunctions &amp;&amp; cleanDynamicCode</code></pre>
<h2>10.4 自定义库的加载</h2>
<p>不改求解器就用上自己的边界条件/模型：</p>
<pre><code class="language-plaintext">// controlDict
libs ("libmyBCs.so" "libmyModels.so");</code></pre>
<p>或命令行：</p>
<pre><code class="language-bash">simpleFoam -libs '("libmyBCs.so")'</code></pre>
<h2>10.5 骨架生成器</h2>
<pre><code class="language-bash">foamNewApp myApp                 # 应用程序骨架（含 Make/files、Make/options）
foamNewBC -f myFixedValue        # 边界条件骨架
foamNewFunctionObject myProbe    # functionObject 骨架
foamNewSource lib myClass        # 库源文件骨架</code></pre>
<h2>10.6 读源码的路径速查</h2>
<div class="table-scroll"><table>
<tr><th>想看什么</th><th>去哪</th></tr>
<tr><td>某求解器解了哪些方程</td><td>&#36;FOAM_SOLVERS/&lt;类别&gt;/&lt;求解器&gt;/ 下的 UEqn.H、pEqn.H</td></tr>
<tr><td>边界条件的实现</td><td>&#36;FOAM_SRC/finiteVolume/fields/fvPatchFields/derived/</td></tr>
<tr><td>湍流模型</td><td>&#36;FOAM_SRC/TurbulenceModels/</td></tr>
<tr><td>离散格式</td><td>&#36;FOAM_SRC/finiteVolume/interpolation/surfaceInterpolation/limitedSchemes/</td></tr>
<tr><td>functionObject</td><td>&#36;FOAM_SRC/functionObjects/</td></tr>
<tr><td>热物性模型</td><td>&#36;FOAM_SRC/thermophysicalModels/</td></tr>
</table></div>
<pre><code class="language-plaintext">grep -rn "class inletOutletFvPatchField" &#36;FOAM_SRC --include=*.H | head
find &#36;FOAM_SRC -name "kOmegaSST*"</code></pre>
<h2>第三部分　文件与字典设置方法</h2>
{% endraw %}
