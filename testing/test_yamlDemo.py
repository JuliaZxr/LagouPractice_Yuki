#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 23:40
# @Author  : Yuki

import yaml
import pytest


class Test_yamlDemo:
    @pytest.mark.parametrize("evn", yaml.safe_load(open("./evn.yml")))
    def test_readyaml(self, evn):
        if "test" in evn:
            print("这是测试环境的ip：", evn["test"])
            # print(evn)
        elif "dev" in evn:
            print("这是开发环境", evn["dev"])
            # print(evn)

    def test_yaml(self):
        print(yaml.safe_load(open("./evn.yml")))