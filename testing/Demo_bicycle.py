#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 10:00
# @Author  : Yuki


class Bicycle():
    def run(self, km):
        print(f"自行车骑行里程为{km}公里")


# A类继承自B类：class A(B)
class EBicycle(Bicycle):
    # 如果属性需要传参定义，那么需要使用构造函数
    def __init__(self, valume):
        self.valume = valume

    def fill_charge(self, vol):
        self.valume = self.valume + vol
        print(f"充了{vol}度电，现在的电量为{self.valume}")

    def run(self, km):
        """
        每骑行10km消耗1度电，电量耗尽时自行车继续骑行

        思路：
        1、要知道当前的电量，就能得到能跑的最大里程数
        2、将最大里程数与需要骑行的里程数做比较，大于等于则只用电动车骑行；否则需要电动车+自行车骑行
        """
        if self.valume * 10 >= km:
            print(f"用电动车骑行了{km}公里")
        elif self.valume * 10 < km:
            print(f"用电动车骑行了{self.valume*10}公里")
            # bike = Bicycle()
            # bike.run(km - self.valume*10)
            super().run(km - self.valume*10)


ebike = EBicycle(1)
ebike.fill_charge(2)
ebike.run(50)
