import mysql.connector
conn= mysql.connector.connect(host='localhost',database='ims',user='root',password='Adityabetter1')

if conn.is_connected():
    print("Connected to mysql database")
cursor.execute("CREATE TABLE table1 (eid INT(1),name_ VARCHAR(30),email VARCHAR(30), gender VARCHAR(6), contact INT(10),birth VARCHAR(10),join VARCHAR(10),pass VARCHAR(30),utype VARCHAR(8),salary INT(30))")
cursor = conn.cursor()
cursor.execute("select * from table1")
rows=cursor.fetchall()
cursor.close()
conn.close()

with open("emp_data.csv","a") as csv_input:
    for row in rows:
        formatted_row = []
        for elem in row:
            if elem is None:
                formatted_row.append('N/A')
            else:
                formatted_row.append(str(elem))
        
        row_data = ','.join(formatted_row)
        csv_input.write(row_data)
