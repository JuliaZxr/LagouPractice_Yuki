#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 20:32
# @Author  : Yuki


class Bicycle:
    def run(self, km):
        print(f"一共用脚骑了{km}公里")


# EBicycle()类继承自Bicycle
class EBicycle(Bicycle):
    # 如果属性需要传参定义，那么可以使用构造函数
    # valume是电动车初始电量
    def __init__(self, valume):
        self.valume = valume

    # vol是充电的电量
    def fill_charge(self, vol):
        self.valume = self.valume + vol
        print(f"充了{vol}度电，现在的电量为{self.valume}")

    # power_km 是电动车所有电量能跑的里程数；km是要跑的里程数
    def run(self, km):
        power_km = self.valume * 10
        if power_km > km:
            print(f"我使用电瓶车骑了{km}公里")
        else:
            print(f"我使用电瓶车骑了{power_km}公里")

            # # 非继承调用方法
            # bike = Bicycle()
            # bike.run(km - power_km)

            # 继承调用方法
            super().run(km - power_km)


ebike = EBicycle(2)
# ebike.fill_charge(3)
ebike.run(10)

# bike = Bicycle()
# bike.run(10)
