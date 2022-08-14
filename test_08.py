# age = int(input("请输入年龄"))
# if age < 10:
#     print("小孩")
# elif age >= 10 and age < 20:
#     print("小朋友")
# elif age >= 20 and age < 30:
#     print("年轻人")
# elif age >= 30 and age < 50:
#     print("中年人")
# else:
#     print("老年人")


# import random
# a = random.randint(1, 5)
# print(a)

# a = 0
# while a < 5:
#     print("*")
#     a += 1

# a = 0
# while a < 4:
#     b = 0
#     while b <= a:
#         print(b + 1, end="")
#         b += 1
#     print()
#     a += 1

# str = "skfksdkfksd"
# num = 0
# for i in str:
#     print(i, end="")
#     num += 1
# print(num)

# print(1 in range(1, 5))

# list1 = [1, 2, 3, 4, 2, 5, 6, 8]
# list1.remove(2)
# del (list1[0])
# print(list1)

# list1 = [x for x in range(12, 0, -1)]
# print(list1)

# a = (0)
# b = (1,)
# c = 1, 2, 3
# d = 6,
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# a = [1, 2, 3]
# b = ["asas", "sdfkjsdf", "sldjfksadf"]
# a = [1, 2, 3, 4, 5, 3]
b = list("12345")

# c = list(range(1, 5))
# a.insert(1, 5)
# print(a.count(3))
# print(a.index(3,3))
# print(b)
# print(c)
# a.reverse()
# print(a)


# list1 = ['张飞', '刘备', '关羽']
# for n in list1:
#     print(n)


# list1 = [x for x in range(0, 10) if x % 2 == 0]
# print(list1)

# tuple1 = tuple()
# print(type(a))

# set1 = {1, 2, 3, 4, 5}
# set2 = set([1, 2, 3])
# print(type(set2))


# str1 = "123 5 48 6 94 0 1"
# a = str1.split(" ")
# sum = 0
# for n in a:
#     sum += int(n)
# print(sum)


# list1 = [1, 2, 3, 4, 5]
# list2 = list1[:5:2]
# print(list2)


# class dog:
#     def __init__(self, name="旺财", age=3):
#         self.name = name
#         self.age = age
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def show_name(self):
#         print(self.name)
#
#     def set_age(self, age):
#         self.age = age
#
#     def get_age(self):
#         return self.age
#
#     def show_age(self):
#         print(self.age)
#
#     def __del__(self):
#         print("%s销毁了" % self.name)
#
#
# d = dog()
# print(d.get_name())
# d.set_name("xiaohei")
# d.show_name()
# d.show_age()

# print(sum(range(1, 101)))
