#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 22:53
# @Author  : Yuki

"""
@pytest.fixture
装饰器用来装饰一个方法，被装饰方法的方法名可以作为一个参数传入到测试方法中;
可以使用这种方式来完成测试之前的初始化，也可以返回数据给测试函数。

作用：一些方法需要依赖前置方法，比如需要执行登录才能继续执行自身方法



-------*------
1、如果被装饰的方法有返回值，那么在其他方法中直接输出方法名==输出该方法的返回值(如果没有设置返回值，则输出None)

"""
import pytest


class Test_fixture():

    # 登录方法
    @pytest.fixture()
    def login(self):
        print("登录账号")
        return ("tom", "pwd123456")

    @pytest.fixture()
    def afterLogin(self):
        print("完成登录后的操作")

    def test_case1(self,login):
        print(login)
        print("这是方法1，需要登录")

    def test_case2(self):
        print("这是方法2，不需要登录")

    def test_case3(self, login, afterLogin):
        print(login)
        print(f"这是方法3，需要登录，账号是{login}")
