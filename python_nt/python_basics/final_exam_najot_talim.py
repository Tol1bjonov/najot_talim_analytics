# 1
# def factorial(n):
#     if n < 0:
#         return "Manfiy son kiritma"
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# print(factorial(4))


#2
# import json
# score = []
# with open('final_exam.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
# for i in data:
#     score.append(i['score'])
# result = []
# for i in data:
#     if max(score) == i['score']:
#         result.append(i['name'])
# print(result)


#3
# a = [
#     {"name": "Olma", "price": 12000},
#     {"name": "Banan", "price": 8000},
#     {"name": "Anor", "price": 15000},
#     {"name": "Olcha", "price": 10000}
# ]
# result = list(map(lambda x: {'name': x['name'], 'price': x['price'] * 2}, a))
# print(result)


#4
# def two_sum(arr, target):
#     result = []
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if i != j and arr[i] + arr[j] == target:
#                 result.append([arr[i], arr[j]])
#
#     return result
# a = [1, 2, 3, 4, 5, 1, 2]
# print(two_sum(a, 5))

#5
# def reverse_n(n):
#     strr = str(n)
#     word = ''
#     for i in strr:
#         if '-' in strr:
#             word = f'-{strr[::-1]}'
#             return word
#     else:
#         num = int(strr[::-1])
#     return num
# print(reverse_n(-987654321))

# 5-savol
# def reverse_n(n):
#     if n < 0:
#         return -int(str(-n)[::-1])
#     return int(str(n)[::-1])
# print(reverse_n(-987654321))
# print(reverse_n(987654321))

#6
# def alone_letter(l):
#     for i in set(l):
#         if l.count(i) == 1:
#             return i
# print(alone_letter('banana'))


#7
# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance
#     def deposit(self):
#         n=int(input('Balansni tuoldiring: '))
#         if n>0:
#             self.balance+=n
#     def withdraw(self):
#         m=int(input('Balansdan yeching: '))
#         if self.balance>m:
#             self.balance-=m
#     def get_balance(self):
#         print(self.balance)
# bnk1 = BankAccount()
# bnk1.deposit()
# bnk1.withdraw()
# bnk1.get_balance()