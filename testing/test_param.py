#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/11 21:15
# @Author  : Yuki
import pytest


# 笛卡尔积，用来生成多个用例组合
@pytest.mark.parametrize("a", [1, 2, 3, 4])
@pytest.mark.parametrize("b", [4, 5, 6, 7, "a", "b"])
def test_case2(a, b):
    print(f"a= {a} b= {b}")
