from psycopg2 import connect
import json
conn = connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='postgres'
)

curr = conn.cursor()

with open('data.json', 'r', encoding='utf-8') as file1:
    data = json.load(file1)
for i in data:
    print(i)

curr.close()
conn.close()