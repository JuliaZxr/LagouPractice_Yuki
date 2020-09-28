#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/28 22:31
# @Author  : Yuki
import requests

"""
页面中共用的，且不属于页面中的方法，写到utils类中，避免写到基类中，增加基类的冗余
"""


class WechatUtils:
    """
    每个页面的corpsecret值都不一致，所以corpsecret需要传参，corpid则是这个app中的定值，所以直接赋值
    """

    def getToken(self, _corpsecret, corpid="wweb26819d4d011560"):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={_corpsecret}"
        result = requests.get(url).json()
        return result["access_token"]
