#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 12:32
# @Author  : Yuki

"""
https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/touch-actions.md
TouchAction
TouchAction对象包含一系列事件。
在所有appium客户端库中，都会创建触摸对象并为其分配一系列事件。
规范中可用的事件是：

press
release
moveTo
tap
wait
longPress
cancel
perform
"""
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction:

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
        self.driver.quit()

    def test_touchAction(self):
        # 定义一个TouchAction类
        action = TouchAction(self.driver)
        # 打印界面的宽和高
        # print(self.driver.get_window_rect())
        # press按住，move_to移动到，release释放，perform执行
        action.press(x=360, y=1150).move_to(x=360, y=400).release().perform()
