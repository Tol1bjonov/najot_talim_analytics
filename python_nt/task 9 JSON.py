import json

with open('result.json', 'r', encoding='utf-8') as result:
    data = json.load(result)

text = []
for i in data['messages']:
    if i.get('from') == 'Yusufjon Tolibjonov':
        text.append(i.get('text'))
        # print(i.get('text'))


with open('my_message.txt', 'w', encoding='utf-8') as msg:
    for i in text:
        msg.write( i + '\n')
