from pymongo import MongoClient

client = MongoClient()
db = client.test
db.testcollection.remove()