from psycopg2 import connect
import json

with open('data.json', 'r', encoding='utf-8') as file1:
    data = json.load(file1)

try:
    conn = connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password='postgres',
        port=5432
    )
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS workers')
    create_script = '''
        CREATE TABLE workers (
            id INT PRIMARY KEY,
            first_name VARCHAR(30),
            last_name VARCHAR(30),
            email VARCHAR(30),
            department VARCHAR(15),
            salary INT
        )
    '''
    cur.execute(create_script)
    for value in data:
        cur.execute(
            "INSERT INTO workers"
            "(id, first_name, last_name, email, department, salary) VALUES(%s,%s,%s,%s,%s,%s)",
            (value['id'], 
            value['first_name'],
            value['last_name'],
            value['email'],
            value['department'], 
            value['salary'])
        )
    cur.execute('SELECT * FROM workers')
    for i in cur.fetchall():
        print(i[2])

    conn.commit()
except Exception as er:
    print("Error:", er)

finally:
    cur.close()
    conn.close()