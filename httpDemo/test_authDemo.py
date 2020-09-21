#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 22:42
# @Author  : Yuki
import requests
from requests.auth import HTTPBasicAuth


def test_authDemo():
    r = requests.get(url="http://httpbin.testing-studio.com/basic-auth/momo/123456",
                     auth=HTTPBasicAuth("momo", "123456"))
    print(r.status_code)
    print(r.text)
