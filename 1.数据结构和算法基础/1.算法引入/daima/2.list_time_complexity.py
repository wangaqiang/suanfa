# timeit模块是准确测量小段代码的执行时间　
from timeit import Timer
# l1 = [1,2]
# l2 = [3,4]
# li = l1+l2

# li = [i for i in range(10000)]

# li = list(range(10000))

# li = []
# for i in range(10000):
    # li.append(i)

def t1():
    li = []
    for i in range(10000):
        li.append(i)

def t2():
    li = []
    for i in range(10000):
        li = li+[i]

def t3():
    li = [i for i in range(10000)]

def t4():
    li = list(range(10000))

def t5():
    li = []
    for i in range(10000):
        li.extend([i])

def t6():
    li = []
    for i in range(10000):
        li.insert(0, i)

def t7():
    li = []
    for i in range(10000):
        li.insert(-1, i)

#　创建Timer实例，第一个参数为要执行的函数或者代码块，第二个参数为初始化代码或者构建环境的导入语句,该实例对象中的方法timeit返回值为测试n遍后所需要的时间．
# timr1 = Timer("t1()", "from __main__ import t1")
# print("append:%d"%timr1.timeit(1000))

# timr2 = Timer("t2()", "from __main__ import t2")
# print("＋:%d"%timr2.timeit(1000)) #这个效率是最慢的额,单位用分钟计算,但是如果是li+=[i]，则没那么夸张

# timr3 = Timer("t3()", "from __main__ import t3")
# print("生成式:%d"%timr3.timeit(1000)) #效率和构造函数的差不多了

# timr4 = Timer("t4()", "from __main__ import t4")
# print("构造函数:%d"%timr4.timeit(1000)) #效率很高的啦

# timr5 = Timer("t5()", "from __main__ import t5")
# print("extend:%d"%timr5.timeit(1000)) #效率和append差不多

# append向后添加比insert向前添加快的多
# timr1 = Timer("t1()", "from __main__ import t1")
# print("append:%d"%timr1.timeit(1000))
# timr6 = Timer("t6()", "from __main__ import t6")
# print("insert向前:%d"%timr6.timeit(1000))
# append向后比insert向后快
timr1 = Timer("t1()", "from __main__ import t1")
print("append:%d"%timr1.timeit(1000))
timr7 = Timer("t6()", "from __main__ import t6")
print("insert向后:%d"%timr7.timeit(1000))
