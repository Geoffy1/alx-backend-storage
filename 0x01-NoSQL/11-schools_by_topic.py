import pymongo

def schools_by_topic(mongo_collection, topic):
    # Use the find() method to get all documents with the specified topic
    cursor = mongo_collection.find({'topics': topic})
    # Return a list of dictionaries representing the matching documents
    return list(cursor)
# Set up a MongoClient instance and get the database and collection
client = pymongo.MongoClient()
db = client['my_db']
collection = db['school']

# Get a list of all schools that have the topic 'data science'
matching_schools = schools_by_topic(collection, 'data science')

# Print out the names of the matching schools
for school in matching_schools:
    print(school['name'])

