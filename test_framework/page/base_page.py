#!/usr/bin/env pytho
# -*- coding: utf-8 -*-
"""
需要driver，定义一个私有_driver，设置类型是WebDriver，且定义为None


"""
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver = None
    _current_element: WebElement = None

    def start(self):
        caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": "true"
        }
        self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self._driver.implicitly_wait(10)
        return self

    def stop(self):
        self._driver.quit()

    # 查找元素方法，并return
    def find(self, by):
        self._current_element = self._driver.find_element(*by)
        return self

    def click(self):
        self._current_element.click()
        return self

    def send_keys(self, keyword):
        pass
        # self._current_element.send_keys(keyword)
        # return self



