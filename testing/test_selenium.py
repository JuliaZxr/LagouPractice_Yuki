#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 20:40
# @Author  : Yuki
from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""
强制等待
sleep(3)

隐式等待：设置一个等待时间，轮询查找（默认0.5s)元素是否出现，如果没有出现就抛出异常，是一个全局的等待
self.driver.implicitly_wait(3)

显示等待：在代码中定义等待条件，当条件发生时才继续执行代码。
程序每隔一段时间（默认0.5s）进行条件判断，如果条件成立，则执行下一步，否则继续等待，直到超过设置的最长时间
"""


class TestHogwarts():
    def setup(self):
        # 实例化driver
        self.driver = webdriver.Firefox()
        # 窗口最大化
        self.driver.maximize_window()
        # 设置隐式等待，使用后无需在方法中每句代码后再去添加sleep()方法；而是自行每步等待5s，使之可以有时间找到元素继续测试，避免网速慢等原因导致元素未被加载，从而导致用例执行失败
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 回收driver
        self.driver.quit()

    def test_hogwarts(self):
        # 通过driver.get打开一个url
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element_by_link_text("精华帖").click()

        """
        # 显示等待中的自定义函数方法；该方法必须要写一个参数-->因为until调用wait函数时，把self.driver传给了wait
        def wait(x):
            return len(self.driver.find_elements_by_css_selector("#show-tag-info > .d-button-label")) >= 1
        # 显示等待，当wait()函数中返回的该元素个数（len代表个数）>=1，则继续执行。否则在设置的10s达到之前，继续等待
        # 传参时，wait不能加()，否则意味着调用，不会再传参
        WebDriverWait(self.driver, 10).until(wait)
        self.driver.find_element_by_link_text("BAT 大厂测试开发技能成长最佳实践 | 霍格沃兹测试学院课程体系").click()
        """
        # 也可以不去自定义方法，采用内置方法

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="show-tag-info"]')))
        self.driver.find_element_by_link_text("BAT 大厂测试开发技能成长最佳实践 | 霍格沃兹测试学院课程体系").click()
