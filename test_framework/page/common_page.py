#!/usr/bin/env pytho
# -*- coding: utf-8 -*-
from test_framework.page.base_page import BasePage
from test_framework.page.log import log


class CommonPage(BasePage):
    def __getattr__(self, item):
        log.debug(f"__getattr__ {item}")
        print(item)
        self._method_name = item
        # 当方法找不到的时候，调用一个通用方法进行处理
        return self._po_method

    # 定义通用方法
    def _po_method(self, **kwargs):
        log.debug(f"_po_method {kwargs}")
        self.po_runSteps(self._method_name, **kwargs)

    # def login_by_password(self, username, password):
    #     self.po_runSteps("login_by_password", username = username, password = password)