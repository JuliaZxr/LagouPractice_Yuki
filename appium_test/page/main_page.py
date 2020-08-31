#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 20:33
# @Author  : Yuki
from appium.webdriver.common.mobileby import MobileBy

from appium_test.page.base_page import BasePage
from appium_test.page.contact_page import ContactPage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def goto_contact(self):
        # Todo 跳转通讯录页面
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return ContactPage(self.driver)