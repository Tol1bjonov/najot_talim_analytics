import json
from psycopg2 import connect

blocked_names = {
    "Saydullayev Oybek",
    "Najot Ta'lim Bot",
    "Chilonzor | Admin",
    None
}

with open('january.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

conn = connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password='postgres',
    port=5432
)

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS january')

cur.execute("""
    CREATE TABLE january (
        id INT PRIMARY KEY,
        name VARCHAR(60),
        message TEXT
    )
""")

for msg in data['messages']:
    name = msg.get('from')
    message = msg.get('text')
    msg_id = msg.get('id')

    if name not in blocked_names and message:
        
        if isinstance(message, list):
            message = ''.join(str(x) for x in message)

        cur.execute(
            """
            INSERT INTO january (id, name, message)
            VALUES (%s, %s, %s)
            """,
            (msg_id, name, message)
        )

conn.commit()

print("Data inserted successfully!")

cur.close()
conn.close()