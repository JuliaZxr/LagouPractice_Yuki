#!/usr/bin/env pytho
# -*- coding: utf-8 -*-
"""
登录的测试用例：
    首先需要一个setup方法，去实例化login_page页面
    存在登录测试方法：test_login（其中需要用户名、密码参数）
        则test_login方法需要数据驱动(通过pytest.mark.parametrize)


"""
import pytest

from test_framework.page.demo_page import DemoPage


class TestDemo:
    def setup_class(self):
        # 初始化一个login页面
        self.demopage = DemoPage()
        # 启动app
        self.demopage.start()

    def teardown_class(self):
        self.demopage.stop()

    # TODO：测试数据的数据驱动
    @pytest.mark.parametrize("username, password", [
        ("user1", "pwd1"),
        ("user2", "pwd2")
    ] )
    def test_login(self, username, password):
        # TODO:登录测试步骤的数据驱动
        self.demopage.loginIn(username, password)
        assert 1 == 1

    @pytest.mark.parametrize("keyword", [
        "alibaba",
        # "baidu",
        # "jd"
    ])
    def test_search(self, keyword):
        self.demopage.search("search")

