#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 18:44
# @Author  : Yuki
from selenium.webdriver.common.by import By

from pageobject.page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID, "corp_name").send_keys("Momo's Company")
        self.find(By.ID, "manager_name").send_keys("Momo")