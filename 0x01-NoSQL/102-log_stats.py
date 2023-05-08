#!/usr/bin/env python3
'''Task 15
'''
from pymongo import MongoClient


def log_stats():
    """Log statistics from the database logs in MongoDB"""

    client = pymongo.MongoClient('mongodb://localhost:27017')
    collection_logs = client.logs.nginx

    print(f"{collection_logs.count_documents({})} logs")

    print("Methods:")
    print(f"\tmethod GET: {collection_logs.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {collection_logs.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {collection_logs.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {collection_logs.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {collection_logs.count_documents({'method': 'DELETE'})}")

    print(f"{collection_logs.count_documents({'path': '/status'})} status check")

    print("IPs:")
    pipeline = [
        {'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10}
    ]
    for ip in collection_logs.aggregate(pipeline):
        print(f"\t{ip['_id']}: {ip['count']}")
