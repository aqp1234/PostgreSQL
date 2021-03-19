import psycopg2

try:
    conn = psycopg2.connect(host="localhost", user="", password='')
    conn.autocommit = True
    cur=conn.cursor()
    cur.execute("CREATE DATABASE testdata;")
    cur.close()
    conn.commit()
    print('success')
    
except Exception as e:
    print(e)

