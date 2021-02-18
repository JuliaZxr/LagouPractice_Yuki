#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 13:43
# @Author  : Yuki

import urllib.request

response: object=urllib.request.urlopen("http://www.baidu.com")
print(response.status)
# print(response.read())
print(response.headers)