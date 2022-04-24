import pymongo
from pymongo.server_api import ServerApi

myClient = pymongo.MongoClient("mongodb://localhost:27017/")

# if you want to deploy then you can get a mongodb database connection pass in 
# your credentials  <user> and <password>. 
# But the link will be different. I'm just sharing the idea. 
#myClient = pymongo.MongoClient("mongodb+srv://<user>:<password>@cluster0.fbl4f.mongodb.net/urldb?retryWrites=true&w=majority", server_api=ServerApi('1'))


dbName = "urldb"
collectionName = 'urlTable'  

dbHandle = None
collectionHandle = None 


if dbName not in myClient.list_database_names():
    dbHandle = myClient[dbName] 
else:
    dbHandle = myClient[dbName]  

if collectionName not in dbHandle.list_collection_names(): 
    collectionHandle = dbHandle[collectionName]
else: 
    collectionHandle = dbHandle[collectionName]


print(dbHandle)
print(collectionHandle) 

def isPresentInDatabase(hashString, collectionHandle):
    return collectionHandle.find_one({hashString : True}) != None 

def fetchURL(hashString, collectionHandle): 
    return collectionHandle.find_one({hashString : True})['url']

def insertDB(hashString, urlString, collectionHandle):
    return collectionHandle.insert_one({hashString: True ,"url" : urlString }) 

