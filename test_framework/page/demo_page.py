#!/usr/bin/env pytho
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from test_framework.page.base_page import BasePage

"""
DemoPage是定义个一个需要测试的页面，继承与基类BasePage
在这个类中，定义这个页面需要的一个方法，eg.登录，忘记密码等

search()方法实现后，再使用po的数据驱动去实现，将search需要的步骤写到yaml文件中，
再在demo_page.py中去读取page_demo.yml数据
"""


class DemoPage(BasePage):
    # _search_button = (By.ID, "com.xueqiu.android:id/home_search")

    # TODO：PO的数据驱动
    # 定义的登录方法，需要两个参数：username, password
    def loginIn(self, username, password):
        pass

    def forget_pwd(self):
        pass

    def back(self):
        self.po_runSteps("back")
        return self

    # 定义的搜索方法，需要一个参数：keyword
    def search(self, keyword2):
        # # 普通的search方法实现
        # self.find(self._search_button).click()

        # 通过po数据驱动实现
        """
        keyword3=keyword2 中的keyword3 对应的是page_demo.yml文件中send_keys: ${keyword3}里的关键字keyword3

        def po_runSteps(self, po_method, **kwargs):
            在调用时，po_method = search；
            search()方法传参过来，keyword2 = ‘alibaba’
            **kwargs又表示关键字参数，它本质上是一个 dict，即通过keyword3=keyword2将‘alibaba’转化成dict == {‘keyword3’:'alibaba'}
        """
        self.po_runSteps("search", keyword3=keyword2)
        return self
