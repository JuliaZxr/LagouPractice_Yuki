#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import allure

@allure.feature("登录模块")
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        print("这是登录：测试用例，登录成功")
        pass

    @allure.story("登录失败")
    def test_login_failure(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登录后登录失败"):
            print("这是登录：测试用例，登录成功")
            assert "1" == 1
            print("登录失败")
        pass

    @allure.story("用户名缺失")
    def test_login_success_a(self):
        print("用户名缺失")
        pass

    @allure.story("登录失败")
    def test_login_failure_a(self):
        print("密码错误")
        assert '2' == 1
        pass

    @allure.story("登录失败")
    def test_login_failure_b(self):
        print("账号不存在")
        assert '2' == 1
        pass