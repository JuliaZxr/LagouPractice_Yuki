#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 16:06
# @Author  : Yuki

"""
字面量插值，格式化输出必须给定指定的类型
"""
print("My name is Yuki")

name = "hogwarts"
print('my name is %s' % name)

age = 18
print('my name is %s, my age is %d, num is %f' % (name, age, 5.201314))

num = 5.201
print('my name is %s, my age is %d, num is %f' % (name, age, num))

# 浮点数默认保留6位小数，可自行定制显示n位小数 %.nf
print('my name is %s, my age is %d, num is %.2f' % (name, age, num))

"""
字面量插值，format()方法,不用给定类型
用法：str.format()
可以将字符串、列表、字典进行拼接
"""

print('we are {} and {}'.format('tom', 'jerry'))
print('my name is {} ,and my age is {}'.format(name, age))
print('my name is {0} ,and my age is {1}'.format(name, age))
print('my name is {0} ,and my age is {1}, {0}{1}{0}'.format(name, age))

list1 = ['lili', 'momo', 'tom']
dic2 = {'name': 'momo', 'gender': 'male'}
print('my list is {}， dict is {}'.format(list1, dic2))
print('my list is {0}， dict is {1}'.format(list1, dic2))

# 列表和字典想要一个一个赋值时，需要解包处理
print('we are {}、 {} and {}'.format(*list1))
print('my name is {name} ,and my gender is {gender}'.format(**dic2))

"""
F-string：字符串格式化，支持3.6以上版本
使用方法：f'{变量名}'
大括号内可以是表达式or函数or常量
"""

print(f'my name is {name}, age is {age}, my list is {list1}, my dict is {dic2}')
print(f"my list is {list1[0]}")
print(f"my dict is {dic2['gender']}")

# 大括号内的表达式
print(f"my name is {name.upper()}")
print(f"my age is {24}")
print(f"result is {(lambda x:x+1)(2)}")
