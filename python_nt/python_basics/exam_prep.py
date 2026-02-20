# a={1,2,3,4,6,7,8}
# b = list(a)
# max = max(b)
# min = min(b)
# for i in range(min, max+1):
#     if i not in b:
#         print(i)

# a=[1,1,1,1,1,2,2,2,2,3,3,4,4,5,6]
# result=[]
# for i in a:
#     if a.count(i) == 1:
#         result.append(i)
# print(result)

# a=(4,1,7,3)
# b=list(a)
# minn=min(b)
# maxn=max(b)
# result=[]
# for i in b:
#     if i == min(b):
#         result.append(max(b))
#     elif i == max(b):
#         result.append(min(b))
#     else:
#         result.append(i)
# print(result)
# 1
# test = " olma anor uzum olma anor orik"
# text_splt = test.split()
# text_dict = {}
# for i in set(text_splt):
#     text_dict[i] = text_splt.count(i)
# print(text_dict)
# 2
# d = {
#     'a': 1,
#     'b': 2,
#     'c':3
# }
# result={}
# for i, j in d.items():
#     result[j]=i
# print(result)
#3
# d={1: 'a', 2:'b', 3:'c', 4:'c'}
# result = []
# result_dict={}
# for i in d.values():
#     result.append(i)
# for j in set(result):
#     result_dict[j]=result.count(j)
# print(result_dict)

#recursive function
# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(10))

# def yigindi_toq(n):
#     if n==1:
#         return 1
#     elif n%2==0:
#         return n-1+yigindi_toq(n-3)
#     else:
#         return n+yigindi_toq(n-2)
# print(yigindi_toq(10))

