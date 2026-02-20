# 2
# def palindrome(text):
#     soz=[]
#     for i in text:
#         if i == i[::-1]:
#             soz.append(i)
#     print(soz)
# palindrome(['alla', 'non', 'wfefer', 'egwvsferf', 'alla'])

# 5
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

#4
def palindrome(text):
    soz = ''
    count = 0
    for i in text:
        if i == i[::-1]:
            if len(i) > count:
                count = len(i)
                soz = i
    print(soz)
palindrome(['allaalla', 'non', 'wfefer', 'egwvsferf', 'al'])

#3
# def check_numbers(nums):
#     num=[]
#     num.append(nums[0])
#     for i in range(1, len(nums)):
#         if num[i] == nums[i-1] + 1:
#             num.append(i)
#             break
#     return num
# print(check_numbers([1,2,3,5,6,7]))


# b=['A', 'B', 'B', 'C', 'C', 'C']
# def function(a):
#     cnt=0
#     v=''
#     for i in set(a):
#         if a.count(i)>cnt:
#             cnt=a.count(i)
#
#     return i
# print(function(b))




















