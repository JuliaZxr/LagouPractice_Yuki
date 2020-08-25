#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 20:30
# @Author  : Yuki
from selenium.webdriver.common.by import By

from pageobject.page.add_member_page import AddMemberPage
from pageobject.page.base_page import BasePage
from pageobject.page.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_contact(self):
        self._driver.find_element(By.CSS_SELECTOR, ".frame_nav_item_title").click()
        return ContactPage(self._driver)

    def goto_add_member(self):
        self._driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMemberPage(self._driver)
