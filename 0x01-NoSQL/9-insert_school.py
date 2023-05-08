import pymongo

def insert_school(mongo_collection, **kwargs):
    # Insert the new document into the collection and return the _id
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
# Set up a MongoClient instance and get the database and collection
client = pymongo.MongoClient()
db = client['my_db']
collection = db['school']

# Insert a new document into the collection using the insert_school() function
document_id = insert_school(collection, name='Holberton school', address='972 Mission street')

# Print the _id of the inserted document
print(document_id)

