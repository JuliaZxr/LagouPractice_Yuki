#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 20:31
# @Author  : Yuki

from selenium import webdriver
from selenium.webdriver.common.by import By

from pageobject.page.base_page import BasePage
from pageobject.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    def add_member(self):
        driver = self._driver
        driver.find_element(By.ID, "username").send_keys("Ben")
        driver.find_element(By.ID, "memberAdd_acctid").send_keys("0505")
        driver.find_element(By.ID, "memberAdd_phone").send_keys("11122223333")
        driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(driver)


