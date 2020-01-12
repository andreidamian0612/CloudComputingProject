import mysql.connector




mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456789"
)

print(mydb)
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)