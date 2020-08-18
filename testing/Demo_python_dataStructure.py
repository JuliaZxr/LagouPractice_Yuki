list_yuki = [1, 2, 3, 4, 5]

# list.append(x):在列表的末尾添加一个元素
list_yuki.append(66)
print("使用append在列表尾部添加一个元素66：", list_yuki)
print("\n")

# list.insert(i, x)：在给定的位置插入一个元素，第一个参数i是要插入元素的索引，0代表头部
list_yuki.insert(0, 99)
print("在列表头部插入元素99：", list_yuki)
print("\n")
list_yuki.insert(2, 22)
print("在列表第三个位置插入元素22：", list_yuki)
print("\n")

# list.remove(x)：移除列表中第一个值为x的元素
list_yuki.remove(22)
print("移除列表中的1：", list_yuki)
print("\n")

# list.pop(i)：删除列表中给定位置的元素并返回它，若没有给定位置，则会删除并返回列表中的最后一个函数
list_yuki.pop(0)
print("移除列表中的第一位元素：", list_yuki)
list_yuki.pop()
print("未给出索引位置，则默认移除列表中最后一个元素并返回：", list_yuki)
print("\n")

# list.sort()：对列表中的元素进行默认升序排列
# list.sort(reverse=True)：对列表中的元素进行降序排列
# list.reverse()：反转列表中的元素
list_momo = [5, 2, 4, 1, 3]
print("列表顺序为：", list_momo)
list_momo.reverse()
print("列表反转后顺序为：", list_momo)
list_momo.sort()
print("列表升序为：", list_momo)
list_momo.sort(reverse=True)
print("列表降序为：", list_momo)
print("\n")

# 列表推导式
"""
用for循环生成一个平方列表[1,4,9]
    1、先定义一个列表
    2、使用range()函数生产数字1,2,3；range(x,y)是左闭右开，生产的元素为x，x+1 ... y-1
    3、使用list.append()来插入列表元素
"""
list_squre1 = []
for i in range(1, 4):
    print(i)
    # i = i * i 等同于 i = i**2
    i = i ** 2
    list_squre1.append(i)

print(list_squre1)

"""
集合：基本用法包括成员检测和消除重复元素
可以使用{}orset()函数创建集合
要创建一个空集合只能用set()而不能用{}，空的{}类型是字典
"""

conA = {1}
conB = set()
len(conB)

print("conA的类型是：", type(conA))
print("conA的长度是：", len(conA))
print("conB的类型是：", type(conB))
print("conB的长度是：", len(conB), "\n")

a = {1, 2, 3}
b = {3, 4, 5}

print("集合a、b的并集：", a.union(b))
print("集合a、b的交集：", a.intersection(b))
print("集合a、b的差集：", a.difference(b), "\n")

print({i for i in "abcaassddw"})

# 将字符串去重变成集合
c = "aabbxbcdbs"
print(set(c))


"""
字典：
以【关键字】为索引
关键字可以是任意不可变类型，通常是字符串或数字
"""
momo_dict = {"a":1, "b":2}
momo_dict2 = dict(a=1, b=2)

print(momo_dict)
print(momo_dict2)

# 打印字典里的所有关键字
print("字典momo_dict里的所有关键字：", momo_dict.keys())
# 打印字典里的所有指
print("字典momo_dict里的所有值：", momo_dict.values())
