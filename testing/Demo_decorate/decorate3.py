#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 12:20
# @Author  : Yuki

"""
实现被装饰函数有参数的情况
"""
import time


def func1(func):
    def func2(m_time):
        print("开始的时间为：", time.strftime("%S"))
        func(m_time)  # 代表传入的函数被调用
        print("我是func2")
        print("结束的时间为：", time.strftime("%S"))

    return func2


@func1
def be_decorate(m_time):
    print("被装饰器装饰的函数")
    time.sleep(m_time)


be_decorate(3)
