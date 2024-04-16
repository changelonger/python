# import math
# 定义变量，下划线命名法
# 定义类，帕斯卡命名法
#   #是单行注释 ctrl+/  是多行注释
"""因为3个引号可以跨行，所以3引号也可以进行单行注释"""

# python的除法默认浮点型，所以如果像c一样，就直接用//
# 比如3/2=1.5，3//2=1,向下取整
# print(7 / 2)  # 3.5
# print(7 // 2)  # 3
# print(7 % 2)  # 1


# print("hello python")
# print("你好" + " python")
# print('I am you "father"')
# print("He said \"Let\'s go\"")
# print("Hello\nHi!")
# print("""123
# 456.
# 789""")
# print("123\
# 456\
# 789")


# a = 1
# print(a)
# print(2 ** 4)
# print(2 * 3)
# print(2 / 3)
# a = math.sin(1)
# print(a)
# print(len("abc"))  # 3
# user_weight = input("请输入您的体重：")  # 此时user_weight是字符型
# user_weight_two = float(input("请输入您的体重："))  # 此时就是浮点型了，可以进行加减运算
# a = int(input("输入a"))
# b = int(input("输入b"))


# if a > b:
#     print('a is more than b')
# elif a < b:
#     print("b is more than a")
# else :
#     print("a is same with b")
# a = 1
# b = 0
# print(a and a)
# print(a and b)
# print(b and b)
# print(a or b)
# print(b or b)
# print(not a)


# # 列表 内部元素有很多种，不唯一
# new_list = []
# new_list.append(input("请输入成员"))
# new_list.append(input("请输入成员"))
# new_list.append(input("请输入成员"))
# new_list.remove(new_list[1])  # 去除第2个元素
# print(new_list)  # 打印完整的列表


# # 字典 相当于map 有键和值，用{}来表示
# # 比如创建一个通讯录
# contact = {"张三": 150456789, "李四": "123456456"}  # 此时里面就是字典类型 "set":"value"
# print(contact["张三"])  # 访问张三
# print(contact.keys())  # 返回所有键
# print(contact.values())  # 返回所有值
# print(contact.items())  # 返回所有键值对
#
# # 注意set类型必须是不可变的，比如int float double ,列表是可变的，所以不行
#
# # # 这里引入元组概念
# # my_tuple = ("张三",25)
# # contact={("张三",15):"15456789"}
# # print(contact[("张三",15)])
#
# print("张三" in contact)  # 判断是否有某个键，返回布尔值
# print("wang" in contact)
# print(len(contact))  # 输出字典中的容量
#
# del contact["张三"]  # 删除张三
# print("张三" in contact)
# print(len(contact))


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# for i in arr:
#     print(i)  # 打印arr里的所有元素，自动换行
# for i in range(0, 10, 1):  # range 代表i从1开始，一直到10(不等于10)，每次步长为1
#     # for 迭代变量 in range(初始值,末位置,迭代长度)左开右闭
#     print(arr[i], end=" ")  # 不换行，每次用空格结尾


# #  while循环
# i = 0
# while i < len(arr):
#     print(arr[i], end=" ")
#     i = i + 1


# message_content = """
# 今年是{生肖}年
# {姓名}给您拜年了
# """.format(生肖="虎",
#            姓名="常国龙")
# print(message_content)

# gpa_dict = {"小明": "5", "小红": "4.9", "小刚": "4.8"}
# for name, gra in gpa_dict.items():
#     print(f"{name}同学你好，你的成绩是：{float(gra):.2f}")浮点型变量可以用：.2f来保留两位小数

# def compute_BMI(height_1, weight_1):
#     return weight_1 / height_1**2
#
# while True:
#     inputs = input("请输入您的身高（米）和体重（千克），空格分隔：").split()  # 意思是转换成了列表再输入
#     if len(inputs) != 2:
#         print("请输入正确的身高和体重！")
#         continue
#     height = float(inputs[0])
#     weight = float(inputs[1])
#     if height == 0:
#         break
#     BMI = compute_BMI(height, weight)
#     print(f"您的BMI指数是: {BMI:.2f}")

# split()函数用来设置多变量输入时的分隔符，默认值是空格，但是也可以根据需求进行个性化设置，
# 比如文中就用了','逗号进行了实验验证
# 输出：其返回值是一个列表，用一个列表储存下输入的多个变量，但是变量中存储的数据类型依旧是字符串str


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.grades = {"语文": 0, "数学": 0, "英语": 0}
#
#     def set_grades(self, course, grade):
#         if course in self.grades:
#             self.grades[course] = grade
#
#     def print_grades(self):
#         print(f"{self.name}同学的成绩是:")
#         for i in self.grades:
#             print(f"{i}:{self.grades[i]}")
#
# a = Student("张三", 10)
# a.grades["数学"] = 100
# a.grades["语文"] = 95
# a.grades["英语"] = 60
# a.print_grades()
# 文件操作
# 打开文件  f = open("文件路径","操作方式")  操作方式有 r,只读、 w ,只写  不写操作方式时候默认读取模式

# print(f.read())  文件内容全部被打印下来
# print(f.read())  打印空字符串  原因是会记录到读取到哪一个位置，第一个操作后已经到了文件末尾
# print(f.read(10))  读10个字节的文件内容
# print(f.readline()) 读取一行的内容
# f.readlines()  返回一个列表，结合for循环使用
# f.close()  关闭文件


# f = open("data.txt", "r", encoding="utf-8")
# print(f.read())
