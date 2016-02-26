from pymongo import MongoClient

client = MongoClient()
db = client.test


key_ ="Connscan-PID"# sys.argv[2] # key is col and value is 127.0.0.1
value ="856"# sys.argv[3]

key_val = {}
key_val[key_] = value

cursor = db.testcollection.find(key_val)





for document in cursor:
	print ' '.join('| {} : {} |'.format(key, val) for key, val in sorted(document.items()))
# print "If Condition basic"
# print "true"