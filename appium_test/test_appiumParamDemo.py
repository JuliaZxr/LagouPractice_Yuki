#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 16:49
# @Author  : Yuki
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *


class TestAppiumParam:
    """
    "skipServerInstallation": "true",//跳过安装程序
    "noReset": "true"//不要清除缓存，初始化应用

    "unicodeKeyBoard": "true",//输入中文必需
    "resetKeyBoard": "true"//输入中文必需
    autoGrantPermissions :让appium自动授权app权限，如果noReset为True，则该条不生效
    """

    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "skipServerInstallation": "true",
            "noReset": "true",
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/action_close").click()

    @pytest.mark.parametrize('searchKey, type, except_price', [
        ('alibaba', '09988', 270),
        ('xiaomi', '01810', 22)

    ])
    def test_searchParam(self, searchKey, type, except_price):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(searchKey)
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/name").click()
        current_price = float(self.driver.find_element(MobileBy.XPATH,
                                                       f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        # except_price = 289
        print(f"当前的价格是{current_price}")
        assert_that(current_price, close_to(except_price, except_price * 0.1))
