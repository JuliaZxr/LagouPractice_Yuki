#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 14:58
# @Author  : Yuki
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestAction():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_clickCase(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")

        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        # 定义一个anction
        action = ActionChains(self.driver)
        # 点击
        action.click(element_click)
        # 右击
        action.context_click(element_rightclick)
        # 双击
        action.double_click(element_doubleclick)
        # 调用perform去执行之前的方法
        action.perform()

    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com/")

        element = self.driver.find_element(By.ID, "s-usersetting-top")
        # 定义一个anction
        action = ActionChains(self.driver)
        # 移动到元素
        action.move_to_element(element)
        # 调用perform去执行之前的方法
        action.perform()

    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")

        dragele = self.driver.find_element(By.ID, "dragger")
        dropele = self.driver.find_element_by_xpath("/html/body/div[2]")
        # 定义一个anction
        action = ActionChains(self.driver)
        # 拖拽
        action.drag_and_drop(dragele, dropele)
        # 调用perform去执行之前的方法
        action.perform()
