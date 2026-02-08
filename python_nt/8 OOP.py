#                         OOP
# class Car:
#     def __init__(self, model, color, km):
#         self.model=model
#         self.color = color
#         self.km=km
#     def show_info(self):
#         print(f"Sizning mashinangiz: {self.model}, rangi: {self.color}, yurgan: {self.km} km")
#
# car1 = Car('Malibu', 'qora', 15000)
# car2 = Car('Gentra', 'qora', 1000)
# b=[car1, car2]
# for i in b:
#     i.show_info()

# class Dataset:
#     def __init__(self, list:list):
#         self.list = list
#     def show_max(self):
#         print(f"Max: {max(self.list)}")
#     def show_min(self):
#         print(f"Min: {min(self.list)}")
#     def show_avg(self):
#         # count=0
#         # for i in self.list:
#         #     count+=i
#         avg = sum(self.list)/len(self.list)
#         print(f"Avg: {avg}")
#
# list1 = Dataset([1,2,3,4,5])
# list1.show_max()
# list1.show_min()
# list1.show_avg()


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def info(self):
        print(f"Xodim -- Ismi: {self.name}, yoshi: {self.age}, maoshi: {self.salary}")

emp1 = Employee('Yusufjon', 20, 2000)
emp1.info()

class Manager(Employee):
    def __init__(self,  name, age, salary, team_size):
        super().__init__(name, age, salary)
        self.team_size = team_size
    def manage(self):
        print(f"Manager \n Ismi: {self.name} \n yoshi: {self.age} \n yligi: {self.salary} \n jamoa sigimi: {self.team_size}")

m1 = Manager('Yusufjon', 20, 2000, 5)
m1.manage()
m1.info()