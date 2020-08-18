#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 17:14
# @Author  : Yuki

"""
文件读取
操作步骤：
    1、打开文件，获取文件描述符
    2、操作文件描述符（读 | 写）
    3、关闭文件（文件读写操作完成后，应及时关闭文件）

open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
参数说明：
name：文件名称的字符串值
mode：只读r。写入w，追加a，默认文件访问模式为只读r
buffering：寄存区缓存
    0：不寄存
    1：访问文件时会寄存行
    >1：寄存区的缓冲大小
    <0:寄存区的缓冲大小为系统默认

图片要使用rb去读取二进制格式
正常的文本使用rt，也是默认的格式
"""
# 打开文件
f = open('Demo_data.txt')

# 查看文件是否可读，并输出结果
print(f.readable())

"""
注意：readline和readlines一起使用的时候，是都生效的
比如readline已经读取了两行，再执行readlines，则会输出的剩下未读取的所有行
如果先执行readlines ，后执行的readline则输出为空
"""

# 将文件每次读取一行，换行符不会被读取
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

# 将文件每行全部读出，并存放在一个列表内，换行符也会被读取
print(f.readlines(), '\n')

# 关闭文件
f.close()

"""
with跟open一起使用，则不需要再去写close文件;
with语句块，可以将文件打开，执行完毕后，自动关闭这个文件
"""

with open('Demo_data.txt') as f:
    print(f.readlines())
