import sqlite3
import pandas as pd

square=lambda n:n*n

conn=sqlite3.connect("Configuracion.db")

conn.create_function("square",1,square)


cursor=conn.cursor()
cursor.execute('''
               SELECT * FROM Color
               ''')

results = cursor.fetchall()
#print(results)
#results = pd.DataFrame(results)
for row in results:
    print(f"1-{row[0]}")
conn.commit()
cursor.close()
conn.close()
