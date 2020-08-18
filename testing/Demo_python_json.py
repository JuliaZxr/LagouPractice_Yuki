#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 17:42
# @Author  : Yuki

import json

"""
json是由列表和字典组成的
"""

dataDic = {
    "name": ["yuki", "momo"],
    "age": 18,
    "gender": "gir"
}

# 查看并打印dataDic的类型
print(type(dataDic))

# 将数据类型转换成字符串
data1 = json.dumps(dataDic)
print(data1)
print(type(data1))

# 将字符串转换成json
data2 = json.loads(data1)
print(type(data2))

# 将数据类型转换成字符串并存储在文件中

# 把文件打开，把里面的字符串转换成数据类型
