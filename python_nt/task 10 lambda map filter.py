                                        ### Map ###
# a=[1,2,3,4,5,6,7]
#
# def square(x):
#     return x**2
#
# result=list(map(square, a))
# print(result)

# a=[100,200, 300]
# def change_to_sum(x):
#     return x*12200
# result = list(map(change_to_sum, a))
# print(result)


# puzzle 1
# words=['python', 'data', 'analysis']
# def change_word(x):
#     return x.upper() + f' - {len(x)}'
# result = list(map(change_word, words))
# print(result)

# puzzle 2
# names = ['Ali', 'Vali', 'Sami']
# scores=[80, 90, 70]
# def match(names, scores):
#     return f'{names} - {scores}'
# result = list(map(match, names, scores))
# print(result)

# puzzle 3
# numbers = [[1,2], [3,4], [5,6]]
# def clclt(x):
#     return sum(x)
# result = list(map(clclt, numbers))
# print(result)

                                         ## Lambda ##
# bu nomi yoq anonymous kichik funksiya
# lambda argument: expression
# 1
# a=[1,2,3,4,5]
# result=list(map(lambda x: x**2, a))
# print(result)

# 2
# a=[10, 90, 50]
# result = list(map(lambda x: x*0.9, a))
# print(result)

# student = [
#     {'name' : 'Ali', 'score': 78},
#     {'name' : 'Nemat', 'score': 48},
#     {'name' : 'Vali', 'score': 87},
# ]
# def function(a):
#     return {
#         'name': a['name'],
#         'score': a['score'] + 5
#     }
# result=list(map(function, student))
# print(result)
# result1 = list(map(lambda x: {'name': x['name'], 'score': x['score']+5 }, student))
# print(result1)

## puzzle 1
# words = ['python', 'data', 'analysis', 'sql']
# result = list(map(lambda x: x.upper() + f' - {len(x)}', words))
# print(result)
#
# #puzzle 2
# names = ['Ali', 'Vali', 'Sami']
# scores=[80, 90, 70]
# result1 = list(map(lambda x,y: f'{x} - {y}', names, scores))
# print(result1)
#
# #puzzle 3
# numbers = [[1,2], [3,4], [5,6]]
# result2 = list(map(lambda x: sum(x),numbers ))
# print(result2)



                                    ### Filter ###
# filter() ruyxatdan shartga mos keladigan elementni qoldiradi
# filter(function, iterable)

# numbers = [1,2,3,4,5,6,7,8]
# def function(x):
#     return x%2==0
# result = list(filter(function, numbers))
# print(result)

# puzzle 1
# numbers = [-9, -3, 0,3,6,10, 15]
# def function(x):
#     return x%3==0 and x>0
# result = list(filter(function, numbers))
# print(result)
#
# result1 = list(filter(lambda x: x%3==0 and x>0, numbers))
# print(result1)


# puzzle 2
# words = ['apple', 'banana', 'avocado', 'cherry', 'apricot']
# def function(x):
#     return x[0] == 'a' and len(x)>6
# result = list(filter(function, words))
# print(result)
# result1 = list(filter(lambda x: x[0] == 'a' and len(x)>6, words))
# print(result1)

# puzzle 3
# students = [
#    {"name": "Ali", "score": 78},
#    {"name": "Vali", "score": 92},
#    {"name": "Sami", "score": 65},
#    {"name": "Zafar", "score": 88}
# ]
# def function(a):
#     return {
#         'name': a['name'],
#         'score': a['score'] + 5
#     }
# def function(x):
#     return x.get('score') > 80
# result = list(filter(function, students))
# print(result)
#lambda
# result1 = list(filter(lambda x: x.get('score') > 80, students ))
# print(result1)

# puzzle 4
# numbers=[1,2,3,4,5,6]
# def function(x): #map
#     return x%2==0
# def function1(x):
#     return x*10
# result = list(map(lambda x: x*10, filter(lambda x: x%2==0, numbers)))
# print(result)

# puzzle 5
# numbers1 = [[1,12], [3,4], [5,6]]
# def fnc(x):
#     return sum(x)
# def fnc2(x):
#     return x>10
# result2 = list(filter(fnc2, map(fnc, numbers1)))
# result3 = list(filter(lambda x:x>10,map(lambda x: sum(x), numbers1) ))
# print(result3)

employees = [
    {'name': 'Ali', 'salary': 1000},
    {'name': 'Vali', 'salary': 2500},
    {'name': 'Sami', 'salary': 800},
    {'name': 'Zafar', 'salary': 3000}
]
result = list()