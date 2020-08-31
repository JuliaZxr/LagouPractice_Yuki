#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 16:25
# @Author  : Yuki
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *

class TestWebdriverWait:
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_getAttribute(self):
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search_ele.get_attribute("resource-id"))
        assert "search" in search_ele.get_attribute("resource-id")

    def test_hamrest(self):
        # 断言10满足equal_to（x），否则抛出异常提示
        assert_that(10, equal_to(10), '提示：断言未通过')
        # 断言12满足 close_to(10, 2)--》10 上下浮动2,
        assert_that(12, close_to(10, 2))
        # 断言字符串包含kitty
        assert_that("hello kitty", contains_string("kitty"))