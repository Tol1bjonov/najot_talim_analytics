import json

# Load
# with open('data.json', 'r') as file:
#     data = json.load(file)

# 1 positioni Analystlar
# count = 0
# for i in data['employees']:
#     if i['position'] == 'Analyst':
#         count+=1
#         print(i)
#     # print(i['position'])
# print(count)

# 2 unique positionlar
# positions = []
# for i in data['employees']:
#     if i['position'] not in positions:
#         positions.append(i['position'])
# print(positions)

# 3 ismi A bilan boshlanadiganlar
# for i in data['employees']:
#     if i['name'][0] == 'A':
#         print(i['name'])
    # 2-yuli, startswith bilan
    # if i['name'].startswith('A'):
    #     print(i['name'])


# with open('dt1.json', 'r') as file:
#     data = json.load(file)
#
# # data['skills'].append('Java')
#
#
# with open('dt1.json', 'w') as file:
#     json.dump(data, file, indent=4)

with open('dt1.json', 'r') as file:
    data = json.load(file)

# data['skills'].append('Java')
# print(data)
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
