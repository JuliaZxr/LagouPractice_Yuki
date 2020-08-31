#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 20:42
# @Author  : Yuki
# from appium_test.page.memberInvite_page import MemberInvitePage
from appium.webdriver.common.mobileby import MobileBy

from appium_test.page.base_page import BasePage


class AddMemberPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def add_member(self, name, gender, tel):
        # Todo 添加成员方法，添加成功后返回成员邀请页面
        from appium_test.page.memberInvite_page import MemberInvitePage

        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        if gender == '男':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f9s").send_keys(tel)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hk6").click()
        toasttext = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert '添加成功' == toasttext
        return MemberInvitePage(self.driver)