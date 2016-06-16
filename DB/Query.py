from pymongo import MongoClient

client = MongoClient()
db = client.test


key_ ="Rekal-FileScan-FileName"# sys.argv[2] # key is col and value is 127.0.0.1
value ="Files\\Content.IE5\\index.dat"# sys.argv[3]

key_val = {}
key_val[key_] = value

cursor = db.fileScanCollection.find()





for document in cursor:
	print ' '.join('| {} : {} |'.format(key, val) for key, val in sorted(document.items()))
