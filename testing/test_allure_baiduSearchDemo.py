#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
import time

from selenium import webdriver
@allure.feature("百度搜索")
@pytest.mark.parametrize("test_data1", ["allure", "pytest", "unittest"])
def test_steps_demo(test_data1):
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
    with allure.step(f"输入搜索词:{test_data1}"):
        driver.find_element_by_id("kw").send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)
    with allure.step("保存图片"):
        driver.save_screenshot("./screenshots/baidu.jpg")
        allure.attach.file("./screenshots/baidu.jpg", name="百度搜索截图", attachment_type=allure.attachment_type.JPG)
    with allure.step("关闭浏览器"):
        driver.quit()