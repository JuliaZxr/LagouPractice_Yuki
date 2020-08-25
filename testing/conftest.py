#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 22:22
# @Author  : Yuki
import pytest

from typing import List


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# scope="session" 整个session域只执行一次
@pytest.fixture(scope="session")
def coonDB():
    print("连接数据库")
    yield
    print("断开数据库连接")
