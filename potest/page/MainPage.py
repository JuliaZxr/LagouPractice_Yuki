#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/23 19:59
# @Author  : Yuki
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from potest.page.BasePage import BasePage
from potest.page.ContactPage import ContactPage


class MainPage(BasePage):
    url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_contactPage(self):
        # Todo 首页跳转通讯录页面
        # 继承了父类，可直接通过self.xxx调用父类类变量
        self.findById("menu_contacts").click()

        # self.driver返回给ContactPage，共用浏览器
        return ContactPage(self.driver)
