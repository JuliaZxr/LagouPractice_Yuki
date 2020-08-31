#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 20:38
# @Author  : Yuki
from appium.webdriver.common.mobileby import MobileBy

from appium_test.page.addMember_page import AddMemberPage
from appium_test.page.base_page import BasePage


class MemberInvitePage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def goto_addMemberByManual(self):
        # Todo 跳转手动新建成员页面
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return AddMemberPage(self.driver)

