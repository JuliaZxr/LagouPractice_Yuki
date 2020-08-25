#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 20:35
# @Author  : Yuki

from pageobject.page.base_page import BasePage
from pageobject.page.main_page import MainPage


class TestAddMember:

    # def setup_class(self):
    #     # 实例化类，使之可以调用所属方法
    #     self.main = MainPage()

    def test_add_member(self):
        self.main = MainPage()
        result = self.main.goto_add_member().add_member().get_memeber_list()
        assert "Ben" in result
    #
    # def test_contact_add_member(self):
    #     self.main.goto_contact().goto_add_member().add_member()
    #
    # def teardown(self):
    #     self.main._driver.quit()
