from pymongo import MongoClient

client = MongoClient()
db = client.test


key_ ="PsList-Name"# sys.argv[2] # key is col and value is 127.0.0.1
value ="svchost.exe"# sys.argv[3]

key_val = {}
key_val[key_] = value

cursor = db.PsListCollection.find(key_val)





for document in cursor:
	print ' '.join('| {} : {} |'.format(key, val) for key, val in sorted(document.items()))
# print "If Condition basic"
# print "true"