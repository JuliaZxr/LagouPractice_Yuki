#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 21:05
# @Author  : Yuki

"""
基类：
存放一些最基本的方法，用的最频繁的方法
1、实例化driver
2、查找元素
"""
from appium import *
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver:WebDriver = None):
        """
        初始化driver
        """
        self.diver = driver

    def find(self, locator):
        return self.diver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(locator).click()

    # def find_and_scroll_and_click(self):

