from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + r'C:\Program Files\graphviz\bin'

dot = Digraph(comment='The Test Table', format="png", encoding='utf8', node_attr={'fontname':'FangSong'})

# 添加圆点A,A的标签是Dot A
dot.node('A', '实现单智能体在楼层内任意位置顺利逃生', {'color':'blue','fontcolor':'blue'})

# 添加圆点 B, B的标签是Dot B
dot.node('B', '实现多智能体协同有序逃生')
# dot.view()

# 添加圆点 C, C的标签是Dot C
dot.node('C', '融合到可视化系统中')
# dot.view()

# 创建一堆边，即连接AB的两条边，连接AC的一条边。
dot.edges(['AB', 'BC'])
dot.view()

# 在创建两圆点之间创建一条边
dot.edge('B', 'C', 'test')
# dot.view()


# 获取DOT source源码的字符串形式
# print(dot.source)
# // The Test Table
# digraph {
#   A [label="Dot A"]
#   B [label="Dot B"]
#   C [label="Dot C"]
#   A -> B
#   A -> C
#   A -> B
#   B -> C [label=test]
# }


# 保存source到文件，并提供Graphviz引擎
# dot.save('test-table.gv')  # 保存
# dot.render('test-table.gv')
dot.view()  # 显示



# 从保存的文件读取并显示

from graphviz import Source

# s = Source.from_file('test-table.gv')
# print(s.source)  # 打印代码
# s.view()  # 显示