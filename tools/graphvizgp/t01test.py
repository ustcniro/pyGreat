from graphviz import Digraph
from graphviz import Source

# 需要在本地安装，配置环境变量
import os
# os.environ["PATH"] += os.pathsep + r'C:\Program Files\graphviz\bin'
# 或许是需要重启的

dot = Digraph(
    name='Graphtest',
    comment='添加到源码第一行的注释',
    filename=None,
    directory=None,
    format="png",
    engine=None,
    encoding='utf8',
    graph_attr={'rankdir':'TB'},
    node_attr={'color':'black','fontcolor':'black','fontname':'FangSong','fontsize':'12','style':'rounded','shape':'box'},
    edge_attr={'color':'#999999','fontcolor':'#888888','fontsize':'10','fontname':'FangSong'},
    body=None,
    strict=False
)
# name: 图的名字，打开时显示的图的名字.
# comment: 添加的源码第一行的注释.
# filename: 指定.
# directory: (Sub)directory for source saving and rendering.
# format: 输出图片的格式 (``'pdf'``, ``'png'``, ...).
# engine: Layout command used (``'dot'``, ``'neato'``, ...).
# encoding: 图的编码方式，such as ‘utf8’.
# graph_attr: 图属性，属性字典的形式.
# node_attr: 节点属性，属性字典的形式.
#   shape可以是oval（椭圆）、circle（圆）、box（圆角矩形）、
# edge_attr: 边（连线）属性，属性字典的形式.
# body: Iterable of verbatim lines to add to the graph ``body``.
# strict (bool): 如果设置了多条A->B，渲染时多条合并.

# 执行view就会保存，指定filename以filename为准，不指定用name
# save()    保存源码，可以指定文件名，文件名取 指定名>filename>name
# render()  保存图片，可以指定文件名，文件名取 指定名>filename>name

# 添加圆点A,A的标签是Dot A
dot.node('A', '实现单智能体在楼层内任意位置顺利逃生', {'color':'blue','fontcolor':'blue'})
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
print(dot.source)
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
# dot.save()  # 保存
# dot.render('rendertest')
# dot.view()  # 显示



# 从保存的文件读取并显示
# s = Source.from_file('test-table.gv')
# print(s.source)  # 打印代码
# s.view()  # 显示