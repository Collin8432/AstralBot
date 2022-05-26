from re import L
from tinydb import TinyDB, Query

db = TinyDB("./secret/database.json")

user = Query()

def insert():
   db.insert({"name": "John", "age": "228"})

def search():
   results = db.search(user.name == "John")
   print(results)
search()
