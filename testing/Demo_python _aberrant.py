#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 23:46
# @Author  : Yuki

try:
    num1 = int(input("请输入一个除数："))
    num2 = int(input("请输入一个被除数："))
    print(num1 / num2)

# 抛出指定的异常

# except ZeroDivisionError:
#     print("被除数不能为0")
# except ValueError:
#     print("输入的需要是数值型整数")

# try:
#     执行代码
# except:
#     发生异常时执行的代码
# else:
#     没有异常时执行的代码、
# finally：
#     不管有没有异常都会执行的代码

except:
    print("被除数不能为0 或 输入的需要是数值型整数")
else:
    print("没有异常哦~")
finally:
    print("已经执行完了")

# 抛出异常

x = int(input("请输入一个数值型整数："))
if x > 5:
    raise Exception("这是抛出的异常信息！！")


# 自定义的异常类
class MyException(Exception):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2


raise MyException("value1", "value2")
