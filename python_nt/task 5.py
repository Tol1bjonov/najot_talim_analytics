# 1-savol:
# def describe_num(num):
#    result = ""
#    if num%3==0:
#        result=result+"Fizz"
#    if num%5==0:
#        result=result+"Buzz"
#    return result or "Faqat 3 va 5 tekshiriladi!"
# print(describe_num(555))

# 2-savol:
# def even_num(num_list):
#     count=0
#     for i in num_list:
#         if i%2==0:
#             count=count+1
#     return f"{count} ta juft son bor"
# nums=[1,2,3,4,5,6,7,88,44,54,64,74]
# print(even_num(nums))

# 3-savol:
# def birlik(n):
#     count=0
#     for i in range(n+1):
#         if i>0 and i<10:
#             count=count+1
#     return f"{count} ta bitta raqamli son bor"
# print(birlik(9))

# 4-savol:
t = (1, (2, (3, (4, 5))))
lst = list(t)
result = []
while lst:
    x = lst.pop(0)
    if isinstance(x, int):
        result.append(x)
    else:
        lst = list(x) + lst
print(result)
print("Yig‘indisi:", sum(result))

