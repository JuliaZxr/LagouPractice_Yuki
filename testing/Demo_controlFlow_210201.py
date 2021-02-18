#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 21:32
# @Author  : Yuki
#
# # 分支结构
# a = 0
# if a == 0:
#     print("a=0")
# else:
#     print("a!=0")
#
# # 多重分支
# b = 9
# if b == 1:
#     print("b == 1")
# elif b == 2:
#     print("b == 2")
# elif b == 3:
#     print("b == 3")
# else:
#     print("b不等于1,2,3")
#
# x = 8
# xx = 8
# if xx > 1:
#     yy = 3 * xx - 5
# elif -1 <= xx <= 1:
#     yy = xx + 2
# elif xx < -1:
#     yy = 5 * xx + 3
# print(yy)
#
# if x >= -1:
#     if x <= 1:
#         y = x + 2
#     else:
#         y = 3 * x - 5
# else:
#     y = 5 * x + 3
# print(y)

# result = 0
# for i in range(1, 20, 2):
#     print(i)
#     result = result + i
# print(result)

# for i in range(0, 5):
#     print(i)
# print("\n")
#
# # break 指跳出循环不再执行
# for i in range(0, 5):
#     if i == 3:
#         break
#     print(i)
# print("\n")
#
# # continue 指跳出本次循环，要继续执行剩下的循环
# for i in range(0, 5):
#     if i == 3:
#         continue
#     print(i)

import random
computer_num = random.randint(1, 100)
print(computer_num)
while True:
    person_num = int(input("请输入一个数字：\n"))
    if person_num > computer_num:
        print("小一点")
    elif person_num < computer_num:
        print("大一点")
    elif person_num == computer_num:
        print("bingo~")
        break
