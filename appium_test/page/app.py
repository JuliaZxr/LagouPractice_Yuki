#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 20:29
# @Author  : Yuki
"""
1、启动app
2、关闭app
3、重启app
4、进入首页

"""
from appium import webdriver

from appium_test.page.base_page import BasePage
from appium_test.page.main_page import MainPage


class App(BasePage):

    def start(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(5)

    def restart(self):
        pass

    def stop(self):
        pass

    def goto_main(self):
        return MainPage(self.driver)