#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 23:15
# @Author  : Yuki

"""
模块：
包含python定义和语句的文件
.py文件
可以作为脚本运行

模块的导入
    1、import 模块名
    2、from 模块名 import <方法 | 变量 | 类>
    3、from 模块名 import *

常用方法：
dir() 找出当前模块定义的对象
dir(sys) 找出参数模块定义的对象
"""
import sys

print("\n", dir(sys))

print("\n", sys.path)
