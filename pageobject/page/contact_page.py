#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 20:30
# @Author  : Yuki
from selenium.webdriver.common.by import By

from pageobject.page.base_page import BasePage


class ContactPage(BasePage):
    def goto_add_member(self):
        from pageobject.page.add_member_page import AddMemberPage
        return AddMemberPage(self._driver)

    def get_memeber_list(self):
        # 这个元素查找出来返回的是一个列表
        name_list = self._driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        # 定义一个空列表
        list1 = []
        # 用循环把返回列表中的值都取出来存到定义的空列表中
        for name in name_list:
            list1.append(name.text)
        return list1
