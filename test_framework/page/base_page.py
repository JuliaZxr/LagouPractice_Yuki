#!/usr/bin/env pytho
# -*- coding: utf-8 -*-
"""
需要driver，定义一个私有_driver，设置类型是WebDriver，且定义为None

读取yml文件的数据是一个公共的方法，所以写在基类中


"""
import logging

import yaml
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _driver: WebDriver = None
    _current_element: WebElement = None

    def __init__(self, po_file = None):
        if po_file is not None:
            self._po_file = po_file

    @classmethod
    def start(cls):
        caps = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": "true"
        }
        cls._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        cls._driver.implicitly_wait(10)
        return cls

    def stop(self):
        BasePage._driver.quit()

    # 查找元素方法，并return
    def find(self, by):
        if by[0] == "text":
            by_new = (By.XPATH, f"//*[contains(@text, '{by[1]}')]")
        elif by[0] == "id":
            by_new = by
        self._current_element = BasePage._driver.find_element(*by_new)
        return self

    def click(self):
        self._current_element.click()
        return self

    def send_keys(self, keyword):
        self._current_element.send_keys(keyword)
        return self

    def find_byXPATH(self, xpath):
        self._current_element = BasePage._driver.find_element(*xpath)

    def po_runSteps(self, po_method, **kwargs):
        # 读取yml文件
        """
            page_demo.yml是对应login_page页面的一个数据驱动文件
            这个页面中存在方法：login（登录）、forget（忘记密码）、search等
            login方法中需要一些操作：find（通过id、text查找元素）、click、send_keys
            这个整体的文件是个词典，每个key中对应的又是一个列表
        """
        # with open("../datas/page_demo.yml", encoding="utf-8") as f:
        with open(self._po_file, encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
            # 找到对应的search（对应的yml文件中的key值），这里search就是po_method参数
            # 找到的yaml_data[po_method]返回的是一个列表，再去循环列表中的每一步，判断是find，click，send_keys再继续处理
            for step in yaml_data[po_method]:
                # 再完成底层的find by click send_keys
                """
                isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
                isinstance() 与 type() 区别：
                type() 不会认为子类是一种父类类型，不考虑继承关系。                
                isinstance() 会认为子类是一种父类类型，考虑继承关系。                
                如果要判断两个类型是否相同推荐使用 isinstance()。
                
                以下是 isinstance() 方法的语法:isinstance(object, classinfo)
                    object -- 实例对象
                    classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。
                如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False
                
                if isinstance(step, dict) -->判断每一步是不是一个词典
                """
                if isinstance(step, dict):
                    # step.keyd() 返回的是一个列表，内容是yml文件中的每一个key值
                    # 然后再去循环 判断每一步是具体的id、 click、send_keys操作，再继续下一步操作
                    for key in step.keys():
                        if key in ["id", "text"]:
                            # step[key]代表的就是每一个id、 click、send_keys对应的具体值
                            # 因为find（）方法中传递的是一个元组，所以在使用的是也需要是一个元组
                            locator = (key, step[key])
                            self.find(locator)
                        elif key == "xpath":
                            locator = (By.XPATH, step[key])
                            self.find_byXPATH(locator)
                        elif key == "click":
                            self.click()
                        elif key == "send_keys":
                            """
                            当key匹配"send_keys"后，
                            step[key] 是取的 page_demo.yml文件中search下的send_keys对于的value值 ${keyword3}，即step[key] = ${keyword3}
                            text = str(step[key]) 即：text = ‘${keyword3}‘
                            
                            po_runSteps(self, po_method, **kwargs)
                            po_runSteps("search", keyword3=keyword2)
                            **kwargs又表示关键字参数，它本质上是一个 dict，即通过keyword3=keyword2将‘alibaba’转化成dict == {‘keyword3’:'alibaba'}
                            即：kwargs = {‘keyword3’:'alibaba'}
                            for k, v in kwargs.items() --》即：k = ‘keyword3’，v = 'alibaba'
                            
                            text.replace("${" + k + "}", v) 的意思是将括号中，逗号后的内容替换逗号前的内容：
                            其中"${" + k + "}"代表的是字符串拼接，由上一句可得k = ‘keyword3’，即"${" + k + "}" = “${keyword3}”
                            text.replace("${" + k + "}", v)  == text.replace("${keyword3}", “alibaba”)
                            就是当"${" + k + "}" 与page_demo.yml文件中search下的send_keys对于的value值 ${keyword3} 相同时，再进行替换
                            将page_demo.yml文件中search下的send_keys对于的value值 ${keyword3}替换成“alibaba”
                            
                            """
                            text = str(step[key])
                            for k, v in kwargs.items():
                                text = text.replace("${" + k + "}", v)
                            self.send_keys(text)

                        # TODO：更多的关键字
                        else:
                            # 如果执行的是存在不是id click send_keys的操作，则输出日志
                            logging.error(f"dont know {step}")
