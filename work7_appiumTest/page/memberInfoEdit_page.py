#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 0:24
# @Author  : Yuki
from work7_appiumTest.page.base_page import BasePage
from work7_appiumTest.page.contact_page import ContactPage


class MemberInfoEditPage(BasePage):
    # 个人信息编辑保存后跳转通讯录页面
    def editMemberInfo(self):
        return ContactPage(self.driver)