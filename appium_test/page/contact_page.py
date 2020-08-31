#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 20:34
# @Author  : Yuki
from appium.webdriver.common.mobileby import MobileBy

from appium_test.page.base_page import BasePage
from appium_test.page.memberInvite_page import MemberInvitePage


class ContactPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    def goto_addMemberPage(self):
        # Todo 跳转同事邀请页面
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return MemberInvitePage(self.driver)