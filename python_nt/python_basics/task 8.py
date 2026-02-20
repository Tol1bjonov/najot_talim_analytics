# 1-savol:
# class Student:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age
#     def is_adult(self):
#         return self.age >= 18
# st1 = Student('Yusufjon', 21)
# print(st1.is_adult())
# st2 = Student('Jahongir', 17)
# print(st2.is_adult())

# 2-savol
# class Counter:
#     def __init__(self):
#         self.first = 0
#     def inc(self):
#         self.first+=1
#         return self.first
#     def dec(self):
#         self.first-=1
#         return self.first
#     def value(self):
#         return self.first
# cntr1 = Counter()
# print(cntr1.value())
# print(cntr1.dec())
# print(cntr1.inc())
# print(cntr1.inc())
# print(cntr1.inc())
# print(cntr1.inc())
# print(cntr1.inc())
# print(cntr1.inc())

# 3-savol:
# class Password:
#     def __init__(self):
#         self._password = 'python'
#     def check(self, p):
#         print(self._password == p)
# psw1 = Password()
# psw1.check('python')
# psw1.check('pythgr')

# 4-savol:
# with open('info.txt', 'r') as file:
#     for i in file:
#         if 'python' in i.lower():
#             print(i.strip())

# 5-savol:

# with open("file1.txt", "r") as f1, \
#      open("file2.txt", "r") as f2, \
#      open("file3.txt", "w") as f3:
#
#     f3.write(f1.read())
#     f3.write("\n")
#     f3.write(f2.read())




