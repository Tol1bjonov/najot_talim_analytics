#1 eng kop takrorlangan soz
# a=['A', 'B', 'B', 'A', 'A', 'c']
# def function(a):
#     v=''
#     cnt=0
#     for i in set(a):
#         if a.count(i) > cnt:
#             cnt=a.count(i)
#             v=i
#     return v, cnt
# print(function(a))

#2 palindrome sozni topish
# def count_palindromes(lst):
#     count = 0
#     for word in lst:
#         if word == word[::-1]:
#             count += 1
#     return count
# print(count_palindromes(["alla", "non", "olma"]))   # Output: 2

#3  ketma ket usuvchi bolaklarni topish
# a=[1,2,3,4,4,5]
# def function(list):
#     result=[a[0]]
#     for i in range(1, len(a)):
#         if list[i]== list[i-1]+1:
#             result.append(list[i])
#         else:
#             break
#     return result
# print(function(a))

#4 eng uzun palindrome soz
# def longest_palindrome(lst):
#     longest = ""
#     max_len = 0
#
#     for word in lst:
#         if word == word[::-1]:
#             if len(word) > max_len:
#                 max_len = len(word)
#                 longest = word
#
#     return longest
# print(longest_palindrome(['alla', 'allaalla', 'non']))

#5 tub son ekanligini aniqlash
# def prime(n):
#     count = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             count += 1
#     if count == 2:
#         return True
#     else:
#         return False
# print(prime(11))
# print(prime(4))

