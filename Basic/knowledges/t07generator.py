# 生成器本质上还是一个迭代器
# 生成器的两种实现方式
    # 生成器函数
    # 生成器表达式

# 一个普通函数
def generator1():
    print(1)
    return 'a'
ret = generator1()
print(ret)
# 1
# a


# 生成器函数
# yield关键字
# 只要含有yield关键字的函数都是生成器函数
# yield不能和return共用且需要写在函数内
def generator2():
    print(1)
    yield 'a'   # 有yield，这是一个生成器函数
# #生成器函数 ： 执行之后会得到一个生成器作为返回值
ret = generator2()   # 生成器
print(ret)
# <generator object generator at 0x00000196912B14C8>
print(ret.__next__())   # 通过.__next__才能取值
# 1
# a


def generator3():
    print(1)
    yield 'a'
    print(2)
    yield 'b'
    yield 'c'
g = generator3()
ret = g.__next__()
print(ret)
# 1
# a
ret = g.__next__()
print(ret)
# 2
# b
ret = g.__next__()
print(ret)
# c

# 既然能__next__，那肯定也能用for来执行，
# （测试这里的时候把上面的__next__写法注释掉；如果不注释掉，这里是没有结果的，因为上面的生成器已经到头了，没有可返回的了）
for i in g:
    print(i)


###################### 对生成函数返回的每一个值做操作
# 以监听一个文件的输入为例，每次文件有输入，就在控制台打印一下
# 函数返回文件的每一行，有对每一行做个性化操作的需求
def tail(filename):
    f = open(filename,encoding='utf-8')
    while True:
        line = f.readline()
        if line.strip():
            # print(line.strip())   # 在函数内print，如果要对每一个line，就必须要在这里（函数内部）改函数
            yield line.strip()  # 通过这种写法构造生成器，

g = tail('file')
for i in g:     # 这个g是变化的，因为tail中有while True，没生成一个，操作一个
    if 'python' in i:
        print('***',i)  # 针对每次新添加（因为是生成器（迭代器）之处输出新行）的做修改，