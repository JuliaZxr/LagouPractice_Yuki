#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 20:54
# @Author  : Yuki

# int_a = 1
# float_a =0.2
# complex_a = 0.2j
#
#
# # 通过type查看变量的数据类型
# print(type(int_a))
# print(type(float_a))
# print(type(complex_a))
#
#
# # 输出字符串换行符
# str_b = "bbbbb\n"
# print(str_b)
#
# # 需要将符号打印出来，使用\ 或者 r 忽略转义符
# str_c = "ccccc\\n"
# str_d = r"ddddd\n"
#
# print(str_c)
# print(str_d)
#
# str_a = "aaaaa"
# print(type(str_a))
#
# # 多个字符串连接使用空格 or +
# str_e = "hello" "yuki"
# print(str_e)
# str_f = "bye"+"momo"
# print(str_f)
#
# # 切片使用[start: stop: step] [开始：结束：步长] 步长默认是1
# str_g = "1234567"
# # 打印字符串的第一个字符
# print(str_g[0])
# print(str_g[1])
# print(str_g[2])
#
# print(str_g[0:5])
# print(str_g[0:5:2])

list1 = [1, 2, 3, 4, 5, 6, 7]
# 打印列表中的第一个数字
print(list1[0])

# 列表切片 [开始：结束：步长] 步长默认为1
print(list1[0:5:2])

# 复制并打印列表
print(list1[:])
