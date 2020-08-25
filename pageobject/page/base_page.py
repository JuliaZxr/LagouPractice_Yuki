#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 18:29
# @Author  : Yuki
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

"""
basepage 每次就做driver实例化的作用，
"""


class BasePage:
    # 定于类变量
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        self._driver = ""
        if driver is None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self._driver = webdriver.Chrome(options=option)

            # 实例化driver
            # self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

        self._driver.implicitly_wait(5)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)
