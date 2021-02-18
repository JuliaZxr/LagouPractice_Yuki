#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 21:17
# @Author  : Yuki

"""
闭包函数：
    在函数内又定义了函数，且外层函数返回的是内层函数的对象

    例如func1()代表调用这个函数，而func1则仅是函数的对象

    即：调用外层函数时是无法执行内层函数的代码。
    想要执行内层函数的代码，需要先调用外层函数，再对结果值进行调用；直接调用内层函数时不行的。

注意：
1、定义的全局变量在外层函数、内层函数都能被调用
2、定义在外层函数的变量，能被内层函数调用
3、但内层函数的变量，不可被外层函数调用
"""


def func1():
    name = "func1的鲸鱼"
    print(name)
    print("我是func1")

    def func2():
        name = "func2的鲸鱼"
        print(name)
        print("我是func2")

    return func2


# 调用外层函数func1()
func1()
print("\n")

# 调用内层函数func2()
func22 = func1()  # func22 == func1() == func2
func22()  # func22() == func2()
