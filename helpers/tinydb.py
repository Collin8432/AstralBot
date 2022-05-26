from tinydb import TinyDB, Query

db = TinyDB("./secret/database.json")

def insert():
   db.insert({"name": "John", "age": "28"})

insert()
print(db.all())