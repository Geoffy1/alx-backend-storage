import pymongo

def list_all(mongo_collection):
    # Use the find() method to retrieve all documents in the collection
    cursor = mongo_collection.find({})
    # Convert the cursor to a list of documents
    documents = list(cursor)
    # Return the list of documents, or an empty list if there are no documents
    return documents if documents else []

