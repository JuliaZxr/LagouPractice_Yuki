#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/20 20:30
# @Author  : Yuki

"""
conftest.py 用法
查找顺序
1、测试用例会优先读 取当前模块下的fixture 方法
2、其次读取当前目录下定义的conftest.py 文件里面定义的fixture方法
3、如果当前文件或者当前目录没有，才会去项目目录下一层一层往上找。

需要注意

conftest.py文件名是不能换的
conftest.py与运行的用例要在同一个package下，并且有__init__.py文件
不需要import导入conftest.py，pytest用例会自动查找
所有同目录测试文件运行前都会执行conftest.py文件
全局的配置和前期工作都可以写在这里，放在某个包下，就是这 个包数据共享的地方。

"""
import pytest


# scope="session" 整个session域只执行一次
@pytest.fixture(scope="session")
def coonDB():
    print("连接数据库-subProgram")
    yield
    print("断开数据库连接-subProgram")
