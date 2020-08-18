#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 23:29
# @Author  : Yuki
import pytest

# 当一个方法上面加上@pytest.fixture() 装饰器就变成了fixture方法
# yield 也相当于return，如果需要返回值，直接写在yield后面即可
# yield 前面的操作相当于setup操作，yield后面的操作相当于teardown操作

"""
当测试用例方法需要调用fixture方法时，在参数中传入fixture方法名login
当测试用例方法需要fixture方法的返回值时，一定要将fixture方法名传入参数

fixture里面的参数scope，可以控制fixture的作用范围：session>module>class>function（默认是function）
"""


@pytest.fixture()
def login():
    print("登录")
    username = "yuki"
    password = 123456
    # return [username, password]
    yield [username, password]
    print("登出")


def test_case1(login):
    print(login)
    print("这是方法1，需要登录")


def test_case2():
    print("这是方法2，不需要登录")


def test_case3(login):
    print(login)
    print(f"这是方法3，需要登录，账号是{login}")
