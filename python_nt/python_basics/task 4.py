# 1-savol
# try:
#     nums = []
#     for i in range(10):
#         n = int(input("Son kiriting: "))
#         nums.append(n)
#     unique_nums = set(nums)
#     print("Uniquelar soni:", len(unique_nums))
# except:
#     print("Faqat raqam kiriting!!")

# 2-savol
# a = {"Ali", "Vali", "Hasan", "Olim"}
# b = {"Vali", "Hasan", "Sardor"}
# c = {"Hasan", "Olim", "Jasmin"}
# result = (a ^ b ^ c) - (a & b & c)
# print(result)

# 3-savol
# t = (4, 1, 7, 3)
# lst = list(t)
#
# min_v = min(lst)
# max_v = max(lst)
#
# min_id = lst.index(min_v)
# max_id = lst.index(max_v)
# lst[min_id], lst[max_id] = lst[max_id], lst[min_id] # shu joyida ikkalasi almashgan
# result = tuple(lst)
# print(result)

# 4-savol
# t = (10, 20, 30, 20, 40, 20)
# son = 20
# last_index = -1
# for i in range(len(t)):
#     if t[i] == son:
#         last_index = i
# print(last_index)

# 5-savol
# t = (1, (2, (3, (4, 5))))
# lst = list(t)    #
# result = []
# while lst:
#     x = lst.pop(0)
#     if isinstance(x, int):
#         result.append(x)
#     else:
#         lst = list(x) + lst
# print(result)
# print("Yig‘indisi:", sum(result))




