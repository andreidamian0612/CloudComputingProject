import mysql.connector

mydb = mysql.connector.connect(
  host="mysql",
  user="root",
  passwd="secret",
  database="mydatabase"
)
cursor = None

def init_connection():
  global cursor
  cursor = mydb.cursor()

def db_init():
  init_connection()
  try:
    cursor.execute("CREATE DATABASE mydatabase")
  except:
    pass
  cursor.execute("USE mydatabase")
  try:
    cursor.execute("""CREATE TABLE Results
                          (
                          StudentName varchar(50),
                          Percentage float
                          );"""
                    )
  except:
    pass

def db_add_result(name, percentage):
  cursor.execute(f"""INSERT INTO Results VALUES(\"{name}\", {percentage});""")
  cursor.commit()