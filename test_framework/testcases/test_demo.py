#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
登录的测试用例：
    首先需要一个setup方法，去实例化login_page页面
    存在登录测试方法：test_login（其中需要用户名、密码参数）
        则test_login方法需要数据驱动(通过pytest.mark.parametrize)


"""
import pytest

from test_framework.page.base_page import BasePage
from test_framework.page.common_page import CommonPage
from test_framework.utils.file_util import FileUtil


class TestDemo:
    testcase_file = "../datas/test_search.yml"
    po_file = "../datas/page_demo.yml"

    data = FileUtil.from_file(testcase_file)

    def setup_class(self):
        self.app = BasePage()
        self.app.start()

    def setup(self):
        pass

    def teardown_class(self):
        self.app.stop()

    # 用common_page代替demo_page
    @pytest.mark.parametrize(data["keys"], data["values"])
    def test_search_common_page(self, keyword1):
        demo = CommonPage(self.po_file)
        demo.search(keyword3 = keyword1)
        demo.back()

    def test_loginByPassword(self):
        po_file = "../datas/page_login.yml"
        login = CommonPage(po_file)
        # login.start()

        # 当执行找不到对应属性或方法时，会调用__getattr__方法，借助于__getattr__方法实现任意方法代理
        # login.xxxx => login.__getattr__
        # login.login_by_password() =>print()
        # print("13322226666", "111111")
        # login.login_by_password("13322226666", "111111")
        login.login_by_password(username = "13322226666", password = "111111")