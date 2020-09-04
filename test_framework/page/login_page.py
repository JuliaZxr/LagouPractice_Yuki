#!/usr/bin/env pytho
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from test_framework.page.base_page import BasePage

"""
DemoPage是定义个一个需要测试的页面，继承与基类BasePage
在这个类中，定义这个页面需要的一个方法，eg.登录，忘记密码等
"""
class LoginPage(BasePage):
    _search_button = (By.ID, "com.xueqiu.android:id/home_search")
   # TODO：PO的数据驱动
   # 定义的登录方法，需要两个参数：username, password
    def loginIn(self, username, password):
        pass

    def forget_pwd(self):
        pass

    # 定义的搜索方法，需要一个参数：keyword
    def search(self, keyword):
        self.find(self._search_button).click()
        return self