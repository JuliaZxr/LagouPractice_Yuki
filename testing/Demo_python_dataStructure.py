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

"""
元组：使用()进行定义
tuple、list、range都是序列数据类型
元组是不可变的，可以通过解包、索引来访问

tuple.count(x) 用来统计该元组中x出现的个数
tuple.index(x) 用来得到该元组中x的索引
"""
# 元组的定义
tuple_yuki = (1, 2, 3)
tuple_yuki2 = 1, 2, 3

print("tuple_yuki", tuple_yuki)
print(type(tuple_yuki))

print("tuple_yuki2", tuple_yuki2)
print(type(tuple_yuki2))

# 元组的不可变特性：元组内的值不可变，执行会报错；但是嵌套在元组里的列表，可以进行修改
a = [1, 2, 3]
tuple_yuki4 = (1, 2, a)
print(tuple_yuki4)

tuple_yuki4[2][0] = "a"
print(tuple_yuki4)

# tuple.count(x) 用来统计该元组中x出现的个数
tuple_yuki5 = (1, 2, 3, "a", "a", "b")
print(tuple_yuki5.count(3))
print(tuple_yuki5.count("a"))
print(tuple_yuki5.count("c"))

# tuple.index(x) 用来得到该元组中x的索引,当元组中x存在多个时，返回的是第一个x的索引
print(tuple_yuki5.index(3))
print(tuple_yuki5.index("a"))

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

# 将字符串去重变成集合
print({i for i in "abcaassddw"})

"""
将字符串去重变成无序集合 or 有序列表

sort 与 sorted 区别：
sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

sorted(iterable, key=None, reverse=False)  
iterable -- 可迭代对象。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
返回重新排序的列表。
"""
# 将字符串去重变成集合
c = "aabbxbcdbs"
print("c的类型是：", type(c))
print("将字符串c去重变成无序集合：", set(c))  # set是集合，这里利用的是集合不重复的特点，但是set是无序集合，所以打印出来的顺序与字符串不一致
print("set(c)的类型是：", type(set(c)))

# 将字符串先转换成list,再使用sorted()按照原list顺序进行去重后返回
list_c3 = sorted(set(c), key=list(c).index)  # sorted(L)返回一个排序后的L，不改变原始的L
print("list_c3的类型是：", type(list_c3))
print("将字符串c去重后变成不改变顺序的列表：", list_c3)


"""
字典：
以【关键字】为索引
关键字可以是任意不可变类型，通常是字符串或数字
字典内key可以重复，但是会被覆盖
dict.pop(x) 指删除字典中key为x的键值对
"""
momo_dict = {"a": 1, "b": 2}
momo_dict2 = dict(a=1, b=2)

print("将字典dict打印出来：", momo_dict)
print("将字典dict2打印出来：", momo_dict2)

# 打印字典里的所有关键字
print("字典momo_dict里的所有关键字：", momo_dict.keys())
# 打印字典里的所有值
print("字典momo_dict里的所有值：", momo_dict.values())

momo_dict3 = {"a": 1, "b": 2, "c": 3, "d": 4}
print("将字典dict3打印出来：", momo_dict3)
momo_dict3.pop("a")
print("删除字典中key为a的所有键值对后输出：", momo_dict3)

# 字典内key可以重复，但是会被覆盖
momo_dict4 = {"a": 1, "b": 2, "a": 3, "d": 4}
print("将字典dict4打印出来，查看重名的key是否被覆盖：", momo_dict4)