#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 18:37
# @Author  : Yuki

"""
类（Class）：抽象的概念，一类事物
方法：类中定义的函数，对外提供的服务
类变量：类变量在整个实例化的对象中是公用的
实例引用：实例化一个对象
实例变量：以‘self.变量名’的方式定义的变量

"""
# 通过class关键字，定义一个类Person
class Person:
    # 定义类变量：在整个实例化的对象中是公用的
    name = "default"
    age = 0
    gender = "male"
    weight = 0

    # 定义类的方法

    """
    构造方法，在类实例化的时候被调用
    
    例如我们可以在这里设置属性，set_name、age、gender、weight
    """
    def __init__(self, name, age, gender, weight):
        print("init function")
        # self.变量名的方式，访问到的变量，叫做实例变量（即每一个实例拥有的属性）
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    # # self.name 调用的是类里面的name属性,set_name 方法是给每个实例设置不同name;age\gender\weight同理
    # def set_name(self, name):
    #     self.name = name
    #
    # def set_age(self, age):
    #     self.age = age
    #
    # def set_gender(self, gender):
    #     self.gender = gender
    #
    # def set_weight(self, weight):
    #     self.weight = weight

    @classmethod
    def eat(self):
        print(f"{self.name} is eating")

    def play(self):
        print(f"{self.name} is playing")

    def jump(self):
        print(f"{self.name} is jumping")


"""
类变量和实例变量的区别：
1、都是可以被修改的
2、类变量是需要类来访问，实例变量需要实例来访问

类方法和实例方法的区别：
1、类方法是不能访问 实例方法
2、类方法要通过添加一个装饰器 @classmethod 
"""

# 类的实例化，创造了一个实例，zs就是实例化的对象
zs = Person("zhangsan", 20, "男", 120)

# 调用类的方法
zs.eat()

# # 为这个对象设置属性
# zs = Person()
# zs.set_name("zhangsan")
# zs.set_age(18)
# zs.set_gender("male")
# zs.set_weight(120)

print(f"zs的姓名是：{zs.name}, 年龄是：{zs.age}, 性别是：{zs.gender}, 体重是：{zs.weight}")
