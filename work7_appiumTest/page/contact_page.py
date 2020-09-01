#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 22:15
# @Author  : Yuki
from appium.webdriver.common.mobileby import MobileBy

from work7_appiumTest.page.base_page import BasePage
from work7_appiumTest.page.inviteMembers_page import InviteMembersPage
from work7_appiumTest.page.memberInfo_page import MemberInfoPage


class ContactPage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    # 方法：通讯录页面跳转邀请成员页面
    def goto_inviteMembersPage(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.findByXpath("//*[@text='添加成员']").click()
        return InviteMembersPage(self.driver)

    # 方法：通讯录页面跳转个人信息页面
    def goto_memberInfotmationPage(self, name):
        self.findByXpath(f"//*[@text='{name}']").click()
        return MemberInfoPage(self.driver)

