from pymongo import MongoClient

client = MongoClient()
db = client.test
db.randCollection.remove()