#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 13:08
# @Author  : Yuki

import time

print(time.asctime())
print(time.time())  # 时间戳
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 获取两天前的时间
now_timestamp = time.time()
two_day_before = now_timestamp - 60*60*24*2
time_tuple = time.localtime(two_day_before)
print(time.strftime("%Y-%m-%d %H:%M:%S", time_tuple))