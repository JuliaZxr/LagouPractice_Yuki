#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 22:05
# @Author  : Yuki

# 定义装饰器，形参，实参是一个函数对象


def func1(func):
    def func2():
        func()  # 代表传入的函数被调用
        print("我是func2")

    return func2


@func1
def be_decorate():
    print("被装饰器装饰的函数")


be_decorate()
# func1(be_decorate)()
