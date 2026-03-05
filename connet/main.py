from psycopg2 import connect

conn = connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password = 'postgres'
)

cur = conn.cursor()
cur.execute("SELECT * FROM airports")
data = cur.fetchall()
print(data)


import json
result = []
for i in data:
    result.append({
        "id": i[0],
        "city": i[1],
        "airport_name": i[2]
    })
with open("airports.json", "w", encoding="utf-8") as file:
    json.dump(result, file, indent=4)



