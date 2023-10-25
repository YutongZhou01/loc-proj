import pymongo

# Connect to the MongoDB server running on localhost:27017
db_client = pymongo.MongoClient('mongodb://root:pass@localhost:27017/admin')
print(db_client.list_database_names())
database = db_client["attackflowdb"]
print(database.list_collection_names())
print(database['images'])
print(list(db_client['attackflowdb']['images'].find()))
