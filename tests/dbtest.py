import pymongo

url = "mongodb+srv://Astral69420:<mypassduh>@cluster0.agbrqlo.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)
result = client["<dbName"]["<collName>"].find()
# print results
for i in result:
    print(i)