import pymongo

def update_topics(mongo_collection, name, topics):
    # Use the update_many() method to update all documents with the given name
    result = mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
    # Return the number of documents updated
    return result.modified_count

