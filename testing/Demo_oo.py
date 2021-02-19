#!/usr/bin/env python
# -*- coding: utf-8 -*-

class House:
    # 静态属性->变量；类变量->在类之中，方法之外
    door = "red"
    floor  = "white"

    # 构造函数，是在类实例化的时候直接执行
    def __init__(self):
        print(self.door)
        # 实例变量->在类之中，方法之中，以self.变量名的方式去定义，实例变量的作用域为这个类中的所有方法
        self.balcony = "大"

    # 动态属性 -> 方法（函数）
    def sleep(self):
        print("房子是用来睡觉的")
        # 普通变量 -> 在类之中，方法之中，但不会以self.命名
        window = "磨砂"
        print(window)
        self.wall = "乳胶漆"

    def cook(self):
        print("房子是用来做饭的")
        print(self.balcony)
        print(self.wall)

# 实例化-> 变量 = 类()
north_house = House()
china_house = House()

# 调用类变量
print(House.door)
print(north_house.door)

"""
调用方法，方法1中的实例变量可以在方法2中使用，
但仅调用方法2时，会报错，因为在调用方法2之前未调用方法1，则方法1中的示例变量就不会被声明,
所以要想实例变量有用，则需要在调用方法2前先调用方法1.

若想要变量在全局使用，则应将变量放在构造函数中。
因为构造函数在类实例化时会直接执行，变量也就直接被声明。
"""
north_house.sleep()
north_house.cook()
