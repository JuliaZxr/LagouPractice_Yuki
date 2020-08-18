# 函数的定义
# 位置参数


def func1(a, b, c):
    print("函数func1的参数a", a)
    print("函数func1的参数b", b)
    print("函数func1的参数c", c)
    print("\n")
    return None


# 函数的调用
func1(1, 2, 3)

"""
默认参数：
默认参数在定义函数的时候使用k=v的形式定义
调用函数时，如果没有传递参数，则会使用默认参数
"""


def func2(a=1):
    print("func2()未传递参数，直接使用默认参数：", a)
    print("\n")
    return a


func2()

"""
关键字参数：
调用函数时，使用k=v的形式进行传参
在函数调用or定义中，关键字参数必须跟随在位置参数的后面
"""


def func3(a, b, c):
    print("func3()参数a的值为：", a)
    print("func3()参数b的值为：", b)
    print("func3()参数c的值为：", c)
    print("\n")


# 全部使用关键字传参


func3(b=2, a=1, c=3)

# 想要一起使用关键字传参和位置传参


func3(4, c=6, b=5)

"""
lambda表达式（匿名函数）
"""

func4 = lambda x, y: x * y

print("func4()两个参数的积为：", func4(5, 6))


def func4_same(x, y):
    print("用def定义函数func4_same()的参数乘积是：", x * y)


func4_same(5, 6)
