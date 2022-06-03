import dbm
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="8432",
  database="testdatabase"
)

cursor = db.cursor()


print(db)