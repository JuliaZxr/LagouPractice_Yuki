#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 12:32
# @Author  : Yuki


import time


def func1(t1):  # 最外层管理 装饰器的参数
    def func2(func):  # 管理传入的函数对象
        def func3(t2):  # 最内层管理被装饰函数的参数
            if func1:
                print("开始的时间为：", time.strftime("%S"))
                func(t2)  # 代表传入的函数被调用
                print("我是func3")
                print("结束的时间为：", time.strftime("%S"))
            else:
                func(t2)  # 代表传入的函数被调用
                print("我是func3")

        return func3

    return func2


@func1(t1=True)
def be_decorate(t2):
    print("被装饰器装饰的函数")
    time.sleep(t2)


# be_decorate(3)
f1 = func1(t1=True)
f2 = f1(be_decorate)
f2(3)