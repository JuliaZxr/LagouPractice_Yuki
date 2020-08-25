#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/20 20:37
# @Author  : Yuki
import pytest

"""
fixture参数化， 带参数传递

在@pytest.fixture()中，通过params=传递参数，fixture方法login()中加入request
"""


@pytest.fixture(params=[("tom", 123456), ("jerry", 654321)], ids=["用户Tom", "用户jerry"])
def login(request):
    # print(request.param)
    print("登录")
    yield request.param
    print("登出")


def test_case1(login):
    print("test_case1")
    print(login)
