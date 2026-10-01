---
title: "第 10 章　编译与二次开发命令"
layout: "reference"
description: "OpenFOAM v2512 命令、文件与配置参考"
manual: 2
---
{% raw %}
<p class="source-note">资料来源：OpenFOAM命令与文件大全_v2512（Claude整理）.docx。网页版已对部分表述作技术性修订，原文可在资料页下载。命令选项以本机 v2512 的 <code>-help</code> 为准。核心模板工具使用 <code>foamGetDict</code>；版本差异与安装步骤需结合官方说明核对。</p><h4>10.1 wmake 系列</h4>
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
<h4>10.2 一个自定义求解器的最小流程</h4>
<pre><code># ① 到你的私有开发目录（不要污染安装目录！）
$ mkdir -p $WM_PROJECT_USER_DIR/applications/solvers
$ cd $WM_PROJECT_USER_DIR/applications/solvers

# ② 复制官方求解器做起点
$ cp -r $FOAM_SOLVERS/incompressible/icoFoam myIcoFoam
$ cd myIcoFoam
$ mv icoFoam.C myIcoFoam.C
$ wclean                       # 清掉复制过来的旧编译产物

# ③ 改 Make/files
$ cat Make/files
myIcoFoam.C
EXE = $(FOAM_USER_APPBIN)/myIcoFoam      # ★ 指向 USER 目录，不是 FOAM_APPBIN

# ④ 编译
$ wmake
$ which myIcoFoam
/home/chen/OpenFOAM/chen-v2512/platforms/linux64GccDPInt32Opt/bin/myIcoFoam</code></pre>
<p>为什么必须放在 $WM_PROJECT_USER_DIR：安装目录随时可能被升级覆盖，而且改动混在官方代码里以后无法分辨。$FOAM_USER_APPBIN 已经在 PATH 里，编译完直接就能用。</p>
<p>Make/files 与 Make/options 是什么</p>
<pre><code># Make/files —— 编译哪些源文件、产物叫什么、放哪
myIcoFoam.C
EXE = $(FOAM_USER_APPBIN)/myIcoFoam

# Make/options —— 去哪找头文件（-I）、链接哪些库（-l）
EXE_INC = \
    -I$(LIB_SRC)/finiteVolume/lnInclude \
    -I$(LIB_SRC)/meshTools/lnInclude
EXE_LIBS = \
    -lfiniteVolume \
    -lmeshTools</code></pre>
<p>编译报 error: xxx.H: No such file 就是 EXE_INC 少了路径；报 undefined reference to ... 就是 EXE_LIBS 少了库。这两类报错的定位方法要记住，应结合完整错误信息进一步检查头文件、链接配置与版本匹配。</p>
<h4>10.3 codeStream 与 codedFixedValue：不编译也能写代码</h4>
<p>是什么：直接在字典里嵌 C++ 代码，OpenFOAM 运行时自动编译成库并加载。</p>
<p>为什么重要：给一个抛物线入口速度、给一个随时间变化的热流，本来要写一个边界条件类 + 编译 + 链接；用 codedFixedValue 三行就完事。</p>
<pre><code>// 0/U 里给一个抛物线入口
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
<pre><code>$ rm -rf dynamicCode
# 或
$ . $WM_PROJECT_DIR/bin/tools/CleanFunctions &amp;&amp; cleanDynamicCode</code></pre>
<h4>10.4 自定义库的加载</h4>
<p>不改求解器就用上自己的边界条件/模型：</p>
<pre><code>// controlDict
libs (&quot;libmyBCs.so&quot; &quot;libmyModels.so&quot;);</code></pre>
<p>或命令行：</p>
<pre><code>$ simpleFoam -libs &#x27;(&quot;libmyBCs.so&quot;)&#x27;</code></pre>
<h4>10.5 骨架生成器</h4>
<pre><code>$ foamNewApp myApp                 # 应用程序骨架（含 Make/files、Make/options）
$ foamNewBC -f myFixedValue        # 边界条件骨架
$ foamNewFunctionObject myProbe    # functionObject 骨架
$ foamNewSource lib myClass        # 库源文件骨架</code></pre>
<h4>10.6 读源码的路径速查</h4>
<div class="table-scroll"><table>
<tr><th>想看什么</th><th>去哪</th></tr>
<tr><td>某求解器解了哪些方程</td><td>$FOAM_SOLVERS/&lt;类别&gt;/&lt;求解器&gt;/ 下的 UEqn.H、pEqn.H</td></tr>
<tr><td>边界条件的实现</td><td>$FOAM_SRC/finiteVolume/fields/fvPatchFields/derived/</td></tr>
<tr><td>湍流模型</td><td>$FOAM_SRC/TurbulenceModels/</td></tr>
<tr><td>离散格式</td><td>$FOAM_SRC/finiteVolume/interpolation/surfaceInterpolation/limitedSchemes/</td></tr>
<tr><td>functionObject</td><td>$FOAM_SRC/functionObjects/</td></tr>
<tr><td>热物性模型</td><td>$FOAM_SRC/thermophysicalModels/</td></tr>
</table></div>
<pre><code>$ grep -rn &quot;class inletOutletFvPatchField&quot; $FOAM_SRC --include=*.H | head
$ find $FOAM_SRC -name &quot;kOmegaSST*&quot;</code></pre>
<h2>第三部分　文件与字典设置方法</h2>
{% endraw %}