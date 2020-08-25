#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 18:29
# @Author  : Yuki
from selenium.webdriver.common.by import By

from pageobject.page.base_page import BasePage
from pageobject.page.register import Register


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/"

    def doto_register(self):
        self.find(By.CSS_SELECTOR, "index_head_info_pCDownloadBtn").click()
        return Register(self._driver)

    def goto_login(self):
        pass
