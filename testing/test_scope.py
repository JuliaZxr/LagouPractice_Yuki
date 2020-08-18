#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 23:51
# @Author  : Yuki

import pytest


@pytest.fixture(scope="module")
def coonDB():
    print("连接数据库")
    yield
    print("断开数据库连接")


def test_case1(coonDB):
    print("test_case1")


class TestDemo1:
    def test_a1(self, coonDB):
        print("test_a1")

    def test_b1(self, coonDB):
        print("test_b1")


class TestDemo2:
    def test_a2(self, coonDB):
        print("test_a2")

    def test_b2(self, coonDB):
        print("test_b2")
