#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 13:58
# @Author  : Yuki
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebdriverWait:
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_webdriverWait(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='阿里巴巴']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='股票']").click()

        locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        # 加隐式等待，首先引入包WebDriverWait，参数设置driver，timeout等待时长---》意思是在10s内如果这个locator可以点击，则继续执行，否则返回异常（默认每0.5s进行查找）
        # 还有一个与之对应的相反方法until_not
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        # *locator -->意思是解元组，
        ele = self.driver.find_element(*locator)
        print(ele)
        current_price = float(ele)
        except_price = 170
        assert current_price > except_price



