#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 0:23
# @Author  : Yuki
from work7_appiumTest.page.base_page import BasePage
from work7_appiumTest.page.memberInfoEdit_page import MemberInfoEditPage


class MemberInfoMorePage(BasePage):
    # 方法：个人信息更多操作页面跳转个人信息编辑页面
    def goto_memberInfoEditPage(self):
        self.findById("com.tencent.wework:id/b87").click()
        return MemberInfoEditPage(self.driver)