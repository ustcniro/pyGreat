# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# 设置x,y轴的数值（y=sinx）
x = np.linspace(0, 10, 10)
y = np.sin(x)

# 创建绘图对象，figsize参数可以指定绘图对象的宽度和高度，单位为英寸，一英寸=80px
plt.figure(figsize=(8, 4))

# 在当前绘图对象中画图（x轴,y轴,给所绘制的曲线的名字，画线颜色，画线宽度）
plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2, marker=1)
# plt.plot(x,y,"b--",linewidth=1)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
'''
    plt.plot(x,y,"b--",linewidth=1)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
    
    **Markers**

    =============    ===============================
    character        description
    =============    ===============================
    ``'.'``          point marker
    ``','``          pixel marker
    ``'o'``          circle marker
    ``'v'``          triangle_down marker
    ``'^'``          triangle_up marker
    ``'<'``          triangle_left marker
    ``'>'``          triangle_right marker
    ``'1'``          tri_down marker
    ``'2'``          tri_up marker
    ``'3'``          tri_left marker
    ``'4'``          tri_right marker
    ``'s'``          square marker
    ``'p'``          pentagon marker
    ``'*'``          star marker
    ``'h'``          hexagon1 marker
    ``'H'``          hexagon2 marker
    ``'+'``          plus marker
    ``'x'``          x marker
    ``'D'``          diamond marker
    ``'d'``          thin_diamond marker
    ``'|'``          vline marker
    ``'_'``          hline marker
    =============    ===============================
    
    **Line Styles**
    =============    ===============================
    character        description
    =============    ===============================
    ``'-'``          solid line style
    ``'--'``         dashed line style
    ``'-.'``         dash-dot line style
    ``':'``          dotted line style
    =============    ===============================    
    
    **Colors**

    The supported color abbreviations are the single letter codes

    =============    ===============================
    character        color
    =============    ===============================
    ``'b'``          blue
    ``'g'``          green
    ``'r'``          red
    ``'c'``          cyan
    ``'m'``          magenta
    ``'y'``          yellow
    ``'k'``          black
    ``'w'``          white
    =============    ===============================
    
    线条样式
    风格字符	说明
    ‘-‘	实线
    ‘–’	破折线
    ‘-.’	点划线
    ‘:’	虚线
    四个单引号	无线条
    
    color:控制颜色，color=’green’ 
    linestyle:线条风格，linestyle=’dashed’ 
    linewidth:线条粗细，又lw=
    marker:标记风格，marker = ‘o’ 
    markerfacecolor:标记颜色，markerfacecolor = ‘blue’ 
    markersize:标记尺寸，markersize = ‘20’
    ————————————————

'''

# X轴的文字
plt.xlabel("Time(s)")

# Y轴的文字
plt.ylabel("Volt")

# 图表的标题
plt.title("PyPlot First Example")

# Y轴的范围
plt.ylim(-1.2, 1.2)

# 显示图示
plt.legend()
# #图例的放置位置upper lower left right
# plt.legend(loc='upper right')

#网格线
plt.grid()

# 保存图
# plt.savefig("sinx.jpg")

# 折线图
# plt.plot([1,2,3,4,5], [2,1,6,5,3], 'ro-', lw=2)

# 显示图，没有这个不显示
plt.show()
