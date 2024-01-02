import mysql.connector
xconn= mysql.connector.connect(host='localhost',database='ims',user='root',password='Adityabetter1')
print(xconn)

if xconn.is_connected():
    print("Connected to mysql database")