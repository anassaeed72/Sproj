from pymongo import MongoClient

# client = MongoClient()
# db = client.test

# cursor = db.randCollection.find()
# for document in cursor:
# 	print ' '.join('| {} : {} |'.format(key, val) for key, val in sorted(document.items()))


client = MongoClient()
db = client.test

# result = db.PsxViewCollection.insert_one(
#    {
#    		"PsxView-Name":"aiqpbter.chm"
#    }
# )



result = db.WindowsAPICollection.insert_one(
   {
   		"WindowsAPI-Name":"SetWindowsHookEx"
   }
)