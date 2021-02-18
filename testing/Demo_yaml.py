#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/18 15:08
# @Author  : Yuki

import yaml

print(yaml.load(open("demo.yml"), Loader=yaml.FullLoader))

print("\n")

print(yaml.load("""
a: 1
b: 2
""", Loader=yaml.FullLoader))

print("\n")

print(yaml.dump({'a': [1, 2]}))
print(yaml.dump([[1, 2, 3], {'a': 1, 'b': 2, 'c': 3}]))