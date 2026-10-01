---
title: "Make/files"
layout: "reference"
description: "在源码目录运行 wmake 编译应用。编译共享库时，在 Make/files 中设置 LIB = $(FOAM_USER_LIBBIN)/libMyModel，在 Make/options 中设置 LIB_LIBS，并运行 wmake libso。Make 变量采用 $(FOAM_USER_APPB"
dictionary: true
---
{% raw %}
<p class="source-note">配置位置：<code>Make/files</code>。下文为参考示例与说明，片段需按求解器、字段、边界名称及几何条件补充；各文件不能任意组合为一个完整算例。</p><h2>关键条目索引</h2><p><code>EXE</code> · <code>LIB</code> · <code>FOAM_USER_APPBIN</code> · <code>FOAM_USER_LIBBIN</code></p><h2>关联命令</h2><p><a href="/commands/?q=wmake">wmake</a></p><h2>本机核对</h2><pre><code>foamVersion
cat Make/files
wmake -help</code></pre><h2>9.14 Make/files 与 Make/options</h2><pre><code># Make/files
myScalarFoam.C

EXE = $(FOAM_USER_APPBIN)/myScalarFoam
EXE_INC = \
    -I$(LIB_SRC)/finiteVolume/lnInclude \
    -I$(LIB_SRC)/meshTools/lnInclude

EXE_LIBS = \
    -lfiniteVolume \
    -lmeshTools</code></pre>
<p>在源码目录运行 wmake 编译应用。编译共享库时，在 Make/files 中设置 <code>LIB = $(FOAM_USER_LIBBIN)/libMyModel</code>，在 Make/options 中设置 LIB_LIBS，并运行 wmake libso。Make 变量采用 $(FOAM_USER_APPBIN) 形式，Bash 变量采用 ${FOAM_USER_APPBIN} 形式。</p>
{% endraw %}