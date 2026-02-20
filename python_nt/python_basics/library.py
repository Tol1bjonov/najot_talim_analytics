from psycopg2 import connect

conn = connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'postgres'
)

cur = conn.cursor()
cur.execute('SELECT * FROM orders')

data = cur.fetchall()
print(data)
