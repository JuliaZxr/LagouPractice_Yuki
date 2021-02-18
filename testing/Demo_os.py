#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 11:47
# @Author  : Yuki

import os

# os.mkdir("testdir")
# os.removedirs("testdir")

# 打印当前目录下的内容，并用list返回
# print(os.listdir("./"))

# 打印当前文件的绝对路径
# print(os.getcwd())

# 先判断该目录下不存在对应文件夹or文件时，再进行创建
print(os.path.exists("bbb"))
if not os.path.exists("bbb"):
    os.mkdir("bbb")
if not os.path.exists("bbb/a.txt"):
    f = open("bbb/a.txt", "w")
    f.write("hello, os using~")
    f.close()
