
#   Puzzle 1
# data = [1, 1, 2, 2, 2, 3, 1, 1]
# distinct=[]
# for i in data:
#     if i not in distinct:
#         distinct.append(i)
# print(distinct)

# Puzzle 2
# data = [1, 1, 2, 2, 2, 3, 1, 1]
# result=[data[0]]
# for i in data[1:]:
#     if i != result[-1]:
#         result.append(i)
# print(result)

#  Puzzle 3
nums = [3, 5, 2, 4, 1, 6]
result = []
for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        result.append(nums[i])
print(result)

