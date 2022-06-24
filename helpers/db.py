import mysql.connector

db = mysql.connector.connect(
  host="containers-us-west-72.railway.app",
  user="root",
  password="PbK9zroblhTWZ0NYQxAh"
)

cursor = db.cursor()


cursor.execute("""
               CREATE DATABASE Astral
               """)