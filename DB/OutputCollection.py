from pymongo import MongoClient

client = MongoClient()
db = client.test

cursor = db.PsListCollection.find()
for document in cursor:
	print ' '.join('| {} : {} |'.format(key, val) for key, val in sorted(document.items()))