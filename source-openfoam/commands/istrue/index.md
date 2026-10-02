---
title: "isTrue · 把 on、yes、true 等开关值转换为 shell 返回码"
layout: reference
description: "把 on、yes、true 等开关值转换为 shell 返回码。"
cms_slug: "command-istrue"
---

<p>把 on、yes、true 等开关值转换为 shell 返回码。</p><h2>调用示例</h2>
<pre><code class="language-bash">source "$WM_PROJECT_DIR/bin/tools/RunFunctions"
isTrue on
echo $?
isTrue -dict system/controlDict -entry runTimeModifiable
</code></pre>
<p>真值返回 0，假值返回 1，无法识别的值返回 2。-dict 方式通过 foamDictionary 读取条目。</p>
<h2>在脚本中查看定义</h2>
<pre><code class="language-bash">type isTrue
</code></pre>
<p><code>type</code> 显示函数定义或别名展开，可用于确认当前终端加载的实现。</p>
<details><summary>v2512 实现</summary>
<pre><code class="language-bash">isTrue()
{
    local value="$1"

    if [ "$value" = "-dict" ]
    then
        shift
        value="$(foamDictionary -value $@ 2&gt;/dev/null)" || return 2
    fi

    case "$value" in
        (t | y | true | yes | on)  return 0 ;;
        (f | n | false | no | off) return 1 ;;
    esac
    return 2
}
</code></pre>
</details><h2>参考</h2><p><a href="https://gitlab.com/openfoam/core/openfoam/-/blob/OpenFOAM-v2512/bin/tools/RunFunctions">源码与说明</a></p>
